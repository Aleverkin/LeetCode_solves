# Длины
# могут
# быть
# пустыми
#
# ab
# aca
#
# "axc"
# "ahbgdc"


def is_subsequence(s, t):
    j = 0
    for i in range(len(s)):
        while j < len(t) and s[i] != t[j]:
            j += 1

        if j == len(t):
            return False

        j += 1

    return True





