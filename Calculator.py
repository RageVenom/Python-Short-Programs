# Menu Driven Calculator.
oper={'+': lambda x,y: x+y,
      '-': lambda x,y: x-y,
      '*': lambda x,y: x*y,
      '/': lambda x,y: x/y,
      '^': lambda x,y: x**y}
print("\t\tCalculator.\n")
print("\tMenu for Operations: \n -> Addition(+) \n -> Subtraction(-) \n -> Multiplication(*)\n -> Division(/) \n -> Power(^) \n")
a=input()
print("Enter two number separate by space.")
x,y=map(int,input().split())
if a in ["+","-","*","^","/"]:
    print(oper[a](x,y))
else:
    print("Wrong Operator.")
