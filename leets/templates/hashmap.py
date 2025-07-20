hashmap = {}

hashmap[1] = 2  # O(1)
1 in hashmap  # O(1)
hashmap.get(1) # O(1)
del hashmap[1] # O(1), no value returned, and throws if not found
hashmap.pop(1, None) # O(1) returns the value, and safe
hashmap.clear() # O(1)
len(hashmap) # O(1)

# Traverse O(n)
for k, v in hashmap.items():
    print(f"({k}, {v})")
