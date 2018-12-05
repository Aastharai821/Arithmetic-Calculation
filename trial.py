def main():
    x=int(input("Enter the first no "))
    y=int(input("Enter the second no "))
    op=input("Enter what operation you wanna do + or - or * or / ")
    if op=='+':
        add(x,y)
    elif op=='-':
        sub(x,y)
    elif op=='*':
        mult(x,y)
    else: 
        op = '/'
        div(x,y)

def add(x,y):
    a=x+y
    print("The sum is: %d"%a)
def sub(x,y):
    b=x-y
    print("The difference is:%d "%b)
def mult(x,y):
    c=x*y
    print("The multiplication is: %d"%c)
def div(x,y):
    d=x/y
    print("The division is: %d"%d)

if __name__ == "__main__":
    main()