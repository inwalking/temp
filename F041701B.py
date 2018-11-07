# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 16:56:53 2017

@author: Administrator
"""

"""
总资产周转率A = 营业收入／资产总额期末余额；当分母未公布或为零或小于零时、分子小于零时以NULL表示；
F041701B	[总资产周转率A] = B001101000	[营业收入] ／ A001000000	[资产总计]
Note:
	
"""

import pandas as pd
import indicators.common.calVar as fn
import indicators.common.subtract as ac
import indicators.common.filter as fa

column_dict= { 'B001101000' :'A1', 'A001000000':'A2'}
indicator = 'F041701B'
def calVal(dataf, accper_list):
    # 计算指标所需的科目
    dataf = ac.col(dataf, column_dict)
    # 赋空
    dataf = ac.null_value(dataf,['A1'],type_null='Negative')
    dataf = ac.null_value(dataf, ['A2'], type_null='Non_Positive')
    #计算
    # indicator_series = fn.get_A1_A1(dataf, indicator,type_null='Non_Positive')
    indicator_series = fn.get_A1_out_A2(dataf, indicator)
    #过滤
    indicator_series = fa.accper_filter(indicator_series, accper_list)
    return indicator_series







def main():
    calVal(dataf, accper_list)

if __name__ == "__main__":
    # dataf = pd.read_csv('F:/GIT_base/data/FS_11to16.csv')
    dataf = pd.read_csv('D:/830800_2017.csv')
    dataf.set_index(['Stkcd', 'Accper'], inplace=True)
    accper_list = ['2015-12-31', '2016-12-31', '2017-12-31']
    main()