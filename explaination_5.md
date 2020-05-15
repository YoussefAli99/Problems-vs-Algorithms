I implemented a Trie, which is a tree like structure that stores a dynamic set of strings. Here first I have made a class for TrieNode which has insert and suffixes methods. Trie class is made with the insert word and find methods.<br>
<br>
Talking about the complexity of this data structure:<br>
<br>
TrieNode:
<br><br>
Insert a character: Time complexity - O(1) Space complexity - O(1)
<br><br>
suffixes of a node: Time complexity: O(m^n) Space complexity: O(m^n) where m is maximum number of elements one level can have & n is the number of levels.
<br><br>
Trie:<br>
<br>
Insert a word: Time complexity: O(n) Space complexity: O(n)
<br><br>
Find a prefix: Time complexity: O(n) Space complexity: O(1)<br>