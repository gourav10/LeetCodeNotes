# Longest Substring with atleast k repeating characters


1. Create a Hashmap to keep the frequency of each character in str.
2. Filter out the characters which have frequencey less than k.
3. Split the string into mulitple substrings at the characters with less frequency.
4. Calculate the max length of each substring, repeat step 2 to calculate the max length of substring.
5. At the end find the max amongst all the substrings. 

Ex: str = "ababbc", k=2
Frquency of characters in string:
a = 2,b=3,c=1
So split str at 'c',
substr = 'ababb'

count the frequency of each character a=2,b=3. As both have frequency >= k, So add the frequency and return the value.