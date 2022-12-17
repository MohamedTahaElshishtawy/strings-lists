size = int(input("Enter the number of student's grades: "))
mark = []
tot = 0
for i in range(size):
    mark.insert(i, input())

for i in range(size):
    if int(mark[i]) > 0 and int(mark[i]) < 100:
        tot = tot+int(mark[i])
avg = tot/5
print("the average of the valid grade is: " + str(avg))