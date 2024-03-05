from typing import List

def dfs(graph: List[List[int]], mark: List[bool], vertex: int) -> None:
    if mark[vertex]:
        return None
    
    mark[vertex] = True
    for adj in graph[vertex]:
        dfs(graph, mark, adj)
