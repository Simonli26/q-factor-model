# q-factor-modeldef cal(df):
    #划分大小市值公司 Sorting the companies into big(B) and small(S) companyies groups according to the market equities(ME)
    df['SB'] = df['ME'].map(lambda x:'B' if x >= df['ME'].median() else 'S')
    #划分高中低ROE公司 Sorting the companies into roubust ROE(R), medium ROE(M) and weak ROE(W) according to the ROEs
    border_down, border_up = df['ROE'].quantile([0.3,0.7])
    border_down, border_up
    df['RMW'] = df['ROE'].map(lambda x:'R' if x >= border_up else 'M')
    df['RMW'] = df.apply(lambda row:'W' if row['ROE'] <= border_down else row['RMW'], axis=1)
    #划分高中低I/A公司 Sorting the companies into conservative(C) investment, neutral investment(N) and aggressive(A) investment according to investment/asset(I/A)
    bd_down,bd_up = df['I/A'].quantile([0.3,0.7])
    bd_down,bd_up
    df['CNA'] = df['I/A'].map(lambda x:'A' if x >= bd_up else 'N')
    df['CNA'] = df.apply(lambda row:'C' if row['I/A'] <= bd_down else row['CNA'], axis=1)
    #组合划分为18组 The formation of 18 portfolios
    df_SRC = df.query('(SB=="S")&(RMW=="R")&(CNA=="C")')
    df_SMC = df.query('(SB=="S")&(RMW=="M")&(CNA=="C")')
    df_SWC = df.query('(SB=="S")&(RMW=="W")&(CNA=="C")')
    df_BRC = df.query('(SB=="B")&(RMW=="R")&(CNA=="C")')
    df_BMC = df.query('(SB=="B")&(RMW=="M")&(CNA=="C")')
    df_BWC = df.query('(SB=="B")&(RMW=="W")&(CNA=="C")')
    df_SRN = df.query('(SB=="S")&(RMW=="R")&(CNA=="N")')
    df_SMN = df.query('(SB=="S")&(RMW=="M")&(CNA=="N")')
    df_SWN = df.query('(SB=="S")&(RMW=="W")&(CNA=="N")')
    df_BRN = df.query('(SB=="B")&(RMW=="R")&(CNA=="N")')
    df_BMN = df.query('(SB=="B")&(RMW=="M")&(CNA=="N")')
    df_BWN = df.query('(SB=="B")&(RMW=="W")&(CNA=="N")')
    df_SRA = df.query('(SB=="S")&(RMW=="R")&(CNA=="A")')
    df_SMA = df.query('(SB=="S")&(RMW=="M")&(CNA=="A")')
    df_SWA = df.query('(SB=="S")&(RMW=="W")&(CNA=="A")')
    df_BRA = df.query('(SB=="B")&(RMW=="R")&(CNA=="A")')
    df_BMA = df.query('(SB=="B")&(RMW=="M")&(CNA=="A")')
    df_BWA = df.query('(SB=="B")&(RMW=="W")&(CNA=="A")')
    #计算各组收益率 Calculating the returns of 18 portfolios
    R_SRC =(df_SRC['RETURN']*df_SRC['ME']).sum() / df_SRC['ME'].sum()
    R_SMC =(df_SMC['RETURN']*df_SMC['ME']).sum() / df_SMC['ME'].sum()
    R_SWC =(df_SWC['RETURN']*df_SWC['ME']).sum() / df_SWC['ME'].sum()
    R_BRC =(df_BRC['RETURN']*df_BRC['ME']).sum() / df_BRC['ME'].sum()
    R_BMC =(df_BMC['RETURN']*df_BMC['ME']).sum() / df_BMC['ME'].sum()
    R_BWC =(df_BWC['RETURN']*df_BWC['ME']).sum() / df_BWC['ME'].sum()
    R_SRN =(df_SRN['RETURN']*df_SRN['ME']).sum() / df_SRN['ME'].sum()
    R_SMN =(df_SMN['RETURN']*df_SMN['ME']).sum() / df_SMN['ME'].sum()
    R_SWN =(df_SWN['RETURN']*df_SWN['ME']).sum() / df_SWN['ME'].sum()
    R_BRN =(df_BRN['RETURN']*df_BRN['ME']).sum() / df_BRN['ME'].sum()
    R_BMN =(df_BMN['RETURN']*df_BMN['ME']).sum() / df_BMN['ME'].sum()
    R_BWN =(df_BWN['RETURN']*df_BWN['ME']).sum() / df_BWN['ME'].sum()
    R_SRA =(df_SRA['RETURN']*df_SRA['ME']).sum() / df_SRA['ME'].sum()
    R_SMA =(df_SMA['RETURN']*df_SMA['ME']).sum() / df_SMA['ME'].sum()
    R_SWA =(df_SWA['RETURN']*df_SWA['ME']).sum() / df_SWA['ME'].sum()
    R_BRA =(df_BRA['RETURN']*df_BRA['ME']).sum() / df_BRA['ME'].sum()
    R_BMA =(df_BMA['RETURN']*df_BMA['ME']).sum() / df_BMA['ME'].sum()
    R_BWA =(df_BWA['RETURN']*df_BWA['ME']).sum() / df_BWA['ME'].sum()
    #计算 SIZE,PROFIT,INVESTMENT Calculating the returns on SIZE factor, PROFIT factor and INVESTMENT factor
    size = (R_SRC + R_SMC + R_SWC + R_SRN + R_SMN + R_SWN + R_SRA + R_SMA + R_SWA - R_BRC - R_BMC - R_BWC - R_BRN - R_BMN - R_BWN - R_BRA - R_BMA - R_BWA) / 9
    profit = (R_SRC + R_BRC + R_SRN + R_BRN + R_SRA + R_BRA - R_BWC - R_BWN - R_BWA - R_SWN - R_SWA - R_SWC) / 6
    investment = (R_SRC + R_BRC + R_SMC + R_BMC + R_SWC + R_BWC - R_BWA - R_BRA - R_SRA - R_BMA - R_SMA - R_SWA) / 6

    size, profit, investment,R_SRC,R_SMC,R_SWC,R_BRC,R_BMC,R_BWC,R_SRN,R_SMN,R_SWN,R_BRN,R_BMN,R_BWN,R_SRA,R_SMA,R_SWA,R_BRA,R_BMA,R_BWA
    #制作表格 Listing the returns of 3 factors and 18 portfolios in a form
    Q_data = pd.DataFrame(index = [], columns = ['SIZE','PROFIT','INV','R_SRC','R_SMC','R_SWC','R_BRC','R_BMC','R_BWC','R_SRN','R_SMN','R_SWN','R_BRN','R_BMN','R_BWN','R_SRA','R_SMA','R_SWA','R_BRA','R_BMA','R_BWA'])

    cal_date = 200305

    Q_data.at[cal_date,'SIZE'] = size
    Q_data.at[cal_date,'PROFIT'] = profit
    Q_data.at[cal_date,'INV'] = investment
    Q_data.at[cal_date,'R_SRC'] = R_SRC
    Q_data.at[cal_date,'R_SMC'] = R_SMC
    Q_data.at[cal_date,'R_SWC'] = R_SWC
    Q_data.at[cal_date,'R_BRC'] = R_BRC
    Q_data.at[cal_date,'R_BMC'] = R_BMC
    Q_data.at[cal_date,'R_BWC'] = R_BWC
    Q_data.at[cal_date,'R_SRN'] = R_SRN
    Q_data.at[cal_date,'R_SMN'] = R_SMN
    Q_data.at[cal_date,'R_SWN'] = R_SWN
    Q_data.at[cal_date,'R_BRN'] = R_BRN
    Q_data.at[cal_date,'R_BMN'] = R_BMN
    Q_data.at[cal_date,'R_BWN'] = R_BWN
    Q_data.at[cal_date,'R_SRA'] = R_SRA
    Q_data.at[cal_date,'R_SMA'] = R_SMA
    Q_data.at[cal_date,'R_SWA'] = R_SWA
    Q_data.at[cal_date,'R_BRA'] = R_BRA
    Q_data.at[cal_date,'R_BMA'] = R_BMA
    Q_data.at[cal_date,'R_BWA'] = R_BWA



    return Q_data



cal(df).to_csv('Q_factor_model.csv')
print(cal(df).head())
