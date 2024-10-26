a = set(input().split())
# for i in sorted(list(a)):
#     print('{\n"key": "', i, '",\n"text": ', i, '\n},', sep="")
print(*a, sep='", "')
