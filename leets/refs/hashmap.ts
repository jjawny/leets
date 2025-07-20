const hashmap = new Map<number, number>();

hashmap.set(1, 2); // O(1)
hashmap.has(1); // O(1)
hashmap.get(1); // O(1)
hashmap.delete(1); // O(1)
hashmap.clear(); // O(n) but on average O(1) in V8
hashmap.size; // O(1)

// Traverse O(n)
for (const [k, v] of hashmap) {
  console.log(`(${k},${v})`);
}
