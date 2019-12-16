# School-District-Analysis
School district analysis using Python

# Project Overview
We have been assigned to organize and analyze data from the school district.
With the help of Maria, she'll be assiting us on downloading sofwares and running the data to produce an analysis

# Resources
Data Source: schools_complete.csv, students_complete.csv
Software: Anaconda, Python 3.7.4, Jupyter Notebook, Visual Studio Code 1.40.2, Pycharm

# Summary

  The analysis shows that:
  Running the raw data through our software we were able to have a better overview of the situation:
    * Nuber of schools: 15
    * Student count: 39,170 
    * Total school budget: $24,649,428
    * Average reading score: 81.88
    * Average math score:    78.99
    * Overall passing rate: 80%

    Top 5 schools in overall passing: 
      1st - Cabrera High School 
      2nd - Thomas High School 
      3rd - Pena High School 
      4th - Griffin High School 
      5th - Wilson High School
    
    Bottom 5 schools in overal passing:
      15th - Rodriguez High School 
      14th - Figueroa High School 
      13th - Huang High School 
      12th - Johnson High School 
      11th - Ford High School

# Challenge Overview

  A new finding revaled that the scores of the 9th graders at Thomas High School are invalid. 
  "While administrators do not know the full extent of this academic dishonesty, they want to uphold the standards of state testing and have turned to us for help." because of this, we need to re-evaluate the situation and caculate the outcomes.

# Challenge Summary

  First we have to change the math and reading scores for the 9th graders at Thomas High School.
  Then we evaluate which calculations have been affected by this change.
    * The average math and reading score from all high schools slighly declined.
  
    Average math score went from 78.99 to 78.93
    Average reading score went from 81.88 to 81.86
    
    * One of the biggest impact is in the percentage of passing by schools(Thomas High School, 9th grade):
      Math:    93.27% vs 66.91% in the new calculation.
      Reading: 93.27% vs 69.66% in the new calculation. 

# Conclusion

  This ultimately lead to an extreme change in their overall ranking.
  
    *(New) Top 5 schools in overall passing: 
      1st - Cabrera High School 
      2nd - Pena High School 
      3rd - Griffin High School 
      4th - Wilson High School
      5th - Wright High School
    
    *(New) Bottom 5 schools in overal passing:
      15th - Thomas High School
      14th - Rodriguez High School 
      13th - Figueroa High School 
      12th - Huang High School 
      11th - Johnson High School
    
   Out of the 15 schools, they used to be the second best. But now they are at the very bottom of the list in regards to overall passing percentage.
      
    
