from pathlib import Path

import numpy as np
import pandas as pd

from satcat.formats import DataStatusCode, LaunchSite, OpsStatusCode

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
    df: pd.DataFrame = pd.read_csv(file, dtype=datatypes,
                                   # index_col='OBJECT_ID',
                                   parse_dates=[6, 8],
                                   date_format=date_format)

    # Replace columns with their respective enums from the satcat package.
    # TODO fix type warnings
    df['OPS_STATUS_CODE'] = [OpsStatusCode(code) for code in df['OPS_STATUS_CODE']]
    df['LAUNCH_SITE'] = [LaunchSite(code) for code in df['LAUNCH_SITE']]
    df['DATA_STATUS_CODE'] = [DataStatusCode(code) for code in df['DATA_STATUS_CODE']]

    # Set columns' data types.
    # See https://pandas.pydata.org/docs/user_guide/categorical.html for explanation of 'category' type.
    df = df.astype({'OPS_STATUS_CODE': 'category', 'LAUNCH_SITE': 'category', 'DATA_STATUS_CODE': 'category'})

    print(f'Loaded DataFrame from {file}\n')
    return df


# Load the SATCAT from the .csv file into a pandas DataFrame.
satcat: pd.DataFrame = load_satcat(satcat_csv)

headers = satcat.columns.to_list()
print(f'{headers = }\n')

print(f'First 10 rows: {satcat.head(10)}\n')
