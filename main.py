import sys
    
def get_user_input():
    return (sys.argv[1], sys.argv[2])

def add_numbers(num1, num2):
    return int(num1) + int(num2)

def main():
    num1, num2 = get_user_input()
    print(add_numbers(num1, num2))
    pass
main()