from QueryExpansion.util import tokenize_and_stem, process_documents, tuple_to_string
import numpy as np
# from indexer.solr_client import search
def findScalars(vocab, queryStems, docs):
    scalars = {}
    documents_terms = []
    doc_dict = {}
    i = 1
    for doc in (docs):
        documents_terms.extend(doc)
        doc_dict[i] = doc
        i += 1
    doc_terms = []
    for term in documents_terms:
        if term not in doc_terms:
            doc_terms.append(term)
    relevant_docs = docs
    # print(doc_terms.count('medal'))
    vector_relevant = []
    for doc in relevant_docs:
        rel_vec = np.zeros(len(doc_terms))
        for term in doc:
            count = doc.count(term)
            rel_vec[doc_terms.index(term)] = count
        vector_relevant.append(rel_vec)

    temp = np.array(vector_relevant)
    temp = temp.transpose()
    correlationMatrix = np.matmul(temp, temp.transpose())
    shape_temp = correlationMatrix.shape

    for i in range(shape_temp[0]):
        for j in range(shape_temp[1]):
            if correlationMatrix[i][j] != 0:
                correlationMatrix[i][j] = correlationMatrix[i][j] / (
                            correlationMatrix[i][j] + correlationMatrix[i][i] + correlationMatrix[j][j])

    for stem in queryStems:
        for word in vocab:
            if stem not in doc_terms:
                s = [0 for _ in range(shape_temp[0])]
                stem_vector = s
            else:
                s = doc_terms.index(stem)
                stem_vector = correlationMatrix[s]
            w = doc_terms.index(word)
            word_vector = correlationMatrix[w]
            val = np.dot(stem_vector, word_vector)
            if val != 0:
                val /= np.linalg.norm(stem_vector)
                val /= np.linalg.norm(word_vector)
            scalars[(stem, word)] = val
    return scalars

def expandQuerySC(query, resultSet):

    queryStems = tokenize_and_stem(query)
    tokens, doc_dict = process_documents(resultSet)

    localVocab = list(set(tokens))
    scalars = findScalars(sorted(localVocab), queryStems, doc_dict.values())
    scalars = sorted(scalars.items(), key=lambda item : item[1], reverse=True)[:10]
    for item in scalars:
        if item[0][1] not in queryStems:
            query += ' ' + item[0][1]
            queryStems.append(item[0][1])
    result = tuple_to_string(query)
    return result

# docs = search('olympics medals', 5)
# print(docs[0])
# new = expandQuerySC('olympics medals', docs)
# print(new)
# docs1 = search(new, 30)
# print(docs1[0])
