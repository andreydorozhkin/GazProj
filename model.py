from numpy.lib.financial import rate
import view
import numpy as np
def sum():
    try:
        num1=int(view.initial_enegry_consum.get())
        num2=int(view.unit_cost_liquefaction_complex.get())
        box_result=str(num1+num2)
        print(box_result)
        view.message_info(["Result","Результат в консоли = "+box_result])    
    except:
        view.message_error(["Error", "AMOGUS, кто то ввел не число"])
       

def do_plot():
    x=[0,28,30]
    y=[200,135,0]
    try:
        [view.ax[x].clear() for x in range(1)]
        view.ax[0].plot(x,y)
        view.canvas.draw()
        view.message_ask(["Request!", "Нет ошибки, график отрисован?"]);
    except:
        view.message_error(["Error", "Где-то ошибка"])

# Эксплутационные расходы по доставке СПГ
def operating_costs_spg(N_cist, N_chw, N_gazif, N_ksg, Q_year, a):
    numerator = Q_year * a/0.9
    costs = numerator + N_ksg + N_cist + N_chw + N_gazif
    return costs

# Коэффциент дисконтирования (вместо t_cl может прийти t0)
def discount_rate(t_cl, E):
    numerator=(1+E)**t_cl-1
    denominator=((1+E)**t_cl)*E
    rate = numerator/denominator
    return rate

# Остаточная ликвидационная стоиомость
def liquidation_value(K_ksg, K_cist, K_khsv, K_gazif, t0, t_cl, K_hswd):
    one_mltpr = (t_cl-t0)/t_cl*(K_ksg+K_cist+K_gazif+K_khsv-K_hswd)
    return one_mltpr

# Расчет критического радиуса
def critical_distance(Y_tcl,  N_spg, Y_t0, K_shgrp, L_spg, C_pg, Q_year, kpd, N_shgrp, K_ud, t_cl):
    one_mltpr = Y_tcl * N_spg
    two_mltpr = Y_t0*(N_spg+K_shgrp-L_spg)
    three_mltpr_1 = Y_tcl-Y_t0
    three_mltpr_2 = (C_pg*Q_year)/kpd+N_shgrp
    three_mltpr = three_mltpr_1*three_mltpr_2
    numerator = one_mltpr-two_mltpr-three_mltpr
    denominator_2 = Y_t0+(Y_tcl-Y_t0)/(4*t_cl)
    denominator = K_ud*denominator_2
    distance = numerator/denominator
    return distance
    
