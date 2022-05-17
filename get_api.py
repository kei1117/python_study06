import requests
import inspect

APP_ID = '1027974265062346254'

def get_api(search_word): 
    
    urls = {
        'rakuten_search':'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?',
        'item_info' :'https://app.rakuten.co.jp/services/api/Product/Search/20170426?',
        'genere_rank' :'https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628'    
    }
        
    from_func_name = inspect.stack()[1].function
    
    url = urls[from_func_name]
            
    params = {
        'applicationId':APP_ID,
        'format':'json',
        'keyword':search_word,
        'formatVersion':2
    }
    
    if from_func_name == 'genere_rank':
        params['genereId'] = params.pop('keyword')
        
    res = requests.get(url, params = params)
    
    try:
        res.raise_for_status()
    except Exception as e:
        print('エラー :',e)
        return res.status_code
    
    res = res.json()
    return res