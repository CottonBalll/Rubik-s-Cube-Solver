#Created By --------- Colton Caraway and Laura Lopera Usme and Caleb Patel

#assign unscrambled cube's values
#1 -> White
#2 -> Orange
#3 -> Green
#4 -> Red
#6 -> Blue
#7 -> Yellow

U = [1,1,1,1,1,1,1,1,1]
L = [2,2,2,2,2,2,2,2,2]
F = [3,3,3,3,3,3,3,3,3]
R = [4,4,4,4,4,4,4,4,4]
B = [5,5,5,5,5,5,5,5,5]
D = [6,6,6,6,6,6,6,6,6]

temp_U = U
temp_L = L
temp_F = F
temp_R = R
temp_B = B
temp_D = D

def unscramble():
  global U
  global L
  global F
  global R
  global B
  global D
  U = [1,1,1,1,1,1,1,1,1]
  L = [2,2,2,2,2,2,2,2,2]
  F = [3,3,3,3,3,3,3,3,3]
  R = [4,4,4,4,4,4,4,4,4]
  B = [5,5,5,5,5,5,5,5,5]
  D = [6,6,6,6,6,6,6,6,6]

def printcube():
  global U
  global L
  global F
  global R
  global B
  global D
  R1 = '       ', U[0:3]
  R2 = '       ', U[3:6]
  R3 = '       ', U[6:9]
  R4 = L[0:3], F[0:3], R[0:3], B[0:3]
  R5 = L[3:6], F[3:6], R[3:6], B[3:6]
  R6 = L[6:9], F[6:9], R[6:9], B[6:9]
  R7 = '       ', D[0:3]
  R8 = '       ', D[3:6]
  R9 = '       ', D[6:9]
  print(R1)
  print(R2)
  print(R3)
  print(R4)
  print(R5)
  print(R6)
  print(R7)
  print(R8)
  print(R9)
  print(' ')
  print(' ')
unscramble()
printcube()

#nice
def u():
  global U
  global L
  global F
  global R
  global B
  global D
  global temp_U
  global temp_L
  global temp_F
  global temp_R
  global temp_B
  global temp_D
  temp_U = U[6], U[3], U[0], U[7], U[4], U[1], U[8], U[5], U[2]
  temp_L = F[0], F[1], F[2], L[3], L[4], L[5], L[6], L[7], L[8]
  temp_F = R[0], R[1], R[2], F[3], F[4], F[5], F[6], F[7], F[8]
  temp_R = B[0], B[1], B[2], R[3], R[4], R[5], R[6], R[7], R[8]
  temp_B = L[0], L[1], L[2], B[3], B[4], B[5], B[6], B[7], B[8]
  temp_D = D
  U = temp_U
  L = temp_L
  F = temp_F
  R = temp_R
  B = temp_B
  D = temp_D
  printcube()

def up():
  global U
  global L
  global F
  global R
  global B
  global D
  global temp_U
  global temp_L
  global temp_F
  global temp_R
  global temp_B
  global temp_D
  temp_U = U[2], U[5], U[8], U[1], U[4], U[7], U[0], U[3], U[6]
  temp_L = B[0], B[1], B[2], L[3], L[4], L[5], L[6], L[7], L[8]
  temp_F = L[0], L[1], L[2], F[3], F[4], F[5], F[6], F[7], F[8]
  temp_R = F[0], F[1], F[2], R[3], R[4], R[5], R[6], R[7], R[8]
  temp_B = R[0], R[1], R[2], B[3], B[4], B[5], B[6], B[7], B[8]
  temp_D = D
  U = temp_U
  L = temp_L
  F = temp_F
  R = temp_R
  B = temp_B
  D = temp_D
  printcube()

def r():
  global U
  global L
  global F
  global R
  global B
  global D
  global temp_U
  global temp_L
  global temp_F
  global temp_R
  global temp_B
  global temp_D
  temp_U = U[0], U[1], F[2], U[3], U[4], F[5], U[6], U[7], F[8]
  temp_L = L
  temp_F = F[0], F[1], D[2], F[3], F[4], D[5], F[6], F[7], D[8]
  temp_R = R[6], R[3], R[0], R[7], R[4], R[1], R[8], R[5], R[2]
  temp_B = U[8], B[1], B[2], U[5], B[4], B[5], U[2], B[7], B[8]
  temp_D = D[0], D[1], B[6], D[3], D[4], B[3], D[6], D[7], B[0]
  U = temp_U
  L = temp_L
  F = temp_F
  R = temp_R
  B = temp_B
  D = temp_D
  printcube()

def rp():
  global U
  global L
  global F
  global R
  global B
  global D
  global temp_U
  global temp_L
  global temp_F
  global temp_R
  global temp_B
  global temp_D
  temp_U = U[0], U[1], B[6], U[3], U[4], B[3], U[6], U[7], B[0]
  temp_L = L
  temp_F = F[0], F[1], U[2], F[3], F[4], U[5], F[6], F[7], U[8]
  temp_R = R[2], R[5], R[8], R[1], R[4], R[7], R[0], R[3], R[6]
  temp_B = D[8], B[1], B[2], D[5], B[4], B[5], D[2], B[7], B[8]
  temp_D = D[0], D[1], F[2], D[3], D[4], F[5], D[6], D[7], F[8]
  U = temp_U
  L = temp_L
  F = temp_F
  R = temp_R
  B = temp_B
  D = temp_D
  printcube()

def f():
  global U
  global L
  global F
  global R
  global B
  global D
  global temp_U
  global temp_L
  global temp_F
  global temp_R
  global temp_B
  global temp_D
  temp_U = U[0], U[1], U[2], U[3], U[4], U[5], L[2], L[5], L[8]
  temp_L = L[0], L[1], D[0], L[3], L[4], D[1], L[6], L[7], D[2]
  temp_F = F[0], F[1], F[2], F[3], F[4], F[5], F[6], F[7], F[8]
  temp_R = U[6], R[1], R[2], U[7], R[4], R[5], U[8], R[7], R[8]
  temp_B = B
  temp_D = R[6], R[3], R[0], D[3], D[4], D[5], D[6], D[7], D[8]
  U = temp_U
  L = temp_L
  F = temp_F
  R = temp_R
  B = temp_B
  D = temp_D
  printcube()

def fp():
  global U 
  global L
  global F
  global R
  global B
  global D
  global temp_U
  global temp_L
  global temp_F
  global temp_R
  global temp_B
  global temp_D
  temp_U = U[0], U[1], U[2], U[3], U[4], U[5], R[0], R[3], R[6]
  temp_L = L[0], L[1], U[8], L[3], L[4], U[7], L[6], L[7], U[6]
  temp_F = F[2], F[5], F[8], F[1], F[4], F[7], F[0], F[3], F[6]
  temp_R = D[0], R[1], R[2], D[1], R[4], R[5], D[2], R[7], R[8]
  temp_B = B
  temp_D = L[2], L[5], L[8], D[3], D[4], D[5], D[6], D[7], D[8]
  U = temp_U
  L = temp_L
  F = temp_F
  R = temp_R
  B = temp_B
  D = temp_D
  printcube()
  
def l():
  global U
  global L
  global F
  global R
  global B
  global D
  global temp_U
  global temp_L
  global temp_F
  global temp_R
  global temp_B 
  global temp_D
  temp_U = B[2], U[1], U[2], B[5], U[4], U[5], B[8], U[7], U[8]
  temp_L = L[0], L[1], L[2], L[3], L[4], L[5], L[6], L[7], L[8]
  temp_F = U[0], F[1], F[2], U[3], F[4], F[5], U[6], F[7], F[8]
  temp_R = R
  temp_B = B[0], B[1], D[0], B[3], B[4], D[3], B[6], B[7], D[6]
  temp_D = F[0], D[1], D[2], F[3], D[4], D[5], F[6], D[7], D[8]
  U = temp_U
  L = temp_L
  F = temp_F
  R = temp_R
  B = temp_B
  D = temp_D
  printcube()

def lp():
  global U
  global L
  global F
  global R
  global B
  global D
  global temp_U
  global temp_L
  global temp_F
  global temp_R
  global temp_B
  global temp_D
  temp_U = F[0], U[1], U[2], F[3], U[4], U[5], F[6], U[7], U[8]
  temp_L = L[2], L[5], L[8], L[1], L[4], L[7], L[0], L[3], L[6]
  temp_F = D[0], F[1], F[2], D[3], F[4], F[5], D[6], F[7], F[8]
  temp_R = R
  temp_B = B[0], B[1], U[6], B[3], B[4], U[3], B[6], B[7], U[0]
  temp_D = B[8], D[1], D[2], B[5], D[4], D[5], B[2], D[7], D[8]
  U = temp_U
  L = temp_L
  F = temp_F
  R = temp_R
  B = temp_B
  D = temp_D
  printcube()
  
def d():
  global U
  global L
  global F
  global R
  global B
  global D
  global temp_U
  global temp_L
  global temp_F
  global temp_R
  global temp_B
  global temp_D
  temp_U = U
  temp_L = L[0], L[1], L[2], L[3], L[4], L[5], B[6], B[7], B[8]
  temp_F = F[0], F[1], F[2], F[3], F[4], F[5], L[6], L[7], L[8]
  temp_R = R[0], R[1], R[2], R[3], R[4], R[5], F[6], F[7], F[8]
  temp_B = B[0], B[1], B[2], B[3], B[4], B[5], R[6], R[7], R[8]
  temp_D = D[6], D[3], D[0], D[7], D[4], D[1], D[8], D[5], D[2]
  U = temp_U
  L = temp_L
  F = temp_F
  R = temp_R
  B = temp_B
  D = temp_D
  printcube()
  
def dp():
  global U
  global L
  global F
  global R
  global B
  global D
  global temp_U
  global temp_L
  global temp_F
  global temp_R
  global temp_B
  global temp_D
  temp_U = U
  temp_L = L[0], L[1], L[2], L[3], L[4], L[5], F[6], F[7], F[8]
  temp_F = F[0], F[1], F[2], F[3], F[4], F[5], R[6], R[7], R[8]
  temp_R = R[0], R[1], R[2], R[3], R[4], R[5], B[6], B[7], B[8]
  temp_B = B[0], B[1], B[2], B[3], B[4], B[5], L[6], L[7], L[8]
  temp_D = D[2], D[5], D[8], D[1], D[4], D[7], D[0], D[3], D[6]
  U = temp_U
  L = temp_L
  F = temp_F
  R = temp_R
  B = temp_B
  D = temp_D
  printcube()
  
def b():
  global U
  global L
  global F
  global R
  global B
  global D
  global temp_U
  global temp_L
  global temp_F
  global temp_R
  global temp_B
  global temp_D
  temp_U = R[2], R[5], R[6], U[3], U[4], U[5], U[6], U[7], U[8]
  temp_L = U[2], L[1], L[2], U[1], L[4], L[5], U[0], L[7], L[8]
  temp_F = F
  temp_R = R[0], R[1], D[8], R[3], R[4], D[5], R[6], R[7], D[2]
  temp_B = B[2], B[5], B[0], B[7], B[4], B[1], B[8], B[5], B[2]
  temp_D = D[0], D[1], D[2], D[3], D[4], D[5], L[0], L[3], L[6]
  U = temp_U
  L = temp_L
  F = temp_F
  R = temp_R
  B = temp_B
  D = temp_D
  printcube()
  
def bp():
  global U
  global L
  global F
  global R
  global B
  global D
  global temp_U
  global temp_L
  global temp_F
  global temp_R
  global temp_B
  global temp_D
  temp_U = L[6], L[3], L[0], U[3], U[4], U[5], U[6], U[7], U[8]
  temp_L = D[6], L[1], L[2], D[7], L[4], L[5], D[8], L[7], L[8]
  temp_F = F
  temp_R = R[0], R[1], U[0], R[3], R[4], U[1], R[6], R[7], U[2]
  temp_B = B[8], B[5], B[2], B[7], B[4], B[1], B[6], B[3], B[0]
  temp_D = D[0], D[1], D[2], D[3], D[4], D[5], R[8], R[5], R[2]
  U = temp_U
  L = temp_L
  F = temp_F
  R = temp_R
  B = temp_B
  D = temp_D
  printcube()
  
def Template():
  global U
  global L
  global F
  global R
  global B
  global D
  global temp_U
  global temp_L
  global temp_F
  global temp_R
  global temp_B
  global temp_D
  temp_U = U[0], U[1], U[2], U[3], U[4], U[5], U[6], U[7], U[8]
  temp_L = L[0], L[1], L[2], L[3], L[4], L[5], L[6], L[7], L[8]
  temp_F = F[0], F[1], F[2], F[3], F[4], F[5], F[6], F[7], F[8]
  temp_R = R[0], R[1], R[2], R[3], R[4], R[5], R[6], R[7], R[8]
  temp_B = B[0], B[1], B[2], B[3], B[4], B[5], B[6], B[7], B[8]
  temp_D = D[0], D[1], D[2], D[3], D[4], D[5], D[6], D[7], D[8]
  U = temp_U
  L = temp_L
  F = temp_F
  R = temp_R
  B = temp_B
  D = temp_D
  printcube()
#nice






