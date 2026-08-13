
from calc import calculater

if __name__ == "__main__":
    x = float(input("enter first number:"))
    y = float(input("enter second number:"))
    c=calculater(x,y)
    print(c.sum ())
    print(c.sub ())
    print(c.mul ())
    print(c.div ())