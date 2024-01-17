# 7567 그릇

bowl = input()
length = 10

for i in range(len(bowl)-1):
    if bowl[i] == bowl[i+1]:
        length += 5
    else:
        bowl[i] != bowl[i+1]
        length += 10

print(length)    