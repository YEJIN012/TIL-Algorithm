numbers = [3, 30, 34, 5, 9]
answer = ''

# numbers = [30, 3]
# 숫자형으로 비교하게되면 303이 되지만,
# 하지만, 330가 더 큰수
# ! 숫자 자릿수가 다른 케이스에서 특이비교가 필요한 것이므로
# 해당 숫자는 반복해서 붙여주고 -> 3030 33
# ! 어차피 문자형 정렬이면 앞자리부터 비교하므로 30 33 비교로 정렬이 끝남. -> 330
# 즉, 모든 원소 각각에 가장 앞에 있는 문자 하나만 맨 뒤에 덧붙이는 것(가장 큰자리의 숫자를 맨 뒤에 더해주는 것)과 동일.


numbers_str = [str(num) for num in numbers]     # 문자형으로 바꾸기
numbers_str.sort(key = lambda num : num, reverse=True)
# 원소들은 1000이하의 숫자이므로
# 최대 한자리 숫자와 1000의 비교를 고려하여 문자열*3한 값을 키로 내림차순 정렬.
answer = str(int(''.join(numbers_str)))
print(answer)
