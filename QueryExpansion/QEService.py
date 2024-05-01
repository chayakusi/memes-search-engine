#from indexer.solr_client import search
#from QueryExpansion.PseudoRelevanceFeedback import expandQuery
from QueryExpansion.AssociationClusters import expandQueryAC
from QueryExpansion.MetricClusters import expandQueryMC
from QueryExpansion.ScalarClusters import expandQuerySC


def run(query, rq_type, results):
    expanded_query = query
    if rq_type == 'association_clusters':
        expanded_query = expandQueryAC(query, results)
    elif rq_type == 'metric_clusters':
        expanded_query = expandQueryMC(query, results)
    elif rq_type == 'scalar_clusters':
        expanded_query = expandQuerySC(query, results)
    return expanded_query


# eq, res = run('swimming medal', 'pseudo_relevance_feedback')
# print(eq, res[0])

__all__ = ['run']
