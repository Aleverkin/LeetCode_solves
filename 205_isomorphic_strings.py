# isomorphic
# strings
#
# s and t - ascii
# s and t
# same
# length
# s.legt
#
# egg
# add
# True
# egg
# ads
#
# true
# fals
# True


def is_isomorphic(s: str, t: str) -> bool:
    d = {}

    for i in range(len(s)):
        try:
            new_let = d[s[i]]

            if new_let != t[i]:
                return False
        except:
            if t[i] in d.keys():
                return False

            d[s[i]] = t[i]

    return True
