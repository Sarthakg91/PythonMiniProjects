# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 23:06:10 2016

@author: Sarthak Ghosh


"""

# plotting the number of posts per day

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

csv =np.loadtxt('C:\Users\Sarthak Ghosh\Documents\GaTech\Data Analytics\Assignment_I\Subreddit_Posts.csv', delimiter=',', usecols=(0,1,2), unpack=True, dtype=np.str)
df=pd.read_csv('C:\Users\Sarthak Ghosh\Documents\GaTech\Data Analytics\Assignment_I\Subreddit_Posts.csv',sep=',')

array_of_dates_and_times=csv[1:2]

array_of_user_names=csv[2:]

dates=[]
times=[]
user_names=[]
daily_usernames=[]
num_of_rows=len(array_of_dates_and_times[0])

i=1
while i<num_of_rows:
    temp=array_of_dates_and_times[0][i].split()
    user_names.append(array_of_user_names[0][i])
    dates.append(temp[0])
    times.append(temp[-1])
    i+=1

#print dates
#print times
#print user_names

unique_dates=[]
number_of_posts=[]

unique_dates.append(dates[0])

i=1
count=1;
while i<len(dates):
    if  dates[i]==unique_dates[-1]:
        count+=1
        i+=1
        
    else:
        number_of_posts.append(count)
        count=1
        unique_dates.append(dates[i])     
        i+=1

number_of_posts.append(count)

print unique_dates
print number_of_posts
plt.plot(number_of_posts)

    
    
