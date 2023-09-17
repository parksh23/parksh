#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      USER
#
# Created:     03-04-2023
# Copyright:   (c) USER 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#오늘도 화이팅..!

ANS=[]
for _ in range(4) :
    Poin  = list(map(int,input().split()))
    point = [[x,y] for x,y in zip(Poin[0::2], Poin[1::2])]
    A,B,C,D = point[0],point[1],point[2],point[3]
    if (B[0]-A[0])+(D[0]-C[0]) < D[0]-A[0] and (B[1]-A[1])+(D[1]-C[1]) < D[1]-A[1]:
        ANS.append("NULL")
    elif (B[0]-A[0])+(D[0]-C[0]) == D[0]-A[0] and (B[1]-A[1])+(D[1]-C[1])==D[1]-A[1]:
        ANS.append("POINT")
    elif (B[0]-A[0])+(D[0]-C[0]) == D[0]-A[0] or (B[1]-A[1])+(D[1]-C[1])==D[1]-A[1]:
        ANS.append("LINE")
    else : ANS.append("FACE")
def print_result() :
    for i in range(1,5):
        print(ANS[i-1])
print_result()
