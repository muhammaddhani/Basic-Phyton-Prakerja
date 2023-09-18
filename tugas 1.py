def add_number(a,b):
    try:
        result = int(a) + int(b)
        return result
    except ValueError:
        raise ValueError("Both parameters must be numerical")
    
try:
    num1 = input("Enter The First Number:")
    num2 = input("Enter the second number:")

    sum_result = add_number(num1, num2)
    print("The sum is:", sum_result)
except ValueError as kesalahan:
    print("error:",str(kesalahan))