croatia = list(input())
N = len(croatia)

cro_lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

cnt = 0
i = 0

while i < N:
    if i <= N-2 and (croatia[i]+croatia[i+1] in cro_lst):
        cnt += 1
        i += 2
    elif i <= N-3 and (croatia[i]+croatia[i+1]+croatia[i+2] in cro_lst):
        cnt += 1
        i += 3
    else:
        cnt += 1
        i += 1

print(cnt)