# Breadth First Search for Disconnected Graph

import queue

#adds adjacent vertext to the provided source vertex in the adjacent list
def addEdge(adjacencyList, sourceVertex, adjacentVertex):
    #initializes an empty list in source vertext index if empty
    if not sourceVertex in adjacencyList:
        adjacencyList[sourceVertex] = []

    #adds the adjacent vertex to the source vertex
    adjacencyList[sourceVertex].append(adjacentVertex)

#Breadth First Search algorithm for the disconnected graph
def breadthFirstSearch(adjacencyLIst):
    visited = {}

    for key, value in adjacencyLIst.items():
        if key not in visited:
            visited[key] = False

        if  visited[key] != True:

            visitingQueue = queue.Queue()
            visited[key] = True
            visitingQueue.put(key)

            while(not visitingQueue.empty()):
                vertex = visitingQueue.get()
                print(vertex, end = " ")

                if vertex in adjacencyLIst:
                    for adjacentVertext in adjacencyLIst[vertex]:
                        if adjacentVertext not in visited:
                            visited[adjacentVertext] = False

                        if(visited[adjacentVertext] != True):
                            visitingQueue.put(adjacentVertext)
                            visited[adjacentVertext] = True



if __name__ == "__main__":
    adjacencyList = {}

    addEdge(adjacencyList, 0, 4)
    addEdge(adjacencyList, 1, 2)
    addEdge(adjacencyList, 1, 3)
    addEdge(adjacencyList, 1, 4)
    addEdge(adjacencyList, 2, 3)
    addEdge(adjacencyList, 3, 4)

    breadthFirstSearch(adjacencyList)