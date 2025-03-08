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

#### Forms of error
* Chance Error: Exists when the sample is only a subset of the population, which is true here.
* Non-response Bias: Exists because individuals may be unresponsive to our phone call.
* Selection Bias: Exists because our sampling strategy is flawed – we are sampling individuals outside of our intended population.

### Pandas
1. Get the mean of the `Height` column. `pandas_df["Height"].mean()`
2. Check if the element in a column of a dataframe is in the given list. `pandas_df["Favorite Food"].isin(SELECT_FOODS)`
3. Distinguish the difference between `agg` and `filter`. When we want to `only keep` rows or `remove` rows, use `filter` which is processing `x` in `lambda x` as DataFrame.


### Regex
1. How to match multiple same pattern
![alt text](image.png)


### Modeling
1. If there's always a unique solution to the optimal parameters $\hat{\theta}$ that minimize MSE?
   * No. See if columns of the design matrix of the model is linearly independent. If so, $X^TX$ is invertible, and the optimal solution exists. Otherwise, not exist.