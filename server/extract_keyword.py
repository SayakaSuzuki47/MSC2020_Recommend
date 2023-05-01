from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

def extract_keywords(text,model_name):
    keyword_tokenizer = AutoTokenizer.from_pretrained(model_name)
    keyword_model = AutoModelForTokenClassification.from_pretrained(model_name)
    keyword_nlp = pipeline("ner", keyword_model, tokenizer=keyword_tokenizer )
    """
    Extract keywords and construct them back from tokens
    """
    result = list()
    keyword = ""
    for token in keyword_nlp(text):
        if token['entity'] == 'I-KEY':
            keyword += token['word'][2:] if \
              token['word'].startswith("##") else f" {token['word']}"
        else:
            if keyword:
                result.append(keyword)
            keyword = token['word']
    # Add the last keyword
    result.append(keyword)
    return list(set(result))
