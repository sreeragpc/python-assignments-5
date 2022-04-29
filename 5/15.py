"""  Write a program to accept an array and display it on the console using functions
Program should contain 3 functions including main() function
"""


def getarray(l):
      size = int(input("enter the size of array"))
      print("enter the elements of array 1")
      for i in range(size):
         l.append(int(input()))
      return l
def displayarray(k):

        print("array = "+str(k))
def main():
    arr=[]
    l1=getarray(arr)
    displayarray(l1)
main()