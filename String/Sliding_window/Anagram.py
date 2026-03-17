p = 'abc'
s = 'cbaebabacd'
p_count = [0] * 26
s_count = [0] * 26

for index in range(len(p)):
    p_count[ord(p[index]) - ord('a')] += 1
    s_count[ord(s[index]) - ord('a')] += 1

print(p_count)
print(s_count)