## Lecture 1
### Logistics
1. slido.com and the number is 3625952

### Intuition from case study of audited tax
Tax audited? how IRS know the race of taxpayers? How do we know who was audited? -> Data from IRS
* Race not reported anywhere in tax return.
* The prevalence of hometowns first names, last names differs across race and ethnicity. Visualize the factor as x axis and audited rate as y axis.
    * Race from hometown: NYC and SF. SF indicates higher probability that residents are identified as asian.
    * First name and last name: probability of particular name that is identified as black, asian, etc.
    * Income: single variable does not fully explain the gap in lower income data.
* The root cause is the algo prioritize the tax credit error over income underreporting error. -> Choosing a right metric to solve the problem.

Data science is to understand the world(Science) and solve problems(engineering)


### Data Science Lifecycle
We have two entry points: asking a question or obtaining data
![alt text](image.png)

Example about students' enrollment profile.
1. Start with a question: Some questions for majors, year, etc
2. Data Acquisition and Cleaning: `majors = pd.read_csv("data/major.csv")`
3. Explanatory of data analysis: Peeking the data by `majors.head(20)` and `names.head(20)`



## Lecture 2: Pandas I
### Tabular data
It's data in table.
* Row: one observation
* Column: features of the observation

Industrial data tool: pandas(panel data)
* Arrange data, extract info by filters, gain insights, add `numpy` function.

### Series
The table is called a `DataFrame`. We think as a collection of named columns, called `Series`. e.g. A `Series` named "candidate", "price", "location", etc.

A `Series` is a 1-dimensional array-like object.
* A sequence of values of the same type. Accessed by calling `s.values`
* A sequence of data labels, called the index. Accessed by calling `s.index`
  * Custom index: Provide index labels for items in a Series by passing an index list. `s = pd.Series([-1,10,2], index=["a","b""c"])`
* `s = pd.Series(["welcome, "to", "Data 100"])`

Selection in `Series`
* A single label. 
* A list of labels. `s[["a","c"]]`
* A filtering condition: we want to select values in the `Series` that satisfy a particular condition.
  * e.g. select all elements that are even. `even = (s%2 == 0)` The output will be a boolean type `Series` object.
  * Apply a boolean condition to the Series
  * Index into our Series using the boolean condition. `pandas` will select only the entries in the Series that satisfy that condition.

### DataFrame
We think of a `DataFrame` as a collection of `Series` that all share the same index.

Creating a `DataFrame`
* The syntax is `pandas.DataFrame(data, index, columns)`
* We can create it from:
    * CSV file. `elections = pd.read_csv("data/elections.csv")`
      * Use exact column as index: `elections = pd.read_csv("data/elections.csv, index_col="Year")`
    * using a list and column names
      * `pd.DataFrame([1,2,3], columns=["Numbers"])`
      * Passing by rows. `pd.DataFrame([[1, "one"], [2, "two"]], columns=["Numbers", "Description"])`
    * a dictionary
      * `pd.DataFrame({"Fruit": ["strawberry", "Orange"], "Price": [5.49, 3.99]})`
    * a Series
      * `s_a = pd.Series(["a1", "a2"], index = ["r1", "r2"])`
      * `s_b = pd.Series(["b1", "b2"], index = ["r1", "r2"])`
      * `pd.DataFrame({"A-column": s_a}, {"B-column": s_b})`
      * Turn a Series to a DataFrame. `pd.DataFrame(s_a)`

### Index
The index, not necessarily number, can also be:
* non-numeric
* having a name

The index is not necessarily unique.

Modify index:
* Make sure creating a copy of the DataFrame or rewrite to correctly reflect the operation. `elections = elections.set_index("Candidate")` or `elections.set_index("Candidate", inplace=True)`
* Use `elections.set_index(inplace=True)` to keep "Candidate" as one of the column

`columns`, `index`, and `shape` can be retrieved by calling `election.xxx`


### Relationship
We think of a `DataFrame` as a collection of `Series` that all share the same index.