# -*- coding: utf-8 -*-
"""
Created on Sat May 30 14:20:17 2020

@author: nitin
"""


items = {}

items[4] = 5 # Weight: Value
items[8] = 10
items[3] = 3
items[5] = 2
items[2] = 3

weight_limit = 10

def Knapsack2(items, WeightLimit):
    num_items = len(items)
    item_wts = list(items.keys())
    item_values = list(items.values())
    
    ret_list = [[0 for j in range(WeightLimit+1)] for i in range(num_items+1)]
    
    for i in range(1, num_items+1):
        for wt in range(WeightLimit+1):
            if item_wts[i-1] > wt:
                ret_list[i][wt] = ret_list[i-1][wt]
            else:
                # Since Current item weight < wt
                # That means value[wt] =
                # MAX OF 
                # current item value + cuurent best value[(wt - Current item weight)] 
                # current best value[wt]
                wght = max(item_values[i-1] + ret_list[i-1][wt - item_wts[i-1]], ret_list[i-1][wt])
                ret_list[i][wt] = wght
                
    return ret_list[num_items][WeightLimit]
            

print(Knapsack2(items,weight_limit))

                
                
            