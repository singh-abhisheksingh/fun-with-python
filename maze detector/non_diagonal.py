import color
import dj
import math
import cv2
import numpy as np

x=20
y=20
list6=[]
def findedge(m,n):
    list5=[(m+40,n),(m-40,n),(m,n+40),(m,n-40)]
    for element in list5:
        if(element[0]>0 and element[1]>0 and 220>=element[0] and 220>=element[1]):
            if(element in color.list4):
                d=math.sqrt((element[0]-m)**2+(element[1]-n)**2)
                graph.add_edge((m,n),element,d)
    #print(graph.edges)
    
if __name__ == '__main__':
    graph = dj.Graph()

    for node in color.list2:
        graph.add_node(node)
    
    for node in color.list3:
        graph.add_node(node)

    #print(graph.nodes)
    for blocks in color.list4:
        findedge(blocks[0],blocks[1])
    list6.append(dj.shortest_path(graph,color.list3[0],color.list3[1])[1])
    print(list6)
    for z in list6:
        for z2 in z:
            cv2.rectangle(color.img,(z2[0]-20,z2[1]-20),(z2[0]+20,z2[1]+20),(0,255,255),-1)
            cv2.rectangle(color.img,(z2[0]-20,z2[1]-20),(z2[0]+20,z2[1]+20),(0,0,0),3)
    cv2.imshow('path',color.img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()