if x < 0:
	print(False)
else:
	x = str(x)

	ans = True
	for i in range(int(len(x) / 2)):
		if x[i] != x[-(i + 1)]:
			ans = False
			break

	print(ans)

# 1
# 11
# 12
# 121
# 12321
# 12221
# 1221
# 1231
# 1234