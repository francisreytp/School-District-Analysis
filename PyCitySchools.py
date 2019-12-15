#%%
# Add the dependencies.
import pandas as pd
import os 

#%%
# Files to load
school_data_to_load = os.path.join("Resources", "schools_complete.csv")
student_data_to_load = os.path.join("Resources", "students_complete.csv")

#%%
# Read the school data file and store it in a Pandas DataFrame.
school_data_df = pd.read_csv(school_data_to_load)
school_data_df

#%%
# Read the student data file and store it in a Pandas DataFrame.
student_data_df = pd.read_csv(student_data_to_load)
student_data_df.head()

#%%
# Determine if there are any missing values in the school data.
school_data_df.count()

# %%
# Determine if there are any missing values in the student data.
student_data_df.count()

# %%
# Determine if there are any missing values in the school data.
school_data_df.isnull()

#%%
# Determine if there are any missing values in the student data.
student_data_df.isnull()

# %%
# Determine if there are any missing values in the student data.
student_data_df.isnull().sum()


# %%
# Determine if there are not any missing values in the school data.
school_data_df.notnull()

# %%
# Determine if there are not any missing values in the student data.
student_data_df.notnull().sum()

#%%
# Determine data types for the school DataFrame.
school_data_df.dtypes

#%%
# Determine data types for the student DataFrame.
student_data_df.dtypes

# %%
# Add each prefix and suffix to remove to a list.
prefixes_suffixes = ["Dr. ", "Mr. ","Ms. ", "Mrs. ", "Miss ", " MD", " DDS", " DVM", " PhD"]

#%%
# Iterate through the words in the "prefixes_suffixes" list and replace them with an empty space, "".
for word in prefixes_suffixes:
    student_data_df["student_name"] = student_data_df["student_name"].str.replace(word,"")

#the student_data_df should be clean at this point
student_data_df.head(8)

# %%
# Combine the data into a single dataset.
school_data_complete_df = pd.merge(student_data_df, school_data_df, on=["school_name", "school_name"])
school_data_complete_df.head()

# %%
# Get the total number of students.
student_count = school_data_complete_df["Student ID"].count()
student_count

#%%
# Calculate the total number of schools.
school_count = school_data_df["school_name"].count()
school_count

# %%
# Calculate the total number of schools
school_count_2 = school_data_complete_df["school_name"].unique()
school_count_2

# %%
# Calculate the total budget.
total_budget = school_data_df["budget"].sum()
total_budget

# %%
# Calculate the average reading score.
average_reading_score = school_data_complete_df["reading_score"].mean()
average_reading_score

# %%
# Calculate the average math score.
average_math_score = school_data_complete_df["math_score"].mean()
average_math_score

#%%
passing_math = school_data_complete_df["math_score"] >= 70
passing_reading = school_data_complete_df["reading_score"] >= 70

# %%
# Get all the students who are passing math in a new DataFrame.
passing_math = school_data_complete_df[school_data_complete_df["math_score"] >= 70]
passing_math.head()

#%%
# Get all the students that are passing reading in a new DataFrame.
passing_reading = school_data_complete_df[school_data_complete_df["reading_score"] >= 70]
passing_reading.head()

# %%
# Calculate the number of students passing math.
passing_math_count = passing_math["student_name"].count()
print(passing_math["student_name"].count())

# Calculate the number of students passing reading.
passing_reading_count = passing_reading["student_name"].count()
print(passing_reading["student_name"].count())

#%%
# Calculate the percent that passed math.
passing_math_percentage = passing_math_count / float(student_count) * 100
print(passing_math_percentage)

# Calculate the percent that passed reading.
passing_reading_percentage = passing_reading_count / float(student_count) * 100
print(passing_reading_percentage)

#%%
# Calculate the overall passing percentage.
overall_passing_percentage = (passing_math_percentage + passing_reading_percentage ) / 2
print(overall_passing_percentage)

#%%
# Adding a list of values with keys to create a new DataFrame.
district_summary_df = pd.DataFrame(
          [{"Total Schools": school_count,
          "Total Students": student_count,
          "Total Budget": total_budget,
          "Average Math Score": average_math_score,
          "Average Reading Score": average_reading_score,
          "% Passing Math": passing_math_percentage,
         "% Passing Reading": passing_reading_percentage,
        "% Overall Passing": overall_passing_percentage}])
district_summary_df

# %%
# Format the "Total Students" to have the comma for a thousands separator.
district_summary_df["Total Students"] = district_summary_df["Total Students"].map("{:,}".format)

district_summary_df["Total Students"]


# %%
# Format "Total Budget" to have the comma for a thousands separator, a decimal separator, and a "$".

district_summary_df["Total Budget"] = district_summary_df["Total Budget"].map("${:,.2f}".format)

district_summary_df["Total Budget"]

# %%
# Format the columns.
district_summary_df["Average Math Score"] = district_summary_df["Average Math Score"].map("{:.1f}".format)

district_summary_df["Average Reading Score"] = district_summary_df["Average Reading Score"].map("{:.1f}".format)

district_summary_df["% Passing Math"] = district_summary_df["% Passing Math"].map("{:.0f}".format)

district_summary_df["% Passing Reading"] = district_summary_df["% Passing Reading"].map("{:.0f}".format)

district_summary_df["% Overall Passing"] = district_summary_df["% Overall Passing"].map("{:.0f}".format)

#%%
# Display the Dataframe
district_summary_df


# %%

# Reorder the columns in the order you want them to appear.
new_column_order = ["Total Schools", "Total Students", "Total Budget","Average Math Score", "Average Reading Score", "% Passing Math", "% Passing Reading", "% Overall Passing"]

# Assign district summary df the new column order.
district_summary_df = district_summary_df[new_column_order]
district_summary_df


# %%

