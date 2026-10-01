
# another question

s = "asdfghjkggaakl"
q = ["s", "f", "g", "k", "k", "a"]

hash_list = [0] * 27

for ch in s:
    ascii_val = ord(ch)
    index = ascii_val - 97
    hash_list[index] += 1
    
for ch in q:
    if ch in q:
        ascii_val = ord(ch)
        index = ascii_val - 97
        
        print(f"the char {ch} freq {hash_list[index]}")
    else:
        print(0)
        
#time complexity of this is O(n+m) and space complexity is O(26) where k is the number of unique elements in the list        