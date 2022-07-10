# Day 10 & 11

Added to Github?: No
Completion date: 09/07/2022
Language: Theory

# Today’s Focus

- Continue the Data Analyst Career Pathway syllabus

# Notes

- Returned to the start of the syllabus
    - [x]  The first section is Why Data science
    - [ ]  Principles of Data literacy
    - [ ]  SQL

---

## Welcome to data science

### Exploring data with SQL

- SQL (pronounced Sequel) stands for Structured Query Language
- SQL allows us to write queries which define a subset of data from a database
- A database is a set of data stored on a computer and is typically structured into tables

For this part I am using the codeacademy compiler. 

The following code does the following:

1. Select all columns (*)
2. From the ‘browse’ database
3. Limits the displayed output to 10 records

```sql
SELECT *
FROM browse
LIMIT 10;
```

When running the commands the following is returned:

![Untitled](Day%2010%20&%2011%208ed481e2be3e4f40b142ecfd5ae4c998/Untitled.png)

The next example showed a rather complex query which captured data of users from a particular month and calculated the churn rate.

---

This section then goes on to briefly introduce a lot of things covering the bread and butter of analytics:

- Explore data (SQL)
- Analyse data (Pandas)
- Visualise data (Matplotlib and Seaborn)
- Probability/Experiments
- Distributions
- Tableau

---

## Principles of Data Literacy

This module contains several sections:

- Introducing Data
- Thinking about data
- Visualising Data
- Analysing Data

At its core data literacy is all about how well we read, interpret and communicate with data.

One key thing to remember with data is the addage Garbage in, garbage out. By this we mean our data driven conclusions are only as strong, robust and well-supported as the data behind them.

As such one of the most important aspects of understanding data is asking the right questions so we end up with useful relevant data.

Questions to keep on your mind when looking at data:

<aside>
💡 Do we have sufficient data to answer the question at hand?

</aside>

<aside>
💡 Can my data answer my exact question?

</aside>

![Untitled](Day%2010%20&%2011%208ed481e2be3e4f40b142ecfd5ae4c998/Untitled%201.png)

### Addressing Bias

If our data is gathered with a bias then it can effect the conclusions we make from it.

Part of good data literacy and uncovering bias means asking the following questions:

<aside>
💡 Who participated in the data?

</aside>

<aside>
💡 Who is left out of the data?

</aside>

<aside>
💡 Who made the data?

</aside>

Statistics can also help us reveal bias.

In an example about discriminatory hiring practices a lawyer named Elaine Shoben showed that hiring practices  by asking the following questions:

1. Could the hiring results have happened by random chance or are they statistically impossible?
2. If the hiring results haven’t happened by chance they must have been as a results of ‘purposeful’ exclusion.
3. If the employer is aware of this ‘purposeful exclusion’ then they show ‘reckless disregard’ for the rights of individual candidates not to be discriminated against.
4. The burden of proof shifts to the employer to prove why hiring requirements are valid and neccessary and not exclusionary.

### Visualisations

Visualisation allows us to explore and understand data-driven arguments and are a powerful tool for communication

In 1986 NASA contracted engineers used a data visualisation to make the argument that the challenger space shuttle should not take off.

There arguments however did not prevent the launch and unfortunately shortly after take-off the shuttle exploded.

Looking at these visualisations it is difficult to understand what they are trying to convey. Its interesting to note that they presented their data in chronological order, when the focus of their message was that at lower temperatures o-rings are more likely to fail. 

When creating a visualisation you should think about the message you are trying to convey and what is the best way to emphasise that message.

![Untitled](Day%2010%20&%2011%208ed481e2be3e4f40b142ecfd5ae4c998/Untitled%202.png)

### Causal Analysis

When you hear the term correlation does not equal causation what we’re really saying is that while two events might be connected or related, that doesn’t mean they’re in a cause-and-effect relation.

A causal link means proving that one event causes another. This is applied heavily in epidemiology, where discovering the correct causal link can mean big things for the prevention and treatment of diseases.

The John Snow cholera case study provides a really interesting thought process.

- Doctor Snow developed a hypothesis by analysing available data
- He then tried to disprove his hypothesis by finding contradictory data to strengthen his explanation
- When his theory was more established he designed a test for that theory.
- The success of that test then lead to further tests that further reinforced his theory and as such allowed him to make a definitive causal link to what was causing cholera.

In lab science we use controlled experiments to isolate variables and prove causation, in data science this can be more difficult but data scientists do the best they can to isolate and control variables and get comfortable with working with some amount of error.

### Ethics of Data Collection and Privacy

Much of the data available to us comes from individuals and would be considered as personally identifiable (i.e. PII or Personally Identifiable Information).

Ethical issues regarding data collection can be divided into the following categories:

- Consent - Individuals must be informed and give their consent for information to be collected (i.e. sneaky click to consent)
- Ownership - Anyone collecting data must be aware that individuals have ownership over their information
- Intention - Individuals must be informed about what information will be taken, how it will be stored and how it will be used.
- Privacy - Information about individuals must be kept secure, this is especially important for all PII.

### Data Collection

We use different methods to collect data:

- We can seek out information that doesn’t already exist through things like surveys, observational studies or recording the results of an experiment.
    - This type of information can be classed as **static** as once collected it doesn’t change.
- It can be made **dynamic** for example in apps or websites which dynamically track clicks and time spent on pages from multiple users at the same time.
    - Sensors and trackers also gather dynamic data e.g. those used in weather predictions.

### Data Sources

Data can come from many different places, many datasets are private or can be accessed for a fee. It can come in the form of CSV or excel files or a database accessed via an API.

Free sources of data include:

- WHO [https://www.who.int/data/gho/](https://www.who.int/data/gho/)
- FiveThirtyEight [https://data.fivethirtyeight.com/](https://data.fivethirtyeight.com/)

---

Stopped here for today and will continue my notes tomorrow July 9, 2022 

---

July 10, 2022 

Continued from here

## Data Types and Quality

### Shape of Data

The shape of data relates to how the data is stored. One of the most common methods is via spreadsheets or tables. Here the things we are measuring (variables) are in columns, and the individual instances (observations) are in the rows.

When selecting variables or measurements we should aim for things that are universal to what we are observing i.e. every entity or instance has that feature (e.g. age in people).

By doing this it allows us to categorise our data better and helps to prevent gaps in our dataset. We need to be smart as to how we combine our variables to also prevent this.

For example we could have a variables for all the individual eye colours but it may be better to just combine them all into one variable called eye colour.

How we combine or separate data can also be influenced by how easy it is to collect that data. 

This thought process can also be applied when we need to tidy data in a data wrangling process.

### Variable Types

Variables can come in different types:

- Variables that are measured are Numerical variables
    - These can be both discrete or continuous
- Variables that are categorized are Categorical variables
    - These can be nominal (i.e. a named value) or dichotomous (i.e. on/off, 1/0, true/false.
    - These can be inherently ordered/ranked and as such are known as ordinal variables (i.e. on a scale of 1 to 5…)

### Dealing With Messy Data

Clean datasets are all alike but a messy dataset can be messy in its own unique way. This is why cleaning data requires critical thought to consider the nuances of the dataset we are working with.

There are however patterns with how a dataset can go wrong so we have a few things we can look for.

Common types of messy data problems include:

- Typos
- Missing Data
- Inconsistent Coding

If we don’t fix these issues when cleaning we can have issues such as: two categories for the same thing, inaccurate statistics, error messages

![Untitled](Day%2010%20&%2011%208ed481e2be3e4f40b142ecfd5ae4c998/Untitled%203.png)

When we observe missing data in our dataset we need to treat it in different ways depending on what we think the root cause may be.

Reasons data can be missing:

- Missing completely at random
- Missing for a random reason
- Structurally missing (i.e. all entities do not possess that variable (e.g. some trees have fruit and some do not)

For structurally missing data we can just ignore it potentially, for the other two types we need to think more carefully.

<aside>
💡 Whatever we do to deal with missing data we need to be careful that it does not affect our analysis.

</aside>

### Accuracy

Once we’ve gathered and cleaned our dataset we need to understand if it is accurate or not. Accuracy is the measure of how well the records reflect reality.

If we can standardised how we do something then there is the potential that that we can make our data more reliable, however if we get this wrong it can effect the accuracy of a dataset systematically.

We need to look at our data critically in order to assess its accuracy and to identify where issues lie. A few useful questions to ask are as follows:

1. Does the data match our expectations/common sense (we can measure this statistically by looking at data distribution and outliers to understand what our data looks like)
2. How could error be introduced into our data collection process as this may aid in the grouping and evaluation of the data to uncover systemic inconsistencies.
3. Identify how duplicates could have been created to ensure we don’t suffer from double accounting.

### Validity

Accuracy and messy data is not the only thing which effects the quality of our dataset, we also need to make sure our dataset actually measures what we think it is measuring. This is known as the **validity** of our dataset.

For example if we use the measurement of one variable to derive the value of another we need to ensure that there is a direct causal relationship otherwise we effect the validity of the data generated for that second variable.

Fidelity of the data can also effect the validity of our data if we use it to derive how things may change (e.g. we try to estimate how much a tree width changes per year but we only have data from today and a measurement 20 years ago).

### Representative Samples

Once all the above steps have been completed and considered we can then think about analysing our data.

Depending how our data was collected we may or may not have biases present. 

One example of a sampling error is that of a convenience sample (i.e. a sample that is collected from something convenient) this results in a bias as we have constrained our sample.

To ensure our data is a good sample it needs to represent a population, any time this is not the case.

By making a representative sample we get a mix of observations that ultimately contains all of the features of the larger population.

---

Finished here for the day

---

## Useful Information

- Cool python library for computational molecular biology

[Biopython](https://biopython.org/)

- Code Challenges

[Code Challenges | Codecademy](https://www.codecademy.com/code-challenges)

- Codeacademy cheatsheet for data

[Principles of Data Literacy: Introduction to Data Cheatsheet | Codecademy](https://www.codecademy.com/learn/paths/data-analyst/tracks/dsf-data-literacy/modules/introduction-to-data-38e13b33-2ba6-4515-bfbf-4a785c9194a9/cheatsheet)

- Course on cleaning data with python

[How to Clean Data with Python | Codecademy](https://www.codecademy.com/learn/practical-data-cleaning)

- Course on handling missing data

[Handling Missing Data | Codecademy](https://www.codecademy.com/learn/handling-missing-data)

## Reflections

- As well as the syllabus projects, it may be worthwhile to have a few of the challenges and personal projects completed for the portfolio.
- While codeacademy is code focussed I will need to dive into topics off platform as well.
- Spent less time learning and practicing programming concepts, which made for a less interesting session.
- Would be interesting to examine some of the case studies presented and see how we could use modern techniques to come to the same conclusions and visualisations.
- I will return to SQL and coding on the next day and interweave outstanding theory at other times otherwise my motivation will wane entirely.

## Tomorrow’s Focus

- Move on to SQL