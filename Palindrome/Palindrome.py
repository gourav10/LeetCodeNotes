import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        #reverse number
        if x<0: return False
        num = x
        reverseNum=0
        while num != 0:
            temp = num%10
            reverseNum = reverseNum*10+temp
            num = math.floor(num/10)
        
        if reverseNum == x:
            return True
        else:
            return False


if __name__ == "__main__":
    x = int(input("Enter a number"))
    s = Solution()
    if(s.isPalindrome(x)):
        print("{} is palindrome".format(x))
    else:
        print("{} is not Palindrome".format(x))


