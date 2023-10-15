# read in the relevant data from the ./races dir and display interesting plots
# usage: python3 analyse.py [race-name]


import argparse

parser = argparse.ArgumentParser(description='Read racing arguments')
parser.add_argument('racename')

args = parser.parse_args()

if __name__ == "__main__":
    print("Analysing race: " + args.racename)