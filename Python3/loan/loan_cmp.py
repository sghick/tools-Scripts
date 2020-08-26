# coding: utf-8

import sys

# 等额本息:还款金固定,本金增多
def equality_interest(principal, total, rate): 
    rtn = list()
    # 剩余未归还本金
    real_principal = principal
    # 还款金
    payments = principal*rate*pow(1 + rate, total)/(pow(1 + rate, total) - 1)
    # 利息总计
    all_interest = 0
    for i in range(1, total + 1):
        # 当期利息
        per_interest = real_principal*rate
        all_interest += per_interest
        # 本金
        per_principal = payments - per_interest
        rtn.append(per_principal)
        # 剩余未归还本金
        real_principal -= per_principal
    return payments, all_interest, rtn

# 等额本金:本金固定,还款金减少
def equality_corpus(principal, total, rate): 
    rtn = list()
    # 剩余未归还本金
    real_principal = principal
    # 本金
    per_principal = principal/total
    # 利息总计
    all_interest = 0
    for i in range(1, total + 1):
        # 当期利息
        per_interest = real_principal*rate
        all_interest += per_interest
        # 当期还款金
        payments = per_principal + per_interest
        rtn.append(payments)
        # 剩余未归还本金
        real_principal -= per_principal
    return per_principal, all_interest, rtn


def print_compare_by_rates_for_interest(principal, years, years_rates):
    # 总期数
    total = years*12
    print('===========  等额本息  ============')
    print('贷款本金:' + str(principal) + ' 元')
    print('贷款年数:' + str(years) + ' 年')
    print('还款总期数:' + str(total))
    print('')
    details = list()
    all_interests = list()
    all_payments = list()
    pthead = '期数\t年月'
    for i in range(0, len(years_rates)):
        per_rate = years_rates[i]/12
        payments, all_interest, per_principals = equality_interest(principal, total, per_rate)
        all_payments.append(payments)
        all_interests.append(all_interest)
        details.append(per_principals)
        pthead = pthead + '\t' + str(round(years_rates[i]*100, 3)) + '%' + '\t'
    print('===========  月供含本金详情  ============')
    for i in range(1, total + 1):
        # 第y年
        m = (i+11)%12 + 1
        if m == 1:
            y = int((i+11)/12)
            print('')
            print('------------  第' + str(y) + '年  ------------')
            print(pthead)
            print('')
        ptstr = str(i) + '\t' + str(m)
        for j in range(0, len(details)):
            ptstr = ptstr + '\t' + str(round(details[j][i-1], 2)) + '\t'
        print(ptstr)

    print('----------------------------------')
    ptpayments = '月供\t'
    for j in range(0, len(details)):
        ptpayments = ptpayments + '\t' + str(round(all_payments[j], 2)) + '\t'
    print(ptpayments)

    ptinst = '利息总计'
    for j in range(0, len(details)):
        ptinst = ptinst + '\t' + str(round(all_interests[j], 2))
    print(ptinst)


def print_compare_by_rates_for_corpus(principal, years, years_rates):
     # 总期数
    total = years*12
    print('===========  等额本金  ============')
    print('贷款本金:' + str(principal) + ' 元')
    print('贷款年数:' + str(years) + ' 年')
    print('还款总期数:' + str(total))
    print('')
    details = list()
    all_interests = list()
    per_principals = list()
    pthead = '期数\t年月'
    for i in range(0, len(years_rates)):
        per_rate = years_rates[i]/12
        per_principal, all_interest, payments = equality_corpus(principal, total, per_rate)
        per_principals.append(per_principal)
        all_interests.append(all_interest)
        details.append(payments)
        pthead = pthead + '\t' + str(round(years_rates[i]*100, 3)) + '%' + '\t'
    print('===========  月供详情  ============')
    for i in range(1, total + 1):
        # 第y年
        m = (i+11)%12 + 1
        if m == 1:
            y = int((i+11)/12)
            print('')
            print('------------  第' + str(y) + '年  ------------')
            print(pthead)
            print('')
        ptstr = str(i) + '\t' + str(m)
        for j in range(0, len(details)):
            ptstr = ptstr + '\t' + str(round(details[j][i-1], 2)) + '\t'
        print(ptstr)

    print('----------------------------------')
    ptprinc = '月供本金'
    for j in range(0, len(details)):
        ptprinc = ptprinc + '\t' + str(round(per_principals[j], 2)) + '\t'
    print(ptprinc)

    ptinst = '利息总计'
    for j in range(0, len(details)):
        ptinst = ptinst + '\t' + str(round(all_interests[j], 2))
    print(ptinst)
        

def get_inputs():
    print('请按照顺序输入所有的参数, 以空格间隔!')
    print('贷款本金(万),贷款年数,贷款年利率(多个利率以\',\'间隔),贷款类型(0:等额本息 1:等额本金).')
    return input('请输入: ')

if __name__ == '__main__':
    args = sys.argv
    star_index = 1
    if len(args) < 3:
        input_str = get_inputs()
        args = input_str.split(' ')
        star_index = 0
        if len(args) < 3:
            exit
    
    principal = float(args[star_index])*10000
    years = int(args[star_index + 1])
    years_rates_str = args[star_index + 2].split(',')
    years_rates = list()
    for i in range(0, len(years_rates_str)):
        years_rates.append(float(years_rates_str[i])/100)
    load_type = 0
    if len(args) > (star_index + 3):
        load_type = int(args[star_index + 3])
    if load_type == 1:
        print_compare_by_rates_for_corpus(principal, years, years_rates)
    else:
        print_compare_by_rates_for_interest(principal, years, years_rates)
        
        
    
    