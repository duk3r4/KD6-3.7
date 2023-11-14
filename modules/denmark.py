import pandas as pd


def dnk_alg_nin(nin):
    df_denmark_yys = pd.read_csv('modules/data/denmark_yys.csv')
    df_denmark_mm = pd.read_csv('modules/data/denmark_mm.csv')
    df_denmark_dd = pd.read_csv('modules/data/denmark_dd.csv')
    # checking the length
    length = len(nin)
    if length != 10:
        print('Wrong length of the ID number. Please, try again')
        return ()
    # checking the DD parameter
    dd = nin[:2]
    if df_denmark_dd['DD'].isin([dd]).any():
        bd_day = df_denmark_dd.at[df_denmark_dd.loc[df_denmark_dd['DD'] == dd].index[0], 'Day']
    else:
        print('The ID number is wrong. Please, try again DD')
        return()
    # checking the MM parameter
    mm = nin[2:4]
    if df_denmark_mm['MM'].isin([mm]).any():
        bd_month = df_denmark_mm.at[df_denmark_mm.loc[df_denmark_mm['MM'] == mm].index[0], 'Month']
    else:
        print('The ID number is wrong. Please, try again XX')
        return()
    # checking the YY parameter
    yy = nin[4:6]
    if df_denmark_yys['YY'].isin([yy]).any():
        if 0 <= int(nin[6]) <= 3:
            bd_year = df_denmark_yys.at[df_denmark_yys.loc[df_denmark_yys['YY'] == yy].index[0],
                                        'YYYY_0-3']
        elif int(nin[6]) == 4:
            bd_year = df_denmark_yys.at[df_denmark_yys.loc[df_denmark_yys['YY'] == yy].index[0],
                                        'YYYY_4']
        elif 5 <= int(nin[6]) <= 8:
            bd_year = df_denmark_yys.at[df_denmark_yys.loc[df_denmark_yys['YY'] == yy].index[0],
                                        'YYYY_5-8']
        elif int(nin[6]) == 9:
            bd_year = df_denmark_yys.at[df_denmark_yys.loc[df_denmark_yys['YY'] == yy].index[0],
                                        'YYYY_9']
    else:
        print('The ID number is wrong. Please, try again YY')
        return()
    # checking the SSSS parameter
    ssss = nin[9]
    sex = 'Female' if int(ssss) % 2 == 0 else 'Male'
    print('\nHere\'s what I got from that ID number:\nDay of birth: ', bd_day, '\nMonth of birth: ',
          bd_month, '\nYear of birth: ', bd_year, '\nSex: ', sex, '\n')
    return()
