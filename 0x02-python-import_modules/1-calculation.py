from calculator_1 import add, sub, mul, div

a = 10
b = 5
addValue = add(a, b)
subValue = sub(a, b)
mulValue = mul(a, b)
divValue = div(a, b)

if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, addValue))
    print("{} - {} = {}".format(a, b, subValue))
    print("{} * {} = {}".format(a, b, mulValue))
    print("{} / {} = {}".format(a, b, divValue))
