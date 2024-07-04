# Index in Python Pandas
## Introduction
 Indexing refers to the process of accessing a specific element in a sequence, such as a string or list, using its position or index number. Indexing in Python starts at 0, which means that the first element in a sequence has an index of 0, the second element has an index of 1, and so on. 
 Idexing in pandas means simply selecting particular rows and columns of data from a DataFrame.

**Import python libraries**
```
import pandas as pd
```
**create a dictionary in jupyter notebook**
```
df = {
    "F_name" : ["Jon", "Wink", "Paul", "Loop"],
    "L_name" : ["Kim", "Zam", "Un", "All"],
    "Email"  : ["Jonkim@email.com", "Winkzam@email.com", "Paulun@email.com", "Loopall@email"]
}
```
**Load your dictionary as a dataframe**
```
dataset = pd.DataFrame(df)
dataset
```
**check if your dataframe has an index**
```
dataset.index
```
**set an index to your dataframe**
- For our case i have set f_name as my index
```
dataset.set_index("F_name", inplace = True)
```
**To load the first five rows in our dataset use df.head() to see if the index was added**
```
dataset.head()
```
**In order to sort an index use the sort function and it will sorted in ascending**
```
dataset.sort_index()
```
**To sort it in descending**
```
dataset.sort_index(ascending = False)
```
**In case you need to remove an index use reset_index() function**
```
dataset.reset_index(inplace = True)
```
## Advatages of indexes
- **Enhanced Speed**: Pandas indexing is designed for speed, especially when working with large datasets.Traditional Python techniques, like list comprehensions or looping through data, can be significantly slower because they process data element by element.
- **Data Alignment**: When performing operations across multiple DataFrames or Series, pandas automatically aligns data based on index labels. This ensures accuracy in calculations without the need for manual alignment.
- **Intuitive Selection**: Pandas indexing provides intuitive selection and subsetting of data. With functions like .loc[] and .iloc[] , you can select data by label or position with ease.
- **Advanced Querying**: Advanced querying with pandas indexing allows you to filter and manipulate your data with powerful conditionals.

  ## Conclusions
   The index() method searches an element and is essential when lookin up for a record in a dataset.
