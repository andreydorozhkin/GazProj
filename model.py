from collections import Counter
from tkinter.constants import N
import view
import numpy as np
import math
import sys
import os
import random


def field_getter(field):
    request=float(field)
    return request
    

def clear():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def do_plot(need_city, points):
    t0=[]
    t=1
    l0=points
    while t!=30:
        t0.append(t)
        t=t+1
    x=t0
    y=l0
    #print(x)
    #print(y)
    try:
        # [view.ax[x].clear() for x in range(1)]
        # view.figure.legend().remove()
        view.ax[0].plot(x,y,label="Q="+str(need_city/1000))
        view.figure.legend(loc = "upper left")
        view.canvas.draw()
        # view.message_ask(["Request!", "Нет ошибки, график отрисован?"]);
    except:
        pass
        # view.message_error(["Error", "Где-то ошибка"])


# Капитальные затраты на комплекс по сжижению газа
def capital_costs_ksg(Q, cost_liquid_gaz):
    costs = 2 * Q * cost_liquid_gaz
    return costs
# Эксплуатационные затраты на комплекс по сжижению газа
def operation_costs_ksg(K_ksg):
    N1 = 0.1*K_ksg
    N2 = 0.05 * K_ksg  
    N3 = 0.04 * K_ksg
    N4 = 0.1 * K_ksg
    N5 = 0.11*K_ksg
    N_ksg = N1 + N2 + N3 + N4 + N5
    return N_ksg


# капитальные вложения в систему газоснабжения объекта СПГ
def capital_costs_spg(K_ksg, K_cist, K_khsv, K_gazif): 
    costs = K_ksg+K_cist+K_khsv+K_gazif
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
    one_step=Y_tcl*N_spg
    two_step=Y_t0*(N_spg+K_shgrp-L_spg)
    three_step1=Y_tcl-Y_t0
    three_step2=((C_pg*Q_year*1380)/kpd)+N_shgrp
    three_step=three_step1*three_step2
    numerator=one_step-two_step-three_step
    four_step=(Y_tcl-Y_t0)
    ext_step=(4*t_cl)
    ext2_step=four_step/ext_step
    five_step=ext2_step+Y_t0
    denominator=K_ud*five_step
    #print(numerator)
    #print(denominator)
    distance=numerator/denominator
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
    K_mass=[80,100,150,200,250,300] 
    mass=[4864558, 5756494, 6110114, 7401794, 8427619, 10360698  ]
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

def critical():
    t0=1
    t_cl=30
    need_city=100000
    for i in range(4):
        need_city=need_city * (10**i)
        print("Need city: " + str(need_city))
        t0=1
        answer=[]
        while t0!=30:
            K_chsw = capital_costs_storage(field_getter(1), field_getter(4049849.86)) #view.number_tank   view.cost_tank  
            CityYear = Q_year(field_getter(need_city)) #view.city_need_energy    
            K_gazif = capital_costs_gazif(CityYear, power_gazif(), field_getter(2554200)) #  view.cost_gasifiers
            a = field_getter(18268.68711) # view.cost_natur_liquided_gas
            K_ksg = capital_costs_ksg(CityYear, a)
            K_cist = capital_costs_cist(field_getter(1), field_getter(27768000)) #  view.number_cistern   view.cost_cistern
            K_spg = capital_costs_spg(K_ksg, K_cist, K_chsw, K_gazif)  #  view.cost_tank
            Y_tcl = discount_rate(t_cl, 0.1)
            Y_t0 = discount_rate(t0, 0.1)
            N_spg = operating_costs_spg(exp_cost_cist(K_cist), operating_costs_storage(K_chsw), operating_costs_gazif(K_gazif), 
                                operation_costs_ksg(K_ksg), CityYear, a)
            K_shgrp = capital_cost_GRPSH(CityYear)
            L_spg = liquidation_value(K_ksg, K_cist, K_chsw, K_gazif, t0, t_cl, 40000)
            C_pg = field_getter(9.5)   #  view.cost_gas
            kpd = 0.9
            N_shgrp = operating_cost_shgrp(K_shgrp)  
            K_ud = finding_K(diametr(CityYear))
            # print("=================")
            # print("Tcl:" + str(t_cl))
            # print("t0:" + str(t0))
            # print("Q0: " + str(CityYear))
            # print("Kхсв: " + str(K_chsw))
            # print("Kгазиф: " + str(K_gazif))
            # print("a: " + str(a))
            # print("Kксг: " + str(K_ksg))
            # print("Kцист: " + str(K_cist))
            # print("Kспг: " + str(K_spg))
            # print("Y_cl: " + str(Y_tcl))
            # print("Y_t0: " + str(Y_t0))
            # print("Испг: " + str(N_spg))
            # print("Кшгрп: " + str(K_shgrp))
            # print("Лспг: " + str(L_spg))
            # print("Cпг: " + str(C_pg))
            # print("КПД: " + str(kpd))
            # print("Ишгрп: " + str(N_shgrp))
            # print("Куд: " + str(K_ud))
            # print("=================")
            answer.append(critical_distance(K_spg, Y_tcl, N_spg, Y_t0, K_shgrp, L_spg, C_pg, CityYear, kpd, N_shgrp, K_ud, t_cl))
            #view.message_info(["Request!", "Ответ: " + answer])
            t0+=1 
        do_plot(need_city, answer)
        need_city=need_city / (10**i)
    

