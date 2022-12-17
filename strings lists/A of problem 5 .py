size = int(input("Enter the number of student's grades: "))
mark = []
invalid_cnt = 0
for i in range(size):
    mark.insert(i, input())

for i in range(size):
    if int(mark[i]) < 0 or int(mark[i]) > 100:
        print("It's invalid grade")
        invalid_cnt+=1
    else:
        print("It's a valid grade")
print("the number of invalid grades is " + str(invalid_cnt))
