from collections import deque

class Solution:
    def __init__(self) -> None:
        self.graph = {}
        self.size: int = None
        
    def findCenter(self, edges: list[list[int]]) -> int:
        self.size = len(edges)

        if 3 <= len(edges) <= 100000:
            for edge in edges:
                    if len(edge) == 2:
                        if edge[0] not in self.graph:
                            self.graph[edge[0]] = [edge[1]]
                        else: 
                            self.graph[edge[0]].append(edge[1])

                        if edge[1] not in self.graph:
                            self.graph[edge[1]] = [edge[0]]
                        else: 
                            self.graph[edge[1]].append(edge[0])
                    else:
                        print("Invalid size")
        
        for key in self.graph.keys():
            if len(self.graph[key]) == self.size:
                return key
        return -1


if __name__ == "__main__":
    # edges = [[1,2],[2,3],[4,2]]
    edges = [[1,2],[5,1],[1,3],[1,4],[2,5]]
    center_of_star_graph = Solution()
    center = center_of_star_graph.findCenter(edges = edges)
    if center != -1:
        print(f"el centro del grafo es: {center}")
    else:
        print("No hay centro en este grafo")
