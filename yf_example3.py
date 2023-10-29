"""
yf_example3.py
Downloads Qantas stock prics for a given year and saves into a CSV file
"""

import os
import toolkit_config as cfg
import yf_example2


def qan_prc_to_csv(year):
    """
    Download Qantas stock prices for a given year into a CSV file.

    Parameters:
    - year (int): The year for which to download the data.

    The CSV file will be named 'qan_prc_YYYY.csv' and saved in the 'data' folder.
    """
    # Define the start and end date for the given year
    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"

    # Create the name of the output file
    output_file_name = f'qan_prc_{year}.csv'

    # Create the path to the output file within the 'data' folder
    output_file_path = os.path.join(cfg.DATADIR, output_file_name)

    yf_example2.yf_prc_to_csv("QAN.AX", output_file_path, start_date, end_date)


if __name__ == "__main__":
    # Example usage: Download Qantas stock prices for the year 2020
    qan_prc_to_csv(year=2020)
