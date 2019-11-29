from Tokenizer import english_tokenizer, persian_tokenizer
from Indexer import positional_indexer
from search_engine import tfidf


def create_positional_index_for_english():
    english_dataset = english_tokenizer.dataSet.data
    documents = positional_indexer.create_documents_dict(english_dataset)
    dictionary = positional_indexer.positional_indexer(documents, "content")
    positional_indexer.write_index_on_file(dictionary,"english_dict")

def load_english_dict():
    return positional_indexer.load_index("english_dict")

def tf_idf_english():
    english_dataset = english_tokenizer.dataSet.data
    documents = positional_indexer.create_documents_dict(english_dataset)
    dictionary = load_english_dict()
    raw_query = input()
    query = english_tokenizer.english_tokenize(raw_query)
    result = tfidf.search_for_query(query,documents,dictionary)
    res_str = ""
    print(english_tokenizer.get_value_by_id(result[1][1], 'content'))
    print(result)

#create_positional_index_for_english()
# print(english_tokenizer.get_value_by_id(18, 'content'))
tf_idf_english()