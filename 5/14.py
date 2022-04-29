"""Write a program to add to two dimensional arrays
Program should accept two 2D arrays and display its sum
"""

size=int(input("enter the size of array"))
matrix1=[]
print("enter the elements of matrix 1")
for i in range(size):
  col1=[]
  for j in range(size):
    col1.append(int(input()))
  matrix1.append(col1)

matrix2=[]
print("enter the elements of matrix 2")
for i in range(size):
  col2=[]
  for j in range(size):
    col2.append(int(input()))
  matrix2.append(col2)

matrix3=[]
for i in range(size):
  col3=[]
  for j in range(size):
    col3.append(0)
  matrix3.append(col3)

for i in range(size):
  for j in range(size):
    matrix3[i][j]=matrix1[i][j]+matrix2[i][j]

for i in range(size):
  for j  in range (size):
     print(matrix3[i][j],end=" ")
  print()
