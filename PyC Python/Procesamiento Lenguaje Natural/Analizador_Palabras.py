import spacy

nlp = spacy.load('es_core_news_lg')

doc = nlp("azul")

for token in doc:
    print(token.text, token.tag_)
