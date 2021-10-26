## N-th Tribonacci Number
### 1137. N-th Tribonacci Number
<h5>Level: Easy</h5>
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

**Approach** <br>
I have used bottom up computation of dynamic programming. Calculations would be done from left to right. 
Assuming objective function is:
C[_i_] = C[_i_]+C[_i-1_]+C[_i-2_] 

Example:
**Input**: n = 4
**Output**: 4
**Explanation**:
index C[_i_] represents the Tribonacci  Number at position i.
C[0]=0, C[1]=1, C[2]=1
C[3] = C[0] +C[1]+C[2] = 0+1+1 =2
C[4] = C[1]+C[2]+C[3] = 1+1+2 = 4