# n! = 1 * 2 * 3 *...*n
# n! =[1 * 2 * 3 * 4...n-1] *n
# n! = n * (n-1)!

# n=int(input("Enter the number: "))
# product =1
# for i in range(n):
#     product = product * (i+1)
# print(product)


# def factorial_iter(n):
#     product=1
#     for i in range(n):
#      product=product * (i+1)
#     return product

 # f= factorial_iter(7)
# print(f)

def factorial_recursice(n):
   if n == 1 or n == 0:
      return 1
   return n *factorial_recursice(n-1)
 
f=factorial_recursice(1)
f=factorial_recursice(0)

print(f)
