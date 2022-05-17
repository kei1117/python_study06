from pprint import pprint
from get_api import get_api
from to_csv import to_csv
    
def rakuten_search(search_word):
    
    data = []
    
    res = get_api(search_word) 

    target_list = res['Items']

    for i, target in enumerate(target_list):
        result = {
            'index':i,
            'search_word':search_word,
            'name':target['itemName'],
            'price':target['itemPrice']
        }
        pprint(result)
        data.append(result)  
        
    to_csv(data)
    
    return res


def item_info(search_word):
    
    data = []
    
    res = get_api(search_word) 
    
    target_list = res['Products']
        
    for i, target in enumerate(target_list):
        
        result = {
            'index':i,
            'search_word':search_word,
            'name':target['productName'],
            'max_price':target['maxPrice'],
            'min_price':target['minPrice']
        }
        
        pprint(result)
        data.append(result)
        
    to_csv(data)
    
    return res


def genere_rank(search_word):
    
    data = []
    
    res = get_api(search_word) 
    
    target_list = res['Items']
        
    for i, target in enumerate(target_list):
        
        result = {
            'index':i,
            'rank':target['rank'],
            'name':target['itemName'],
        }
    
        pprint(result)
        data.append(result)
        
    to_csv(data)
    
    return res


if __name__ == "__main__":
        
    while True:
        try:
            select_api = input('使用するAPIの番号を入力してください!\n1:楽天市場商品検索API\n2:商品価格ナビ製品検索API\n3:楽天市場ランキングAPI\n4:終了\n>>>>>>')
            search_word = input('検索したいワードを入力してください？')

            if int(select_api) == 1:
                rakuten_search(search_word)
            elif int(select_api) == 2:
                item_info(search_word)
            elif int(select_api) == 3:
                genere_rank(search_word)
            elif int(select_api) == 4:
                print('終了します')
                break
        except Exception as e:
            print('エラーーー！',e)
            print('1〜4の数字を入力してください!')

    