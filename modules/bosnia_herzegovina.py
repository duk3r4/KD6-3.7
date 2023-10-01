import pandas as pd


def bih_alg_nin(nin):
    df_bih_yyy = pd.read_csv('modules/data/bosnia_herzegovina_yyy.csv')
    df_bih_mm = pd.read_csv('modules/data/bosnia_herzegovina_mm.csv')
    df_bih_dd = pd.read_csv('modules/data/bosnia_herzegovina_dd.csv')
    df_bih_rr = pd.read_csv('modules/data/bosnia_herzegovina_rr.csv')
    # checking the length
    length = len(nin)
    if length != 13:
        print('Wrong length of the ID number. Please, try again')
        return()
    # checking the DD parameter
    dd = nin[0:2]
    if df_bih_dd['DD'].isin([dd]).any():
        bd_day = df_bih_dd.at[df_bih_dd.loc[df_bih_dd['DD'] == dd].index[0], 'Day']
    else:
        print('The ID number is wrong. Please, try again')
        return()
    # checking the MM parameter
    mm = nin[2:4]
    if df_bih_mm['MM'].isin([mm]).any():
        bd_month = df_bih_mm.at[df_bih_mm.loc[df_bih_mm['MM'] == mm].index[0], 'Month']
    else:
        print('The ID number is wrong. Please, try again')
        return()
    # checking the YYY parameter
    yyy = nin[4:7]
    if df_bih_yyy['YYY'].isin([yyy]).any():
        bd_year = df_bih_yyy.at[df_bih_yyy.loc[df_bih_yyy['YYY'] == yyy].index[0], 'YYYY']
    else:
        print('The ID number is wrong. Please, try again')
        return()
    # checking the RR parameter
    rr = nin[7:9]
    if df_bih_rr['RR'].isin([rr]).any():
        status = df_bih_rr.at[df_bih_rr.loc[df_bih_rr['RR'] == rr].index[0], 'Status']
        reg = df_bih_rr.at[df_bih_rr.loc[df_bih_rr['RR'] == rr].index[0], 'Political region']
    else:
        print('The ID number is wrong. Please, try again')
        return()
    # checking the BBB parameter
    bbb = nin[9:12]
    if bbb.isnumeric():
        if 0 <= int(bbb) <= 499:
            sex = 'Male'
        else:
            sex = 'Female'
    else:
        print('The ID number is wrong. Please, try again')
        return()
    k = nin[12]
    print('\nHere\'s what I got from that ID number:\nDay of birth: ', bd_day, '\nMonth of birth: ',
          bd_month, '\nYear of birth: ', bd_year, '\nSex: ', sex, '\nStatus: ', status,
          '\nPolitical region of birth (for persons born before 1976, political region where they '
          'were first registered): ', reg, '\nChecksum symbol: ', k, '\n')
    return()
