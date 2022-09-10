def maxDepth(self, s: str) -> int:
    stack = []

    for ch in s:
        if ch in ['(', ')']:
            stack.append(ch)

    cnt_max = 0
    cnt = 0
    while len(stack) > 0:
        parth = stack.pop()

        if parth == ')':
            cnt += 1
        else:
            if cnt > cnt_max:
                cnt_max = cnt

            cnt -= 1

    return cnt_max