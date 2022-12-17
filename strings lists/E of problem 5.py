size = int(input("Enter the number of student's grades: "))
mark = []
cnt = 0
for i in range(size):
    mark.insert(i, input())

for i in range(size):
    if int(mark[i]) > 0 and int(mark[i]) < 100:
        if int(mark[i]) > 85: # we don't have to calculate the 85% of the grades in this problem
            print("This grade is grater than 85% is: " + str(mark[i]))
            cnt+=1
print("The number of grades that's greater than 85% is: " + str(cnt))




