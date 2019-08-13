
# coding: utf-8

# In[18]:


import random
import math
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import networkx.drawing
import operator
import nbimporter
import GRAPHS

def plotting(no_of_graphs,measure_unsorted,graph_list):
    print ("-----------------------------DEGREE CENTRALITY GRAPH-------------------------------------")
    for i in range(no_of_graphs):
        plt.title('DEGREE CENTRALITY GRAPH')
        x,y=zip(* sorted(measure_unsorted[0][i].items()))
        plt.plot(x,y)
        xint=range(int(min(x)),int(math.ceil(int(max(x))+1)),len(graph_list[i])/6)
        plt.xticks(xint)
        plt.ylabel('Degree Centrality Measures')
        plt.xlabel('Node')
        plt.savefig("/home/dst-fist-server1/Desktop/jadavpur_internship/CODES/Degree_Centrality/Graph_1.png")
        plt.close()
    
    print ("-----------------------------CLOSENESS CENTRALITY GRAPH-------------------------------------")
    for i in range(no_of_graphs):
        plt.title('CLOSENESS CENTRALITY GRAPH')
        x,y=zip(* sorted(measure_unsorted[1][i].items()))
        plt.plot(x,y)
        xint=range(int(min(x)),int(math.ceil(int(max(x))+1)),len(graph_list[i])/6)
        plt.xticks(xint)
        plt.ylabel('Closeless Centrality Measures')
        plt.xlabel('Node')
        plt.savefig("/home/dst-fist-server1/Desktop/jadavpur_internship/CODES/Closeness_Centrality/Graph_1.png")
        plt.close()
    
    print ("------------------------------EIGENVECTOR CENTRALITY GRAPH---------------------------------------")
    for i in range(no_of_graphs):
        plt.title('EIGENVECTOR CENTRALITY GRAPH')
        x,y=zip(* sorted(measure_unsorted[2][i].items()))
        plt.plot(x,y)
        xint=range(int(min(x)),int(math.ceil(int(max(x))+1)),len(graph_list[i])/6)
        plt.xticks(xint)
        plt.ylabel('Eigenvector Centrality Measures')
        plt.xlabel('Node')
        plt.savefig("/home/dst-fist-server1/Desktop/jadavpur_internship/CODES/Eigenvector_Centrality/Graph_1.png")
        plt.close()
        
        
def normalized_graph(no_of_graphs,measure_unsorted,graph_list):
    normalize_val=[[[float(0.0) for k in range(len(graph_list[j]))] for i in range(3)] for j in range(no_of_graphs)]
    a=0
    b=1
    for i in range(no_of_graphs):
        for j in range(3):
            min_val=(min(measure_unsorted[j][i].items(),key=lambda z: z[1]))[1]
            max_val=(max(measure_unsorted[j][i].items(),key=lambda z: z[1]))[1]
            for k in range(len(graph_list[i])):
                normalize_val[i][j][k]=a+((measure_unsorted[j][i][k+1]-min_val)/(max_val-min_val)*(b-a))
    
    for i in range(no_of_graphs):
        plt.title('NORMALIZED GRAPH COMPARISON')
        index=[0 for k in range(len(graph_list[i]))]
        for k in range(len(graph_list[i])):
            index[k]=k+1
            
        plt.plot(index,normalize_val[i][0],label='degree centrality')
        xint=range(int(min(index)),int(math.ceil(int(max(index))+1)),len(graph_list[i])/6)
        plt.xticks(xint)
        
        plt.plot(index,normalize_val[i][1],label='closeness centrality')
        xint=range(int(min(index)),int(math.ceil(int(max(index))+1)),len(graph_list[i])/6)
        plt.xticks(xint)
        
        plt.plot(index,normalize_val[i][2],label='eigenvector centrality')
        xint=range(int(min(index)),int(math.ceil(int(max(index))+1)),len(graph_list[i])/6)
        plt.xticks(xint)
        
        plt.legend()
        plt.ylabel('Normalized Values')
        plt.xlabel('Node')
        plt.savefig("/home/dst-fist-server1/Desktop/jadavpur_internship/CODES/Normalized_graph/Graph_1.png")
        plt.close()
        
# def nodes_per_degree(no_of_graphs,graph_list,degree_of_each_node):
if __name__=='__main__':
    no_of_graphs=1
    graph_list=graph_list=[[]for i in range(no_of_graphs)]
    
    graph_list=GRAPHS.graph_create_dataset(no_of_graphs)
    
    neighbor=[[[] for j in range(len(graph_list[i]))]for i in range(no_of_graphs)]
    degree_of_each_node=[[[] for j in range(len(graph_list[i]))]for i in range(no_of_graphs)]
    print(len(graph_list[0]))
    for i in range(no_of_graphs):
        for j in range(len(graph_list[i])):
            try:
                neighbor[i][j]=list((graph_list[i].neighbors(j+1)))
            except:
                neighbor[i][j]=list()
            if(len(neighbor[i][j])==1 and neighbor[i][j][0]==j+1):
                degree_of_each_node[i][j]=0
            else:
                degree_of_each_node[i][j]=len(neighbor[i][j])
     
    degree_count=[int(0) for i in range(len(graph_list[i]))]
    for i in range(no_of_graphs):
        index=[0 for k in range(len(graph_list[i]))]
        for k in range(len(graph_list[i])):
            index[k]=k+1
    
    for i in range(no_of_graphs):
        for j in range(len(graph_list[i])):
            degree_count[int(degree_of_each_node[i][j])]=degree_count[int(degree_of_each_node[i][j])]+1
            
            
    plt.title('NUMBER OF NODES PER DEGREE VALUE')
    plt.plot(index,degree_count,label='degree distribution')
    xint=range(int(min(index)),int(math.ceil(int(max(index))+1)),len(graph_list[i])/6)
    plt.xticks(xint)
    plt.legend()
    plt.ylabel('No. of Nodes with that degree value')
    plt.xlabel('Degree Value')
    plt.savefig("/home/dst-fist-server1/Desktop/jadavpur_internship/CODES/Degree_distribution/Graph_1.png")
    plt.close()       
                

