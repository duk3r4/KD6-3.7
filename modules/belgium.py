import pandas as pd


def bel_alg_nin(nin):
    df_belgium_yy = pd.read_csv('modules/data/belgium_yy.csv')
    df_belgium_mm = pd.read_csv('modules/data/belgium_mm.csv')
    df_belgium_dd = pd.read_csv('modules/data/belgium_dd.csv')
    # checking the length
    length = len(nin)
    if length != 11:
        print('Wrong length of the ID number. Please, try again')
        return()
    # checking the YY parameter
    yy = nin[0:2]
    if df_belgium_yy['YY'].isin([yy]).any():
        bd_year = df_belgium_yy.at[df_belgium_yy.loc[df_belgium_yy['YY'] == yy].index[0], 'YYYY']
    else:
        print('The ID number is wrong. Please, try again')
        return()
    # checking the MM parameter
    mm = nin[2:4]
    if df_belgium_mm['MM'].isin([mm]).any():
        bd_month = df_belgium_mm.at[df_belgium_mm.loc[df_belgium_mm['MM'] == mm].index[0], 'Month']
    else:
        print('The ID number is wrong. Please, try again')
        return()
    # checking the DD parameter
    dd = nin[4:6]
    if df_belgium_dd['DD'].isin([dd]).any():
        bd_day = df_belgium_dd.at[df_belgium_dd.loc[df_belgium_dd['DD'] == dd].index[0], 'Day']
    else:
        print('The ID number is wrong. Please, try again')
        return()
    # checking the XXX parameter
    xxx = nin[6:9]
    if xxx.isnumeric():
        if int(xxx) % 2 == 0:
            sex = 'Female'
        else:
            sex = 'Male'
    else:
        print('The ID number is wrong. Please, try again')
        return()
    cd = nin[9:11]
    print('\nHere\'s what I got from that ID number:\nDay of birth: ', bd_day, '\nMonth of birth: ',
          bd_month, '\nYear of birth: ', bd_year, '\nSex: ', sex, '\nChecksum number: ', cd)
    return()


def bel_alg_icn(icn):
    if len(icn) == 12:
        print('\nHere\'s what I got from that ID number:\nThe card owner is a Belgium citizen\n')
        return()
    elif len(icn) == 9:
        print('\nHere\'s what I got from that ID number:\nThe card owner is a third country citizen\n')
        return()
    elif len(icn) == 10:
        print('\nHere\'s what I got from that ID number:\nThe card owner is a EU/EEA/Swiss citizen\n')
        return()
    else:
        print('The ID number is wrong. Please, try again')
        return()
