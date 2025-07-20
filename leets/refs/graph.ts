/*
    __________________    _____ __________  ___ ___  
   /  _____/\______   \  /  _  \\______   \/   |   \ 
  /   \  ___ |       _/ /  /_\  \|     ___/    ~    \
  \    \_\  \|    |   \/    |    \    |   \    Y    /
   \______  /|____|_  /\____|__  /____|    \___|_  /s 
          \/        \/         \/                \/  
*/
{
  // Example for [a: [b,c], b: [c]]
  //    a
  //   / \
  //  v   v
  //  c <- b
  const graph = new Map<string, string[]>();

  /* =========== OPS =========== */

  graph.set("a", ["b", "c"]); // ~O(1) depending on collisions
  graph.get("a"); // O(1)
  graph.has("a"); // O(1)
  graph.delete("a"); // O(1) and don't forget to delete all edges!
}
