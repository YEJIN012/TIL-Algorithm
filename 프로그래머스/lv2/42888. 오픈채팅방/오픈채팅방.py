def solution(record):
    nickname = {}
    id_action = [] 
    
    # 기록을 전체 순회하면서, nickname 딕셔너리에서 id별 최종 닉네임을 저장한다.
    #                      id_action 배열에 유저들의 동작을 [id, action] 이중배열로 순서대로 기록한다.
    for idx, r in enumerate(record) :
        arr = r.split(' ')
        if len(arr) >= 3 :
            nickname[arr[1]] = arr[2]
        id_action.append([arr[1],arr[0]])
    
    # 최종 return되는 result 배열에
    # id별 최종 닉네임과 기록된 액션에 대한 출력메세지를 순서대로 저장한다.
    result = []
    for idaction in id_action :
        message = str(nickname[idaction[0]])
        if idaction[1] == "Enter" :
            result.append(message + '님이 들어왔습니다.')
        elif idaction[1] == "Leave" :
            result.append(message + '님이 나갔습니다.')
        
    return result