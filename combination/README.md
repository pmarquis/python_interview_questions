Problem (level: 3/5 and can be 4/5)
-------
Write a function which take a word as parameter, create an alphabet with the letters and return all the combination 
of word.
The expected output is an infinite stream of all possible combinations.

Example
-------
f("abc")
should return "a" ,"b" ,"c" ,"aa" ,"ab" ,"ac" ,"ba" ,"bb" ,"bc" ,"ca" ,"cb" ,"cc", "aaa", etc...

More
----
* You can ask to do it both way, using a recursive function or a generator.
* You can ask to do it for a single letter, using map and a lambda: "a" return ["a", "aa", "aaa", ...]

