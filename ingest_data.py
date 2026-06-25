from pathlib import Path

import pandas as pd

data: Path = Path('./data')
satcat_csv: Path = data / 'satcat.csv'
satcat_xlsx: Path = data / 'satcat.xlsx'


def load_satcat(file: Path) -> pd.DataFrame:
    df: pd.DataFrame = pd.read_csv(file)
    print(f'Loaded DataFrame from {file}\n')
    return df


# Load the SATCAT from the .csv file into a pandas DataFrame.
satcat: pd.DataFrame = load_satcat(satcat_csv)
print(satcat.values[0])
