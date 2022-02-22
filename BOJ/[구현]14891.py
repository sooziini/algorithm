# 톱니바퀴 - 구현

import sys

gears=[list(sys.stdin.readline().rstrip()) for _ in range(4)]
k=int(sys.stdin.readline())
needs={}

def rotate(needs):
    global gears
    for gear_idx, direc in needs.items():
        if direc==-1:
            tmp=[gears[gear_idx].pop(0)]
            gears[gear_idx]+=tmp
        elif direc==1:
            tmp=[gears[gear_idx].pop(-1)]
            gears[gear_idx]=tmp+gears[gear_idx]

def chk(gear_idx, direc):
    global needs
    needs[gear_idx]=direc
    prev,next=gear_idx-1,gear_idx+1
    if prev>=0 and prev not in needs:
        if gears[prev][2]!=gears[gear_idx][6]:
            chk(prev, direc*-1)
    if next<=3 and next not in needs:
        if gears[gear_idx][2]!=gears[next][6]:
            chk(next, direc*-1)

for _ in range(k):
    gear_num,direc=map(int, sys.stdin.readline().split())
    chk(gear_num-1, direc)
    rotate(needs)

print(sum(int(gears[i][0])*pow(2, i) for i in range(4)))