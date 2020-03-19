import re
def longestPal(s):
    pattern = r'\,|\s|\:|\.|\-|\_'
    s = re.sub(pattern, '', s.lower())
    ans = ""
    for i in range(len(s)):
        for k in range(2):
            temp = helper(s, i, i + k)
            if len(temp) > len(ans):
                ans = temp
    return ans
def helper(s, l, r):
    while l >= 0 and r < len(s) and s[r] == s[l]:
        l -= 1
        r += 1
    return s[l+1:r]
x = input(">")
print(longestPal(x))