#palindrome using slicing

def isPalindrome(s):
    return s ==s[::-1]
s="malayalam"
n=isPalindrome(s)
if n:
    print("yes")
else:
    print("no")
