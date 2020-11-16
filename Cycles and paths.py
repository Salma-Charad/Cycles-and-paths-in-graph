import sys
# ask user for number of vertices
verts = eval(input("enter number of vertices: "))

# ask number of edges
edges = eval(input("enter number of edges: "))

# make Adjacency matrix of the graph
AdjMat = [[0]*verts for i in range(verts)]

# ask the user to enter the edges one by one and enter this info into AdjMat
for i in range(edges):
    a,b= (input("Enter edge: ")).split(" ")
    a = eval(a)
    b = eval(b)
    AdjMat[a-1][b-1] = 1
    AdjMat[b-1][a-1] = 1


#Find the degrees of vertices and store them
degrees = [0]*verts
for i in range(verts):
  for j in range(verts):
    degrees[i] = degrees[i] + AdjMat[i][j]


#If a vertex has a degree greater than 2, the the graph is not only composed of paths and cycles
for k in range(verts):
  if degrees[k]>2:
    print("Sorry, this graph is not composed of only paths and cycles as components")
    sys.exit()

#Check for the case of a single node (A single node doesn't even have a path to itself, else if will be considered a path)
for i in range(verts):
 if degrees[k]==0:
    print("Sorry, this graph is not composed of only paths and cycles as components, it contains a single node")
    sys.exit()
 
#We check the number of cycles and paths 
visited_nodes =[0]*verts
next_vert =0
print('This graph has only paths and cycles as components.')

flag=1
SizesArray = []
counter= 0
while visited_nodes != [1]*verts:
  
  #First looks for unvisited nodes with degree 1 as they constitute the beginning of a path
  for i in range(verts):
    if visited_nodes[i] == 0 and degrees[i]==1:
      next_vert = i
      visited_nodes[i] =1
      flag =1

      for k in range(verts):
        if AdjMat[next_vert][k]==1:
          if visited_nodes[k] == 0:
            visited_nodes[k]=1
            next_vert =k
            flag =flag+1
          else:
            break

      if degrees[next_vert]==1 and visited_nodes == [1]*verts:
        SizesArray.append(flag)
        break

      elif degrees[next_vert]==1 and visited_nodes != [1]*verts:
        SizesArray.append(flag)
  
  visited= [0]*len(SizesArray)
  for i in range(len(SizesArray)):
    if visited[i]==0:
      visited[i]=1
      for j in range(len(SizesArray)):
        if SizesArray[i] == SizesArray[j]:
          if visited[j]==0:
            counter=counter+1
            visited[j]=1
      print ("The graph contains " + str(counter+1) + " Path(s) of size "+ str( SizesArray[i]))
 
  SizesArray = []

  #Once all the paths have been traversed, it will look for beginning of cycles that have not been traversed 
  for i in range(verts):
    if visited_nodes[i] == 0 and degrees[i]==2:
      next_vert = i
      visited_nodes[i] =1
      flag =1
 

      for k in range(verts):
        if AdjMat[next_vert][k]==1:
          if visited_nodes[k] == 0:
            visited_nodes[k]=1
            next_vert =k
            flag =flag+1
          else:
            break

      if degrees[next_vert]==2 and visited_nodes == [1]*verts:
        SizesArray.append(flag)
        break

      elif degrees[next_vert]==2 and visited_nodes != [1]*verts:
        SizesArray.append(flag)
  
  counter= 0  
  visited= [0]*len(SizesArray)
  for i in range(len(SizesArray)):
    if visited[i]==0:
      visited[i]=1
      for j in range(len(SizesArray)):
        if SizesArray[i] == SizesArray[j]:
          if visited[j]==0:
            counter=counter+1
            visited[j]=1
      print ("The graph contains " + str(counter+1) + " Cycle(s) of size "+ str( SizesArray[i]))
    
















    


 


  

