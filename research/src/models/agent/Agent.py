"""super class of Agent"""
#-*- coding: utf-8 -*-

# author : Takuro Yamazaki
# last update : 05/23/2017
# description : エージェントの親モデル

import numpy as np

class Agent(object):
    """super class of agent"""
    def __init__(self, agent_id: int, neighbors: np.ndarray, state_set: np.ndarray, action_set: np.ndarray):
        self.agent_id = agent_id
        self.neighbors = neighbors
        self.action_set = action_set #action文字列の集合
        self.state_set = state_set #state文字列の集合
        self.reward_lst = []
        self.prev_action = None
        self.c_st = 0
        self.len_a = len(action_set)
        self.len_s = len(state_set)

    def get_neighbors(self):
        return self.neighbors

    def update_q(self, *args, **kwargs):
        pass

    def act(self, *args, **kwargs):
        pass
