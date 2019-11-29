import math

from Indexer import bigram_indexer
import editdistance

def compute_draft_candidate (term, bigram_index: dict):
    term_bigrams = bigram_indexer.extract_bigrams(term)
    draft_candidate = []
    for this_bigram in term_bigrams:
        if (this_bigram in bigram_index.keys()):
            for word in bigram_index[this_bigram]:
                if (word not in draft_candidate):
                    draft_candidate.append(word)
    return draft_candidate

def jaccard_distance(term, draft_candidate : list):
    jaccard_distance_list = []
    term_bigrams = bigram_indexer.extract_bigrams(term)
    for candidate in draft_candidate:
        candidate_bigrams = bigram_indexer.extract_bigrams(candidate)
        delta = compute_delta(term_bigrams,candidate_bigrams)
        sum = compute_sum(term_bigrams,candidate_bigrams)
        score = len(delta) / len(sum)
        jaccard_distance_list.append((candidate,score))
    jaccard_distance_list.sort(key = lambda x : x[1])
    return jaccard_distance_list

def final_candidate(term,bigram_index):
    draft = compute_draft_candidate(term,bigram_index)
    jaccard = jaccard_distance(term,draft)
    edit_list = []
    for i in range(min(len(jaccard), 20)):
        edit_list.append(( jaccard[i][0] ,editdistance.eval(term,jaccard[i][0]) ))
    edit_list.sort(key = lambda x : x[1])
    return edit_list[0:4]


def compute_delta (l1, l2):
    res = []
    for i in l1:
        if (i not in l2):
            res.append(i)
    for i in l2:
        if (i not in l1):
            res.append(i)
    return res

def compute_sum(l1, l2):
    res = []
    for i in l1:
        if (i not in res):
            res.append(i)
    for i in l2:
        if (i not in res):
            res.append(i)
    return res