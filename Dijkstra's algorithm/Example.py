graph={}
graph["inicio"]={}
graph["inicio"]["a"]=6
graph["inicio"]["b"]=2
graph["a"]={}
graph["a"]["fim"]=1
graph["b"]={}
graph["b"]["a"]=3
graph["b"]["fim"]=5
graph["fim"]={}

infinit=float("inf")
costs={}
costs["a"]=6
costs["b"]=2
costs["fim"]=infinit

parents={}
parents["a"]="inicio"
parents["b"]="inicio"
parents["fim"]=None

def findInTheLowestCost(costs):
    lowestCost=float("inf")
    nodeLowestCost=None
    for node in costs:
        cost=costs[node]
        if (cost < lowestCost) and (node not in processed):
            lowestCost=cost
            nodeLowestCost=node
    return nodeLowestCost
processed=[]
node=findInTheLowestCost(costs)#Try find the lowest cost that wasnt found yet
print(f"First node: {node}")
while node is not None:#While yet have ties to be process...
    cost=costs[node]
    neighbor=graph[node]
    for n in neighbor.keys():# Get ['a','b'] keys from graph['b']
        newCost=cost+neighbor[n]
        if costs[n]>newCost:
            costs[n]=newCost
            parents[n]=node
    processed.append(node)
    node=findInTheLowestCost(costs)
    print(processed)
    print(node)