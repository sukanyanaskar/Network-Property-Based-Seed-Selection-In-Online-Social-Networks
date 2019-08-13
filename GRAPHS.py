
# coding: utf-8

# In[1]:


import networkx as nx
import matplotlib.pyplot as plt
import networkx.drawing

def graph_create_dataset(graph_no):
    graph=[[]for i in range(graph_no)]
    with open("/home/dst-fist-server1/Desktop/jadavpur_internship/CODES/dataset/facebook.txt") as fp1:  
        graph[0]=nx.Graph()
        for line in fp1:
            temp=line.split(" ")
            x=int(temp[0])
            y=int((temp[1].split("\n"))[0])
            graph[0].add_edges_from([(x,y)])
    
#     with open("/home/dst-fist-server1/Desktop/jadavpur_internship/CODES/dataset/hamster.txt") as fp2:
#         graph[0]=nx.Graph()
#         for line in fp2:
#             temp=line.split(" ")
#             x=int(temp[0])
#             y=int((temp[1].split("\n"))[0])
#             graph[0].add_edges_from([(x,y)])
            
#     with open("/home/dst-fist-server1/Desktop/jadavpur_internship/CODES/dataset/hamster_full.txt") as fp3:
#         graph[0]=nx.Graph()
#         for line in fp3:
#             temp=line.split(" ")
#             x=int(temp[0])
#             y=int((temp[1].split("\n"))[0])
#             graph[0].add_edges_from([(x,y)])
    
#     with open("/home/dst-fist-server1/Desktop/jadavpur_internship/CODES/dataset/google_plus.txt") as fp4:
#         graph[0]=nx.Graph()
#         for line in fp4:
#             temp=line.split(" ")
#             x=int(temp[0])
#             y=int((temp[1].split("\n"))[0])
#             graph[0].add_edges_from([(x,y)])
    
#     with open("/home/dst-fist-server1/Desktop/jadavpur_internship/CODES/dataset/twitter.txt") as fp5:
#         graph[0]=nx.Graph()
#         for line in fp5:
#             temp=line.split(" ")
#             x=int(temp[0])
#             y=int((temp[1].split("\n"))[0])
#             graph[0].add_edges_from([(x,y)])
            
#     with open("/home/dst-fist-server1/Desktop/jadavpur_internship/CODES/dataset/brightkite.txt") as fp6:   # error is coming
#         graph[0]=nx.Graph()
#         for line in fp6:
#             temp=line.split(" ")
#             x=int(temp[0])
#             y=int((temp[1].split("\n"))[0])
#             graph[0].add_edges_from([(x,y)])
            
#     with open("/home/dst-fist-server1/Desktop/jadavpur_internship/CODES/dataset/Epinions.txt") as fp7:
#         graph[0]=nx.Graph()
#         for line in fp7:
#             temp=line.split(" ")
#             x=int(temp[0])
#             y=int((temp[1].split("\n"))[0])
#             graph[0].add_edges_from([(x,y)])
            
#     with open("/home/dst-fist-server1/Desktop/jadavpur_internship/CODES/dataset/facebook_wosn.txt") as fp8:
#         graph[0]=nx.Graph()
#         for line in fp8:
#             temp=line.split(" ")
#             x=int(temp[0])
#             y=int((temp[1].split("\n"))[0])
#             graph[0].add_edges_from([(x,y)])
              
#     with open("/home/dst-fist-server1/Desktop/jadavpur_internship/CODES/dataset/gowalla.txt") as fp9:    # very big
#         graph[0]=nx.Graph()
#         for line in fp9:
#             temp=line.split(" ")
#             x=int(temp[0])
#             y=int((temp[1].split("\n"))[0])
#             graph[0].add_edges_from([(x,y)])
            
#     with open("/home/dst-fist-server1/Desktop/jadavpur_internship/CODES/dataset/hyves.txt") as fp10:
#         graph[0]=nx.Graph()
#         for line in fp10:
#             temp=line.split(" ")
#             x=int(temp[0])
#             y=int((temp[1].split("\n"))[0])
#             graph[0].add_edges_from([(x,y)])
            
#     with open("/home/dst-fist-server1/Desktop/jadavpur_internship/CODES/dataset/livemocha.txt") as fp11:
#         graph[0]=nx.Graph()
#         for line in fp11:
#             temp=line.split(" ")
#             x=int(temp[0])
#             y=int((temp[1].split("\n"))[0])
#             graph[0].add_edges_from([(x,y)])
            
#     with open("/home/dst-fist-server1/Desktop/jadavpur_internship/CODES/dataset/petster_cat.txt") as fp12:
#         graph[0]=nx.Graph()
#         for line in fp12:
#             temp=line.split(" ")
#             x=int(temp[0])
#             y=int((temp[1].split("\n"))[0])
#             graph[0].add_edges_from([(x,y)])
            
#     with open("/home/dst-fist-server1/Desktop/jadavpur_internship/CODES/dataset/slashdot.txt") as fp13:
#         graph[0]=nx.Graph()
#         for line in fp13:
#             temp=line.split(" ")
#             x=int(temp[0])
#             y=int((temp[1].split("\n"))[0])
#             graph[0].add_edges_from([(x,y)])
            
#     with open("/home/dst-fist-server1/Desktop/jadavpur_internship/CODES/dataset/youtube.txt") as fp14:
#         graph[0]=nx.Graph()
#         for line in fp14:
#             temp=line.split(" ")
#             x=int(temp[0])
#             y=int((temp[1].split("\n"))[0])
#             graph[0].add_edges_from([(x,y)])
            
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
           
    

