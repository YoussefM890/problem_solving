from collections import defaultdict, deque
from typing import List


class Is_Graph_Bipartite :
    def isBipartite(self, g: List[List[int]]) -> bool:
        visited = defaultdict(int)
        for index,i in enumerate(g) :
            if index in visited : continue
            visited[index] = 1
            l = deque([index])
            while l :
                cur = l.popleft()
                for i in g[cur] :
                    if i in visited :
                        if visited[i] == visited[cur] : return False
                    else :
                        visited[i] = -1 * visited[cur]
                        l.append(i)
        return True


is_graph_bipartite = Is_Graph_Bipartite()
print(is_graph_bipartite.isBipartite([[1],[0]]))
