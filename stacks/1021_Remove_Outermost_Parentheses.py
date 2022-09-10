class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        cnt = 0
        ans = []

        for ch in s:
            if ch == '(':
                cnt += 1
                if cnt != 1:
                    ans.append(ch)
            else:
                cnt -= 1
                if cnt != 0:
                    ans.append(ch)

        return "".join(ans)