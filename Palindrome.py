# Owm solution
def isPalindrome(text):
    reversed_str = "".join(list(reversed(text.lower().replace(" ", ""))))
    return reversed_str == text.lower()
    
print(isPalindrome("RAcecar"))

# Tutorial's solution
import re

def is_palindrome(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backwards = forwards[::-1]
    return forwards == backwards