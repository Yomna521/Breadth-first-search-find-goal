#Breadth-first algorithm

def neighbour(map, node, m, n):
    calc_neighbour= [-8, -7, 1, 9, 8, 7, -1, -9]
    neighbour=[]
    for i in range(0,len(map[node])):
        a = map[node][i]
        if(a==1):
            x= node+calc_neighbour[i]+1
            if(x>0 and x<=m*n):
                neighbour.append(x)
    return neighbour

def get_graph(map, m, n):
    graph={}
    for node in range(0, len(map)):
        graph[node+1] = []
        x= neighbour(map, node, m, n)
        for i in range(len(x)):
            graph[node+1].append(x[i])

    return graph


def bfs(graph, root, goal):
    explored = []
    queue = [[root]]
 
    # return path if start is goal
    if root == goal:
        return 
 
    # loop over all possible routes
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node not in explored:
            neighbours = graph[node]
            neighbours.sort()
            # go through all neighbour nodes, construct a new path and push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path 
            
            explored.append(node)
 
    # in case there's no path between the 2 nodes
    return None

if __name__ == "__main__":
   line1= input().split(' ')
   m = int(line1[0])
   n = int(line1[1])
   s = int(line1[2])
   map = []
   

   for i in range(m*n):
       line=input()
       line = line.split(' ')
       b=[]
       for x in range (1,9):
           b.append(int(line[x]))
       map.append(b) 
    
   #corner nodes
   corner1 = 1
   corner2 = n
   corner3 = m*n - n + 1
   corner4 = m*n 

   graph =get_graph(map, m, n)
   path1 = bfs(graph, s, corner1)
   path2 = bfs(graph, s, corner2)
   path3 = bfs(graph, s, corner3)
   path4 = bfs(graph, s, corner4)

   if path1 !=None:
    for i in range(len(path1)):
        print(path1[i],end=' ')
    print('')
   if path2 != None:
    for i in range(len(path2)):
       print(path2[i],end=' ')
    print('')
   if path3 != None:
    for i in range(len(path3)):
        print(path3[i],end=' ')
    print('')
   if path4 != None:
    for i in range(len(path4)):
        print(path4[i],end=' ')
    print('')
