from pathlib import Path

import numpy as np
import pandas as pd

data: Path = Path('./data')
satcat_csv: Path = data / 'satcat.csv'
satcat_xlsx: Path = data / 'satcat.xlsx'

# Which datatype appears in each column of the file. Dates (LAUNCH_DATE, DECAY_DATE) are handled by the parse_dates and
# date_format arguments in pd.read_csv()/pd.read_excel().
datatypes = {'OBJECT_NAME': str,
             'OBJECT_ID': str,
             'NORAD_CAT_ID': np.uint16,
             'OBJECT_TYPE': str,
             'OPS_STATUS_CODE': str,
             'OWNER': str,
             'LAUNCH_DATE': str,
             'LAUNCH_SITE': str,
             'DECAY_DATE': str,
             'PERIOD': float,
             'INCLINATION': float,
             'APOGEE': 'Int16',
             'PERIGEE': 'Int16',
             'RCS': float,
             'DATA_STATUS_CODE': str,
             'ORBIT_CENTER': str,
             'ORBIT_TYPE': str,
             }

date_format: str = '%d/%m/%Y'  # The date format used for the LAUNCH_DATE and DECAY_DATE fields.


def load_satcat(file: Path) -> pd.DataFrame:
    df: pd.DataFrame = pd.read_csv(file, dtype=datatypes, parse_dates=[6, 8], date_format=date_format)
    print(f'Loaded DataFrame from {file}\n')
    return df


# Load the SATCAT from the .csv file into a pandas DataFrame.
satcat: pd.DataFrame = load_satcat(satcat_csv)

headers = satcat.columns.to_list()
print(f'{headers = }\n')

print(f'First 10 rows: {satcat.head(10)}\n')
