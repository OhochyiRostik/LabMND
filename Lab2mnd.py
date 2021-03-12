import random, math, numpy as np

X = [[-1, -1],
 	 [1, -1],
     [-1, 1]]

variant = 121
Ymax = (30 - variant)*10
Ymin = (20 - variant)*10
X1min = 10
X1max = 40
X2min = -30
X2max = 45
m = 5

Y = [[random.randint(Ymin, Ymax) for i in range(m)] for j in range(3)]


serY = []
disp = []
for i in range(3):
	serY.append(round(sum(Y[i])/m, 2))
	s = 0
	for j in range(m):
		s += (Y[i][j]-serY[i])**2
	disp.append(round(s/m, 2))

sigma = math.sqrt((2*(2*m-2))/(m*(m-4)))
F1=disp[0]/disp[1]
F2=disp[2]/disp[0]
F3=disp[2]/disp[1]

O1=((m-2)/m)*F1
O2=((m-2)/m)*F2
O3=((m-2)/m)*F3

R1=abs(O1-1)/sigma
R2=abs(O2-1)/sigma
R3=abs(O3-1)/sigma


mx1 = (X[0][0]+X[1][0]+X[2][0])/3
mx2 = (X[0][1]+X[1][1]+X[2][1])/3
my = sum(serY)/3


a1 = (X[0][0]**2+X[1][0]**2+X[2][0]**2)/3
a2 = (X[0][0]*X[0][1] + X[1][0]*X[1][1] + X[2][0]*X[2][1])/3
a3 = (X[0][1]**2+X[1][1]**2+X[2][1]**2)/3


a11 = (X[0][0]*serY[0]+X[1][0]*serY[1]+X[2][0]*serY[2])/3

a22 = (X[0][1]*serY[0]+X[1][1]*serY[1]+X[2][1]*serY[2])/3


b0 = (np.linalg.det([[my,mx1,mx2],[a11,a1,a2],[a22,a2,a3]])/
	np.linalg.det([[1,mx1,mx2],[mx1,a1,a2],[mx2,a2,a3]]))

b1 = (np.linalg.det([[1,my,mx2],[mx1,a11,a2],[mx2,a22,a3]])/
	np.linalg.det([[1,mx1,mx2],[mx1,a1,a2],[mx2,a2,a3]]))

b2 = (np.linalg.det([[1,mx1,my],[mx1,a1,a11],[mx2,a2,a22]])/
	np.linalg.det([[1,mx1,mx2],[mx1,a1,a2],[mx2,a2,a3]]))

ynorm1 = b0-b1-b2
ynorm2 = b0+b1-b2
ynorm3 = b0-b1+b2

dx1 = abs(X1max-X1min)/2
dx2 = abs(X2max-X2min)/2

x10 = (X1max+X1min)/2
x20 = (X2max+X2min)/2

A0 = b0-b1*(x10/dx1)-b2*(x20/dx2)
A1 = b1/dx1
A2 = b2/dx2

ynat1 = A0+A1*X1min+A2*X2min
ynat2 = A0+A1*X1max+A2*X2min
ynat3 = A0+A1*X1min+A2*X2max


print('Нормована матриця планування експерименту: ')
for i in range(3):
	print(X[i])
print('Матриця планування: ')
for i in range(3):
	print(Y[i])
print('Середні значення У: ', serY)
print('Дисперсії: ', disp)
print('Основне відхилення: ', round(sigma, 2))
print('Критерії романовського: ','R1 =', round(R1, 1),' R2 =', round(R2, 1),' R3 =', round(R3, 1))
print('-----------------------------------------------------------------------------')
if R1<2 and R2<2 and R3<2:
	print(round(R1, 1), '<Rkr=2')
	print(round(R2, 1), '<Rkr=2')
	print(round(R3, 1), '<Rkr=2')
	print('Дисперсія однорідна')
	print('-----------------------------------------------------------------------------')
	print('Нормовані коефіцієнти рівняння регресії: ','b0 =', round(b0, 1),' b1 =', round(b1, 1),' b2 =', round(b2, 1))
	print('b0-b1-b2 =', round(ynorm1, 1))
	print('b0+b1-b2 =', round(ynorm2, 1))
	print('b0-b1+b2 =', round(ynorm3, 1))
	print('Натуралізовані коефіцієнти рівняння регресії: ','a0 =', round(A0, 1),' a1 =', round(A1, 1),' a2 =', round(A2, 1))
	print('a0+a1*X1min+a2*X2min =', round(ynat1, 1))
	print('a0+a1*X1max+a2*X2min =', round(ynat2, 1))
	print('a0+a1*X1min+a2*X2max =', round(ynat3, 1))
else:
	print('Дисперсія не однорідна (')
	print('-----------------------------------------------------------------------------')