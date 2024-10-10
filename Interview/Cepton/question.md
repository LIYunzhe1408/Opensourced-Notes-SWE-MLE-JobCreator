Cepton Programming Question:

We are looking for a program that manages “intensity” by segments. Segments are intervals from -infinity to infinity, we liked you to implement functions that updates intensity by an integer amount for a given range. All intensity starts with 0. Please implement these two functions:

add(from, to, amount)  
set(from, to, amount)
You should implement the functions based on your own interpretation of the problem and document any assumptions you make. 

Here is an example sequence (data stored as an array of start point and value for each segment.):
* Start: []
* Call: add(10, 30, 1) => [[10,1],[30,0]]
* Call: add(20, 40, 1) => [[10,1],[20,2],[30,1],[40,0]]
* Call: add(10, 40, -2) => [[10,-1],[20,0],[30,-1],[40,0]]
<br></br>
* Start: []
* Call: add(10, 30, 1) => [[10,1],[30,0]]
* Call: add(20, 40, 1) => [[10,1],[20,2],[30,1],[40,0]]
* Call: add(10, 40, -1) => [[20,1],[30,0]]
* Call: add(10, 40, -1) => [[10,-1],[20,0],[30,-1],[40,0]]