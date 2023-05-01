#Largest number in List.
print("Enter list of number with spaces.")
arr=list(map(int,input().split()))
print(max(arr))
    
#Smallest number in List.
print("Enter list of number with spaces.")
arr=list(map(int,input().split()))
print(min(arr))

#Sum of all number in List.
print("Enter list of number with spaces.")
arr=list(map(int,input().split()))
print(sum(arr))

#Sorting of List(Ascending order).
print("Enter list of number with spaces.")
arr=list(map(int,input().split()))
arr.sort()
print(arr)

#print all number of List
print("Enter list of number with spaces.")
arr=list(map(int,input().split()))
print(*arr)

#Print all values of List in single Line.
print("Enter list of number with spaces.")
arr=list(map(int,input().split()))
print(*arr,end=" ")

#Reversed of List.
print("Enter list of number with spaces.")
arr=list(map(int,input().split()))
print(arr[::-1])
