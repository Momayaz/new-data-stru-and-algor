# Implement a Queue using two Stacks.

## Challenge

Create a brand new PseudoQueue class. This PseudoQueue class will implement our standard queue interface (enqueue(value), dequeue()), but will internally only utilize 2 Stack objects.

### Example Input ---> Output:

**enqueue(value)**
Input: </br>
[10]->[15]->[20] </br>
Arg: </br>
5 </br>
Output: </br>
[5]->[10]->[15]->[20] </br>

Input: </br>
Empty </br>
Arg: </br>
5 </br>
Output: </br>
[5]->[ </br>

**dequeue()** </br>
Input: </br>
[5]->[10]->[15]->[20] </br>

Output: </br>
20 </br>

Internal State: </br>
[5]->[10]->[15]) </br>

## Approach & Efficiency

- **init**(self, stack1) - initialization of the PseudoQueue class with the 1 given Stack and 1 empty Stack
- enqueue(value) - Method to inserts value into the PseudoQueue, using a first-in, first-out approach.
- dequeue() - Method to extract a value from the PseudoQueue, using a first-in, first-out approach. Returns value of extracted node

## Solution

![Whiteboard Solution](../../../assets/queue-with-stacks.jpg)
