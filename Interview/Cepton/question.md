## Programming Question

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



## CTO Interview
1. What's meaning of the Python range when you do a for loop?
2. What kind of member functions a iterator provide?
    * `__next__()`: This method returns the next item in the sequence. It raises a StopIteration exception when there are no more items to return.
    * `__iter__()`: This method returns the iterator object itself. It's often used in for loops and other constructs that expect iterables.
        ```python
        class MyIterator:
        def __init__(self, data):
            self.data = data
            self.index = 0
    
        def __iter__(self):
            return self
    
        def __next__(self):
            if self.index < len(self.data):
                value = self.data[self.index]
                self.index += 1
                return value
            else:
                raise StopIteration
        ```
3. How do I use linear regression?
    * It attempts to fit a straight line through the data points that minimizes the difference between the predicted values and the actual values.
    * The relationship between dependent variable $y$ and independent variables $x_1, x_2, ..., x_n$ is linear.
        $$y = \omega x + b+\epsilon$$
        The goal is to find the coefficients $\omega$, $\b$ that best fit the data.
        When we have more than one independent variable, it becomes multiple linear regression.
    * To find the best fitting line, we need to estimate the values of the coefficient that minimizes the prediction error(i.e. actual value and predicted value)
        $$error = \frac{1}{2n}\Sigma^{n}_{i=1}(\omega^{T}x^{(i)}+b-y^{(i)})^2$$
        Take derivative of the error and set it equal to 0
        $$\omega^*=(X^{T}X)^{-1}X^{T}\omega$$