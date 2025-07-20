/*
  ________   ____ __________________ ______________
  \_____  \ |    |   \_   _____/    |   \_   _____/
   /  / \  \|    |   /|    __)_|    |   /|    __)_
  /   \_/.  \    |  / |        \    |  / |        \
  \_____\ \_/______/ /_______  /______/ /_______  /s
         \__>                \/                 \/
*/
{
  let front = 0;
  const queue: number[] = [];

  /* =========== OPS =========== */

  queue.push(); // enqueue O(1)
  queue.shift(); // dequeue O(n)
  const dequeue = () => queue[front++]; // dequeue O(1)
  queue[front]; // or queue[0] if shifting, peek front O(1)
  queue.length === front; // or === 0 if shifting, isEmpty O(1)

  // Traverse O(n)
  for (let i = front; i < queue.length; i++) {
    console.log(queue[i]);
  }
}
