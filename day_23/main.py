low = "abcdefghijklmnopqrstuvwxyz"
upp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

shift = 1

trans = dict(     zip(map(ord, low), low[shift:] + low[:shift])     )

# print(low[shift:] + low[:shift])
thing = "abc"
result = list(map(ord, low))
print(result)