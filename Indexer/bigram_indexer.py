from Indexer import positional_indexer


def bigram_indexer(positional_dict: dict):
    terms = positional_dict.keys()
    index = {}
    for this_term in terms:
        term_bigrams = extract_bigrams(this_term)
        for this_bigram in term_bigrams:
            if (this_bigram not in index.keys()):
                index[this_bigram] = []
            index[this_bigram].append(this_term)
    return index


def extract_bigrams(term):
    res = []
    for i in range(len(term) - 1):
        res.append(term[i:i + 2])
    return res
