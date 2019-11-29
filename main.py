from Tokenizer import english_tokenizer, persian_tokenizer
from Indexer import positional_indexer, bigram_indexer
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
    # print (result)
    for i in range(10):
        print ("result number : " + str(i+1) + " document number " + str(result[i][0]))
        print(english_tokenizer.dataSet.get_value_by_id(result[i][0], 'content'))
        print()
        print()

def phase_2_positional_index_output():
    dictionary = load_english_dict()
    query = input()
    positional_indexer.show_search_result(dictionary,query)

def phase_2_bigram_index_output():
    dictionary = load_english_dict()
    res = bigram_indexer.bigram_indexer(dictionary)
    print(res)

#create_positional_index_for_english()

# tf_idf_english()

# phase_2_positional_index_output()

# phase_2_bigram_index_output()