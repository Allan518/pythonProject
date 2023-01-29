class Solution:
    def isValid(s):
        p1 = 0
        p2 = 0
        p3 = 0
        for i in range(len(s)):
            if s[i] == "(":
                p1 += 1
            elif s[i] == ")":
                if p2 != 0 or p3 != 0 or p1 < 1:
                    return False
                p1 -= 1
            elif s[i] == "{":
                p2 += 1
            elif s[i] == "}":
                if p1 != 0 or p3 != 0 or p2 < 1:
                    return False
                p2 -= 1
            elif s[i] == "[":
                p3 += 1
            elif s[i] == "]":
                if p1 != 0 or p2 != 0 or p3 < 1:
                    return False
                p3 -= 1
        if p1 == 0 & p2 == 0 & p3 == 0:
            return True
        return False
    print(isValid("{}{}())("))
