# read in the relevant data from the ./races dir and display interesting plots
# usage: python3 analyse.py [race-name]

import argparse
import pandas as pd
import matplotlib as plot

parser = argparse.ArgumentParser(description='Read racing arguments')
parser.add_argument('racename')
# TODO: need to restrict this to only the allowed types: CSV, TXT, XLS
parser.add_argument('-f', '--format', required=True, help='the file format, supported formats: csv, (TODO)')

args = parser.parse_args()

if __name__ == "__main__":
    filename = args.racename + '.' + args.format
    filepath = 'races/' + filename
    print('\nSearching for file: ' + filepath)
    race_data = pd.read_csv(filepath, encoding = "latin")
    print(race_data)

    # TODO: include the overall, men's, women's, etc... as separate CSV files. Easier to analyse
    
