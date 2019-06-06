# -*- coding: utf-8 -*-
"""
Created on Fri Mar 04 13:35:34 2016

@author: Sarthak Ghosh
"""
import re
index_array={}
index_array_2={}
def get_moral_lexicons(moralString):
    
    mapFlag=0;
    start_lex_flag=0
    indexToSearch=""
    l_item=""
    lexicon_str = "("
    with open("MoralFoundations.dic", "r") as file_handle:
        for line in file_handle:
            
            lexicon_item = line.strip()
            
            if'%' in lexicon_item and mapFlag==0:
                #first % has been found
                mapFlag=1
                continue
            elif mapFlag==1 and '%' not in lexicon_item:
                item=lexicon_item.split()
                #print item
                index_array[item[0]]=item[1]
                index_array_2[item[1]]=item[0]
                if moralString in item[1]:
                    indexToSearch=item[0]
            elif mapFlag==1 and '%' in lexicon_item:
                mapFlag=0
                start_lex_flag=1
                continue
            elif start_lex_flag==1 and len(indexToSearch)!=0 and len(lexicon_item)!=0:
                item=lexicon_item.split()
                if indexToSearch in item:
                    #print "found word"
                    if "*" in item[0]:
                        l_item = r"\b{0}\b".format(item[0].replace("*", ".*?"))
                    else:
                        l_item = r"\b{0}\b".format(item[0])
                    
                    lexicon_str += l_item + "|"
    lexicon_str = lexicon_str[:-1] + ")"
    #print lexicon_str
    #lexicon.append(lexicon_str)
    return lexicon_str

def get_all_moral_lexicons():
    moral_lexicons = {}
    moral_lexicons["HarmVirtue"] = get_moral_lexicons("HarmVirtue")
    moral_lexicons["HarmVice"] = get_moral_lexicons("HarmVice")
    moral_lexicons["FairnessVirtue"] = get_moral_lexicons("FairnessVirtue")
    moral_lexicons["FairnessVice"] = get_moral_lexicons("FairnessVice")	
    moral_lexicons["IngroupVirtue"] = get_moral_lexicons("IngroupVirtue")
    moral_lexicons["IngroupVice"] = get_moral_lexicons("IngroupVice")
    moral_lexicons["AuthorityVirtue"] = get_moral_lexicons("AuthorityVirtue")
    moral_lexicons["AuthorityVice"] = get_moral_lexicons("AuthorityVice")
    moral_lexicons["PurityVirtue"] = get_moral_lexicons("PurityVirtue")
    moral_lexicons["PurityVice"] = get_moral_lexicons("PurityVice")
    moral_lexicons["MoralityGeneral"] = get_moral_lexicons("MoralityGeneral") 
    return moral_lexicons

def get_dictionary_of_counts(post, moral_lexicons):
    moral_lexicon_to_count = {}
    for moral_lexicon_name in set(moral_lexicons.keys()):
        moral_lexicon_to_count[moral_lexicon_name] = 0

    for moral_lexicon_name, moral_lexicon_item in moral_lexicons.iteritems():
        #print moral_lexicon_item        
        pattern = re.compile(moral_lexicon_item)
        #print pattern
        count = len(pattern.findall(post))
        moral_lexicon_to_count[moral_lexicon_name] += count
    return moral_lexicon_to_count
    
        
                    
             
            
         


             
                    
	      
             
		     

		     
        
    
        
 
 

