/*
  __________        .__             .__  __          ________                               
  \______   \_______|__| ___________|__|/  |_ ___.__.\_____  \  __ __   ____  __ __   ____  
   |     ___/\_  __ \  |/  _ \_  __ \  \   __<   |  | /  / \  \|  |  \_/ __ \|  |  \_/ __ \ 
   |    |     |  | \/  (  <_> )  | \/  ||  |  \___  |/   \_/.  \  |  /\  ___/|  |  /\  ___/ 
   |____|     |__|  |__|\____/|__|  |__||__|  / ____|\_____\ \_/____/  \___  >____/  \___  >s
                                              \/            \__>           \/            \/ 
*/
{
  // Can also implement using a heap-style for O(log n) enqueue and dequeue
  class PriorityQueue<T> {
    private items: T[] = [];
    enqueue(item: T): void {
      this.items.push(item);
      this.items.sort((a, b) => a - b); // Replace with comparator for complex types
    }
    dequeue(): T | undefined {
      return this.items.shift();
    }
  }
}
