import pandas as pd


def cze_alg_nin(nin):
    df_cze_yy = pd.read_csv('modules/data/cze_svk_yy.csv')
    df_cze_xx = pd.read_csv('modules/data/cze_svk_xx.csv')
    df_cze_dd = pd.read_csv('modules/data/cze_svk_dd.csv')
    # checking the length
    c = 'None (for people born before 1 January 1954)'
    length = len(nin)
    if length == 10:
        c = nin[9]
    elif length != 9:
        print('Wrong length of the ID number. Please, try again')
        return()
    # checking the YY parameter
    yy = nin[:2]
    if df_cze_yy['YY'].isin([yy]).any():
        bd_year = df_cze_yy.at[df_cze_yy.loc[df_cze_yy['YY'] == yy].index[0], 'YYYY']
    else:
        print('The ID number is wrong. Please, try again YY')
        return()
    # checking the XX parameter
    xx = nin[2:4]
    if df_cze_xx['XX'].isin([xx]).any():
        bd_month = df_cze_xx.at[df_cze_xx.loc[df_cze_xx['XX'] == xx].index[0], 'Month']
        sex = df_cze_xx.at[df_cze_xx.loc[df_cze_xx['XX'] == xx].index[0], 'Sex']
    else:
        print('The ID number is wrong. Please, try again XX')
        return()
    # checking the DD parameter
    dd = nin[4:6]
    if df_cze_dd['DD'].isin([dd]).any():
        bd_day = df_cze_dd.at[df_cze_dd.loc[df_cze_dd['DD'] == dd].index[0], 'Day']
    else:
        print('The ID number is wrong. Please, try again DD')
        return()
    # checking the XXX parameter
    sss = nin[6:9]
    print('\nHere\'s what I got from that ID number:\nDay of birth: ', bd_day, '\nMonth of birth: ',
          bd_month, '\nYear of birth: ', bd_year, '\nSex: ', sex,
          '\nSequence number of person with the same date of birth: ', int(sss), '\nChecksum symbol: ',
          c, '\n')
    return()
