from collections import defaultdict, deque 
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        answer = []
        var_dict = defaultdict(dict)
        for i in range(len(equations)):
            a, b = equations[i]
            value = values[i]
            var_dict[a][b] = value
            var_dict[b][a] = 1 / value
        def findDivision(query):
            if query[0] in var_dict and query[1] in var_dict:
                var_set = set()
                queue = deque([(query[0], 1)])
                while queue:
                    var, value = queue.popleft()
                    if var == query[1]:
                        return value
                    var_set.add(var)
                    if var in var_dict:
                        for key, new_value in var_dict[var].items():
                            if key not in var_set:
                                var_set.add(key)
                                queue.append((key, new_value * value))
            return -1            
        for query in queries:
            answer.append(findDivision(query))
        return answer


            


#1 a -> 2b -> 
#b1 -> 1/2a 
#1b -> 3c 
#1c -> 1/3b

