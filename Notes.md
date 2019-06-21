DFS
```Create an empty set to store visited nodes
    # Create an empty Queue and enqueue the starting vertex
    # While the queue is not empty...
      # Dequeue the first vertex
      # If that vertex has not been visited...
        # Mark it as visited
        # Then add all of its neighbors to the back of the queue
```

BFS
```Create an empty set to store visited nodes
    # Create an empty Queue and enqueue A PATH TO the starting vertex
    # While the queue is not empty...
      # Dequeue the first PATH
      # GRAB THE VERTEX FROM THE END OF THE PATH
      # IF VERTEX = TARGET, RETURN PATH
      # If that vertex has not been visited...
          # Mark it as visited
          # Then add A PATH TO all of its neighbors to the back of the queue
              # Copy the path
              # Append neighbor to the back of the copy
              # Enqueue copy
```