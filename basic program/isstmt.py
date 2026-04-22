#big2
# num1= int(input("Enter a number"))
# num2=int(input('Enter another number'))
#
# if num1 ==num2:
#     print('Both are equal')
# elif num1 >num2 :
#     print(num1, 'is big.')
# else:
#     print(num2, 'is big')

#big 3
#
# num1= int(input("Enter a number"))
# num2 =int(int("Enter another number"))
# num3 =int(int("Enter another number"))
#
# if num1==num2 and num2 == num3:
#     print('All value are equal')
#
# elif num1>num2 and num1>num3:
#     print(num1, 'num1 is biggest')
# elif num2>num1 and num2>num3:
#     print(num2, 'num2 is biggest')
# elif num3>num2 and num3>num1:
#     print(num3 ,'num3 is biggest')

#weekday
ch=int(input('Enter a number bet 1-7'))

match (ch):
    case 1 :
        print('Monday')
    case 2 :
        print('Tuesday')
    case 3:
        print('Wed')
    case 4:
        print('Thus')
    case 5:
        print('friday')
    case 6:
        print('sat')
    case 7:
        print('sun')
    case _:
        print('Invalid choice')