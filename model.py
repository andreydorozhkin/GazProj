from collections import Counter
import view
import numpy as np
import math
import sys
import os
import random

def field_getter(field): #Я добавил автозаполнение чтобы не париться, но вообще нужны цельные данные
    request=float(field)
    return request
    

def clear():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def do_plot():
    t0=[0,5,10,15,20,25,30]
    l0=[9.48,1.73,0.8,0.532,0.423,0.374,0.35]
    l1=[12.69,2.7,1.48,1.12,0.98,0.912,0.87]
    l2=[38.57,10.55,7.05,5.99,5.54,5.31,5.19]
    if view.combo_exsample_gas_material.get()=="Сталь":
        x=t0
        y=l0
        try:
            #[view.ax[x].clear() for x in range(1)]
            view.figure.legend().remove()
            view.ax[0].plot(x,y, color="red",label="Q=100" )
            view.figure.legend(loc = "upper left")
            view.canvas.draw()
            view.message_ask(["Request!", "Нет ошибки, график отрисован?"]);
        except:
            view.message_error(["Error", "Где-то ошибка"])
    if view.combo_exsample_gas_material.get()=="Полиэтилен":
        x=t0
        y=l2
        try:
            #[view.ax[x].clear() for x in range(1)]
            view.ax[0].plot(x,y,color="blue",label="Q=1000")
            view.figure.legend(loc = "upper left")
            view.canvas.draw()
            view.message_ask(["Request!", "Нет ошибки, график отрисован?"]);
        except:
            view.message_error(["Error", "Где-то ошибка"])


# Капитальные затраты на комплекс по сжижению газа
def capital_costs_ksg(Q, cost_liquid_gaz):
    costs = 2 * Q * cost_liquid_gaz
    return costs

# капитальные вложения в систему газоснабжения объекта СПГ
def capital_costs_spg(K_ksg, K_cist, K_khsv, K_gazif, K_tank): 
    costs = K_ksg+K_cist+K_khsv+K_gazif+K_tank
    return costs

# Капитальные затраты на цистерны
def capital_costs_cist(number, cost):
    return number*cost

# Эксплуатационные затраты на обслуживание ГРП
def Q_year(need_city):
    q = need_city/12185.4
    return q

# Эксплуатационны затраты на ШГРП
def operating_cost_shgrp(K_shgrp):
    return K_shgrp/10
#Капитальные затраты на газораспределительные шкафы
def capital_cost_GRPSH(Q):
    cap_GRPSH=(19.35906314*Q*1380)/1800  #Q_y-Это список
    return cap_GRPSH

# Мощность газификатора
def power_gazif():
    return 200/1380

# Капитальные затраты на газификатор
def capital_costs_gazif(Q_year, power_gazif, cost_gazif):
    capital=math.ceil(Q_year/power_gazif/365/24)
    capital*=cost_gazif
    return capital

# Эксплуатационные затраты на газификатор
def operating_costs_gazif(capital_costs):
    return capital_costs / 100

# Капитальные затраты на хранилища
def capital_costs_storage(num_storage, cost_storage):
    return num_storage * cost_storage

# Эксплуатационные затраты на хранилища
def operating_costs_storage(K_chsw):
    return K_chsw*0.5/100

#Экспулатауционные затраты на цистерны  #Новый пункт
def exp_cost_cist(number_cist):
    exp=(number_cist/100)*5
    return exp

# Эксплутационные расходы по доставке СПГ
def operating_costs_spg(N_cist, N_schw, N_gazif, N_ksg, Q_year, a):
    numerator = Q_year * a/0.9
    costs = numerator + N_cist + N_ksg  + N_schw + N_gazif
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
def critical_distance(K_spg, Y_tcl,  N_spg, Y_t0, K_shgrp, L_spg, C_pg, Q_year, kpd, N_shgrp, K_ud, t_cl):
    one_mltpr = Y_tcl * N_spg
    two_mltpr = Y_t0*(N_spg+K_shgrp-L_spg)
    three_mltpr_1 = Y_tcl-Y_t0
    three_mltpr_2 = (C_pg*Q_year)/kpd+N_shgrp
    three_mltpr = three_mltpr_1*three_mltpr_2
    numerator = K_spg+one_mltpr-two_mltpr-three_mltpr
    denominator_2 = Y_t0+(Y_tcl-Y_t0)/(4*t_cl)
    denominator = K_ud*denominator_2
    distance = numerator/denominator
    return distance


def diametr(Q0):
    P_ud = 0.25/(1.1*field_getter(10)*1000) #view.factory_distance
    p0 = 0.101325
    A=0.101325/0.6*162*(pow(3.14,2))
    material_steel=[0.022, 2, 5] 
    material_polyethylene=[0.0446, 1.75, 4.75]  #A,m1,m2
    B=material_steel[0]
    m=material_steel[1]
    m1=material_steel[2]
    dp=(A*B*p0*(pow(Q0,m)))/P_ud
    x=dp
    y=m1
    dp=pow(x,(1/y))
    return dp


#Нахождение К-удельное
def finding_K(dp):
    K_mass=[80,100,150,200,250,300] #Список удельных К
    mass=[4864.558, 5756.494, 6110.114, 7401.794, 8427.619, 10360.698  ]
    array_difference=[]
    K_ud=float()
    for i in K_mass:
        if i>=dp:
            array_difference=array_difference+[i-dp]
        if i<=dp:
            array_difference=array_difference+[dp-i]
    mylist = array_difference
    doubles=[k for k,v in Counter(mylist).items() if v>1]
    if len(doubles)==1:
        smallest_number = min(array_difference)
        ind=array_difference.index(smallest_number)
        K_ud=K_mass[ind+1]
        money=mass[ind+1]
        return money
    smallest_number = min(array_difference)
    ind=array_difference.index(smallest_number)
    K_ud=K_mass[ind]
    money=mass[ind]
    return money   

# def critical():
#     answer = str((field_getter(view.cost_natur_liquided_gas)))
#     view.message_info(["Request!", "Ответ: " + answer])


def critical():
    t_cl=30
    t0=1
    CityYear = Q_year(field_getter(100000)) #view.city_need_energy    
    K_chsw = capital_costs_storage(field_getter(1), field_getter(4049849.86)) #view.number_tank   view.cost_tank  
    K_gazif = capital_costs_gazif(CityYear, power_gazif(), field_getter(2554200)) #  view.cost_gasifiers
    a = field_getter(18268.68711) # view.cost_natur_liquided_gas
    K_ksg = capital_costs_ksg(CityYear, a)
    K_cist = capital_costs_cist(field_getter(1), field_getter(27768000)) #  view.number_cistern   view.cost_cistern
    K_spg = capital_costs_spg(K_ksg, K_cist, K_chsw, field_getter(409849.86),   #  view.cost_tank
                              K_gazif)
    Y_tcl = discount_rate(t_cl, 0.1)
    Y_t0 = discount_rate(t0, 0.1)
    N_spg = operating_costs_spg(exp_cost_cist(K_cist), operating_costs_storage(K_chsw), operating_costs_gazif(K_gazif), 
                                capital_costs_ksg(CityYear, a), CityYear, a)
    K_shgrp = capital_cost_GRPSH(CityYear)
    L_spg = liquidation_value(K_ksg, K_cist, K_chsw, K_gazif, 1, t_cl, 40000)
    C_pg = field_getter(9.5)   #  view.cost_gas
    kpd = 0.9
    N_shgrp = operating_cost_shgrp(K_shgrp)  
    K_ud = finding_K(diametr(CityYear))
    answer = str(critical_distance(K_spg, Y_tcl, N_spg, Y_t0, K_shgrp, L_spg, C_pg, CityYear, kpd, N_shgrp, K_ud, t_cl))
    print("t_cl:" + str(t_cl))
    print("t0:" + str(t0))
    print("Q0: " + str(CityYear))
    print("K_chsw: " + str(K_chsw))
    print("K_gazif: " + str(K_gazif))
    print("a: " + str(a))
    print("K_ksg: " + str(K_ksg))
    print("K_cist: " + str(K_cist))
    print("K_spg: " + str(K_spg))
    print("Y_cl: " + str(Y_tcl))
    print("Y_t0: " + str(Y_t0))
    print("N_spg: " + str(N_spg))
    print("K_shgrp: " + str(K_shgrp))
    print("L_spg: " + str(L_spg))
    print("C_pg: " + str(C_pg))
    print("kpd: " + str(kpd))
    print("N_shgrp: " + str(N_shgrp))
    print("K_ud: " + str(K_ud))
    view.message_info(["Request!", "Ответ: " + answer]) 

