sqaures = []

for i in range(6):
    sqaures.append(i*i)

print(sqaures)

sq = [i*i for i in range(6)]
print(sq)


nums = [-2,-3,3,4,-1,7]

#new_
nums = [0 if val<0 else val for val in nums]
print(new_nums)

