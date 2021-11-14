# 696. Count Binary Substrings
## Level: Easy

Give a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.


Approach for this problem:
    Approach 1: Create groups of varying sizes of legal substrings
        1. We can convert the string s into an array groups that represents the length of same-character contiguous blocks within the string. For example, if s = "110001111000000", then groups = [2, 3, 4, 6].
        2. For every binary string of the form '0' * k + '1' * k or '1' * k + '0' * k, the middle of this string must occur between two groups.
        3. Let's try to count the number of valid binary strings between groups[i] and groups[i+1]. If we have groups[i] = 2, groups[i+1] = 3, then it represents either "00111" or "11000". We clearly can make min(groups[i], groups[i+1]) valid binary strings within this string. Because the binary digits to the left or right of this string must change at the boundary, our answer can never be larger.

        Code:
        ```
        class Solution(object):
            def countBinarySubstrings(self, s):
                groups = [1]
                for i in xrange(1, len(s)):
                if s[i-1] != s[i]:
                    groups.append(1)
                else:
                    groups[-1] += 1

                ans = 0
                for i in xrange(1, len(groups)):
                    ans += min(groups[i-1], groups[i])
                return ans

        ```
        Runtime: O(n)

    Approach 2: Linear Scan 
        Intuition and Algorithm

        We can amend our Approach #1 to calculate the answer on the fly. Instead of storing groups, we will remember only       prev = groups[-2] and cur = groups[-1]. Then, the answer is the sum of min(prev, cur) over each different final     (prev, cur) we see.
        
        class Solution(object):
            def countBinarySubstrings(self, s):
                ans, prev, cur = 0, 0, 1
                for i in xrange(1, len(s)):
                    if s[i-1] != s[i]:
                        ans += min(prev, cur)---> This would give the number of substrings in substring s[i]
                        prev, cur = cur, 1
                    else:
                        cur += 1

                return ans + min(prev, cur)
