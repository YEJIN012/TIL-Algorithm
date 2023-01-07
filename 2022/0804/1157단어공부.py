word = input()
word_upper = word.upper()

alphabet_numbers = []
alphabet = list(map(str,set(word_upper))) # 중복 알파벳 제거- 사용된 고유 알파벳 리스트

for i in alphabet :
    alphabet_numbers.append(word_upper.count(i)) # 각 알파벳이 단어에서 사용된 횟수를 받은 alphabet_numbers 리스트

# print(alphabet)
# print(alphabet_numbers)
max = max(alphabet_numbers) # max = 가장 많이 사용된 알파벳의 사용된 횟수
# print(max)
index = alphabet_numbers.index(max) # alphabet_numbers 리스트에서 가장 많이 사용된 알파벳의 index (=alphabet 리스트에서의 index)
# print(index)
if alphabet_numbers.count(max) != 1: # max 값이 여러개이면 ? 출력
    print('?')

else :
    print(alphabet[index])