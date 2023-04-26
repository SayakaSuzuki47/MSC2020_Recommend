import requests
import re
import xml.etree.ElementTree as ET
from collections import Counter

def make_keyword_msc2020_list(keyword):
    keyword_for_url = keyword.replace(" ", "%20")
    url = 'https://oai.zbmath.org/v1/helper/filter?filter=keyword%3A'+ keyword_for_url + '&metadataPrefix=oai_zb_preview'
    headers = {'accept': 'text/xml'}
    
    response = requests.get(url, headers=headers)
    root = ET.fromstring(response.text)
    
    classifications = []
    for classification in root.iter('{https://zbmath.org/zbmath/elements/1.0/}classification'):
        classifications.append(classification.text)
        
    count = Counter(classifications)
    
    return count

def make_msc2020_num_list(lst):
    if len(lst)==0:
        print("Alert! : Please include words that are characteristic of the sentence.")
    else:
        counter = make_keyword_msc2020_list(lst[0])
        if len(lst)>1:
            for classification in lst[2:]:
                counter = counter + make_keyword_msc2020_list(classification)
        return counter