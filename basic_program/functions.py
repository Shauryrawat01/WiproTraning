#functions
# def add(n1,n2):
#     sum= n1+n2
#     return sum
#

#driver
# num1=int(input('Enter a number'))
# num2=int(input('Enter a number'))
#
# res =add(num1,num2)
# print('add: ',res)


#arbitary
# def add(nums):
#     sum= 0
#     for n in nums:
#         sum +=n
#     return sum
#
# numbers =list()
# count =int(input("HOw many no."))
#
# for _ in range(1,count+1):
#     numbers.append(int(input('No: ')))
# #print(numbers)
# print(add(numbers))

#optional
# def add(n1,n2,n3=10):
#     return n1+n2+n3
#driver
# num1 =int(input("Enter the number"))
# num2=int(input('Enter the number'))
#
# print(add(num1,num2))
# print(add(num1,num2,100))

#lambda
numbers = [1, 2, 3, 4, 5]
sq = lambda nums: [num * num for num in nums if num % 2 == 0]
print(sq(numbers))