/*
    _______________________________
   /   _____/\_   _____/\__    ___/
   \_____  \  |    __)_   |    |
   /        \ |        \  |    |
  /_______  //_______  /  |____|s
          \/         \/
*/
{
  const set = new Set<number>();

  /* =========== OPS =========== */

  set.add(1); // O(1)
  set.has(1); // O(1)
  set.delete(1); // O(1)
  set.clear(); // O(n)
  set.size; // O(1)

  // Traverse O(n)
  for (const item of set) {
    console.log(item);
  }
}
