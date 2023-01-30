import sys
import heapq
input = sys.stdin.readline

def prim(start, V) :
    MST = [0] * (V+1)       # MST 담긴 노드 표시.
    q = [[0,start]]
    total = 0               # 최소 가중치 총합.
    MST[start] = 1          # 시작점 표시하고 시작.

    for _ in range(V) :     # 간선 수만큼 반복.
        k = 0
        minV = 1e9
        for i in range(V+1) :
            if MST[i]
V, E = map(int, input().split())
edge = [[] for _ in range(V+1)]
for _ in range(E) :
    a, b, c = map(int,input().split())  # a정점과 b정점이 가중치 c간선으로 연결.
    edge[a].append((b,c))
    edge[b].append((a,c))
