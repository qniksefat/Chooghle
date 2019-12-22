from Indexer import positional_indexer
from search_engine import tfidf
import pandas as pd
import numpy as np

def creating_data_set(raw_dataset : dict):
    documents = positional_indexer.create_documents_dict(raw_dataset)
    dictionary = positional_indexer.positional_indexer(documents, "content")
    documents_size = len(documents.keys())
    dataset = []
    first_row =[]
    for term in dictionary.keys():
        first_row.append(term)
    first_row.append("tag")
    dataset.append(first_row)
    for key in documents.keys():
        this_document = documents[key]
        print(this_document['id'])
        this_doc_tfidf_vector = []
        for term in dictionary.keys():
            this_term_tfidf = tfidf.compute_tfidf_for_document(term,this_document,dictionary,documents_size)
            this_doc_tfidf_vector.append(this_term_tfidf)
        this_doc_tfidf_vector.append(this_document["tag"])
        dataset.append(this_doc_tfidf_vector)
    return dataset