"""
  LAB 07
  PROGRAMMING PROBLEM 02

	The columns labeled FG, 3PT, and FT of the data set in the Analyzing Basketball Statistics case study (Download the files here >> CaseStudy2) do not show a single integer value but instead show values with the format <makes-attempts>, which is not suitable for the kind of data analysis performed on the other columns. For example, analysts might like to view the mean of free throws attempted as well as mean of the free throw percentage. You can correct this problem with a cleaning step that, for each such column:
    •	removes it from the data frame
    •	creates two new columns from this series, where the first column includes the numbers of makes and the second column includes the number of attempts
    •	inserts the new pairs of columns into the data frame at the appropriate positions, with the appropriate column headings (for example, FTM and FTA)
	Define a function named cleanStats in the file hoopstatsapp.py. This function expects a data frame as an argument and returns the frame cleaned according to the steps listed previously. You should call this function after the frame is loaded from the CSV file and before it is passed to the HoopStatsView constructor.
"""

"""
File: hoopstatsapp.py

The application for analyzing basketball stats.
"""

from hoopstatsview import HoopStatsView
import pandas as pd

def main():
    """Creates the data frame and view and starts the app."""

		#TODO
    frame = pd.read_csv("cleanbrogdonstats.csv")
    HoopStatsView(frame)

if __name__ == "__main__":
    main()
