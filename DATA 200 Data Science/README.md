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


### Takeaway
We explore the components of `DataFrame` which  is a collections of `Series` that all share the same index. We also learnt some basic operations on `Series` to analyze the data.


## Lecture 3: Pandas II
Utility functions in pandas
* Extracting data using `.iloc`
* Usage of `[]`


### `loc` V.S. `iloc`
`loc` function for label-based extraction
* `elections.loc[1:10, ["Candidate", "Party"]]`: parameters are [row label, column label] or 
* `elections.loc[[1, 2], ["Candidate", "Party"]]` for specific labels
* The row argument can not be skipped, while the column argument can skip to indicate all columns

`iloc` function for integer-based extraction
* The integer means the position of the data in the `DataFrame`, counting from the 0. Basically it's equivalent to the index.
* The arguments to `.iloc` can be
  * A list: `elections.iloc[[1, 2, 3], [1, 2]]` grab the exact data.
  * A slice(**exclusive** of the right hand side of the slice): `elections.iloc[[1, 2, 3], 0:3]`
  * A single value. `elections.iloc[[1, 2, 3], 1]`

When to use?
* Safer and Readable: For `loc`, if data gets updated, rows shuffle, column shuffle, we do not want to rely on the position index.
* Grab the median number in a sorted array or data. e.g. movie earning.

### `[]` square bracket
`[]` is for context-dependent extraction
* Only takes one argument, which may be
  * A slice of row numbers `iloc` A range of values->integer
  * A list of of column labels `loc`. `elections[["Candidate", "Party"]]`
  * A single column label `loc`

Why use?
* Make the code shorter

Chaining
* `weird['b'][1]` will give a whole column first and then choose the item

### Conditional Selection
how to automatically select `names[[True, False, True, True, False]]`?
* Create a `Series` as a boolean series to filter the `DataFrame`
  * `logical_operator = (names["Sex"] == 'F')`
* `loc` can also work: `names.loc[names["Sex"] == 'F', :]`

How to combine different conditions
* `&` is `and`, `|` is `or`: `names[(names["Sex"] == 'F') | (names["Years"] < 2000)]`
* Bitwise operation & | ^(XOR exclusive or) ~(not)


Alternatives to direct boolean array selection
* `.isin`: `names[names["Name"].isin(chosen_names)]` chosen_name is a list that is provided.
* `.str.startwith`: `names[names["Name"].str.startwith("N")]`

### Other operations on column
Adding a column:
* Use `[]` to reference the desired new column
* assign this column to a `Series` of the appropriate length
```python
babyname_lengths = babynames["Name"].str.len()
babynames["name_lengths"] = babyname_lengths
```

You can also:
* Modify a column `babynames["name_lengths"] = babynames["name_lengths"]-1`
* Rename a column `.rename(columns={"Original": "New"})`
* Drop a column/row `.drop("Label", axis="columns")`


### Utility functions
* Average number: `np.mean(variable)`
* `.shape` and `.size` is the capacity
* `.describe()` provides the summary of the `DataFrame`. Also, `names["Sex"].describe()` is also callable on `Series`
* `.sample()` random selection of rows from the `DataFrame`, it can be chained with `iloc` [Question] what is replacement?
* `.value_counts()` counts the number of occurrences of each unique value in a `Series`
* `.unique()` returns a array of every unique value in a `Series`
* `Series.sort_values()` equals `DataFrame.sort_values(by=column_name)`


## Lecture 4: Pandas III
### Custom Sort
Remember the method `names.sort_values(by="column_name", ascending=False)`.
* Approach 2: Use the `key` argument. `lambda x: x.str.len()` where x is the input.
* Approach 3: Use the `map` function.

### Grouping
Group together rows that fall under the same category. e.g. group together all rows from the same year. Or, you may use it to perform an operation that aggregates across all rows in the category, like sum up the total number of babies born in that year.
* `groupby()` + `groupby().agg(sum)`
* `sum`, `mean`, `max`... can be called in `agg`. Or customized functions can be called.
* `max` will affect all columns, which lead to an entire row of the max for the specific group.
![alt text](image-1.png)
* `groupby('Year').count()` returns the number in a group. null value will not be counted.
* Filter. `groupby().filter(f)` where `f = lambda sf: sf["num"].sum() > 10` sf is the whole table that is grouped. Output structure will be the same as the one before `groupby()` unless the elements are not been filtered.

### Pivot table
Group two or more columns of interest.


### Joining Tables
`pd.merge(left=xxx, right=xxx, left_on=, right_on=)` or `DataFrame.merge(right=xxxx, left_on=column_name, right_on=column)`



## Lecture 5: Data Wrangling
EDA is unboxing data. Explanatory Data Analysis
* We often prefer rectangular data
  * Easy to manipulate and analyze
  * Tables and matrices are two kinds of rectangular data

Structure: How `.csv` or `.tsv` file works in python?
* `.csv` file expects the delimiter of comma rather than semi-comma, while `.tsv` file expects the delimiter to be the `tab`.
  * use `sep='\t'` in `pd.read_csv()` to indicate the separate delimiter is `tab`
  * Why `.csv` or `.tsv`
* `repr(string)` will make the string to be raw, when printing, you will know the exact content in the string.
* When reading the csv file using pandas `pd.read_csv()`, assign `header=1` to indicate the header is the second row.
* When merge, argument `left_on` and `right_on` are the columns that two dataframe going to match. If there are duplicate columns, suffixes `_x` and `_y` will be used to modify these columns. We can use `suffixes=('_case', '_population')` in the merge function to specify the suffix we want to have for duplicate columns
* JSON(JavaScript Object Notation) is another important, non-rectangular, and commonly used structure
  * A list of dictionaries. Basically they're nested dictionaries.
  * The type of the output of `json.load(f)` is `dict`, use `.keys()` to grab the top level keys.
  * Use panda to read json, `pd.read_json()`, then `pd.DataFrame()` to rectangularize a json data.

Granularity: How fine is each datum
* Fine grained: one row represents a person
* Coarse grained: Mixing groups all together.
* Rollup record = a summary of record
* `.drop(0)` to drop the first row.
* assign `thousand=','` when `pd.read_csv()` to tell the panda that every time seeing a comma, it's a sign of thousand format.

Variable types: Quantitative and Qualitative(categorical)
* Quantitative: numerical values. Price, temperature
* Qualitative: Ordinal-grade level, age group(ordered). Nominal-Cal ID number, phone brand(unordered)
* When storing time, we use the integer(seconds) that from the Jan 1 1970. Before that, it will be negative, after that, will be positive.


## Homework 2 notes
1. In general, we strongly suggest having your filenames hard coded as string literals only once in a notebook. It is very dangerous to hardcode things twice because if you change one but forget to change the other, you can end up with bugs that are very hard to find.
2. Often when working with zipped data, we'll never unzip the actual zip file. This saves space on our local computer. However, for this homework the files are small, so we're just going to unzip everything. This has the added benefit that you can look inside the CSV files using a text editor, which might be handy for understanding the structure of the files. The cell below will unzip the CSV files into a sub-directory called `data`.


## Lecture 6: Text Wrangling and Regex(Regular expression)
Potential issues in data:
* Duplicate rows, columns -> Identify and ignore/drop
* Labeling error -> apply corrections
* Missing data -> 
  * Keep as NaN: Good default, create a `Missing` category
  * **Bad Default** Dangerous to drop, but you can after thinking why it's missing
  * Imputation: Infer missing values: Mean/Median to replace NaN

For text, we want to:
* Canonicalization: covert data into a standard form.
  * Extract patterns in text and change them to fit our expectation
* Extract Information

Regex Basics:
* Concatenation: BAAB matches BAAB.  
* BAB | BAAB matches BAB or BAAB = | is or
* AB*A matches AA, ABA, ABBA = any numbers of B
* (AB)*A matches A, ABA, ABABA = () is a group
* .u.u.u. matches CUMULUS JUGULUM = .- look for any character other than \n
* [A-Za-z] matches A, a, B = define a character class
* AB+ matches AB, ABB, ABB + one or more
* AB? matches A, AB = ? zero or one
* AB{2} matches ABB = {x} repeat exactly x times
* AB{0, 2} matches AB, ABB, A = {x, y} repeat between x and y times
* ^abc matches abc 123 not 123 abc = matches beginning
* abc$ matches 123 abc not abc 123 = matches the end of a string (Start with power, end with money)
* 

More on Character Classes
* \w, \W(not): [A-Z] any uppercase letter between A and Z
* \d, \D(not): [0-9] any digit between 0 and 9
* \s, \S(not): [A-Za-z0-9] any letter any digit



## Lecture 7: Visualization
Goal of visualization
* High-level overview of complex dataset
* Help us understand data/result better
* Communicate results/conclusions to others

Distribution describes
* The **set of values** that a variable can possibly take.
* the **frequency** with which each value occurs
* ... for a single variable.
* The percentages should sum to 100%



Several visualization methods
* Bar plots
  * import matplotlib    
    * `import matplotlib.pyplot as plt`
  * Use seaborn
    * `import seaborn as sns`
    * `sns.countplot(data=wb, x="Continent")`
* Distribution of quantitative variables
* Side-by-side box and violin plots.
  * Quartiles
  * interesting: the whisker in a box plot is not exactly the maximum or minimum value. They indicate the expected upper or lower bound of the data points, the points outside of them are outliers.
* Histograms


## Lecture 8
Apply transformation can make it clear seeing the distribution of data.
* log
* power
* root

Encoded variable
* x
* y
* color
* area


Avoid Area charts! Length bar is better. Avoid jiggling the baseline. Line plot is much easier to understand.


## Lecture 9: Sampling
Sampling is to take information from the population and then get inference.

Errors(Variances)
* Random samples can vary from what is expected, in any direction. -> Increase size of random sample


Common Biases
* Selection biases: Literary Digest poll excluded people not in phone books.
* Response biases: very depend on how you question. -> improve questions
* Non-responsive biases: result varies between those who response and those not response

Probability Sample:
* If we know the probability that any subset of individuals in the sampling frame will be selected, our sample is a probability sample

Simple Random Sample:
* Without replacement
* Same chance for every possible group to be selected
  * Like (3, 13) is 1/10, while (3, 4) is 0 not 1/10

Stratified Random Sampling
* Split dataset into stratums.
* The strata is not overlapping with others.
* Then Simple random sample can be performed on each strata.
* Benefit: guarantee the proportional representation; reduced chance error.
* Limitation: add a layer of complexity; population proportions of group is not always known.

Post-stratification:
1. Divide your sample and population
2. Calculate the overall response in each sample cell
3. Aggregate over the sample cells, proportionally weighing each sample cell by the size of the corresponding cell.


## Lecture 10: Introduction to Modeling
Simple linear regression is introduced today.

What is a model:
* an idealized representation of a system: The fall of an object on Earth as subject to a constant acceleration due to gravity.
* a good estimation
* All models are wrong, but some are useful. None of models are perfect.

Why build a model
* To explain a complex system or a phenomena, have a simple and interpretable model.
* To make accurate predictions.
* To make casual inference about if one thing causes another thing.

What is the regression line
* The regression line is a unique straight line that minimize the mean squared error
* Residual value = observed y - regression estimate. $y_i-\hat{y_i}$
* ![](./questions.png)

What is the correlation
* the average of the product of x and y, both measured in standard units.
* Different from the covariance which not divided by $\sigma$ but equals $r\sigma{_x}\sigma{_y}$
* Measures the strength of a linear association between two variables. r=1 is perfect linear association r=-1 is negative association(it has correlation, but when x increases, y decreases).
* Increase x, can or cannot predict the value of y.
* One thing to mention, On a parabola, the correlation between x and y is considered "non-linear" because while there is a clear relationship between the variables, it is not a straight line, meaning a standard correlation coefficient (which measures linear relationships) would be close to zero, even though the data clearly shows a pattern; the relationship is quadratic, where y is proportional to x squared. 
* Rearrange the correlation, it can be a regression line equation.(slope + intercept)

The modeling process:
* Dataset is the observation. 
* x is independent variable, called the input, feature, or the attribute.
* y is dependent variable, called the output, outcome, or response
* Use x to predict y, the prediction is denoted as $\hat{y}$
* Parametric model: $\hat{y_i}=\theta{_0}+\theta{_1}x_i$
* We will pick the parameters that appears best according to some criterion we choose. So the performance of different $\theta$ to fit a model will be estimated to be evaluated.
* kNN classifier is not a parametric model.

When build a model:
1. Choose a model
2. Choose a loss function
   * Evaluate how bad the prediction is.
   * L2 and L1 loss.
   * Why averaging but not summing up? We want the value to be affected by the dataset size. We wanna normalize.
   * Empirical risk is the average loss of a model over a given training dataset, depending on $\theta$. It's the risk that we wanna minimize.
3. Fit the model. Choose the best parameters of the model given our data.
   * For linear, take derivatives to solve.
4. Evaluate the model

## Lecture 11: Constant Model
### Modeling process
Sum of squared error of simple linear regression
* Just residual, the sum of them might be cancelled out
* After square, we want to choose a line to make the total area of the boxes(squares) as small as possible.
* Measure quality of linear model fit relative to constant model. $R^{2} = \frac{\Delta{area}}{ConstantModelArea}$. In other word, it's the fraction of variance in y as MSE_constant model is same as $\sigma^2$

#### MSE
Choose a Model
  * The constant model is the one with only one parameter. $\hat{y}=\theta_{0}$
    * e.g. You sell boba drink in a week. You want to predict the sale in the next day. For SLR, you may have variables like the day in the week, the weather, etc. But for constant model, you always predict the same amount.
    * Ignoring these factors simplifies assumptions.
    * Still a parametric model, but just one parameter
    * Still determine the best $\theta_{0}$ that minimizes average loss

Choose a loss function
  * Mean Square Error: $\hat{R}(\theta)=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y_i})^2$

Fit the model(minimize the loss)
  * For constant model, $\hat{R}(\theta)=\frac{1}{n}\sum_{i=1}^{n}(y_i-\theta_{0})^2$
  * With calculus, the average loss is minimized by $\theta_0=mean(y)=\bar{y}$
    * Take first derivative
    * Set equal to 0, then can solve $\hat{\theta_0}$
  * Conclusion: The mean of the outcomes($y$) achieves the minimum MSE of the constant model.
    * How to interpret. The representation is the sample variance of the sample. $\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y_i})^2={\sigma^2_y}=R(\hat\theta_0)={R}(\bar{y})$. $\sigma$ is the standard deviation of the sample
    * The value of the loss function when we plug in the optimal value to minimize the loss function(The minimum of MSE): $R(\hat{\theta_0})=minR(\theta_0)=\sigma^2_y$
    * The argument that minimizes MSE: $\hat{\theta_0}=argminR(\theta_0)=\bar{y}$ 

#### MAE
Choose a loss function
  * Mean Absolute Error: $\hat{R}(\theta)=\frac{1}{n}\sum_{i=1}^{n}(|y_i-\hat{y_i}|)$

Fit the model(minimize the loss)
  * For constant model, $\hat{R}(\theta)=\frac{1}{n}\sum_{i=1}^{n}(|y_i-\theta_0|)$
  * Derived from the example, the minimum value is not the mean.
  * With calculus, the number greater than $\hat{\theta_0}$ should be equal to the number smaller than $\hat{\theta_0}$. Then it is the median comes from.
  * $\hat{\theta_0}=median(y)$

#### Summary
1. Define the objective function as average loss
  * plug in L1 or L2 loss
2. Find the minimum of the objective function
  * Differentiate with respect to $\theta$
  * Set equal to 0
  * Solve for $\hat{\theta}$


Evaluate the model performance
* rug plot and scatter plot
* Finding minimizing values: MSE is smooth, while MAE is piecewise where at each kinks, it's not differentiable, hard to minimize.
* Uniqueness: Add one more data point, then MSE still has a unique $\hat{\theta_0}$ while MAE has infinitely many $\hat{\theta_0}$ when the number of data points is even.
* Sensitivity to outliers: MSE is sensitivity to outliers but MAE is more robust.

### Transformation for linear models
* See each axis
  * If values appear compressed, magnify differences with **Square transform**
  * If large values appear unconstrained, squish difference with **log transform**
* After prediction, we need to transform it back by a inverse function
  * e.g. $\hat{\log(Age)}=\theta_0+\theta_1Length$ -> $\hat{Age}=\exp^{\theta_0+\theta_1Length}$
![alt text](image-2.png)
* The reason why we use it is to deal with the initial feature points are not linear, instead of changing a non-linear model, we transform data