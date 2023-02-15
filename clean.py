import pandas as pd
import sys

# read command line arguments
contact_file = sys.argv[1]
other_file = sys.argv[2]
output_file = sys.argv[3]

# load dataframes from csv files
contact_df = pd.read_csv(contact_file)
other_df = pd.read_csv(other_file)

# merge dataframes based on respondent ID
merged_df = pd.merge(contact_df, other_df, left_on='respondent_id', right_on='id')

# drop any rows with missing values
cleaned_df = merged_df.dropna()

# drop rows where job contains 'insurance' or 'Insurance'
cleaned_df = cleaned_df[~cleaned_df['job'].str.contains('insurance|Insurance')]

# select columns to keep in output file
output_cols = ['respondent_id', 'name', 'address', 'phone', 'job', 'company', 'birthdate']
cleaned_df = cleaned_df[output_cols]

# write cleaned dataframe to output file
cleaned_df.to_csv(output_file, index=False)

# print shape of output file
print(f"Output file shape: {cleaned_df.shape}")
