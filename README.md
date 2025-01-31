<head></head>
Find All Duplicates

Write a function (or static method in the case of Java) that accepts a list of integers and returns a list of only those integers that appear more than once.

If we are just returning true or false based off there being duplicate numbers then we can use many methods.

The nested loop method uses an outer for loop which starts at index 0(i) and an inner for loop that starts at i+1(j). Then then j increments each loop by 1 until it reaches the last index of the list. For each loop of the inner loop we compare if list[i]==list[j]. If this condition is ever met we return true and the program ends. Else it returns false. This has an O(n^2) time complexity which is not ideal, however it is very easy to convert this method to be able to return a list of the duplicate numbers by adding them to a new list instead of returning true if the 'if' condition is met.

Another solution is to use the list given as a argument and make a hashset out of it. Since hashsets don't allow duplicates, we then simply compare the length of the given list vs the hashset and if they're different, we return true. This method is far more effecient, I think O(n) since it has to iterate through the whole list to add the contents to the hashset? However this method is not easily convertable to return a list of the duplicate numbers.
