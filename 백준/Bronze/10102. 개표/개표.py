V = int(input())
vote = input()

A = vote.count('A')
B = V - A

print('A' if A > B else 'Tie' if A == B else 'B')