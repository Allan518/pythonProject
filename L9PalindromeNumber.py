class Solution(object):
    def isPalindrome(x):
        s = str(x)

        if s[0] == '-':
            return False

        t_f = True

        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                t_f = False
                break

        return t_f
    print(isPalindrome(1321))
    '''def is_palindrome(x):
        s = str(x)
        if s[0] == "-":
            return False
        ans = True
        for i in range(len(s) // 2):
            if s[i] != s[len[s] - 1 - i]:
                ans = False
        return ans

    print(is_palindrome(121))'''
