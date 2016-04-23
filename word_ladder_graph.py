from graph import Graph
from queue import Queue

def build_graph(word_file):
    d = {}
    g = Graph()
    with open(word_file,"r") as f:
        words = f.read().split("\n")
    for word in words:
        for i in xrange(len(word)):
            bucket = word[:i]+"_"+word[i+1:]
            if bucket in d.keys():
                d[bucket].append(word)
            else:
                d[bucket] = [word]
        for bucket in d.keys():
            for word1 in d[bucket]:
                for word2 in d[bucket]:
                    if word1 != word2:
                        g.add_edge(word1,word2)
    return g

def bfs(g,start):
    start.distance = 0
    start.predecessor = None
    vertex_queue = Queue()
    vertex_queue.put(start)
    while vertex_queue.size() > 0:
        current_vertex = vertex_queue.get()
        for neighbor in current_vertex.connected_to.keys():
            if neighbor.color == "white":
                neighbor.color = "gray"
                neighbor.distance = current_vertex.distance + 1
                neighbor.predecessor = current_vertex
    
if __name__ == '__main__':
    g = build_graph("words.txt")
