def carry_forward(arr):
    result=0
    acounter=0
    for i in range(len(arr)):
        if arr[i]=='a':
            acounter+=1
        elif arr[i]=='g':
            result+=acounter
        else:
            pass
    return result

arr=list(map(str,input().split()))
i=input()
j=input()
print(carry_forward(arr))