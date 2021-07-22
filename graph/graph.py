def imprime(d,f,N):
    out_arestas(tree)
    out_arestas(back)
    out_arestas(forward)
    out_arestas(cross)
    for i in range(N):
        print("Vertice ",i+1,":", d[i], f[i])
    print("Topological sorting: ", end="")
    for i in top_sort:
        print(i+1, end=" ")
    print()
    print("Connected Component[", len(connect_comp), "]:", connect_comp)

def out_arestas(dic):
    for i in dic.keys():
        print(f"{i} --> {dic[i]}")
    print()

def loadlist():
    with open('graph/test.txt', 'r') as file:
        list = file.readlines() # ler todas as linhas e salva em list
        for i in range(len(list)):
            line = list[i].split()
            if i == 0:
                directed = True if line[2] == 'D' else False
                N = int(line[0])    
                adj_list = [[] for _ in range(N)] # criando uma list de list
                trans_adjList = [[] for _ in range(N)]
            else:
                adj_list[int(line[0])-1].append(int(line[1])-1)
                trans_adjList[int(line[1])-1].append(int(line[0])-1)
                if directed == False:
                    adj_list[int(line[1])-1].append(int(line[0])-1)
                    trans_adjList[int(line[0])-1].append(int(line[1])-1)     
    return adj_list, trans_adjList, N


def DFS_visit(u):
    global mark, count
    color[u] = "Gray"
    mark+=1
    d[u] = mark
    for v in adj_list[u]:
        if color[v] == "White":
            tree[(u, v)] = "Tree Edge"
            DFS_visit(v)
        elif color[v] == "Gray":
            back[(u, v)] = "Back Edge"
        elif d[u] < f[v]:
            forward[(u, v)] = "Forward Edge"
        else:
            cross[(u, v)] = "Cross Edge"
    color[u] = "Black"
    mark+=1
    f[u] = mark
    top_sort[count] = u
    count-=1


def connect_comp_DFSvisit(u):
    global mark, count
    color[u] = "Gray"
    mark+=1
    d[u] = mark
    for v in trans_adjList[u]:
        if color[v] == "White":
            DFS_visit(v)
    color[u] = "Black"
    mark+=1
    f[u] = mark

def DFS():
    for u in V:
        color[u]="White"
    for u in V:
        if color[u] == "White":
            DFS_visit(u)

def connect_comp_DFS():
    index = -1
    temp = []
    for u in top_sort:
        color[u]="White"
        temp.append(u)
    for u in top_sort:
        if color[u] == "White":
            connect_comp_DFSvisit(u)
            connect_comp.append([u])
            index+=1
        for u in temp: # u é conteúdo
            if color[u] == "Black":
                connect_comp[index].append(u)
                temp.pop(temp.index(u))
       
[adj_list, trans_adjList, N]=loadlist()
#V = list(range(0,N))
V = [0, 1, 2, 3, 4, 5, 6, 7]
color = [0]*N    
d = [0]*N
f = [0]*N
top_sort = [0]*N
connect_comp = []
tree = {}
back = {}
forward = {}
cross = {}
mark = 0
count = N-1
DFS()
connect_comp_DFS()
imprime(d, f, N)
