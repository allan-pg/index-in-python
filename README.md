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

## Advatages of indexes
- **Enhanced Speed**: Pandas indexing is designed for speed, especially when working with large datasets.Traditional Python techniques, like list comprehensions or looping through data, can be significantly slower because they process data element by element.
- **Data Alignment**: When performing operations across multiple DataFrames or Series, pandas automatically aligns data based on index labels. This ensures accuracy in calculations without the need for manual alignment.
- **Intuitive Selection**: Pandas indexing provides intuitive selection and subsetting of data. With functions like .loc[] and .iloc[] , you can select data by label or position with ease.
- **Advanced Querying**: Advanced querying with pandas indexing allows you to filter and manipulate your data with powerful conditionals.
  
