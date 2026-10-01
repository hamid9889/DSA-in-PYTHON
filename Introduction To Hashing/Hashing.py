# brout force solution 

n = [1,3,4,6,2,5,6,5,2,1,5,6]
m = [3,4,6,2,5,6,5]

for num in m :
    count = 0
    for x in n:
        if x == num :
            count +=1
            
print(count)            

# optimal solution

n = [1,3,4,6,2,5,6,5,2,1]
m = [3,4,6,2,5,6,5]

hash_list = [0] *10
for num in n:
    hash_list[num ]+=1

print(" start of the hash list")   
for num in m:
        if num<1 or num>10:
            print(0)
        else:
            print(f"the num {num} freq {hash_list[num]}")    

#time complexity of this is O(n) and space complexity is O(N) where k is the number of unique elements in the list


# with using dictionary
n = [1,3,4,6,2,5,6,5,2,1]
m = [3,4,6,2,5,6,5]
hash_dict = {}

for num in n:
    if num in hash_dict:
        hash_dict[num] +=1
    else:
        hash_dict[num] = 1


for num in m:
    if num in hash_dict:
        print(f"the num {num} freq {hash_dict[num]}")
    else:
        print(0) 
        



        


































