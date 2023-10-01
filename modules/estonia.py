import pandas as pd


def est_alg_nin(nin):
    df_estonia_yy = pd.read_csv('modules/data/estonia_yy.csv')
    df_estonia_mm = pd.read_csv('modules/data/estonia_mm.csv')
    df_estonia_dd = pd.read_csv('modules/data/estonia_dd.csv')
    # checking the length
    length = len(nin)
    if length != 11:
        print('Wrong length of the ID number. Please, try again')
        return()
    # checking the G parameter
    g = nin[0]
    if int(g) % 2 == 0:
        sex = 'Female'
    else:
        sex = 'Male'
    # checking the YY parameter
    yy = nin[1:3]
    if df_estonia_yy['YY'].isin([yy]).any():
        if 1 <= int(g) <= 2:
            bd_year = df_estonia_yy.at[df_estonia_yy.loc[df_estonia_yy['YY'] == yy].index[0],
                                       'YYYY_1-2']
        elif 3 <= int(g) <= 4:
            bd_year = df_estonia_yy.at[df_estonia_yy.loc[df_estonia_yy['YY'] == yy].index[0],
                                       'YYYY_3-4']
        elif 5 <= int(g) <= 6:
            bd_year = df_estonia_yy.at[df_estonia_yy.loc[df_estonia_yy['YY'] == yy].index[0],
                                       'YYYY_5-6']
    else:
        print('The ID number is wrong. Please, try again')
        return()
    # checking the MM parameter
    mm = nin[3:5]
    if df_estonia_mm['MM'].isin([mm]).any():
        bd_month = df_estonia_mm.at[df_estonia_mm.loc[df_estonia_mm['MM'] == mm].index[0], 'Month']
    else:
        print('The ID number is wrong. Please, try again')
        return()
    # checking the DD parameter
    dd = nin[5:7]
    if df_estonia_dd['DD'].isin([dd]).any():
        bd_day = df_estonia_dd.at[df_estonia_dd.loc[df_estonia_dd['DD'] == dd].index[0], 'Day']
    else:
        print('The ID number is wrong. Please, try again')
        return()
    # checking the SSS parameter
    sss = nin[7:10]
    c = nin[10]
    msg = f'\nPersonal mail for contacting government agencies: {nin}@eesti.ee'
    print('\nHere\'s what I got from that ID number:\nDay of birth: ', bd_day, '\nMonth of birth: ', bd_month,
          '\nYear of birth: ', bd_year, '\nSex: ', sex,
          '\nSequence number of person with the same date of birth: ', int(sss), '\nChecksum symbol: ', c,
          msg, '\n')
    return()
