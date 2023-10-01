import pandas as pd


def alb_alg_nin(nin):
    df_albania_yy = pd.read_csv('modules/data/albania_yy.csv')
    df_albania_mm = pd.read_csv('modules/data/albania_mm.csv')
    df_albania_dd = pd.read_csv('modules/data/albania_dd.csv')
    # checking the length
    length = len(nin)
    if length != 10:
        print('Wrong length of the ID number. Please, try again')
        return()
    # checking the YY parameter
    yy = nin.upper()[0:2]
    if df_albania_yy['YY'].isin([yy]).any():
        bd_year = df_albania_yy.at[df_albania_yy.loc[df_albania_yy['YY'] == yy].index[0], 'YYYY']
    else:
        print('The ID number is wrong. Please, try again')
        return()
    # checking the MM parameter
    mm = nin.upper()[2:4]
    if df_albania_mm['MM'].isin([mm]).any():
        bd_month = df_albania_mm.at[df_albania_mm.loc[df_albania_mm['MM'] == mm].index[0], 'Month']
        sex = df_albania_mm.at[df_albania_mm.loc[df_albania_mm['MM'] == mm].index[0], 'Sex']
    else:
        print('The ID number is wrong. Please, try again')
        return()
    # checking the dd parameter
    dd = nin.upper()[4:6]
    if df_albania_dd['DD'].isin([dd]).any():
        bd_day = df_albania_dd.at[df_albania_dd.loc[df_albania_dd['DD'] == dd].index[0], 'Day']
    else:
        print('The ID number is wrong. Please, try again')
        return()
    sss = nin.upper()[6:9]
    c = nin.upper()[9]
    print('\nHere\'s what I got from that ID number:\nDay of birth: ', bd_day, '\nMonth of birth: ',
          bd_month, '\nYear of birth: ', bd_year, '\nSex: ', sex,
          '\nSequence number of person with the same date of birth: ', int(sss), '\nChecksum symbol: ', c, '\n')
    return()
