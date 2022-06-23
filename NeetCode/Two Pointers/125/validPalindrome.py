import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        regex = re.compile('[^a-zA-Z0-9]')
        
        lower = s.lower()
        phrase = lower.strip(' ')
        phrase = regex.sub('', phrase)
        for i in range(int(len(phrase) / 2)):
            if phrase[i] != phrase[len(phrase) - i - 1]:
                return False
        return True
             