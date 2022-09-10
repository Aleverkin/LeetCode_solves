inpt = ["flower", "flow", "flight"]

m = min([len(x) for x in inpt])

ans = inpt[0][:m]
close = False
for j in range(m):
    s = inpt[0][j]

    for x in inpt[1:]:
        if x[j] != s:
            ans = inpt[0][:j]
            close = True
            break

    if close:
        break

print(ans)
