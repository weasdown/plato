from enum import Enum

import numpy as np


class DataStatusCode(Enum):
    """
    Data status code.

    See https://celestrak.org/satcat/satcat-format.php.
    """
    NoCurrentElements = 'NCE'
    NoInitialElements = 'NIE'
    NoElementsAvailable = 'NEA'
    Blank = np.nan

    def __repr__(self) -> str:
        return f'DataStatusCode.{self.name}'


class OpsStatusCode(Enum):
    """
    Operational status code.

    See https://celestrak.org/satcat/status.php.
    """
    Operational = '+'
    Nonoperational = '-'
    Partially_Operational = 'P'
    Backup_Standby = 'B'
    Spare = 'S'
    Extended_Mission = 'X'
    Decayed = 'D'
    Unknown = '?'
    Blank = np.nan

    def __repr__(self) -> str:
        return f'OpsStatusCode.{self.name}'
