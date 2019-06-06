# -*- coding: utf-8 -*-
"""
Created on Fri Mar 04 16:30:50 2016

@author: Sarthak Ghosh
"""
#morality in posts
import pandas as pd
from tabulate import tabulate
import statistics
import moralLexiconDicOpen

#load the files
columnnames=['UserId','Date','UserName','Subject','Post']
df=pd.read_csv('C:\Users\Sarthak Ghosh\Documents\GaTech\Data Analytics\Assignment_I\Subreddit_Posts_1.csv',names=columnnames)
posts=df.Post.tolist()

all_moral_lexicons = moralLexiconDicOpen.get_all_moral_lexicons()

moralDimensions=["HarmVirtue", "HarmVice", "FairnessVirtue",
"FairnessVice", "IngroupVirtue", "IngroupVice", "AuthorityVirtue", "AuthorityVice", "PurityVirtue",
"PurityVice", "MoralityGeneral"]

d = {}
for item in moralDimensions:
    d[item] = []
    
list_of_mg = []
for post in posts:
    outCountDict =  moralLexiconDicOpen.get_dictionary_of_counts(post, all_moral_lexicons)  
    for item in moralDimensions:
        d[item].append(float(outCountDict[item])/len(post.split(' ')))
    list_of_mg.append(d[moralDimensions[-1]][-1])
 
sorted_indices = sorted(range(len(list_of_mg)), key = lambda k:list_of_mg[k])

print "low morality general scores :"
for index in sorted_indices[:5]:
    print posts[index], list_of_mg[index] 
print "high morality general scores :"
for index in sorted_indices[-5:]:
    print posts[index], list_of_mg[index] 
    
final_list = []      
for item in moralDimensions:
    final_list.append([item,statistics.mean(d[item]),statistics.median(sorted(d[item])),statistics.pstdev(d[item])])
 
print tabulate(final_list, headers=["moral_dimensions","mean","median","sdev"],tablefmt="grid")
 