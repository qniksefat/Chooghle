from Tokenizer import english_tokenizer, persian_tokenizer
from Indexer import positional_indexer, bigram_indexer
from search_engine import tfidf
from query_corrector import query_corrector


def create_positional_index_for_english():
    dataset = english_tokenizer.DataSet('../Data/English.csv', has_tag=False)
    english_dataset = dataset.data
    documents = positional_indexer.create_documents_dict(english_dataset)
    dictionary = positional_indexer.positional_indexer(documents, "content")
    positional_indexer.write_index_on_file(dictionary, "english_dict")


def create_positional_index_not_stemmed_for_english():
    dataset = english_tokenizer.DataSet('../Data/English.csv', has_tag=False)
    not_stemmed_dataset = dataset.not_stemmed_data
    documents = positional_indexer.create_documents_dict(not_stemmed_dataset)
    dictionary = positional_indexer.positional_indexer(documents, "content")
    positional_indexer.write_index_on_file(dictionary, "not_stemmed")


def load_not_stemmed_dict():
    return positional_indexer.load_index("not_stemmed")


def load_english_dict():
    return positional_indexer.load_index("english_dict")


def tf_idf_english():
    dataset = english_tokenizer.DataSet('../Data/English.csv', has_tag=False)
    english_dataset = dataset.data
    documents = positional_indexer.create_documents_dict(english_dataset)
    dictionary = load_english_dict()
    raw_query = input()
    query = english_tokenizer.analyser(raw_query)
    result = tfidf.search_for_query(query, documents, dictionary)
    # print (result)
    for i in range(10):
        print("result number : " + str(i + 1) + " document number " + str(result[i][0]) + "with score : " + str(
            result[i][1]))
        print(dataset.get_value_by_id(result[i][0], 'content'))
        print()
        print()


def tf_idf_english_with_correction():
    dataset = english_tokenizer.DataSet('../Data/English.csv', has_tag=False)
    english_dataset = dataset.data
    documents = positional_indexer.create_documents_dict(english_dataset)
    dictionary = load_english_dict()
    not_stemmed_dictionary = load_not_stemmed_dict()
    bigram_index = bigram_indexer.bigram_indexer(not_stemmed_dictionary)

    raw_query = input()
    query_terms = raw_query.split(" ")
    change_flag = 0
    new_query = ""
    for term in query_terms:
        term_alternative = query_corrector.final_candidate(term, bigram_index)
        if (term_alternative[0][1] != 0):
            change_flag = 1
            new_query += term_alternative[0][0] + " "
    if (change_flag == 1):
        print("did you mean : " + new_query)
        print()
        print()
        raw_query = new_query
    query = english_tokenizer.analyser(raw_query)
    result = tfidf.search_for_query(query, documents, dictionary)
    # print (result)
    for i in range(min(10, len(result))):
        print("result number : " + str(i + 1) + " document number " + str(result[i][0]) + "with score : " + str(
            result[i][1]))
        print(dataset.get_value_by_id(result[i][0], 'content'))
        print()
        print()


def final_english_search_engine():
    dataset = english_tokenizer.DataSet('../Data/English.csv', has_tag=False)
    english_dataset = dataset.data
    documents = positional_indexer.create_documents_dict(english_dataset)
    dictionary = load_english_dict()
    not_stemmed_dictionary = load_not_stemmed_dict()
    bigram_index = bigram_indexer.bigram_indexer(not_stemmed_dictionary)
    print("enter query : ")
    raw_query = input()
    while (raw_query != "exit"):
        query_terms = raw_query.split(" ")
        change_flag = 0
        new_query: str = ""
        for term in query_terms:
            term_alternative = query_corrector.final_candidate(term, bigram_index)
            if (term_alternative[0][1] != 0):
                change_flag = 1
            new_query += term_alternative[0][0] + " "

        if (change_flag == 1):
            print("did you mean : " + new_query)
            print()
            print()
            raw_query = new_query
        query = english_tokenizer.analyser(raw_query)
        result = tfidf.search_for_query(query, documents, dictionary)
        # print (result)
        for i in range(min(10, len(result))):
            print("result number : " + str(i + 1) + " document number " + str(result[i][0]) + "with score : " + str(
                result[i][1]))
            print(dataset.get_value_by_id(result[i][0], 'content'))
            print()
            print()
        print("enter new query: ")
        raw_query = input()


def phase_2_positional_index_output():
    dictionary = load_english_dict()
    query = input()
    positional_indexer.show_search_result(dictionary, query)


def phase_2_bigram_index_output():
    dictionary = load_english_dict()
    res = bigram_indexer.bigram_indexer(dictionary)
    print(res)


def phase_4_query_corrector():
    dictionary = load_not_stemmed_dict()
    bigram_index = bigram_indexer.bigram_indexer(dictionary)
    term = input()
    # term = english_tokenizer.english_tokenize(term)
    res = query_corrector.final_candidate(term, bigram_index)
    print(res)


# create_positional_index_for_english()
# create_positional_index_not_stemmed_for_english()

# tf_idf_english()

# phase_2_positional_index_output()

# phase_2_bigram_index_output()

# phase_4_query_corrector()

# tf_idf_english_with_correction()

final_english_search_engine()
