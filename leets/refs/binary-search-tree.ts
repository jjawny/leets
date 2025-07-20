/*
  __________  ____________________
  \______   \/   _____/\__    ___/
   |    |  _/\_____  \   |    |   
   |    |   \/        \  |    |   
   |______  /_______  /  |____|   
          \/        \/            
*/
{
  type Node<T> = {
    value: T;
    left?: Node<T>;
    right?: Node<T>;
  };

  // Example
  const binarySearchTree: Node<number> = {
    value: 1,
    left: { value: 2 },
    right: {
      value: 3,
      right: {
        value: 4,
      },
    },
  };

  // DFS
  function traverseDFS<T>(node: Node<T> | undefined): void {
    if (!node) return;

    traverseDFS(node.left);

    console.log(node.value);

    traverseDFS(node.right);
  }

  // BFS
  function traverseBFS<T>(root: Node<T>): void {
    if (!root) return;

    let front = 0;
    const queue: Node<T>[] = [root];

    while (front < queue.length) {
      const node = queue[front];
      if (!node) break;

      console.log(node.value);

      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
      front++;
    }
  }
}
