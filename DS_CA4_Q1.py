vertices = []
t = int(input())
for j in range(t):
    graph = {}
    n = int(input())
    for i in range(0,n):
        v = input()
        vertices.append(v)
        graph[v] = []
        possible = True
        for ver in graph:
            if v[0] == ver[-1] and v != ver:
                graph[ver].append(v)
                graph[v].append(ver)
            if v[-1] == ver[0] and v != ver:
                graph[ver].append(v)
                graph[v].append(ver)


        for vert in graph:
            if graph[vert] == []:
                # print ("BIG IF")
                possible = False
    print (graph)

    if possible:
        print ("possible")
    else:
        print ("not possible")
