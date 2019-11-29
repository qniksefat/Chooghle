import math
from Indexer.positional_indexer import *


def compute_tfidf_for_document (term, document: dict, dictionary: dict, documents_size):
    document_id = document["id"]
    if term not in dictionary.keys():
        return 0
    posting_list: dict = dictionary[term]
    if document_id not in posting_list.keys():
        return 0
    tf = len(posting_list[document_id])
    df = len(posting_list.keys())
    idf = math.log(documents_size / df, 2)
    tf_idf = tf * idf
    return tf_idf

def compute_tfidf_for_query (term, query: list, dictionary: dict, document_size):
    if term not in dictionary.keys():
        return 0
    posting_list: dict = dictionary[term]
    tf = 0
    for item in query:
        if (term == item):
            tf += 1
    df = len (posting_list.keys())
    idf = math.log(documents_size / df, 2)
    tf_idf = tf * idf
    return tf_idf

def compute_score (query : list, document : dict, dictionary : dict, documents_size):
    query_vect = []
    document_vect = []
    for term in query:
        query_vect.append(compute_tfidf_for_query(term,query,dictionary,documents_size))
        document_vect.append(compute_tfidf_for_document(term,document,dictionary,documents_size))
    query_vect_len = compute_vectore_length(query_vect)
    document_vect_len = compute_vectore_length(document_vect)
    score = 0
    for i in range(len(query_vect)):
        score += query_vect[i] * document_vect[i]
    #score = score / query_vect_len / document_vect_len
    return score

def compute_vectore_length (vector : len):
    res = 0
    for i in range(len(vector)):
        res += vector[i] * vector[i]
    return math.sqrt(res)

def search_for_query (query, documents : dict, dictionary : dict):
    documents_size = len(documents.keys())
    candidate_documents = []
    for term in query:
        this_docs = search_for_term(term,index)
        for docId in this_docs:
            if (docId not in candidate_documents):
                candidate_documents.append(docId)
    scored_documents = []
    for document_id in candidate_documents:
        document = documents[document_id]
        document_score = compute_score(query,document,dictionary,documents_size)
        scored_documents.append((document_id,document_score))
    sorted_documents = sorted(scored_documents,key= lambda x : x[1],reverse=True)
    return sorted_documents


documents = create_documents_dict(sample_docs())
documents_size = len(documents.keys())

index = positional_indexer(documents, "content")

sample_query =[ "is"]

res = search_for_query(sample_query,documents,index)
print(res)
