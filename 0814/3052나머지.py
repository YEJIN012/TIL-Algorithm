N = list(int(input()) for _ in range(10)) # 줄 별 입력값을 하나의 리스트 N으로 받기
reminder = []

for i in N :
    reminder.append(i % 42) # 나머지 리스트
reminder_set = set(reminder) # set으로 중복제거
print(len(reminder_set))


