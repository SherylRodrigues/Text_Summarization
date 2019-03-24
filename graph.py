#!/usr/bin/env python 
# -- coding: utf-8 -- 

import codecs
import re
each_one=[]
list_of_sentences=[]
with codecs.open('sov.txt', encoding='utf-8') as f:
    text=f.read()
#def split_sentences(text):
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
    for stuff in sentences:
        list_of_sentences.append(stuff)
        print stuff  
        
print(list_of_sentences)

f = open('sov_dict.txt', 'r')
subject_list=[]
object_list=[]
verb_list=[]
pos_triple=[]
newDict = {}
for sent in list_of_sentences:
    for line in f:
        k,v = line.strip().split('/')
        newDict[k.strip()] = v.strip()
        if v=='N-NNP':
            subject_list.append(k)
            print('SUBJECT:',subject_list)
            #for i in subject_list[0]:
                #print(i)
        if v=='N-NN':
            object_list.append(k)
            print('OBJECT',object_list)                 
        if v=='V-VM-VF':
            verb_list.append(k)
            print('VERB',verb_list)
        
        pos_triple=subject_list+object_list+verb_list
            
            %matplotlib notebook
import networkx as nx
import matplotlib.pyplot as pl
from matplotlib.font_manager import FontProperties
prop= FontProperties()

labels={}
graph = nx.Graph()

#words= ["सनरायझर्साक","विकेटीन","जैत"]

for subject in subject_list:
    s=subject.decode('utf-8')
    graph.add_node(s)
    labels[s]=s

    
for obj in object_list:
    b=obj.decode('utf-8')
    graph.add_node(b)
    labels[b]=b
    
for verb in verb_list:
    v=verb.decode('utf-8')
    graph.add_node(v)
    labels[v]=v
#for word in pos_triple:
   # w = word.decode('utf-8')
   # graph.add_node(w)
   # labels[w]=w
    
graph.add_edge(subject_list[0].decode('utf-8'),object_list[0].decode('utf-8'))
graph.add_edge(object_list[0].decode('utf-8'),verb_list[0].decode('utf-8'))

graph.add_edge(subject_list[1].decode('utf-8'),object_list[1].decode('utf-8'))
graph.add_edge(object_list[1].decode('utf-8'),verb_list[1].decode('utf-8'))


graph.add_edge(subject_list[2].decode('utf-8'),object_list[2].decode('utf-8'))
graph.add_edge(object_list[2].decode('utf-8'),verb_list[2].decode('utf-8'))

graph.add_edge(subject_list[3].decode('utf-8'),object_list[3].decode('utf-8'))
graph.add_edge(object_list[3].decode('utf-8'),verb_list[3].decode('utf-8'))

graph.add_edge(subject_list[4].decode('utf-8'),object_list[4].decode('utf-8'))
graph.add_edge(object_list[4].decode('utf-8'),verb_list[4].decode('utf-8'))
graph.add_edge(subject_list[5].decode('utf-8'),object_list[5].decode('utf-8'))
graph.add_edge(object_list[5].decode('utf-8'),verb_list[5].decode('utf-8'))

pos=nx.spring_layout(graph)
nx.draw(graph, with_labels = True, font_family = "Nirmala UI", node_size = 40, font_size = 10, node_color = "lightblue")
pl.show()

