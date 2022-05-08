Referential array
---
- an array with contents that are object references instead of various values of varying sizes
- each element would use the same size elements and is fixed, constant time access
- lists and tuples are referential structures
- reference object is immutable
  - when slicing a lists, the new elements reference the same elements as the original, but will be stored in a new instance of a list
  - new list in normal manner is a shallow copy, that keeps the same references as the original lists
  - to create a deep copy, you will need to use the deepcopy function from the copy module
  - reference object is immutable
  - when reassignment occurs, it creates a value and references that, it does not change original value
  - array.extend, adds references of the original list to the extended list, does not copy elements

Dynamic array
---
- when you build a list, you don't have to specify how large it is, you can constantly add to it
- a list will normally have a greater capacity than the current length
- if you keep adding/appending elements, the space will eventually fill up
- if you add elements, size gets allocated in chunks
- how to expand space for a new array
  - create new array B, store elements of A into B, reassignment of B to A 
- rule of thumb when creating new sized arrays is to double the size of the current array

Amortization
---

How to solve problems
---
- whiteboard/write it out first
- brute force it
- look at the solution and code it out