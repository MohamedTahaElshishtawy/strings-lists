size = int(input("Enter the number of student's grades: "))
mark = []
validation =[]
for i in range(size):
    mark.insert(i, input())
    validation.insert(i,0)

for i in range(size):
    if int(mark[i]) < 0 or int(mark[i]) > 100:
        validation[i] = 0
    else:
        validation[i] = 1

print("the invalid grade list is: " + str(validation))