#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  Linear O(n), As the size of the input increases, the runtime or space used will grow at the same rate.


b)  O(n log n) - there is one for loop that will run through the range of n and w while loop that will run through half of n. 


c) O(n) - This function will run n times to sum the number of bunny ears for n bunnies. 

## Exercise II
I would probably start by defining a middle variable, finding the middle of the list of floors. Drop the egg, if it doesn't break then we can remove every floor below that, and continue the test on every floor above. Find the middle, drop, repeat. Until we come to our answer. AKA Binary Search, I believe this is O(Log n) Logarithmic as it would divide n in half and then the floors in half. 
