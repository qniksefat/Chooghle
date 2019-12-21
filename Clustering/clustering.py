from Indexer import positional_indexer



def creating_data_set(raw_dataset : dict):
    documents = positional_indexer.create_documents_dict(raw_dataset)
    dictionary = positional_indexer.positional_indexer(documents, "content")

    dataset = {}