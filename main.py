class Solution:
    def is_palindrome(self, x: int) -> bool:
        if (str(x))[::1] == (str(x))[::-1]:
            print("true")
            return True

        else:
            print("false")
            return False


ob = Solution()
ob.is_palindrome(56789)
