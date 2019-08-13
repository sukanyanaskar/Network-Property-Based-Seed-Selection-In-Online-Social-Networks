
# coding: utf-8

# In[ ]:


import networkx as nx
import matplotlib.pyplot as plt
import networkx.drawing

def homophily_oneset(graph,vertices):
    l=len(vertices)
    if (l<1):
        return -1
    h=0.0
    g2=nx.to_dict_of_lists(graph)
    for x in vertices:
        for ver in g2[x]:
            if ver in vertices:
                h+=1.0
                #print (x,ver,h)
    return h/(2.0*l)
def homophily_avg(graph,focals):
    avgh=0.0
    c=0.0
    #print(len(focals))
    for group in focals:
        x=homophily_oneset(graph,focals[group])
        if x>=0:
            avgh+=x
            c+=1.0
    return avgh/c


def clustering(graph,vertex):
    """ finds clustering coefficient of vertex
        in graph from the set of vertices provided
    """
    k=graph.degree[vertex]
    if k>1:
        c=0.0
        for w in graph.neighbors(vertex+1):
            for x in graph.neighbors(vertex+1):
                if (x in graph.neighbors(w)) and x!=w:
                    c=c+1.0
        c=c/2
        return ((2*c)/(k*(k-1)))
    return 0

def focal_structures(graph):
    """ finds focal_structures in graph based on clustering coefficients
        if clustering coefficients of two vertices are more than the
        average clustering coefficient and they are adjacent, the two verticesa
        are included in the same focal structure
    """
    s=0
    p=0
    dictt={}
    c_co=[]
    ver=sorted(list(graph.nodes))
    for x in range(len(ver)):       #get clustering coefficient for each vertex
        dictt[x]=[]
        c_co.append(clustering(graph,ver[x]))
        s=s+c_co[x]
    avg=(s/len(graph))
    visited=[]
    for i in range(len(ver)):
        visited.append(0)
    for i in range(len(ver)):
        f=-1
        for x in range(len(ver)):
            for y in range(len(dictt[x])):
                if dictt[x][y]==ver[i]:
                    f=x
                    break
            if f>-1:
                break
        if f==-1:
            dictt[p].append(ver[i])
            f=p
            p=p+1
        for x in range(i+1,len(ver)):    #cluster vertices based on clustering coefficient
            if visited[x]==0 and (ver[x]+1 in graph.neighbors(ver[i]+1)) and ((c_co[i] > avg and c_co[x] > avg) or (c_co[i] < avg and c_co[x] < avg)):
                dictt[f].append(ver[x])
                visited[x]=1
    for i in range(len(ver)):
        dictt[i]=list(set(dictt[i]))
    return dictt

def graph_create_dataset(graph_no):
    graph=[[]for i in range(graph_no)]
#     with open("/home/sukanya/Desktop/jadavpur_internship/CODES/dataset/facebook.txt") as fp1:  
#         graph[0]=nx.Graph()
#         for line in fp1:
#             temp=line.split(" ")
#             x=int(temp[0])
#             y=int((temp[1].split("\n"))[0])
#             graph[0].add_edges_from([(x,y)])
            
#     with open("/home/sukanya/Desktop/jadavpur_internship/CODES/dataset/hamster.txt") as fp2:
#         graph[0]=nx.Graph()
#         for line in fp2:
#             temp=line.split(" ")
#             x=int(temp[0])
#             y=int((temp[1].split("\n"))[0])
#             graph[0].add_edges_from([(x,y)])
            
#     with open("/home/sukanya/Desktop/jadavpur_internship/CODES/dataset/hamster_full.txt") as fp3:
#         graph[0]=nx.Graph()
#         for line in fp3:
#             temp=line.split(" ")
#             x=int(temp[0])
#             y=int((temp[1].split("\n"))[0])
#             graph[0].add_edges_from([(x,y)])
    
    """with open("/home/sukanya/Desktop/jadavpur_internship/CODES/dataset/google_plus.txt") as fp4:
        graph[0]=nx.Graph()
        for line in fp4:
            temp=line.split(" ")
            x=int(temp[0])
            y=int((temp[1].split("\n"))[0])
            graph[0].add_edges_from([(x,y)])"""
    
    with open("/home/sukanya/Desktop/jadavpur_internship/CODES/dataset/twitter.txt") as fp5:
        graph[0]=nx.Graph()
        for line in fp5:
            temp=line.split(" ")
            x=int(temp[0])
            y=int((temp[1].split("\n"))[0])
            graph[0].add_edges_from([(x,y)])
            
#     with open("/home/sukanya/Desktop/jadavpur_internship/CODES/dataset/brightkite.txt") as fp6:  
#         graph[0]=nx.Graph()
#         for line in fp6:
#             temp=line.split(" ")
#             x=int(temp[0])
#             y=int((temp[1].split("\n"))[0])
#             graph[0].add_edges_from([(x,y)])
            
#     with open("/home/sukanya/Desktop/jadavpur_internship/CODES/dataset/Epinions.txt") as fp7:
#         graph[0]=nx.Graph()
#         for line in fp7:
#             temp=line.split(" ")
#             x=int(temp[0])
#             y=int((temp[1].split("\n"))[0])
#             graph[0].add_edges_from([(x,y)])
            
#     with open("/home/sukanya/Desktop/jadavpur_internship/CODES/dataset/facebook_wosn.txt") as fp8:
#         graph[0]=nx.Graph()
#         for line in fp8:
#             temp=line.split(" ")
#             x=int(temp[0])
#             y=int((temp[1].split("\n"))[0])
#             graph[0].add_edges_from([(x,y)])

#     with open("/home/sukanya/Desktop/jadavpur_internship/CODES/dataset/slashdot.txt") as fp9:
#         graph[0]=nx.Graph()
#         for line in fp9:
#             temp=line.split(" ")
#             x=int(temp[0])
#             y=int((temp[1].split("\n"))[0])
#             graph[0].add_edges_from([(x,y)])
            
#     with open("/home/sukanya/Desktop/jadavpur_internship/CODES/dataset/advogato.txt") as fp10:    
#         graph[0]=nx.Graph()
#         for line in fp10:
#             temp=line.split(" ")
#             x=int(temp[0])
#             y=int((temp[1].split("\n"))[0])
#             graph[0].add_edges_from([(x,y)])
            
    return(graph)
           

if __name__=='__main__':
    graph_no=1
    graph=[[]for i in range(graph_no)]
    graph=graph_create_dataset(graph_no)

    ################### ASSORTATIVITY  ##############################
#     with open("/home/sukanya/Desktop/jadavpur_internship/CODES/Assortativity_homophily.odt","a+") as sn:
#         sn.write("\n")
#         sn.write(" ASSORTATIVITY OF THE NETWORKS CONSIDERED ---------")
#         sn.write("\n\n")
#         for i in range(graph_no):
#             corr_coeff=nx.degree_pearson_correlation_coefficient(graph[i])                         
#             sn.write("Assortativity of Graph "+str(i+1)+" : "+str(corr_coeff))
#             sn.write("\n")
            
    ####################### HOMOPHILY ##################################
    with open("/home/sukanya/Desktop/jadavpur_internship/CODES/Assortativity_homophily.odt","a+") as sn:
        sn.write("\n")
#         sn.write(" HOMOPHILY OF THE NETWORKS CONSIDERED ---------")
#         sn.write("\n\n")
        for i in range(graph_no):
            focal_struct=focal_structures(graph[i])
#             print(focal_struct)
            homophily=homophily_avg(graph[i],focal_struct)
            sn.write("Homophily of Graph "+str(i+1)+" : "+str(homophily))
            sn.write("\n")

