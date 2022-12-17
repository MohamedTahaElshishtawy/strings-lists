size = int(input("Enter the number of student's grades: "))
mark = []
min = 100
max = 0

for i in range(size):
    mark.insert(i, input())


for i in range(size):
    if int(mark[i]) > 0 and int(mark[i]) < 100:
        if(int(mark[i]) < min):
            min = int(mark[i])
            mn = i
        if(int(mark[i]) > max):
            max = int(mark[i])
            mx = i


print("The highest grade is: " + str(max) + " and it's index is: " + str(mx))
print("The lowest grade is: "  + str(min) + " and it's index is: " + str(mn))
