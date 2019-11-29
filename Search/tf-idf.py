import math
from . import positional_indexer
positional_indexer.

def compute_tfidf ( term, document : dict, dictionary : dict):
    document_content = document["content"]
    document_id = document["id"]
    if (term not in dictionary.keys()):
        return 0
    posting_list : dict = dictionary[term]
    if (document_id not in posting_list.keys()):
        return 0
    tf = len(posting_list[document_id])
    df = len(posting_list.keys())
    N = len(dictionary.keys())
    idf = math.log(N / df,2)
    tf_idf = tf*idf
    return tf_idf
