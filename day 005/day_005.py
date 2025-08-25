''' generate scores
import random

i = 0
scores = []
while i < 17:
    scores.append(random.randint(30, 100))
    i += 1

print(scores)
'''

scores = [55, 93, 92, 51, 84, 73, 63, 36, 55, 31, 93, 35, 99, 90, 46, 53, 63]
# print(max(scores))
max_score = 0
for score in scores:
    if max_score < score:
        max_score = score
print(max_score)

# range function
gauss_challenge = 0
for number in range(1, 101):
    gauss = gauss + number
print(gauss_challenge)
