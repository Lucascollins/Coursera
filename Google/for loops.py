def square(n):
    return n*n

def sum_sqaures(x):
    sum = 0
    for n in range(x):
        sum+= square(n) 
    return sum

# print(sum_sqaures(10))

# friends = ["Lucas","Luana","Ravenna","Daniel"]
# for friend in friends:
    # print("HI " + friend)
values = [2 , 2 ,2, 2,2]
sum = 0
length = 0 
for value in values:
	sum += value
	length += 1
print("Total sum : " + str(sum) + " - Average : " + str(sum/length))