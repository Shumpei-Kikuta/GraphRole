import warnings
from pprint import pprint

import networkx as nx

from graphrole import RecursiveFeatureExtractor, RoleExtractor


# load the well known karate_club_graph from Networkx
# edgelist = pd.read_csv("../")
# G = nx.from_pandas_edgelist()
G = nx.barbell_graph(10, 10)

# extract features
feature_extractor = RecursiveFeatureExtractor(G)
features = feature_extractor.extract_features()

role_extractor = RoleExtractor(n_roles=2)
role_extractor.extract_role_factors(features)

print(f'\nFeatures extracted from {feature_extractor.generation_count} recursive generations:')
print(features)
print(role_extractor.roles)