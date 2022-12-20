jobs =  [[0, 3], [4, 9], [4, 6]]
answer = 0
N = len(jobs)
for i in range(len(jobs)) :
    jobs[i] += [jobs[i][0],jobs[i][0]+jobs[i][1]]   # [요청시간, 소요시간, 작업시작가능시간, 종료예정시간]
print(jobs)

jobs.sort(key = lambda x : x[0])        # 첫 시작은 작업을 진행중이지 않으므로, 먼저 요청된 작업 순으로 정렬.
for i in range(len(jobs)-1, 0, -1) :
    for j in range(i) :
        if jobs[j][2] == jobs[j+1][2] and jobs[j][3] > jobs[j+1][3] :   # 작업시작가능시간이 동일한 경우, 종료시간이 빠른 작업을 우선으로 나열 (버블정렬)
            jobs[j], jobs[j+1] = jobs[j+1], jobs[j]
print(jobs)

cnt = 1
job = jobs.pop(0)   # job : 진행될 작업
# 중간에 작업이 쉬어가는 경우 실제 시간보다 작업시간이 작을 수 있다. (-> 종료시간이 남은 작업들의 요청시간보다 이른 경우)
realtime = job[3]   # 실제 시간(작업종료시간)
jobtime = job[1]    # 실제 작업 시간
print(jobtime, realtime)

flag = 0        # 작업을 쉬어가는지, 이어가는지 판별 flag
while jobs :
    for i in range(len(jobs)):      # 남은 작업리스트 순회.
        flag = 0
        if realtime > jobs[i][0] :  # 현재 시간(작업종료시간)이  요청시간을 지났으면,
            jobs[i][2] = realtime   # 시작가능시간은 현재시간으로 바뀐다(딜레이).
            jobs[i][3] = jobs[i][2] + jobs[i][1]    # 종료예정시간도 바뀜.
            flag = 1                # 작업이 쉬지않고 이어감.
        else :  # 요청시간이 현재시간보다 빠른 애들이 이제 없으면,
            break   # 끝
    if flag == 1 :  # 작업을 쉬지않고 이어가면,
        jobs.sort(key=lambda x: x[2])   # 시작가능시간을 기준으로 남은 작업리스트 재정렬.
    else :          # 작업을 쉬어가면,
        jobs.sort(key=lambda x: x[0])   # 요청시간을 기준으로 남은 작업리스트 재정렬.
    print(jobs)
    for i in range(len(jobs) - 1, 0, -1):
        for j in range(i):
            if jobs[j][2] == jobs[j + 1][2] and jobs[j][3] > jobs[j + 1][3] :   # 작업시작가능시간이 동일한 경우, 종료시간이 빠른 작업을 우선으로 나열 (버블정렬)
                jobs[j], jobs[j + 1] = jobs[j + 1], jobs[j]
    print(jobs)

    # 재정렬 후, 다음 작업 선택.
    job = jobs.pop(0)
    print(job)
    if job[0] < realtime :      # 요청시간이 현재 시간보다 빨랐으면,
        jobtime += (realtime-job[0]) + job[1]   # 작업시간 = 대기시간 + 소요시간    # job[2] = realtime
    else :                      # 대기가 없었으면,
        jobtime += job[1]       # 작업시간 = 소요시간
    realtime = job[3]           # 현재시간 = 작업 종료시간
    print(jobtime, realtime)
avg = jobtime // N
answer = avg
print(answer)