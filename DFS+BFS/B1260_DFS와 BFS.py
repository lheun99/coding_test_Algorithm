from collections import deque

def solution():
    a, b, c = map(int, input().split())
    arr = [[] for i in range(a+1)]

    for i in range(b):
        d, e = map(int, input().split())
        arr[d].append(e)
        arr[e].append(d)
    
    for i in arr:
        i.sort()


    visited = [False] * (a+1)
    visited[0] = True

    visited_2 = [False] * (a+1)
    visited_2[0] = True

    global dfs_a, bfs_a
    dfs_a = [] 
    bfs_a = []
    
    dfs(arr, visited, c)
    bfs(arr, visited_2, c)

    for i in dfs_a:
        print(i, end = " ")

    print()
    
    for i in bfs_a:
        print(i, end = " ") 

def dfs(arr, visited, c):
    visited[c] = True
    #print(c, end = " ")
    dfs_a.append(c)

    for i in arr[c]:
        if not visited[i]:
            dfs(arr, visited, i)


def bfs(arr, visited_2, c):
    q = deque([c])
    visited_2[c] = True

    while q:
        v = q.popleft()
        #print(v, end = " ")
        bfs_a.append(v)

        for i in arr[v]:
            if not visited_2[i]:
                q.append(i)
                visited_2[i] = True


solution()
