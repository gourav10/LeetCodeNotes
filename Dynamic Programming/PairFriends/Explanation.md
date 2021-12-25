## Problem: <br>
### Given n friends, each one can remain single or can be paired up with some other friend. Each friend can be paired only once. Find out the total number of ways in which friends can remain single or can be paired up. 

### Difficulty: Medium<br>

**Approach** <br>
This is a combinatrics problem in which we need to find the total possible ways we can form pairs.
There are mainly two ways:
1. Form no pair
2. Form pairs with remaining numbers
<br>
The Recurrence Relation:<br>
C[n] = C[n-1]+(n-1)C[n-2]

