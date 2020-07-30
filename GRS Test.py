# -*- coding: utf-8 -*-
"""
Created on Mon May  4 17:46:34 2020

@author: lisiz
"""

"""
Function GRS_test(factor, resid, alpha) is to conduct GRS test according
to Gibbons, Ross & Shanken(1989) to receive GRS-statistic and p-value.

H0: alpha1=alpha2=...=alphaN

Parameters:
  T = number of months
  N = number of portfolios
  L = number of factors

Inputs:
  factor: matrix of FF factors with shape (T, L)
  resid: matrix of residuals with shape (T, N)
  alpha: matrix of intercepts with shape (N, 1)

Outputs:
  f_grs: GRS-statistic
  p_grs: P-value

"""
import numpy as np
import pandas as pd
import scipy.stats as stats
resid= pd.read_excel(r"C:\Users\lisiz\OneDrive\Q factor model\GRS.xlsx",sheet_name ='residual3')
factor= pd.read_excel(r"C:\Users\lisiz\OneDrive\Q factor model\GRS.xlsx",sheet_name ='factor')
alpha= pd.read_excel(r"C:\Users\lisiz\OneDrive\Q factor model\GRS.xlsx",sheet_name ='alpha3')
N = resid.shape[1]
T = resid.shape[0]
L = factor.shape[1]
def GRS_test(factor, resid, alpha):
    N = resid.shape[1]
    T = resid.shape[0]
    L = factor.shape[1]

    if (T-N-L) < 0:
        print('can not conduct GRS test because T-N-L<0')
        print(N)
        print(T)
        print(L)
        return

    factor = np.asmatrix(factor)                   # factor matrix (T, L)
    resid = np.asmatrix(resid)                     # residual matrix (T, N)
    alpha = np.asmatrix(alpha).reshape(N, 1)       # intercept matrix (N, 1)

    mean_return_factor = (factor.mean(axis=0))

    # covariance matrix of residuals
    cov_resid = (resid.T * resid) / (T-L-1)
    # covariance matrix of factors
    cov_factor = ((factor - mean_return_factor).T * (factor - mean_return_factor)) / (T-1)

    mean_return_factor = mean_return_factor.reshape(L, 1)

    # GRS statistic
    f_grs = float((T/N) * ((T-N-L)/(T-L-1)) * ((alpha.T * np.linalg.inv(cov_resid) * alpha) / (1 + mean_return_factor.T * np.linalg.inv(cov_factor) * mean_return_factor)))

    # p-value
    p_grs = 1 - stats.f.cdf(f_grs, N, (T-N-L))

    return f_grs, p_grs

print(GRS_test(factor, resid, alpha))
