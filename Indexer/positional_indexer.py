import pickle

def create_documents_dict (documents):
    result = {}
    for document in documents:
        result[document["id"]] = document
    return result

def positional_indexer(documents : dict, field):
    index = {}
    for this_doc_id in documents.keys():
        this_document : dict= documents[this_doc_id]
        this_doc_content : list = this_document[field]
        for position in range(len(this_doc_content)):
            term = this_doc_content[position]
            if term in index.keys():
                posting_list : dict = index[term]
                if this_doc_id in posting_list.keys():
                    this_term_positions : list = posting_list[this_doc_id]
                    this_term_positions.append(position + 1)
                else:
                    posting_list[this_doc_id] = []
                    posting_list[this_doc_id].append(position + 1)
            else:
                index[term] = {}
                posting_list : dict= index[term]
                posting_list[this_doc_id] = []
                posting_list[this_doc_id].append(position+1)
    return index

def remove_document_from_index(id, index : dict):
    if ( id not in index.keys()):
        return index
    index.pop(index[id])
    return index

def add_document_to_index(document : dict, index : dict) :
    if (document["id"] in index):
        return index
    index[document["id"]] = document
    return index

def get_posting_list(index: dict, term):
    if term in index:
        return index[term]
    else:
        return None

def show_search_result (index : dict, term):
    posting_list : dict = get_posting_list(index,term)
    if posting_list is None:
        print("term is not find in documents")
    else:
        print ("this term posting list is " + str(posting_list))
        print()
        for doc_id in posting_list.keys():
            positions : list = posting_list[doc_id]
            positions_text = ""
            for i in range(len(positions)):
                positions_text += str(positions[i])
                positions_text += ", "
            positions_text = positions_text[0:-2]
            print ("\"" + str(term) + "\" found in document " + str(doc_id) + " in this positions: " + positions_text)

def search_for_term(term, index):
    posting_list : dict = get_posting_list(index,term)
    result = []
    if (posting_list == None) :
        return result
    for docid in posting_list.keys():
        result.append(docid)
    return result

def write_index_on_file(index,name):
    file = open("Data\\" + name + ".pkl", "wb")
    pickle.dump(index, file)
    file.close()

def load_index(name):
    file = open("Data\\" + name + ".pkl", "rb")
    index = pickle.load(file)
    file.close()
    return index
