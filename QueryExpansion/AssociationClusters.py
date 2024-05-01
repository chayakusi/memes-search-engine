# Query Expansion using Association Clusters
from collections import defaultdict
from QueryExpansion.util import tokenize_and_stem, process_documents, tuple_to_string


# from indexer.solr_client import search

def findAssociations(localVocab, queryStems, doc_dict):
    associations = defaultdict(int)
    for stem in localVocab:
        for qStem in queryStems:
            cu = 0
            cv = 0
            for doc_terms in doc_dict.values():
                cs = doc_terms.count(stem)
                cqs = doc_terms.count(qStem)
                cu += cs
                cv += cqs
                associations[(qStem, stem)] += (cs*cqs)
            associations[(qStem, stem)] /= (cu*cu+cv*cv+cu*cv)
    return associations


def expandQueryAC(query, resultSet):
    queryStems = tokenize_and_stem(query)
    tokens, doc_dict = process_documents(resultSet)

    localVocab = set(tokens)
    associations = findAssociations(localVocab, queryStems, doc_dict)
    associations = sorted(associations.items(), key = lambda item:item[1], reverse = True)[:10]
    for item in associations:
        if item[0][1] not in queryStems:
            query += " " + item[0][1]
            queryStems.append(item[0][1])
    return tuple_to_string(query)

# docs = search('swimming medals', 30)
# print(docs[0])
# new = expandQueryAC('olympics medals', docs)
# print(new)
# docs1 = search(new, 30)
# print(docs1[0])

# expandQueryAC('swimming medals', docs)