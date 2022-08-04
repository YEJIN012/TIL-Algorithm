now = list(map(int, input().split()))
cooking = int(input())
now[0] += (now[1] + cooking) // 60 
now[0] = now[0] % 24
now[1] = (now[1] + cooking) % 60
# print(now)
end_time = ' '.join(map(str,now))
print(end_time)