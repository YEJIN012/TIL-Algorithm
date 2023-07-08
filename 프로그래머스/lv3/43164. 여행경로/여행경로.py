def solution(tickets):
    global visited
    t_dict = {tickets[0][0] : [tickets[0][1]]}
    visited = {tickets[0][0] : [0]}
    for i in range(1, len(tickets)) :
        if tickets[i][0] in t_dict.keys() :
            t_dict[tickets[i][0]].append(tickets[i][1])
            t_dict[tickets[i][0]].sort()
            visited[tickets[i][0]].append(0)
        else :
            t_dict[tickets[i][0]] = [tickets[i][1]]
            visited[tickets[i][0]] = [0]
    # t_dict = {'ICN': ['ATL', 'SFO'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}
    # visited = {'ICN': [0, 0], 'SFO': [0], 'ATL': [0, 0]}
    
    def dfs (s, answer) :
        global visited
        
        sum_visited  = 0
        for r in visited.values() :
            sum_visited += sum(r)
        if sum_visited == len(tickets) :
            answer.append(s)
            return
        
        else :
            for i in range(len(t_dict[s])) :
                if visited[s][i] == 0 :
                    visited[s][i] = 1
                    answer.append(s)
                    dfs(t_dict[s][i], answer)

    answer = []
    dfs('ICN', answer)
    
    
    return answer