from main import *

def test_rakuten_search():
    keyword = 'ipad'
    res = rakuten_search(keyword)
    
    assert res['Items']
    assert res['Items'][0]['itemName']
    assert res['Items'][0]['itemPrice']
    
    
def test_item_info():
    keyword = 'ipad'
    res = item_info(keyword)
    
    assert res['Products']
    assert res['Products'][0]['productName']
    assert res['Products'][0]['maxPrice']
    assert res['Products'][0]['minPrice']
    

def test_genere_rank():
    genereId = 0
    res = genere_rank(genereId)
    
    assert res['Items']
    assert res['Items'][0]['rank']
    assert res['Items'][0]['itemName']