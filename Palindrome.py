#Take Number as a String.
Num=input()

#Check Number is equals to its reverse.
if Num==Num[::-10]:
  print("Palindrome.")
else:
  print("Not a Palindrome.")
