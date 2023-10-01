import pandas as pd


def fra_alg_nin(ssn):
    df_france_yy = pd.read_csv('modules/data/france_yy.csv')
    df_france_mm = pd.read_csv('modules/data/france_mm.csv')
    df_france_com = pd.read_csv('modules/data/france_com.csv', low_memory=False)
    df_france_com_comer = pd.read_csv('modules/data/france_com_comer.csv')
    df_france_pays = pd.read_csv('modules/data/france_pays.csv')
    # checking the length
    length = len(ssn)
    if length != 13:
        print('Wrong length of the ID number. Please, try again')
        return()
    # checking the S parameter
    s = ssn[0]
    temp = [3, 4, 7, 8]
    if int(s) == 1:
        sex = 'Male'
    elif int(s) == 2:
        sex = 'Female'
    elif int(s) in temp:
        sex = 'Unknown (the number has been assigned to the person on a temporary basis)'
    else:
        print('Wrong length of the ID number. Please, try again')
        return()
    # checking the YY parameter
    yy = ssn[1:3]
    if df_france_yy['YY'].isin([yy]).any():
        bd_year = df_france_yy.at[df_france_yy.loc[df_france_yy['YY'] == yy].index[0], 'YYYY']
    else:
        print('The ID number is wrong. Please, try again')
        return()
    # checking the MM parameter
    mm = ssn[3:5]
    if df_france_mm['MM'].isin([mm]).any():
        bd_month = df_france_mm.at[df_france_mm.loc[df_france_mm['MM'] == mm].index[0], 'Month']
    elif 20 <= int(mm) <= 30:
        bd_month = 'Unknown (the person was registered on the basis of a civil status document not specifying the ' \
                   'month of birth)'
    elif 50 <= int(mm) <= 99:
        bd_month = 'Unknown (the person was registered on the basis of a civil status document not specifying the ' \
                   'month of birth)'
    else:
        print('The ID number is wrong. Please, try again')
        return()
    # checking the LLOOO parameter
    llooo = ssn.upper()[5:10]
    if df_france_com['COG'].isin([llooo]).any():
        reg = df_france_com.at[df_france_com.loc[df_france_com['COG'] == llooo].index[0], 'REG']
        ncc_reg = df_france_com.at[df_france_com.loc[df_france_com['COG'] == llooo].index[0], 'NCC_REG']
        nccenr_reg = df_france_com.at[
            df_france_com.loc[df_france_com['COG'] == llooo].index[0], 'NCCENR_REG']
        libelle_reg = df_france_com.at[
            df_france_com.loc[df_france_com['COG'] == llooo].index[0], 'LIBELLE_REG']
        dep = df_france_com.at[df_france_com.loc[df_france_com['COG'] == llooo].index[0], 'DEP']
        ncc_dep = df_france_com.at[df_france_com.loc[df_france_com['COG'] == llooo].index[0], 'NCC_DEP']
        nccenr_dep = df_france_com.at[
            df_france_com.loc[df_france_com['COG'] == llooo].index[0], 'NCCENR_DEP']
        libelle_dep = df_france_com.at[
            df_france_com.loc[df_france_com['COG'] == llooo].index[0], 'LIBELLE_DEP']
        ncc_com = df_france_com.at[df_france_com.loc[df_france_com['COG'] == llooo].index[0], 'NCC_COM']
        nccenr_com = df_france_com.at[
            df_france_com.loc[df_france_com['COG'] == llooo].index[0], 'NCCENR_COM']
        libelle_com = df_france_com.at[
            df_france_com.loc[df_france_com['COG'] == llooo].index[0], 'LIBELLE_COM']
    elif df_france_com_comer['COG'].isin([llooo]).any():
        ncc_com_comer = df_france_com_comer.at[
            df_france_com_comer.loc[df_france_com_comer['COG'] == llooo].index[0], 'NCC_COM_COMER']
        nccenr_com_comer = df_france_com_comer.at[
            df_france_com_comer.loc[df_france_com_comer['COG'] == llooo].index[0], 'NCCENR_COM_COMER']
        libelle_com_comer = df_france_com_comer.at[
            df_france_com_comer.loc[df_france_com_comer['COG'] == llooo].index[0], 'LIBELLE_COM_COMER']
        comer = df_france_com_comer.at[
            df_france_com_comer.loc[df_france_com_comer['COG'] == llooo].index[0], 'COMER']
        ncc_comer = df_france_com_comer.at[
            df_france_com_comer.loc[df_france_com_comer['COG'] == llooo].index[0], 'NCC_COMER']
        nccenr_comer = df_france_com_comer.at[
            df_france_com_comer.loc[df_france_com_comer['COG'] == llooo].index[0], 'NCCENR_COMER']
        libelle_comer = df_france_com_comer.at[
            df_france_com_comer.loc[df_france_com_comer['COG'] == llooo].index[0], 'LIBELLE_COMER']
    elif df_france_pays['COG'].isin([llooo]).any():
        libcog = df_france_pays.at[
            df_france_pays.loc[df_france_pays['COG'] == llooo].index[0], 'LIBCOG']
        libenr = df_france_pays.at[
            df_france_pays.loc[df_france_pays['COG'] == llooo].index[0], 'LIBENR']
        codeiso2 = df_france_pays.at[
            df_france_pays.loc[df_france_pays['COG'] == llooo].index[0], 'CODEISO2']
        codeiso3 = df_france_pays.at[
            df_france_pays.loc[df_france_pays['COG'] == llooo].index[0], 'CODEISO3']
    else:
        print('The ID number is wrong. Please, try again')
        return()
    # checking the KKK parameter
    kkk = ssn[10:12]
    mm_comment_2 = 'The person was registered on the basis of an incomplete civil status document'
    print('\nHere\'s what I got from that ID number:\nMonth of birth: ', bd_month, '\nYear of birth: ',
          bd_year, '\nSex: ', sex)
    if df_france_com['COG'].isin([llooo]).any():
        print('The region of origin: ', ncc_reg, '/', nccenr_reg, '/', libelle_reg, ' (', reg,
              ')\nThe department of origin: ', ncc_dep, '/', nccenr_dep, '/', libelle_dep, ' (', dep,
              ')\nThe commune of origin: ', ncc_com, '/', nccenr_com, '/', libelle_com)
    elif df_france_com_comer['COG'].isin([llooo]).any():
        print('The territory of origin: ', ncc_com_comer, '/', nccenr_com_comer, '/',
              libelle_com_comer, '\nThe commune of origin: ', ncc_comer, '/', nccenr_comer, '/',
              libelle_comer, ' (', comer, ')')
    elif df_france_pays['COG'].isin([llooo]).any():
        print('The country of origin: ', libcog, '/', libenr, ' (', codeiso2, '/', codeiso3, ')')
    print('Sequence number of person with the same date of birth: ', int(kkk), '\n')
    return()
