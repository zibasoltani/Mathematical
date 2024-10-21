import math

def math_operations(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("خطا: تقسیم بر صفر امکان‌پذیر نیست.")
        return num1 / num2
    elif operator == '^':
        return math.pow(num1, num2)
    else:
        raise ValueError("خطا: عملگر نامعتبر است.")

# دریافت ورودی از کاربر
try:
    number1 = float(input("عدد اول را وارد کنید: "))
    number2 = float(input("عدد دوم را وارد کنید: "))
    operator = input("عملگر ریاضی (+, -, *, /, ^) را وارد کنید: ")

    result = math_operations(number1, number2, operator)
    print("نتیجه:", result)

except ValueError as ve:
    print(ve)
except ZeroDivisionError as ze:
    print(ze)