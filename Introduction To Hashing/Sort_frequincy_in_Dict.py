num = [5, 2, 3, 5, 1, 2, 3, 4, 5]

freq_map = {}
for i in range(0 , len(num)):
    if num[i] in freq_map:
        freq_map[num[i]] += 1
         
    else:
        freq_map[num[i]] = 1

print(freq_map)
print(freq_map[5])

#time complexity of this is O(n) and space complexity is O(N) where k is the number of unique elements in the list



# secound method

num = [5, 2, 3, 5, 1, 2, 3, 4, 5]

freq_map = {}
for i in range(0, len(num)):
    freq_map[num[i]] = freq_map.get(num[i], 0) + 1

print(freq_map)
print(freq_map[5])










