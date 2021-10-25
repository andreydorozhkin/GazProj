from collections import Counter
import view
import numpy as np
import math

def cost_gas(field):
    request=float(field.get())
    return request
    
def cost_natur_liquided_gas(field):
    request=float(field.get())
    return request

def city_need_energy(field):
    request=float(field.get())
    return request

def cost_cistern(field):
    request=float(field.get())
    return request

def volume_cistern(field):
    request=float(field.get())
    return request

def number_cistern(field):
    request=float(field.get())
    return request

def cost_tank(field):
    request=float(field.get())
    return request

def number_tank(field):
    request=float(field.get())
    return request

def cost_gasifiers(field):
    request=float(field.get())
    return request

def cost_laying_high(field):
    request=float(field.get())
    return request

def cost_laying_medium(field):
    request=float(field.get())
    return request

def cost_GRPSH(field):
    request=float(field.get())
    return request

def efficiency_GRPSH(field):
    request=float(field.get())
    return request

def cost_maintenance_GRPSH(field):
    request=float(field.get())
    return request

def cost_maintenance_gas_pipeline(field):
    request=float(field.get())
    return request

def cost_maintenance_gas_pipeline(field):
    request=float(field.get())
    return request

def gas_material(field):
    request=float(field.get())
    return request

def do_plot():
    t0=[0,5,10,15,20,25,30]
    l0=[9.48,1.73,0.8,0.532,0.423,0.374,0.35]
    l1=[12.69,2.7,1.48,1.12,0.98,0.912,0.87]
    l2=[38.57,10.55,7.05,5.99,5.54,5.31,5.19]
    if view.combo_exsample_gas_material.get()=="Сталь":
        x=t0
        y=l0
        try:
            [view.ax[x].clear() for x in range(1)]
            view.ax[0].plot(x,y, color="red",label="Q=100" )
            view.figure.legend(loc = "upper left")
            view.canvas.draw()
            view.message_ask(["Request!", "Нет ошибки, график отрисован?"]);
        except:
            view.message_error(["Error", "Где-то ошибка"])
    if view.combo_exsample_gas_material.get()=="1000":
        x=t0
        y=l1
        try:
            #[view.ax[x].clear() for x in range(1)]
            view.ax[0].plot(x,y,color="green",label="Q=1000")
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

# Эксплуатационные затраты на обслуживание ГРП
def Q_year(need_city):
    return need_city/12185.4

# Эксплуатационны затраты на ШГРП
def operating_cost_shgrp(K_shgrp):
    return K_shgrp/10

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

def coof_A(Pm):
    A=0.101325/Pm*162*(pow(3.14))
    return A

def diametr(A,p0,Q0,P_ud):
    material_steel=[0.022, 2, 5] 
    material_polyethylene=[0.0446, 1.75, 4.75]  #A,m1,m2
    if view.comboExample.get()=="Сталь":
        B=material_steel[0]
        m=material_steel[1]
        m1=material_steel[2]
    if view.comboExample.get()=="Полиэтилен":
        B=material_polyethylene[0]
        m=material_polyethylene[1]
        m1=material_polyethylene[2]
    else:
        pass
    dp=(A*B*p0*(Q0**m))/P_ud
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