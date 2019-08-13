
# coding: utf-8

# In[2]:

#import sys

#import nbimporter
import random
import math
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import networkx.drawing
import operator

#import GRAPHS
#import time_cost
#import Centrality_graph
                
###########################-----------------------------------------------------------##################################

def graph_create_dataset(graph_no):
    graph=[[]for i in range(graph_no)]
    """with open("/home/sukanya/Desktop/jadavpur_internship/CODES/dataset/facebook.txt") as fp1:  
        graph[0]=nx.Graph()
        for line in fp1:
            temp=line.split(" ")
            x=int(temp[0])
            y=int((temp[1].split("\n"))[0])
            graph[0].add_edges_from([(x,y)])"""
    
    """with open("/home/sukanya/Desktop/jadavpur_internship/CODES/dataset/hamster.txt") as fp2:
         graph[0]=nx.Graph()
         for line in fp2:
             temp=line.split(" ")
             x=int(temp[0])
             y=int((temp[1].split("\n"))[0])
             graph[0].add_edges_from([(x,y)])"""
            
    """with open("/home/sukanya/Desktop/jadavpur_internship/CODES/dataset/hamster_full.txt") as fp3:
         graph[0]=nx.Graph()
         for line in fp3:
             temp=line.split(" ")
             x=int(temp[0])
             y=int((temp[1].split("\n"))[0])
             graph[0].add_edges_from([(x,y)])"""
    
    """with open("/home/sukanya/Desktop/jadavpur_internship/CODES/dataset/google_plus.txt") as fp4:
         graph[0]=nx.Graph()
         for line in fp4:
             temp=line.split(" ")
             x=int(temp[0])
             y=int((temp[1].split("\n"))[0])
             graph[0].add_edges_from([(x,y)])"""
    
    """with open("/home/sukanya/Desktop/jadavpur_internship/CODES/dataset/twitter.txt") as fp5:
         graph[0]=nx.Graph()
         for line in fp5:
             temp=line.split(" ")
             x=int(temp[0])
             y=int((temp[1].split("\n"))[0])
             graph[0].add_edges_from([(x,y)])"""
            
    with open("/home/sukanya/Desktop/jadavpur_internship/CODES/dataset/brightkite.txt") as fp6:   
         graph[0]=nx.Graph()
         for line in fp6:
             temp=line.split(" ")
             x=int(temp[0])
             y=int((temp[1].split("\n"))[0])
             graph[0].add_edges_from([(x,y)])
            
    #with open("/home/sukanya/Desktop/jadavpur_internship/CODES/dataset/Epinions.txt") as fp7:
         #graph[0]=nx.Graph()
         #for line in fp7:
             #temp=line.split(" ")
             #x=int(temp[0])
             #y=int((temp[1].split("\n"))[0])
             #graph[0].add_edges_from([(x,y)])"""
            
    """with open("/home/sukanya/Desktop/jadavpur_internship/CODES/dataset/facebook_wosn.txt") as fp8:
         graph[0]=nx.Graph()
         for line in fp8:
             temp=line.split(" ")
             x=int(temp[0])
             y=int((temp[1].split("\n"))[0])
             graph[0].add_edges_from([(x,y)])"""
              
            
    """with open("/home/sukanya/Desktop/jadavpur_internship/CODES/dataset/slashdot.txt") as fp9:
         graph[0]=nx.Graph()
         for line in fp9:
             temp=line.split(" ")
             x=int(temp[0])
             y=int((temp[1].split("\n"))[0])
             graph[0].add_edges_from([(x,y)])"""

    """with open("/home/sukanya/Desktop/jadavpur_internship/CODES/dataset/advogato.txt") as fp10:   
             graph[0]=nx.Graph()
             for line in fp10:
                 temp=line.split(" ")
                 x=int(temp[0])
                 y=int((temp[1].split("\n"))[0])
                 graph[0].add_edges_from([(x,y)])"""
            
     #     nx.draw(graph[0],with_labels=True,node_size=50,font_size=8)
#     plt.show()
#     nx.draw(graph[1],with_labels=True,node_size=50,font_size=8)
#     plt.show()
#     nx.draw(graph[2],with_labels=True,node_size=50,font_size=8)
#     plt.show()
#     nx.draw(graph[3],with_labels=True,node_size=50,font_size=8)
#     plt.show()
#     nx.draw(graph[4],with_labels=True,node_size=50,font_size=8)
#     plt.show()

    return(graph)
           
    


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
        plt.savefig("/home/sukanya/Desktop/jadavpur_internship/CODES/Degree_Centrality/Graph_9.png")
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
        plt.savefig("/home/sukanya/Desktop/jadavpur_internship/CODES/Closeness_Centrality/Graph_9.png")
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
        plt.savefig("/home/sukanya/Desktop/jadavpur_internship/CODES/Eigenvector_Centrality/Graph_9.png")
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
        plt.savefig("/home/sukanya/Desktop/jadavpur_internship/CODES/Normalized_graph/Graph_9.png")
        plt.close()

def time_cost_calc(stack,top_val1,neighbor_nodes,l):
    key=0
    dup=0
    length=0
    top_val2=top_val1
    time=1
    test=0
#     print (str(top_val1))
    while(test<100):      #(not(top_val1==-1 and top_val2==(l-1))):
        if(top_val1==-1):
            top_val1=top_val2
#             print(stack)
#             print(top_val1)
            time=time+1
            test=test+1
            if(top_val1+1==l):
                break
        else:
            key=int(stack[top_val1])
            length=len(neighbor_nodes[key-1])
            for i in range(length):
                for j in range(top_val2+1):
                    if(neighbor_nodes[key-1][i]==stack[j]):
                        dup=1
                        break
                    else:
                        dup=0
                    
                if(dup==0):
                    top_val2=top_val2+1
                    stack[top_val2]=neighbor_nodes[key-1][i]
            top_val1=top_val1-1
#     print ""
    return(time)
    


if __name__=='__main__':
    no_of_graphs=1
    graph_list=[[]for i in range(no_of_graphs)]    
    graph_list=graph_create_dataset(no_of_graphs)
    print(graph_list)
    measure=[[[]for i in range(no_of_graphs)]for j in range(3)]       ### 3 for the three centrality measures
    measure_unsorted=[[[]for i in range(no_of_graphs)]for j in range(3)]
    
    for j in range(no_of_graphs):
    	measure[0][j]=nx.degree_centrality(graph_list[j])
        print("1")
        measure_unsorted[0][j]=measure[0][j]
        measure[0][j]=sorted(measure[0][j].items(),key=operator.itemgetter(1),reverse=True)  ## descending
        
    for j in range(no_of_graphs):
        measure[1][j]=nx.closeness_centrality(graph_list[j])
        print("2")
        measure_unsorted[1][j]=measure[1][j]
        measure[1][j]=sorted(measure[1][j].items(),key=operator.itemgetter(1),reverse=True)   ## descending
        
    for j in range(no_of_graphs):
        measure[2][j]=nx.eigenvector_centrality_numpy(graph_list[j])
        print("3")
        measure_unsorted[2][j]=measure[2][j]
        measure[2][j]=sorted(measure[2][j].items(),key=operator.itemgetter(1),reverse=True)  ## descending     

    with open("/home/sukanya/Desktop/jadavpur_internship/CODES/Result_corr_coeff.odt","a+") as sn:
        sn.write("\n")
        sn.write(" FOR GRAPH 6 :----")
        sn.write("\n\n")
        ##### correlation coefficient between degree and closeness centrality  
        a,b=zip(* sorted(measure_unsorted[0][i].items()))
        x=b
        a,b=zip(* sorted(measure_unsorted[1][i].items()))
        y=b
        corr_coeff=np.corrcoef(x,y)[0,1]
        sn.write("Correlation Coefficient between Degree and Closeness Centrality : "+str(corr_coeff))
        sn.write("\n")
        plt.title('CORRELATION_COEFFICIENT')
        plt.scatter(x,y)
        plt.ylabel('closeness_centrality_values')
        plt.xlabel('degree_centrality_values')
        plt.savefig("/home/sukanya/Desktop/jadavpur_internship/CODES/Correlation_Coefficifent/degree_closeness/Graph_6.png")
        plt.close()
        
        ##### correlation coefficient between closeness and eigenvector centrality  
        a,b=zip(* sorted(measure_unsorted[1][i].items()))
        x=b
        a,b=zip(* sorted(measure_unsorted[2][i].items()))
        y=b
        corr_coeff=np.corrcoef(x,y)[0,1]
        sn.write("Correlation Coefficient between Closeness and Eigenvector Centrality : "+str(corr_coeff))
        sn.write("\n")
        plt.title('CORRELATION_COEFFICIENT')
        plt.scatter(x,y)
        plt.ylabel('eigenvector_centrality_values')
        plt.xlabel('closeness_centrality_values')
        plt.savefig("/home/sukanya/Desktop/jadavpur_internship/CODES/Correlation_Coefficifent/closeness_eigenvector/Graph_6.png")
        plt.close()
        
        ##### correlation coefficient between degree and eigenvector centrality  
        a,b=zip(* sorted(measure_unsorted[2][i].items()))
        x=b
        a,b=zip(* sorted(measure_unsorted[0][i].items()))
        y=b
        corr_coeff=np.corrcoef(x,y)[0,1]
        sn.write("Correlation Coefficient between Eigenvector and Degree Centrality : "+str(corr_coeff))
        sn.write("\n")
        plt.title('CORRELATION_COEFFICIENT')
        plt.scatter(x,y)
        plt.ylabel('degree_centrality_values')
        plt.xlabel('eigenvector_centrality_values')
        plt.savefig("/home/sukanya/Desktop/jadavpur_internship/CODES/Correlation_Coefficifent/eigenvector_degree/Graph_6.png")
        plt.close()

"""    ###############     plotting of the centrality values
    
    plotting(no_of_graphs,measure_unsorted,graph_list)
    normalized_graph(no_of_graphs,measure_unsorted,graph_list)
    
   ########### finding neighbors

    neighbor=[[[] for j in range(len(graph_list[i]))]for i in range(no_of_graphs)]
    degree_of_each_node=[[[] for j in range(len(graph_list[i]))]for i in range(no_of_graphs)]
    
    for i in range(no_of_graphs):
        for j in range(len(graph_list[i])):
#             try:
#                 neighbor[i][j]=list((graph_list[i].neighbors(j+1)))
#             except:
#                 neighbor[i][j]=list()
            neighbor[i][j]=list((graph_list[i].neighbors(j+1)))
            if(len(neighbor[i][j])==1 and neighbor[i][j][0]==j+1):
                degree_of_each_node[i][j]=0
            else:
                degree_of_each_node[i][j]=len(neighbor[i][j])
    
#     Centrality_graph.nodes_per_degree(no_of_graphs,graph_list,degree_of_each_node)
    
     #----------------------------------------------------------------------------------------------------
        
        ##################### finding connected components of a graph ################################
    connected_comp=[[] for i in range(no_of_graphs)]
    
    for i in range(no_of_graphs):
        connected_comp[i]=list(nx.connected_components(graph_list[i]))
    for i in range(no_of_graphs):
        for j in range(len(connected_comp[i])):
            connected_comp[i][j]=list(connected_comp[i][j])
            
    measure_wrt_cc=[[[[]for k in range(len(connected_comp[i]))]for i in range(no_of_graphs)]for j in range(3)]
    
    for k in range(3):
        for i in range(no_of_graphs):
            for j in range(len(connected_comp[i])):
                for l in range(len(connected_comp[i][j])):
                    measure_wrt_cc[k][i][j].append((connected_comp[i][j][l],measure_unsorted[k][i][connected_comp[i][j][l]]))  
            
    #-----------------------------------------------------------------------------------------------------
    percent=[0.05,0.1,0.15]
#     percent=[0.01] 
    
    time_cost_mat=[[[[-1 for j in range(2)] for i in range(no_of_graphs)] for m in range(len(percent))] for k in range(3)]
    
    cost=0
    
    st=[int(-1)for q in range(76000)]
    top=-1
    flag=0
    dup=0
    
    temp_seed=[[[[int(-1)for q in range(76000)] for i in range(no_of_graphs)] for m in range(len(percent))] for k in range(3)]
    
    for k in range(3):
        for m in range(len(percent)):
            for i in range(no_of_graphs):
                for j in range (int(percent[m]*len(graph_list[i]))):   #1 if(1>(percent[m]*len(graph_list[i]))>=0.5) else 
                    temp_seed[k][m][i][j]=measure[k][i][j][0]              
    for k in range(3):
        st=[int(-1) for q in range(76000)]
        top=-1
        cost=0
        flag=0
        dup=0
        for m in range(len(percent)):
            st=[int(-1) for q in range(76000)]
            top=-1
            cost=0
            flag=0
            dup=0
            for j in range(no_of_graphs):
                st=[int(-1) for q in range(76000)]
                top=-1
                cost=0
                flag=0
                dup=0
                if(len(connected_comp[j])>1):
                    for l in range(len(connected_comp[j])):
                        if(k==1):
                            top=top+1
                            st[top]=(max(measure_wrt_cc[k][j][l],key=lambda z: z[1]))[0]
                            cost=cost+(max(measure_wrt_cc[k][j][l],key=lambda z: z[1]))[1]
                        elif(k==0 or k==2):
                            top=top+1
                            st[top]=(max(measure_wrt_cc[k][j][l],key=lambda z: z[1]))[0]
                            if(k==0):
                                cost=cost+degree_of_each_node[j][st[top]]
                            else:
                                cost=cost+(max(measure_wrt_cc[k][j][l],key=lambda z: z[1]))[1]
#                 print(st)
                if((top+1)<int(percent[m]*(len(graph_list[j])))):
                    for x in range(int(percent[m]*(len(graph_list[j])))):
                        for y in range(0,top):
                            if(temp_seed[k][m][j][x]==st[y]):
                                dup=1
                                break
                            else:
                                dup=0
                        if(dup==1):
                            continue
                        elif(dup==0):
                            top=top+1
                            st[top]=int(temp_seed[k][m][j][x])
                            flag=st[top]
                            if(k==0):
                                cost=cost+degree_of_each_node[j][flag]
                            elif(k==2 or k==1):
                                cost=cost+measure[k][j][flag-1][1]
                        if((top+1)==int(percent[m]*(len(graph_list[j])))):
                            break
#                     print(st)
                time_cost_mat[k][m][j][1]=cost
#                 print "INITIAL SEED SELECTED for graph "+str(i+1)+" for "+str(int(percent[m]*100))+"% : "+str(st)
#                 print "Number of seed selected for graph "+str(j+1)+ " for "+str(int(percent[m]*100))+"% : "
                time_cost_mat[k][m][j][0]=time_cost_calc(st,top,neighbor[j],len(graph_list[j]))
                st=[int(-1) for q in range(76000)]
                top=-1
                cost=0
                flag=0
                dup=0
    with open("/home/sukanya/Desktop/jadavpur_internship/CODES/Result.odt","a+") as sn:                            
        sn.write("-------------------------------------TIME-COST TRADE_OFF-------------------------------------------")       
        sn.write ("\n")
        sn.write("[Note: First element of the list is time and the second one is cost. If time is 0 that means no seed is selected with the initial percentage.]")
        sn.write("\n")

        for k in range(3):
            if(k==0):
                sn.write("BASED ON DEGREE CENTRALITY VALUES : ")
                sn.write("\n")
            if(k==1):
                sn.write("BASED ON CLOSENESS CENTRALITY VALUES : ")
                sn.write("\n")
            if(k==2):
                sn.write("BASED ON EIGENVECTOR CENTRALITY VALUES : ")
                sn.write ("\n")
            for m in range(len(percent)):
                sn.write ("Time-cost tradeoff when Initial Percentage of seed selection is "+str(int(percent[m]*100))+"% :")
                sn.write ("\n")
                for i in range(no_of_graphs):
                    sn.write ("Graph 5: "+str(time_cost_mat[k][m][i]))
                sn.write ("\n")
        sn.write("\n")"""
                


# In[ ]:




