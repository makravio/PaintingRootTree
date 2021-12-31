# this is script to paint tree
# made by makrav.io
# 31.12.2021

from tkinter import *

root = Tk()
root.title("Painting tree")

C = Canvas(height=600, width=800, bg="white")
C.pack()

NODE_SIZE = 20
P_SIZE = 30
START_HGT = 150
RZ = 100

class Node:
    def __init__(self, id, x, y):
        self.id = id
        self.size = NODE_SIZE
        self.x = x
        self.y = y

    def paint(self):
        C.create_oval(self.x - self.size, self.y - self.size, self.x + self.size, self.y + self.size, width=2)
        C.create_text(self.x, self.y, text=str(self.id), font="Arial 15")

n = int(input("Enter your tree's nodes amount: "))
graph = [[] for i in range(n)]
edges = []
a = list(map(int, input("Enter n - 1 integers: parents of vertex: ").split()))

for i in range(n - 1):
    edges.append([a[i] - 1, i + 1])
    graph[a[i] - 1].append(i + 1)
    graph[i + 1].append(a[i] - 1)

used = [0 for i in range(n)]
nodes = []

def dfs(v, level):
    used[v] = 1
    nodes.append([level, v])
    for u in graph[v]:
        if not used[u]:
            dfs(u, level + 1)

def key(x):
    return x[0]

dfs(0, 0)
nodes.sort(key = key)

nodes_vis = [0 for i in range(n)]

ind = 0

while ind < n:
    now_level = nodes[ind][0]
    new_ind = ind + 1
    while new_ind < n and nodes[new_ind][0] == now_level:
        new_ind += 1
    new_ind -= 1
    total = new_ind - ind + 1
    wdt_total = (NODE_SIZE * 2) * total + (total - 1) * P_SIZE
    start_pos = (800 - wdt_total) // 2
    for i in range(ind, new_ind + 1):
        nodes_vis[nodes[i][1]] = Node(nodes[i][1] + 1, start_pos + (i - ind) * (P_SIZE + NODE_SIZE * 2), RZ * now_level + START_HGT)
        nodes_vis[nodes[i][1]].paint()
    ind = new_ind + 1

for edge in edges:
    l = nodes_vis[edge[0]]
    r = nodes_vis[edge[1]]
    C.create_line(l.x, l.y + NODE_SIZE, r.x, r.y - NODE_SIZE, width=3, fill="orange")

root.mainloop()