size = int(input("Enter the number of student's grades: "))
mark = []
total = 0
cnt = 0
for i in range(size):
    mark.insert(i, input())

for i in range(size):
    if int(mark[i]) > 0 and int(mark[i]) < 100:
        total = total + int(mark[i])
avg = total/size
for i in range(size):
    if int(mark[i]) > 0 and int(mark[i]) < 100:
        if int(mark[i]) > avg:
            print("This grade is greater than their average: " + str(mark[i]))
            cnt+=1
print("The number of grades that's greater than their average is: " + str(cnt))
