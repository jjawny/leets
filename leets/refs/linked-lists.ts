/*
  .____    .__        __              .___.____    .__          __   
  |    |   |__| ____ |  | __ ____   __| _/|    |   |__| _______/  |_ 
  |    |   |  |/    \|  |/ // __ \ / __ | |    |   |  |/  ___/\   __\
  |    |___|  |   |  \    <\  ___// /_/ | |    |___|  |\___ \  |  |  
  |_______ \__|___|  /__|_ \\___  >____ | |_______ \__/____  > |__|s
          \/       \/     \/    \/     \/         \/       \/        
*/
{
  type Node<T> = {
    value: T;
    next?: Node<T>
  }
  
  // Example
  const linkedList: Node<number> = {
    value: 1,
    next: {
      value: 2,
      next: {
        value 3,
        ...
      }
    }
  }
  
  // Traverse
  while (currNode) {
    console.log(node.value);
    currNode = currNode.next
  }
}
