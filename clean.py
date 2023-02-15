import argparse
import pandas as pd


def clean_data(contact_file, other_file, output_file):
    # Load data from input files
    contact_df = pd.read_csv(contact_file)
    other_df = pd.read_csv(other_file)

    # Merge data based on ID column
    merged_df = pd.merge(contact_df, other_df, left_on='respondent_id', right_on='id')

    # Drop rows with missing values
    merged_df.dropna(inplace=True)

    # Drop rows if job column contains 'insurance' or 'Insurance'
    merged_df = merged_df[~merged_df['job'].str.contains('insurance|Insurance')]

    # Select the desired columns
    cleaned_df = merged_df[['respondent_id', 'name', 'address', 'phone', 'job', 'company', 'birthdate']]

    # Write cleaned data to output file
    cleaned_df.to_csv(output_file, index=False)

if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('contact_info_file', help='path to the respondent_contact.csv file')
    parser.add_argument('other_info_file', help='path to the respondent_other.csv file')
    parser.add_argument('output_file', help='path to the output file')
    args = parser.parse_args()

    # Clean data and write to output file
    clean_data(args.contact_info_file, args.other_info_file, args.output_file)

