# coding: utf-8

import sys
    
# 等额本息(按月还)
def print_interest(principal, years, years_rate, type):
    # 总期数
    total_m = years*12
    # 每期利息
    per_rate = years_rate/12
    # 剩余未归还本金
    real_principal = principal
    if type == 1:
        print('===========  等额本金  ============')
    else:
        print('===========  等额本息  ============')
    print('贷款本金:' + str(principal) + ' 元')
    print('贷款年数:' + str(years) + ' 年')
    print('贷款年利率:' + str(years_rate) + '%')
    print('还款总期数:' + str(total_m))
    # 计算每期还款情况
    print('===========  还款详细  ============')

    # 每期还款额
    per_principal = 0
    payments = 0
    if type == 1:
        per_principal = principal/total_m
    else:
        payments = principal*per_rate*pow(1 + per_rate, total_m)/(pow(1 + per_rate, total_m) - 1)
    # 利息总计
    all_interest = 0
    for i in range(1,total_m + 1):
        # 第y年
        m = (i+11)%12 + 1
        if m == 1:
            y = int((i+11)/12)
            print('------------  第' + str(y) + '年  ------------')
            print('期数\t年月\t月供本金\t月供利息\t月供\t\t剩余本金')
        # 当月利息
        per_interest = real_principal*per_rate
        all_interest += per_interest
        # 剩余未归还本金
        real_principal -= per_principal
        # 当月还款额
        if type == 1:
            payments = per_principal + per_interest
            print(str(i) + '\t' + str(m) + '\t' + str(round(per_principal, 2)) + '\t\t' + str(round(per_interest, 2)) + '\t\t- ' + str(round(payments, 2)) + ' -\t' + str(round(real_principal, 2)))
        else:
            per_principal = payments - per_interest
            print(str(i) + '\t' + str(m) + '\t- ' + str(round(per_principal, 2)) + ' -\t\t' + str(round(per_interest, 2)) + '\t\t' + str(round(payments, 2)) + '\t' + str(round(real_principal, 2)))
    
    print('')
    if type == 1:
        print('===========  等额本金  ============')
    else:
        print('===========  等额本息 ============')
    print('贷款本金:' + str(principal) + ' 元')
    print('贷款年数:' + str(years) + ' 年')
    print('贷款年利率:' + str(years_rate*100) + '%')
    print('还款总期数:' + str(total_m))
    print('每期还款额:' + str(round(payments, 2)) + ' 元')
    print('利息总计:' + str(round(all_interest, 2)))
    print('====================================')

def get_inputs():
    print('请按照顺序输入所有的参数, 以空格间隔!')
    print('贷款本金(万),贷款年数,贷款年利率(%),贷款类型(0:等额本息 1:等额本金).')
    return input('请输入: ')

if __name__ == '__main__':
    args = sys.argv
    star_index = 1
    if len(args) < 3:
        input_str = get_inputs()
        args = input_str.split(' ')
        star_index = 0
    
    principal = float(args[star_index])*10000
    years = int(args[star_index + 1])
    years_rates = float(args[star_index + 2])/100
    type = 0
    if len(args) > (star_index + 3):
        type = int(args[star_index + 3])
    print_interest(principal, years, years_rates, type)
        
    
    