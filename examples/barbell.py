import warnings
from pprint import pprint

import networkx as nx
import pandas as pd

from graphrole import RecursiveFeatureExtractor, RoleExtractor


for node_num in [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
    # load the well known karate_club_graph from Networkx
    edgelist = pd.read_csv("../graph/{}_5_double_barbell.edgelist".format(node_num), sep=" ", header=None)
    edgelist = edgelist.rename(columns={0: "source", 1: "target"})
    G = nx.from_pandas_edgelist(edgelist)

    # extract features
    feature_extractor = RecursiveFeatureExtractor(G)
    features = feature_extractor.extract_features()

    role_extractor = RoleExtractor(n_roles=None)
    role_extractor.extract_role_factors(features)

    print(f'\nFeatures extracted from {feature_extractor.generation_count} recursive generations:')
    print(features)
    print(role_extractor.roles)
    print(role_extractor.role_percentage)

    df = role_extractor.role_percentage
    df[0] = df.index
    print(df)
    cols = [0] + ["role_{}".format(i) for i in range(df.shape[1] - 1)]
    df.to_csv("../emb/{}_5_double_barbell.emb".format(node_num), sep=" ", index=False, columns=cols)
