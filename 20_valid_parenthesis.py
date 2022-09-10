# [
# ([](
# ([{}])
# (([])}
# (([{[]}]))
# []{}()
# []{}(
# )(

s = '[]{}('
stack = []
open = ['[', '(', '{']
open_close = {'[': ']',
              '{': '}',
              '(': ')'}

ans = True
for v in s:
    if v in open:
        stack.append(open_close[v])
    else:
        if len(stack) == 0:
            ans = False
            break
        else:
            if v != stack.pop():
                ans = False
                break

if len(stack) != 0:
    ans = False

print(ans)
