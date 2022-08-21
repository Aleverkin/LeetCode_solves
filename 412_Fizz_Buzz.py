n = 15

ans = []
for x in range(1, n + 1):
    if x % 5 == 0:
        if x % 3 == 0:
            ans.append("FizzBuzz")
            continue
        else:
            ans.append("Buzz")
            continue
    elif x % 3 == 0:
        ans.append("Fizz")
    else:
        ans.append(str(x))


print(ans)