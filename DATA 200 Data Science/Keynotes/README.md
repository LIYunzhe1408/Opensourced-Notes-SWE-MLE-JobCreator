## Mid-term
### Sampling
![alt text](Sampling-1.png)
* Sampling Frame: The set of people that could **possibly** end up in the sample

#### Type of Sampling
![alt text](Sampling-2.png)

In a **probability sample**, we provide the chance that any specified set of individuals will be in the sample (individuals in the population can have different chances of being selected; they don’t all have to be uniform), and we sample at random based off this known chance. For this reason, probability samples are also called random samples
* Probability Sampling: We can find the specific chance that any set of individuals will be
in the sample. The probability of every 100th individual being in the sample is 1; for all
others, it’s 0.

A uniform random sample with replacement is a sample drawn uniformly at random with replacement.
* Some individuals in the population might get picked more than once.
> Random Sample without Replacement: This is not a random sample, as not every individual has the same probability of being chosen.
> Random Sample with Replacement: This is not a random sample, as not every individual has the same probability of being chosen. Additionally, this is not being conducted with replacement.

A simple random sample (SRS) is a sample drawn uniformly at random without replacement.
* Every individual (and subset of individuals) has the same chance of being selected from the sampling frame.
* Every pair has the same chance as every other pair.
* Every triple has the same chance as every other triple.
And so on.
* **Non-responsive bias -> $p$(disagree to participate) $\neq$ $p$(agree to participate)**

A stratified random sample, where random sampling is performed on strata (specific groups), and the groups together compose a sample.

#### Forms of error and bias
* Chance Error: Random sampling
* Non-response Bias: Exists because individuals may be unresponsive to our phone call.
* Selection Bias: systematically excludes (or favors) particular groups
* Response bias: occurs because people don’t always respond truthfully. Survey designers pay special detail to the nature and wording of questions to avoid this type of bias. for survey, those with strong feelings (positive or negative) are often more likely to respond.

### Pandas
1. Get the mean of the `Height` column. `pandas_df["Height"].mean()`
2. Check if the element in a column of a dataframe is in the given list. `pandas_df["Favorite Food"].isin(SELECT_FOODS)`
3. Distinguish the difference between `agg` and `filter`. When we want to `only keep` rows or `remove` rows, use `filter` which is processing `x` in `lambda x` as DataFrame.
4. The number of rows in the subframe after grouping is `len(sf)` or `sf.shape[0]`
5. `sort_values(ascending=True)` while `value_counts(ascending=False)`
6. `df.groupby("column").agg('sum')` is adding up number for each cell not counting!!! For counting, pick one column and `agg('count')`


### Regex
1. How to match multiple same pattern
![alt text](image.png)
2. This problem tests the concept of capturing groups. To answer this question, we need to recognize that if capturing groups are present in the pattern, re.findall will return only the characters contained in the capturing group. Otherwise, it will return all matched characters.
![alt text](image-3.png)

### Visualization
* For distribution
  * Histogram – a classic way to see the overall shape (bins of wait times).
  * Kernel Density Estimate (KDE) plot – a smooth estimate of the distribution.
  * Box plot – shows quartiles, median, and potential outliers.
  * Violin plot – similar to box plot but shows a KDE shape on each side.
* For categorical data
  * Bar chart – generally for categorical data (counts per category).
  * Count plot – also for categorical data, showing how many observations per category.
* `sns.histplot(data=dataframe, x="Wait Time", rug=True, kde=True, stat="density")` where rug is small sticks on the graph
* KDE
  * The sum of the area in KDE curve is 1. **Pay attention to the value on x-axis**
  * Boxcar Kernel is a piecewise constant function with vertical jumps (no sloped or curved segments).
  * Gaussian Kernel: A larger bandwidth makes each bump wider and thus produces a smoother, more gently varying curve (fewer lumps). A smaller bandwidth makes each bump narrower, often revealing **more** local peaks.
* For side-by-side box:
  * Median: the line split the box
  * Interquartile range: the edges of the box marking the first (Q1) and third quartiles (Q3). 
  * whiskers: The lines extending from the box, called whiskers, show the range of the data, typically extending to the minimum and maximum values that are not outliers. 



### Data Transformation
We expect the **residual** plot of a good-performing **linear model** to display **no clear trends**. However, there is a clear pattern present in the residual plot (the scatter points are in a roughly parabolic shape)
![alt text](image-2.png)

### Modeling
1. If there's always a unique solution to the optimal parameters $\hat{\theta}$ that minimize MSE?
   * No. See if columns of the design matrix of the model is linearly independent. If so, **$X^TX$** is invertible(**Not $X$ itself**), and the optimal solution exists. Otherwise, not exist.
   * Linearly dependent -> not full rank -> not invertible -> no unique optimal
2. Why is the critical point found in Part (c) guaranteed to be a minimum and not a maximum?
   * The critical point of a convex function is always a minimum. Because MSE is a convex function, the critical point occurring at the value of $\theta$ calculated in Part (c) is guaranteed to be a minimum.
3. The design matrix contains a column of bias!!! So the number of features + 1
4. The residual vector is a $n\times{1}$ vector where $n$ is the number of samples, representing the the errors in prediction per sample.
5. The sum of the residuals $\sum_{i=1}^n{e_i}$ in Ordinary Least Squares regression is not necessarily when there's no intercept(all ones column)
6. $H=X(X^TX)^{-1}X^T$, then $HH=X(X^TX)^{-1}X^TX(X^TX)^{-1}X^T=X(X^TX)^{-1}$ $(X^TX)$ $(X^TX)^{-1}X^T=X(X^TX)^{-1}X^T=H$
7. C is ruled out, because the first, third, and fourth columns are not linearly independent in this case.
![alt text](image-1.png) 