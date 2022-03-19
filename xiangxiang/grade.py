credit = [3, 3, 3, 2, 1, 4, 2, 2, 2, 2, 2, 2, 2]
score = [78, 88, 96, 81, 90, 85, 93, 95, 90, 90, 85, 85, 85]
label = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
sum1 = 0
sum2 = 0

for index in range(len(score)):
    sum1 = sum1 + credit[index] * score[index]
    if label[index] != 0:
        sum2 = sum2 + credit[index] * score[index]

print("score1 = ", sum1/30)
print("score2 = ", sum2/16)