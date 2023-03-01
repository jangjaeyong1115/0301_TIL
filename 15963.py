import sys
input = sys.stdin.readline

a,b = map(int,input().split())

if a == b:
    print(1)

if a != b:
    print(0)