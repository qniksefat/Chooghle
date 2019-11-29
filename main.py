from Tokenizer import english_tokenizer, persian_tokenizer
from Indexer import positional_indexer
from search_engine import tfidf

def tf_idf_english():
    english_dataset = english_tokenizer.read_from_file()
    documents = positional_indexer.create_documents_dict(english_dataset)
    dictionary = positional_indexer.positional_indexer(documents,"content")
    raw_query = input()
    query = english_tokenizer.english_tokenize(raw_query)
    result = tfidf.search_for_query(query,documents,dictionary)
    print(result)

#tf_idf_english()