def reverse_array(A,B,C):
    while(B<C):
        A[B],A[C]=A[C],A[B]
        B+=1
        C-=1
    return A


A=list(map(int,input("Enter the array Elements: ").split()))
B=int(input("Enter the Start range: "))
C=int(input("Enter the End range: "))
output=reverse_array(A,B,C)
print("The Reversed Array: ",end=" ")
for i in range(len(A)):
    print(A[i],end=" ")