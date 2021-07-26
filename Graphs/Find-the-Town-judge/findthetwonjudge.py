from collections import deque

class Solution:
    def __init__(self) -> None:
        self.graph = {}
        self.search_queue = deque()
        self.searched = set()
        self.judge: int = None
        self.there_is_a_judge: bool = False

    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        '''
        trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
        '''
        #1) load the information to the graph
        if 1 <= n <= 1000 and len(trust) < 104:
            for edge in trust:
                """
                check if the node already exist
                """
                if len(edge) == 2:
                    if edge[0] not in self.graph:
                        self.graph[edge[0]] = [edge[1]]
                    else: 
                        self.graph[edge[0]].append(edge[1])
                else:
                    print("Invalid pair of values")
        else:
            print("Number of labels or soze of the trust vector not allowed")

        #TODO: 2) Look for the judge base on the information given
        #load the search_queue with the first key of the graph's keys
        self.search_queue += self.graph[list(self.graph.keys())[0]]

        while self.search_queue:
            person = self.search_queue.popleft()
            if person not in self.searched:
                if self.person_is_judge(person):
                    self.set_judge(person)
                    self.set_there_is_a_judge(True)
                else:
                    self.searched.add(person)
                    try:
                        self.search_queue += self.graph[person]
                    except KeyError:

                        # if it's not define and not a judge, then the vector brakes the rules and there´s no judge at all.
                        break
        if self.get_there_is_a_judge():
            return self.get_judge()
        else:
            return -1
    #TODO: 3) return the result
    
    def person_is_judge(self, person:int) -> bool :
        for key in self.graph:
            if person not in self.graph[key]:
                return False
            
        try:
            # when i'm loading the graph, there's no way the key "judge" exist, it's always as a second value
            self.graph[person]
            return False
        except KeyError:
            return True
    
    ################# SETTERS ####################
    def set_there_is_a_judge(self, state: bool):
        self.there_is_a_judge = state

    def set_judge(self, person:int):
        self.judge = person

    ################# GETTERS ####################
    def get_judge(self):
        return self.judge
    
    def get_there_is_a_judge(self):
        return self.there_is_a_judge
        
        
if __name__ == "__main__":
    
    """ n = 2
    trust = [[1,2]] """

    """ n = 3
    trust = [[1,3],[2,3]] """

    """ n = 3
    trust = [[1,3],[2,3],[3,1]] """
    
    """ n = 3
    trust = [[1,2],[2,3]] """
    
    n = 4
    trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
    
    judge_finder = Solution()
    judge = judge_finder.findJudge(n=n,trust=trust)
    if judge != -1:
        print(f"The judge is: {judge}")
    else:
        print("There is no Judge in the Town")
