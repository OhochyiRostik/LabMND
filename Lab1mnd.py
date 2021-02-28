import random

listX = []
listX1 = []
listX2 = []
listX3 = []
for i in range(8):
	listX.append([random.randint(0, 20) for i in range(3)])
	listX1.append(listX[i][0])
	listX2.append(listX[i][1])
	listX3.append(listX[i][2])
print("Матриця Х: ")
for i in listX:
	print(*i, sep='      ')


# listA = [1, 2, 3, 4]

# listA = []
# for i in range(4):
# 	listA.append(random.randint(0, 10))

listA = [int(i) for i in input('Введіть значення 4 ашок через пробіл: ').split()]



listY = []
for i in range(8):
	listY.append(listA[0]+(listA[1]*listX1[i])+(listA[2]*listX2[i])+(listA[3]*listX3[i]))
serY = sum(listY)/len(listY)



listx0 = []
listx0.append((max(listX1)+min(listX1))/2)
listx0.append((max(listX2)+min(listX2))/2)
listx0.append((max(listX3)+min(listX3))/2)


listdx = []
listdx.append(max(listX1)-listx0[0])
listdx.append(max(listX2)-listx0[1])
listdx.append(max(listX3)-listx0[2])


listXN = []
for i in range(8):
	listXN.append([round((listX[i][j]-listx0[j])/listdx[j], 1) for j in range(3)])


lst = []
for i in listY:
	if serY-i>=0:
		lst.append(i)
y = max(lst)
xy = listX[listY.index(y)]


# print("Матриця Х: ")
# for i in listX:
# 	print(*i, sep='      ')
# print()
# print(listX1)
# print(listX2)
# print(listX3)

print("Ашки: ", listA)
print("Ігрики: ", listY)
print("Середнє ігрик:",serY)
print("Х0: ",listx0)
print("dx: ",listdx)
print()

print("Матриця нормованих Х: ")
for i in listXN:
	print(*i, sep='   ')
print()

print("Необхідний У:", y)
print("Необхідна група Х:", xy)
