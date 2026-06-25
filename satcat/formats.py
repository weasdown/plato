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


class LaunchSite(Enum):
    """
    Site that the object was launched from.

    See https://celestrak.org/satcat/launchsites.php.

    AFETR	Air Force Eastern Test Range, Florida, USA
    AFWTR	Air Force Western Test Range, California, USA
    ANDSP	Andøya Spaceport, Nordland, Norway
    ALCLC	Alâcantara Launch Center, Maranhão, Brazil
    BOS     Bowen Orbital Spaceport, Queensland, Australia
    CAS     Canaries Airspace
    DLS     Dombarovskiy Launch Site, Russia
    ERAS	Eastern Range Airspace
    FRGUI	Europe's Spaceport, Kourou, French Guiana
    HGSTR	Hammaguira Space Track Range, Algeria
    JJSLA	Jeju Island Sea Launch Area, Republic of Korea
    JSC     Jiuquan Space Center, PRC
    KODAK	Kodiak Launch Complex, Alaska, USA
    KSCUT	Uchinoura Space Center (Formerly Kagoshima Space Center—University of Tokyo, Japan)
    KWAJ	US Army Kwajalein Atoll (USAKA)
    KYMSC	Kapustin Yar Missile and Space Complex, Russia
    NSC     Naro Space Complex, Republic of Korea
    PLMSC	Plesetsk Missile and Space Complex, Russia
    RLLB	Rocket Lab Launch Base, Mahia Peninsula, New Zealand
    SCSLA	South China Sea Launch Area, PRC
    SEAL	Sea Launch Platform (mobile)
    SEMLS	Semnan Satellite Launch Site, Iran
    SMTS	Shahrud Missile Test Site, Iran
    SNMLP	San Marco Launch Platform, Indian Ocean (Kenya)
    SPKII	Space Port Kii, Japan
    SRILR	Satish Dhawan Space Centre, India (Formerly Sriharikota Launching Range)
    SUBL	Submarine Launch Platform (mobile)
    SVOBO	Svobodnyy Launch Complex, Russia
    TAISC	Taiyuan Space Center, PRC
    TANSC	Tanegashima Space Center, Japan
    TYMSC	Tyuratam Missile and Space Center, Kazakhstan (Also known as Baikonur Cosmodrome)
    UNK     Unknown
    VOSTO	Vostochny Cosmodrome, Russia
    WLPIS	Wallops Island, Virginia, USA
    WOMRA	Woomera, Australia
    WRAS    Western Range Airspace
    WSC     Wenchang Satellite Launch Site, PRC
    XICLF	Xichang Launch Facility, PRC
    YAVNE   Yavne Launch Facility, Israel
    YSLA    Yellow Sea Launch Area, PRC
    YUN     Yunsong Launch Site (Sohae Satellite Launching Station), Democratic People's Republic of Korea (North Korea)
    """
    Air_Force_Eastern_Test_Range_Florida_USA = 'AFETR'
    Air_Force_Western_Test_Range_California_USA = 'AFWTR'
    Andoya_Spaceport_Nordland_Norway = 'ANDSP'
    Alacantara_Launch_Center_Maranhao_Brazil = 'ALCLC'
    Bowen_Orbital_Spaceport_Queensland_Australia = 'BOS'
    Canaries_Airspace = 'CAS'
    Dombarovskiy_Launch_Site_Russia = 'DLS'
    Eastern_Range_Airspace = 'ERAS'
    Spaceport_Kourou_French_Guiana = 'FRGUI'
    Hammaguira_Space_Track_Range_Algeria = 'HGSTR'
    Jeju_Island_Sea_Launch_Area_Republic_of_Korea = 'JJSLA'
    Jiuquan_Space_Center_PRC = 'JSC'
    Kodiak_Launch_Complex_Alaska_USA = 'KODAK'
    Uchinoura_Space_Center_Japan = 'KSCUT'
    US_Army_Kwajalein_Atoll = 'KWAJ'
    Kapustin_Yar_Missile_and_Space_Complex_Russia = 'KYMSC'
    Naro_Space_Complex_Republic_of_Korea = 'NSC'
    Plesetsk_Missile_and_Space_Complex_Russia = 'PLMSC'
    Rocket_Lab_Launch_Base_Mahia_Peninsula_New_Zealand = 'RLLB'
    South_China_Sea_Launch_Area_PRC = 'SCSLA'
    Sea_Launch_Platform = 'SEAL'
    Semnan_Satellite_Launch_Site_Iran = 'SEMLS'
    Shahrud_Missile_Test_Site_Iran = 'SMTS'
    San_Marco_Launch_Platform_Indian_Ocean_Kenya = 'SNMLP'
    Space_Port_Kii_Japan = 'SPKII'
    Satish_Dhawan_Space_Centre_India = 'SRILR'
    Submarine_Launch_Platform = 'SUBL'
    Svobodnyy_Launch_Complex_Russia = 'SVOBO'
    Taiyuan_Space_Center_PRC = 'TAISC'
    Tanegashima_Space_Center_Japan = 'TANSC'
    Tyuratam_Missile_and_Space_Center_Baikonur_Cosmodrome_Kazakhstan = 'TYMSC'
    Unknown = 'UNK'
    Vostochny_Cosmodrome_Russia = 'VOSTO'
    Wallops_Island_Virginia_USA = 'WLPIS'
    Woomera_Australia = 'WOMRA'
    Western_Range_Airspace = 'WRAS'
    Wenchang_Satellite_Launch_Site_PRC = 'WSC'
    Xichang_Launch_Facility_PRC = 'XICLF'
    Yavne_Launch_Facility_Israel = 'YAVNE'
    Yellow_Sea_Launch_Area_PRC = 'YSLA'
    Yunsong_Launch_Site_North_Korea = 'YUN'

    def __repr__(self) -> str:
        return self.name


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

# TODO add enums for ORBIT_CENTER, ORBIT_TYPE
