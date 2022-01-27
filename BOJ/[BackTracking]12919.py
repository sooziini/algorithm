# A와 B 2 - BackTracking

import sys

s=sys.stdin.readline().rstrip()
t=sys.stdin.readline().rstrip()

def back_tracking(string):
    if len(string)==len(s):
        return string==s
    if string[0]=='B' and back_tracking(string[:0:-1]):
        return True
    if string[-1]=='A' and back_tracking(string[:-1]):
        return True

print(1 if back_tracking(t) else 0)

# 시간 초과
def change_string(string):
    if len(string)==len(t):
        return string==t
    if change_string(string+'A'):
        return True
    if change_string((string+'B')[::-1]):
        return True

print(1 if change_string(s) else 0)