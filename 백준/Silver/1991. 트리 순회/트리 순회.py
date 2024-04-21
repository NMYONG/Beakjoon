N = int(input())
TREE = {}

ansPreorder = []
ansInorder = []
ansPostorder = []

for _ in range(N):
    root, left, right = input().split()
    TREE[root] = [left, right]

# 전위 순회
def preOrder(root):
    if root != '.':
        ansPreorder.append(root)
        preOrder(TREE[root][0])
        preOrder(TREE[root][1])

def inOrder(root):
    if root != '.':
        inOrder(TREE[root][0])
        ansInorder.append(root)
        inOrder(TREE[root][1])

def postOrder(root):
    if root != '.':
        postOrder(TREE[root][0])
        postOrder(TREE[root][1])
        ansPostorder.append(root)

preOrder('A')
inOrder('A')
postOrder('A')

print(''.join(map(str, ansPreorder)))
print(''.join(map(str, ansInorder)))
print(''.join(map(str, ansPostorder)))
