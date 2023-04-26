from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

def extract_keywords(text,model_name):
    keword_tokenizer = AutoTokenizer.from_pretrained(model_name)
    keword_model = AutoModelForTokenClassification.from_pretrained(model_name)
    keword_nlp = pipeline("ner", keword_model, tokenizer=keword_tokenizer )
    """
    Extract keywords and construct them back from tokens
    """
    result = list()
    keyword = ""
    for token in keword_nlp(text):
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
