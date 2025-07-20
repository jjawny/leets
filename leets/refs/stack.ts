/*
    _________________________  _________  ____  __.
   /   _____/\__    ___/  _  \ \_   ___ \|    |/ _|
   \_____  \   |    | /  /_\  \/    \  \/|      <
   /        \  |    |/    |    \     \___|    |  \
  /_______  /  |____|\____|__  /\______  /____|__ \s
          \/                 \/        \/        \/
*/
{
  const stack: number[] = [];

  /* =========== OPS =========== */

  stack.push(); // O(1)
  stack.pop(); // O(1)
  stack[stack.length - 1]; // peek top O(1)
  stack.length === 0; // is empty O(1)

  // Traverse O(n)
  for (let i = 0; i < stack.length; i++) {
    console.log(stack[i]);
  }
}
