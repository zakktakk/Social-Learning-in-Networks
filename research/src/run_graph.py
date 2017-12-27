#-*- coding: utf-8 -*-
# author : Takuro Yamazaki
# description : グラフ構造とアルゴリズムごとの結果の違い

import os
from collections import OrderedDict

"""simulation world"""
from world import synchro_world

"""network"""
from networks import network_utils

"""agent"""
# defaultはこの4種類にしよう
from agent import WoLF_PHC_Agent as wpa
from agent import Q_Learning_Agent as ql
from agent import Actor_Critic_Agent as aca
from agent import SARSA_Agent as sarsa

"""payoff matrix"""
from world.payoff_matrix import *

graph_prefix = "../src/networks/"

# graphの定義
cG = network_utils.graph_generator.complete_graph
pcG = network_utils.graph_generator.powerlaw_cluster_graph

all_graph = OrderedDict((("powerlaw_cluster",pcG), ("complete",cG),
                         ("multiple_clustered",graph_prefix+"multiple_clustered.gpickle"),
                         ("inner_dence_clustered", graph_prefix+"inner_dence_clustered.gpickle"),
                         ("one_dim_regular", graph_prefix+"onedim_regular.gpickle")))

# payoffmatrixの定義
all_matrix = ["prisoners_dilemma"]

# agentの定義
all_agent = OrderedDict((("q",ql.Q_Learning_Agent), ("wolf_phc",wpa.WoLF_PHC_Agent), ("actor_critic",aca.Actor_Critic_Agent)))
# all_agent = {"sarsa":sarsa.SARSA_Agent}

RESULT_DIR = "../results/graph/"
for ag in all_agent.keys():
    if not os.path.exists(RESULT_DIR+ag):
        os.makedirs(RESULT_DIR+ag)
    print(ag)
    for G in all_graph:
        if not os.path.exists(RESULT_DIR+ag+"/"+G):
            os.makedirs(RESULT_DIR+ag+"/"+G)
        print("  "+G)
        for g in all_matrix:
            print("    "+g)
            RESULT_NAME = RESULT_DIR+ag+"/"+G+"/"+g
            W = synchro_world.synchro_world(100, 1000, eval(g)(), all_graph[G], all_agent[ag])
            W.run()
            W.save(RESULT_NAME)

print('done!!')
