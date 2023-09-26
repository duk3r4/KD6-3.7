import pandas as pd


def fin_alg_nin(nin):
    while True:
        df_finland_yy = pd.read_csv('modules/data/finland_yy.csv')
        df_finland_mm = pd.read_csv('modules/data/finland_mm.csv')
        df_finland_dd = pd.read_csv('modules/data/finland_dd.csv')
        # checking the length
        length = len(nin)
        if length != 11:
            print('Wrong length of the ID number. Please, try again')
            break
        # checking the DD parameter
        dd = nin[0:2]
        if df_finland_dd['DD'].isin([dd]).any():
            bd_day = df_finland_dd.at[df_finland_dd.loc[df_finland_dd['DD'] == dd].index[0], 'Day']
        else:
            print('The ID number is wrong. Please, try again')
            break
        # checking the MM parameter
        mm = nin[2:4]
        if df_finland_mm['MM'].isin([mm]).any():
            bd_month = df_finland_mm.at[df_finland_mm.loc[df_finland_mm['MM'] == mm].index[0], 'Month']
        else:
            print('The ID number is wrong. Please, try again')
            break
        # checking the YY parameter
        yy = nin[4:6]
        if df_finland_yy['YY'].isin([yy]).any():
            pass
        else:
            print('The ID number is wrong. Please, try again')
            break
        # checking the C parameter
        c = nin.upper()[6]
        xixcent = ['+']
        xxcent = ['-', 'U', 'V', 'W', 'X', 'Y']
        xxicent = ['A', 'B', 'C', 'D', 'E', 'F']
        if c in xixcent:
            bd_year = df_finland_yy.at[df_finland_yy.loc[df_finland_yy['YY'] == yy].index[0], 'YYYY_19']
        elif c in xxcent:
            bd_year = df_finland_yy.at[df_finland_yy.loc[df_finland_yy['YY'] == yy].index[0], 'YYYY_20']
        elif c in xxicent:
            bd_year = df_finland_yy.at[df_finland_yy.loc[df_finland_yy['YY'] == yy].index[0], 'YYYY_21']
        else:
            print('The ID number is wrong. Please, try again')
            break
        # checking the ZZZ parameter
        zzz = nin[7:10]
        if int(zzz) % 2 == 0:
            sex = 'Female'
        else:
            sex = 'Male'
        q = nin.upper()[10]
        print('\nHere\'s what I got from that ID number:\nDay of birth: ', bd_day, '\nMonth of birth: ',
              bd_month, '\nYear of birth: ', bd_year, '\nSex: ', sex,
              '\nSequence number of person with the same date of birth: ', int(zzz), '\nChecksum symbol: ',
              q, '\n')
        break
