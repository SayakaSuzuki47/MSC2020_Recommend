import requests
import re

def make_url_search_keyword(keyword):
    keyword_for_url = keyword.replace(" ", "%20")
    url = 'https://oai.zbmath.org/v1/helper/filter?filter=keyword'+ keyword_for_url + '&metadataPrefix=oai_zb_preview'
    return url