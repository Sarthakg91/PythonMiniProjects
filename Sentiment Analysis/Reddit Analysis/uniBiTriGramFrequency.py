# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 23:56:09 2016

@author: Sarthak Ghosh
"""
#Frequency of uni,bi and trigrams in reddit posts
import pandas as pd
import matplotlib.pyplot as plt 
import statistics as stats
import nltk
from nltk.util import ngrams
from operator import itemgetter
from tabulate import tabulate


columnnames=['UserId','Date','UserName','Subject','Post']
df=pd.read_csv('C:\Users\Sarthak Ghosh\Documents\GaTech\Data Analytics\Assignment_I\Subreddit_Posts_1.csv',names=columnnames)
dateAndTime= df.Date.tolist()
usernames=df.UserName.tolist();
posts=df.Post.tolist();
titles=df.Subject.tolist()

length_of_posts=[]
length_of_titles=[]
for post in posts:
    length_of_posts.append(len(post.split(' ')))    
#print length_of_posts
for title in titles:
    length_of_titles.append(len(title.split(' ')))

print "mean_of_posts"

mean_of_posts=stats.mean(length_of_posts)

print mean_of_posts

print "mean of titles"
mean_of_titles=stats.mean(length_of_titles)
print mean_of_titles
#print " mean of titles"
#print mean_of_titles
#print " mean of posts"
#print mean_of_posts
print "sdev_posts"
sdev_posts=stats.pstdev(length_of_posts)
print sdev_posts
print "sdev_titles"
sdev_titles=stats.pstdev(length_of_titles)
print sdev_titles
#print sdev_titles




listOfUniGrams_belowMean=[]
listOfUniGrams_aboveMean=[]
listOfBiGrams_belowMean=[]
listOfBiGrams_aboveMean=[]
listOfTriGrams_belowMean=[]
listOfTriGrams_aboveMean=[]
for post in posts: 
    unigrams=ngrams(post.split(), 1)
    bigrams=ngrams(post.split(), 2)
    trigrams=ngrams(post.split(), 3)
    if len(post.split(' '))>mean_of_posts:
        for unigram in unigrams:
            listOfUniGrams_aboveMean.append(unigram)
        for bigram in bigrams:
            listOfBiGrams_aboveMean.append(bigram)
        for trigram in trigrams:
            listOfTriGrams_aboveMean.append(trigram)
    elif len(post.split(' '))<mean_of_posts:
        for unigram in unigrams:
            listOfUniGrams_belowMean.append(unigram)
        for bigram in bigrams:
            listOfBiGrams_belowMean.append(bigram)
        for trigram in trigrams:
            listOfTriGrams_belowMean.append(trigram)
        

ftrib=[]#freq of tri grams below mean 
ftria=[]#freq of tri grams above mean
fbib=[]#freq of bi grams below mean
fbia=[]#freq of bi grams above mean
funib=[]#freq of uni grams elow mean
funia=[]#frew of uni grams above mean 

#get freq distribution for those below mean 
fdist = nltk.FreqDist(listOfTriGrams_belowMean)

#sort according to the frequencies
for k,v in fdist.items():
    ftrib.append((k,v))
ftrib.sort(key=lambda tup: tup[1], reverse=True)

#get freq distribution for those above mean 
fdist = nltk.FreqDist(listOfTriGrams_aboveMean)
#sort according to the frequencies
for k,v in fdist.items():
    ftria.append((k,v))
ftria.sort(key=lambda tup: tup[1], reverse=True)


 #get freq distribution of bi grams above mean        
fdist = nltk.FreqDist(listOfBiGrams_aboveMean)
#sort according to the frequencies
for k,v in fdist.items():
    fbia.append((k,v))
fbia.sort(key=lambda tup: tup[1], reverse=True)

#get freq distribution of bi grams below mean  
fdist = nltk.FreqDist(listOfBiGrams_belowMean)
#sort according to the frequencies
for k,v in fdist.items():
    fbib.append((k,v))
fbib.sort(key=lambda tup: tup[1], reverse=True)

#get freq distribution of uni grams below mean 
fdist = nltk.FreqDist(listOfUniGrams_belowMean)

#sort according to the frequencies
for k,v in fdist.items():
    funib.append((k,v))
    
funib.sort(key=lambda tup: tup[1], reverse=True)

#get freq distribution of uni grams above mean 
fdist = nltk.FreqDist(listOfUniGrams_aboveMean)
for k,v in fdist.items():
    funia.append((k,v))
#sort according to the frequencies
funia.sort(key=lambda tup: tup[1], reverse=True)


#finding the max frequency of any uni-, bi-, or tri-gram
max_freq_below_mean=max(fbib[0],ftrib[0],funib[0], key=itemgetter(1))
max_freq_above_mean=max(fbia[0],ftria[0],funia[0], key=itemgetter(1))

templist=[]
fbib_top_25=[]

print "Bi-grams for posts below mean"
#forming 25 rows of the forme (n-gram, raq freq, normalized freq) for 6 tables
for i in range(25): 
    #print fbib[i][1]/20        
    templist.append(fbib[i][0])#appending the n-gram tuple
    #print templist
    templist.append(fbib[i][1])#appending the raw freq
    templist.append(float(fbib[i][1])/max_freq_below_mean[1])
    templist_copy = [item for item in templist]
    fbib_top_25.append(templist_copy)
#    fbib_top_25.append(templist)
    templist[:]=[]
    
print tabulate(fbib_top_25,headers=["bi-gram","raw freq", "normalized freq"],tablefmt="grid")

print
print
print "Bi-grams for posts above mean"
fbia_top_25=[]
for i in range(25): 
    #print fbib[i][1]/20      
    templist.append(fbia[i][0])#appending the n-gram tuple
    templist.append(fbia[i][1])#appending the raw freq
    templist.append(float(fbia[i][1])/max_freq_above_mean[1])
    templist_copy = [item for item in templist]
    fbia_top_25.append(templist_copy)
#    fbia_top_25.append(templist)
    templist[:]=[]
       
print tabulate(fbia_top_25,headers=["bi-gram","raw freq", "normalized freq"],tablefmt="grid")



print
print
funia_top_25=[]
print "uni-grams for posts above mean"
for i in range(25): 
        
    templist.append(funia[i][0])#appending the n-gram tuple
    templist.append(funia[i][1])#appending the raw freq
    templist.append(float(funia[i][1])/max_freq_above_mean[1])
    templist_copy = [item for item in templist]
    funia_top_25.append(templist_copy)
    templist[:]=[]

print tabulate(funia_top_25,headers=["uni-gram","raw freq", "normalized freq"],tablefmt="grid")
print
print
print "tri-grams for posts above mean"
ftria_top_25=[]
for i in range(25): 
        
    templist.append(ftria[i][0])#appending the n-gram tuple
    templist.append(ftria[i][1])#appending the raw freq
    templist.append(float(ftria[i][1])/max_freq_above_mean[1])
    templist_copy = [item for item in templist]
    ftria_top_25.append(templist_copy)
    templist[:]=[]
       
print tabulate(ftria_top_25,headers=["tri-gram","raw freq", "normalized freq"],tablefmt="grid")
print
print

print "uni-grams for posts below mean"
funib_top_25=[]
for i in range(25): 
    #print fbib[i][1]/20
    
    
    templist.append(funib[i][0])#appending the n-gram tuple
    templist.append(funib[i][1])#appending the raw freq
    templist.append(float(funib[i][1])/max_freq_below_mean[1])
    templist_copy = [item for item in templist]
    funib_top_25.append(templist_copy)
    templist[:]=[]
       

print tabulate(funib_top_25,headers=["uni-gram","raw freq", "normalized freq"],tablefmt="grid")
#print fbib_top_25
print
print
print "tri-grams for posts below mean"
ftrib_top_25=[]
for i in range(25): 
    #print fbib[i][1]/20  
    
    templist.append(ftrib[i][0])#appending the n-gram tuple
    templist.append(ftrib[i][1])#appending the raw freq
    templist.append(float(ftrib[i][1])/max_freq_below_mean[1])
    templist_copy = [item for item in templist]
    ftrib_top_25.append(templist_copy)
    templist[:]=[]

print tabulate(ftrib_top_25,headers=["tri-gram","raw freq", "normalized freq"],tablefmt="grid")




