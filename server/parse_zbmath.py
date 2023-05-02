import requests
import re
import xml.etree.ElementTree as ET
from collections import Counter

def make_keyword_msc_list(keyword):
    keyword_for_url = keyword.replace(" ", "%20")
    url = 'https://oai.zbmath.org/v1/helper/filter?filter=keyword%3A'+ keyword_for_url + '&metadataPrefix=oai_zb_preview'
    params = {'accept': 'text/xml'}
    response = requests.get(url, params=params)
    root = ET.fromstring(response.text)
    
    classifications = []
    for classification in root.iter('{https://zbmath.org/zbmath/elements/1.0/}classification'):
        classifications.append(classification.text)
        
    classifications
    
    return classifications

def make_msc_num_list(lst,num = 10):
    try:
        if len(lst) == 0:
            raise ValueError("Alert! : Please include words that are characteristic of the sentence.")
    except ValueError as e:
        print(e)
        return
    count_dct = {}
    for keyword in lst:
        classifications = make_keyword_msc_list(keyword)
        for index in classifications:
            count_dct[index] = count_dct.get(index, 0) +1
    count_dct = sorted(count_dct.items(), key=lambda x:x[1],reverse = True)
    min_num = min(num, len(count_dct))
    return count_dct[0:min_num]
