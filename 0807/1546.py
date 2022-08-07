N = int(input())
report = list(map(int,input().split()))
max = max(report)
fake_report = []
for i in report :
        fake_report.append(i/max*100)

avrg = sum(fake_report)/N
print(avrg)