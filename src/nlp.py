import json
import nltk
from nltk.corpus import treebank

def request(request):
    return _getLanguageData(request["text"])

def _getLanguageData(text):
    words = _getWords(text)
    tags = _getTags(words)
    return {
        "tags" : tags,
        "words" : words,
        "text" : text
    }

def _getWords(text):
    tokens = nltk.word_tokenize(text)
    return tokens

def _getTags(words):
    tags = nltk.pos_tag(words)
    tagResults = []
    for tag in tags:
        tagResult = {}
        tagResult["word"] = tag[0]
        tagResult["tag"] = tag[1]
        tagResults.append(tagResult)
    return tagResults

def _getNamedEntities(tags):
    entities = nltk.chunk.ne_chunk(tags)
    return entities
