# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 23:56:34 2020

@author: lisiz
"""
import pandas as pd
import statsmodels.api as sm

df = pd.read_excel(r"C:\Users\lisiz\OneDrive\Q factor model\DATA.xlsx",sheet_name ='REGRESSION')
stock_names = {'R_SRC','R_SMC','R_SWC','R_BRC','R_BMC','R_BWC',
               'R_SRN','R_SMN','R_SWN','R_BRN','R_BMN','R_BWN',
               'R_SRA','R_SMA','R_SWA','R_BRA','R_BMA','R_BWA'} 
param=pd.DataFrame()
for a in ['R_SRC','R_SMC','R_SWC','R_BRC','R_BMC','R_BWC','R_SRN','R_SMN','R_SWN','R_BRN','R_BMN','R_BWN','R_SRA','R_SMA','R_SWA','R_BRA','R_BMA','R_BWA']: 
    model = sm.OLS(df[a], sm.add_constant( df[['SIZE', 'PROFIT', 'INV','RmRf']].values)) 
    result = model.fit(cov_type='HAC',cov_kwds={'maxlags':1})
    param[a]=result.params
    print(a + '\n') 
    print(result.summary())
   
param.index=['Alpha','SIZE FACTOR','PROFIT FACTOR','INV FACTOR','RmRf FACTOR'] 
print(param)