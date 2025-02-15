"""
  LAB 07
  PROGRAMMING PROBLEM 01

  Visit the website of the U.S. Bureau of Labor Statistics at https://www.bls.gov/data/home.htm and download the data for the average price of bread, as shown earlier in this chapter (there will be data for more recent years added since these words were written). You can also use the breadprice.csv file here >> Chapter 11 Data files. Write a program in a file named breadprice.py that loads the data set and cleans it as you did earlier in this chapter. Then include code to display a line plot of the average price for each year in the table.
"""

import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('data/breadprice.csv')

    df_copy = df.copy() # Make a copy to ensure no data from the original dataframe is lost
    df_copy.dropna(inplace=True) #Clean

    df_copy['AveragePrice'] = df_copy.mean(axis=1, numeric_only=True)
  
    plt.figure(figsize=(10, 7))
    plt.plot(df_copy['Year'], df_copy['AveragePrice'])
    plt.xlabel('Year')
    plt.ylabel('Average Price')
    plt.title("Average Price of Bread Per Year")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
