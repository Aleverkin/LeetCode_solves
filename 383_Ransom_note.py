ransomNote = "aabb"
magazine = "babbbbaa"


def my_ord(letter):
    return ord(letter) - ord('a')


ar = [0 for _ in range(26)]

for let in ransomNote:
    pos = my_ord(let)
    ar[pos] += 1

for let in magazine:
    pos = my_ord(let)

    if ar[pos] > 0:
        ar[pos] -= 1

if sum(ar) == 0:
    ans = True
else:
    ans = False

print(ans)
