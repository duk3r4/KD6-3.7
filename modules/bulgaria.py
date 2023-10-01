import pandas as pd


def bgr_alg_nin(nin):
    df_bulgaria_yy = pd.read_csv('modules/data/bulgaria_yy.csv')
    df_bulgaria_mm = pd.read_csv('modules/data/bulgaria_mm.csv')
    df_bulgaria_dd = pd.read_csv('modules/data/bulgaria_dd.csv')
    df_bulgaria_xxs = pd.read_csv('modules/data/bulgaria_xxs.csv')
    # checking the length
    length = len(nin)
    if length != 10:
        print('Wrong length of the ID number. Please, try again')
        return()
    # checking the MM parameter
    mm = nin[2:4]
    if df_bulgaria_mm['MM'].isin([mm]).any():
        bd_month = df_bulgaria_mm.at[df_bulgaria_mm.loc[df_bulgaria_mm['MM'] == mm].index[0], 'Month']
    else:
        print('The ID number is wrong. Please, try again')
        return()
    # checking the YY parameter
    yy = nin[0:2]
    if df_bulgaria_yy['YY'].isin([yy]).any():
        if 1 <= int(mm) <= 12:
            bd_year = df_bulgaria_yy.at[
                df_bulgaria_yy.loc[df_bulgaria_yy['YY'] == yy].index[0], 'YYYY_1900']
        elif 21 <= int(mm) <= 32:
            bd_year = df_bulgaria_yy.at[
                df_bulgaria_yy.loc[df_bulgaria_yy['YY'] == yy].index[0], 'YYYY_1800']
        elif 41 <= int(mm) <= 52:
            bd_year = df_bulgaria_yy.at[
                df_bulgaria_yy.loc[df_bulgaria_yy['YY'] == yy].index[0], 'YYYY_2000']
    else:
        print('The ID number is wrong. Please, try again')
        return()
    # checking the DD parameter
    dd = nin[4:6]
    if df_bulgaria_dd['DD'].isin([dd]).any():
        bd_day = df_bulgaria_dd.at[df_bulgaria_dd.loc[df_bulgaria_dd['DD'] == dd].index[0], 'Day']
    else:
        print('The ID number is wrong. Please, try again')
        return()
    # checking the XXX parameter
    xxs = nin[6:9]
    if df_bulgaria_xxs['XXS'].isin([xxs]).any():
        reg = df_bulgaria_xxs.at[df_bulgaria_xxs.loc[df_bulgaria_xxs['XXS'] == xxs].index[0], 'Region']
    else:
        print('The ID number is wrong. Please, try again')
        return()
    s = nin[8:9]
    if int(s) % 2 == 0:
        sex = 'Male'
    else:
        sex = 'Female'
    c = nin[9]
    print('\nHere\'s what I got from that ID number:\nDay of birth: ', bd_day, '\nMonth of birth: ',
          bd_month, '\nYear of birth: ', bd_year, '\nSex: ', sex, '\nPlace of birth: ', reg,
          '\nChecksum symbol: ', c, '\n')
    return()
