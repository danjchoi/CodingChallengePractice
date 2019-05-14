class Solution:
    def _odd_palindrome(self, s):
        center = 1
        left = center - 1
        right = center + 1
        longest = s[0]
        while center < len(s):
            while 0 <= left and right < len(s) and s[left] == s[right]:
                current_palindrome = s[left:right + 1]
                longest = (
                    current_palindrome
                    if len(longest) <= len(current_palindrome)
                    else longest
                )
                left -= 1
                right += 1
            center += 1
            left = center - 1
            right = center + 1
        return longest

    def _even_palindrome(self, s):
        left_start = 0
        right_start = 1
        longest = ""
        while left_start < len(s) - 1:
            left = left_start
            right = right_start
            while 0 <= left and right < len(s) and s[left] == s[right]:
                current_palindrome = s[left:right + 1]
                longest = (
                    current_palindrome
                    if len(longest) < len(current_palindrome)
                    else longest
                )
                left -= 1
                right += 1
            left_start += 1
            right_start += 1
        return longest

    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        odd_pali = self._odd_palindrome(s)
        even_pali = self._even_palindrome(s)
        return odd_pali if len(odd_pali) > len(even_pali) else even_pali
        
def stringToString(input):
    # import json

    # return json.loads(input)
    return input

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            s = stringToString(line);
            
            ret = Solution().longestPalindrome(s)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()