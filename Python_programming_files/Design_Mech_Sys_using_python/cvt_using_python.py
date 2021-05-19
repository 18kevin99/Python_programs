from tkinter import *
from tkinter import messagebox 
import math
import sys

root = Tk()
root.title("Design of CVT")


def axial_disp(rp, rp_min, alpha = 11 ):
    a_d = 2 * (rp - rp_min) * math.tan(math.radians(alpha))
    return a_d

def belt_lgt(l1 , l2):
    m = max (l1, l2)
    
    if (m < 813):
        m = 813
    elif(m > 813 and m < 890):
        m = 890
    elif(m > 890):
        m = 914
    
    return m

def acc(t_r, e_p, max_rpm, s_r):
    
    t_whl = t_r * s_r * 2

    F = t_whl * 2 / float(tyre_dia.get())
    a = F / int(grss_wt.get())

    return a  

def take_inp():
    
    vm = float(float(max_speed.get()) * (5/18))
    N = float(vm *60 / (math.pi * float(tyre_dia.get())))
    
    speed_red = round(float(max_rpm.get()) / N)
    cvt_red = round(float(max_rpm.get()) / (speed_red * N), ndigits= 3)

    air_res = .5 * 1.22 * float(frt_area.get()) * (vm ** 2)

    roll_res = .05 * int(grss_wt.get()) * 9.81

    t_rated = (float(eng_pow.get()) * 1000 * 60 )/(2 * math.pi * int(max_rpm.get()))     
    acc_res = float(acc(t_rated, float(eng_pow.get()), int(max_rpm.get()), speed_red) * int(grss_wt.get()) / 9.81)
    
    total_res = air_res + roll_res + acc_res
    #print (total_res)

    torque_req = total_res * (float(tyre_dia.get())/2)
    #print(torque_req)

    gr_rto = torque_req / (speed_red * t_rated)

    d1l = 155
    d1s = 45

    d2l = (gr_rto * (d1s + 14)) + 14
    d2s = (cvt_red * (d1l - 14)) - 14

    d1s_pt_dia = round(d1s + 14, ndigits= 2)
    d1l_pt_dia = round(d1l - 14, ndigits= 2)
    d2l_pt_dia = round(d2s + 14, ndigits= 2)
    d2s_pt_dia = round(d2l - 14, ndigits= 2)

    ctc_dst = 215
    l1 = (2 * ctc_dst) + ((math.pi / 2) * (d1s + d2l)) + (((d1l - d2s) ** 2)/(4 * ctc_dst))
    l2 = (2 * ctc_dst) + ((math.pi / 2) * (d2s + d1l)) + (((d2l - d1s) ** 2)/(4 * ctc_dst))

    blt_length = belt_lgt(l1, l2)
    #print(blt_length)

    a_d_prim = axial_disp((d1l/2), (d1s/2))
    print(a_d_prim)
    a_d_sec = axial_disp((d2l/2), (d2s/2))

    s_yt = 570
    K = 1.184
    P = 400
    c = 8
    wire_dia = round(((K * 8 * P * c )/(math.pi * s_yt))** 0.5)
    mean_coil_dia = c * wire_dia

    deflc = round(a_d_prim)
    G = 81370
    act_coil = round(deflc * G * (wire_dia**4)/ (8 * P * (mean_coil_dia**3)))

    tot_coil = act_coil + 2

    act_defl = (8 * P * (mean_coil_dia**3) * tot_coil / (G * (wire_dia**4)))
    
    s_l = tot_coil * wire_dia
    t_gap = (tot_coil-1) * 1.25
    fr_lgt = round(s_l + t_gap + act_defl, ndigits= 2)
    
    top = Toplevel()
    top.title("Second Window")
    Lbl1 = Label(top, text = "The gear ratio of the gearbox is {}". format(speed_red)).pack()
    Lbl2 = Label(top, text = "The cvt reduction  {}". format(cvt_red)).pack()
    Lbl3 = Label(top, text = "Larger dia of secondary pulley {}". format(d2l_pt_dia)).pack()
    Lbl4 = Label(top, text = "Smaller dia of secondary pulley {}". format(d2s_pt_dia)).pack()
    Lbl5 = Label(top, text = "Larger dia of primary pulley {}". format(d1l)).pack()
    Lbl6 = Label(top, text = "Smaller dia of primary pulley {}". format(d1s)).pack()
    Lbl7 = Label(top, text = "Belt Length {}". format(blt_length)).pack()
    Lbl8 = Label(top, text = "Wire diameter of spring {}". format(wire_dia)).pack()
    Lbl9 = Label(top, text = "Mean Coil Diameter {}". format(mean_coil_dia)).pack()
    Lbl10 = Label(top, text = "Total No of Coils {}". format(tot_coil)).pack()
    Lbl11 = Label(top, text = "Solid Length {}". format(s_l)).pack()
    Lbl12 = Label(top, text = "Free length of spring {}". format(fr_lgt)).pack()
    


frame = LabelFrame(root, text ="Inputs", padx = 5, pady = 5)
frame.pack(padx = 10, pady = 10)

eng_pow = Entry(frame, width = 20, borderwidth = 5)
eng_pow.grid(row = 0, column = 1)
frt_area = Entry(frame, width = 20, borderwidth = 5)
frt_area.grid(row = 1, column = 1)
grss_wt = Entry(frame, width = 20, borderwidth = 5)
grss_wt.grid(row = 2, column = 1)
max_rpm = Entry(frame, width = 20, borderwidth = 5)
max_rpm.grid(row = 3, column = 1)
min_rpm = Entry(frame, width= 20, borderwidth=5)
min_rpm.grid(row = 4, column = 1)
max_speed = Entry(frame, width= 20, borderwidth=5)
max_speed.grid(row = 5, column = 1)
tyre_dia = Entry(frame, width= 20, borderwidth=5)
tyre_dia.grid(row = 6, column = 1)



lbl1= Label(frame, text = "Engine power").grid(row=0, column=0)
lbl2= Label(frame, text = "Frontal Area").grid(row=1, column=0)
lbl3= Label(frame, text = "Gross weight").grid(row=2, column=0)
lbl4= Label(frame, text = "max rpm").grid(row=3, column=0)
lbl5= Label(frame, text = "min rpm").grid(row=4, column=0)
lbl6= Label(frame, text = "max speed").grid(row=5, column=0)
lbl5= Label(frame, text = "tyre dia").grid(row=6, column=0)

Btn1 = Button(frame, text = "Submit", padx = 10, pady= 10, command = take_inp).grid(row = 7, column = 0, columnspan = 2)

root.mainloop()