import os

print( "Recursion Examples\n\n0. Exit\n1.Palindrome\n2.Factorial\n3.Fibonacci\n4.GCD\n5.Tower of Hanoi\n6.Binary Search\n7.Word Count\n8.Structural Recursion\n")
print("Enter your choice:\n")
var= int(input())

if var == 1:
   print("1 - palindrome")
   import palindrome
   #print (var)
elif var == 2:
   print("2 - factorial")
   import factorial
   #print (var)
elif var == 3:
   print("3 - fibonacci")
   import fibonacci
   #print (var)
elif var == 4:
   print("4 - GCD")
   import gcd
   #print (var)
elif var == 5:
   print("5 - Tower of Hanoi")
   import towerofhanoi
   #print (var)
elif var == 6:
   print("6 - Binary Search")
   import binarysearch
   #print (var)
elif var == 7:
   print("7 - Word Count")
   import wordcount
   #print (var)
elif var == 8:
   print("8 - Structural Recursion")
   import structuralrecursion
   #print (var)
elif var == 0:
   print(" 0 - Exit")
   exit()
   #print (var)

print ("Thanks for using Recursion, Good bye!")


