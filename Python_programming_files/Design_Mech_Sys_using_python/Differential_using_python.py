"""

This program is solely designed to give the gear calculations of the diff. gears and not the crown 
and propeller shaft gears, which will be attempted at a further time
This program uses Tkinter to create the GUI

"""
from tkinter import *
from tkinter import messagebox 
import math
import sys

root = Tk()
root.title("Differential design program")

def static(P, rpm, m, z, delt, Y_v, mat_sb, psi_m):
    b = psi_m* m
    global mt, R
    mt = m + (b * math.sin(math.radians(delt))/z)
    #print (mt)
    R = m* z/(2* math.sin(math.radians(delt)))
    v = math.pi* mt* z* int(rpm)/60
    Ft = P/v
    Cv = (3.5 + v)/3.5
    Fd = Ft* Cv
    Fs = mat_sb* b* Y_v* (1-b/R)/(1/mt)
    if Fs > Fd:
        return True
    else:
        return False

def wear(P, rpm, i, m , delt, z, mat_sc,psi_m, E=2e5):
    M_t = (P* 1000000* 60)/ (2* math.pi* int(rpm))
    b = psi_m* m
    sig_c = (0.72/(R-b/2))* math.sqrt(math.sqrt((i** (2)+1)** 3)* E* M_t/(i* b))
    
    if mat_sc > sig_c:
        return True
    else:
        return False

def module(P, Y_v, z, rpm, mat_sb, psi_m = 10):
    M_t = (P* 1000000* 60)/ (2* math.pi* int(rpm))
    m = round(1.28* ((M_t/(Y_v* mat_sb* psi_m* z))** .333), 3) 

    if (m < 1):
        m = 1
    elif(m > 1 and m < 1.25):
        m = 1.25
    elif(m > 1.25 and m < 1.5):
        m = 1.5
    elif(m > 1.5 and m < 2):
        m = 2
    elif(m > 2 and m < 2.5):
        m = 2.5
    elif(m > 2.5 and m < 3):
        m = 3
    elif(m > 3 and m < 4):
        m = 4
    elif(m > 4 and m < 5):
        m  = 5
    elif(m > 5 and m < 6):
        m = 6
    elif(m > 6 and m < 8):
        m = 8
    elif(m > 8 and m < 10):
        m = 10
    elif(m > 10 and m < 12):
        m = 12
    elif(m > 12 and m < 16):
        m = 16
    elif(m > 16):
        m = 20

    m *= 1.25
     
    return m

def take_inp():
    top = Toplevel()
    top.title("Second Window")
    #a = whl_dia.get()
    #Lbl1 = Label(top, text = "the gear ratio of the diff is {}". format(a)).pack()
    A = round(2* math.pi* (int(whl_dia.get())/2)* 0.0254, 3)
    B = round(math.pi* int(turn_r.get())* 2,3)
    C = round(math.pi* (int(turn_r.get()) -(int(track_wt.get()) * 0.0254))* 2, 3)
    D = round(C/A, 3)
    E = round(B/A, 3)
    F = round(E/D, 3)
    Lbl1 = Label(top, text = "The gear ratio of the diff is {}". format(F)).pack()
    Lbl2 = Label(top, text = """\nFollowing assumptions are made in the calculation of gear
        Service factor = 1.2
        20 degree full depth
        Precision cut gears""").pack()

    rpm = int(vel.get()) * 60 * (5/18) * F * E / (2 * math.pi* (int(turn_r.get()) + (int(track_wt.get())*0.0254)/2))
    print(rpm)

    p_mat_sb = material[clicked1.get()]['sb']
    g_mat_sb = material[clicked2.get()]['sb']
    p_mat_sc = material[clicked1.get()]['sc']
    g_mat_sc = material[clicked2.get()]['sc']

    P_act = 1.2 * float(P_inp.get())

    psi_m = 10

    z1 = 18
    z2 = math.ceil(F * z1)
    if (z1 % 2 == 0 and z2 % 2 == 0):
        z2 += 1

    lbl6 = Label(top, text = f"\nz1 is {z1} and z2 is {z2}").pack()

    i_act = z2/z1
    if (((i_act-F)/F)> 0.3):
        messagebox.showwarning("error", "Not Feasible")

    del1 = round(math.degrees(math.atan((1/i_act))), 3)
    del2 = 90 - del1

    lbl7 = Label(top, text = f"Semi cone angle: {del1} and {del2}").pack()

    z_v1 = math.ceil(z1/math.cos(math.radians(del1)))
    z_v2 = math.ceil(z2/math.cos(math.radians(del2)))

    Y_v1 = round(math.pi * (0.154-(.912/z_v1)), 3)
    Y_v2 = round(math.pi * (0.154-(.912/z_v2)), 3)
    lbl8 = Label(top, text = f"Lewis form factor of pinion: {Y_v1}  Gear: {Y_v2}").pack()
    lbl_n = Label(top, text = """Finding weaker element and checking for failure 
    by dynamic load and wear""").pack()

    if (Y_v1 * p_mat_sb < Y_v2 * g_mat_sb):
        lbl11 = Label(top, text ="Pinion is weaker").pack()
        m = module(P_act, Y_v1, z1, rpm, p_mat_sb)
        lbl13 = Label(top, text = "Testing for failure").pack()
        lbl14 = Label(top, text = f"Required b/m ratio for dyanamic load is {psi_m}").pack()
        lbl15 = Label(top, text = f"Required material hardness for wear criteria is {material[clicked1.get()]['BHN']}").pack()
        while static(P_act, rpm, m, z1, del1, Y_v1, p_mat_sb, psi_m) != True:
            psi_m += 2
            lbl14 = Label(top, text = f"Required b/m ratio for dyanamic load is {psi_m}").pack()
            while wear(P_act, rpm, i_act, m, del1, z1, p_mat_sc, psi_m) != True:
                material[clicked1.get()]['BHN'] += 5
                material[clicked1.get()]['sc'] = 2.8 * material[clicked1.get()]['BHN'] - 70
                lbl15 = Label(top, text = f"Required material hardness for wear criteria is {material[clicked1.get()]['BHN']}").pack()
        

    else:
        lbl11 = Label(top, text ="Gear is weaker")
        m = module(P_act, Y_v2, z2, rpm, g_mat_sb)
        lbl13 = Label(top, text = "Testing for failure").pack()
        lbl14 = Label(top, text = f"Required b/m ratio for dyanamic load is {psi_m}").pack()
        lbl15 = Label(top, text = f"Required material hardness for wear criteria is {material[clicked2.get()]['BHN']}").pack()
        while static(P_act, rpm, m, z2, del2, Y_v2, g_mat_sb, psi_m) != True:
            psi_m += 2
            lbl14 = Label(top, text = f"Required b/m ratio for dyanamic load is {psi_m}").pack()
            while wear(P_act, rpm, i_act, m, del2, z2, g_mat_sc, psi_m) != True:
                material[clicked2.get()]['BHN'] += 5
                material[clicked2.get()]['sc'] = 2.8 * material[clicked1]['BHN'] - 70
                lbl15 = Label(top, text = f"Required material hardness for wear criteria is {material[clicked2.get()]['BHN']}").pack()

    lbl12 = Label(top, text = f"Module is {m}").pack()

    frame4 = LabelFrame(root, text = "RESULT", padx = 5, pady = 5)
    frame4.pack(padx = 10, pady = 10)

    frame2 = LabelFrame(frame4, text = "Tooth Proportions", padx = 5, pady = 5)
    frame2.pack(padx = 10, pady = 10)

    res1 = Label(frame2, text = f"{mt}").grid(row = 0, column = 1)
    res1_t = Label(frame2, text = f"addendum = ").grid(row = 0, column = 0)
    res2 = Label(frame2, text = f"{.2 * mt}").grid(row = 1, column = 1)
    res2_t = Label(frame2, text = f"clearance =").grid(row = 1, column = 0)
    res3 = Label(frame2, text = f"{mt + .2 * mt}").grid(row = 2, column = 1)
    res3_t = Label(frame2, text = f"dedendum =").grid(row = 2, column = 0)
    res4 = Label(frame2, text = f"{2 * mt}").grid(row = 3, column = 1)
    res4_t = Label(frame2, text = f"working_depth  =").grid(row = 3, column = 0)
    res_t = Label(frame2, text = f"Pinion").grid(row = 4, column = 1)
    res5 = Label(frame2, text = f"{del1}").grid(row = 5, column = 1)
    res5_t = Label(frame2, text = f"reference angle").grid(row = 5, column = 0)
    res6 = Label(frame2, text = f"{del1 + math.degrees(math.atan((mt/R)))}").grid(row = 6, column = 1)
    res6_t = Label(frame2, text = f"tip angle").grid(row = 6, column = 0)

    frame3 = LabelFrame(frame4, text = "Circular Dimensions", padx = 5, pady = 5)
    frame3.pack(padx = 10, pady = 10)

    res_T1 = Label(frame3, text = f"Pinion").grid(row = 0, column = 1)
    res_T2 = Label(frame3, text = f"Gear").grid(row = 0, column = 2)
    res_1 = Label(frame3, text = f"d1 = {mt * z1}").grid(row = 1, column = 1)
    res_2 = Label(frame3, text = f"d2 = {z2 * mt}").grid(row = 1, column = 2)
    res_3 = Label(frame3, text = f"d_a1 = {z1*mt + 2*mt*math.cos(math.radians(del1))}").grid(row = 2, column = 1)
    res_4 = Label(frame3, text = f"d_a2 = {z2*mt + 2*mt*math.cos(math.radians(del2))}").grid(row = 2, column = 2)
    res_5 = Label(frame3, text = f"d_f1 = {z1*mt - 2.4*mt*math.cos(math.radians(del1))}").grid(row = 3, column = 1)
    res_6 = Label(frame3, text = f"d_f2 = {z2*mt + 2.4*mt*math.cos(math.radians(del2))}").grid(row = 3, column = 2)
    
frame = LabelFrame(root, text ="Inputs", padx = 5, pady = 5)
frame.pack(padx = 10, pady = 10)

whl_dia = Entry(frame, width = 20, borderwidth = 5)
whl_dia.grid(row = 0, column = 1)
turn_r = Entry(frame, width = 20, borderwidth = 5)
turn_r.grid(row = 1, column = 1)
track_wt = Entry(frame, width = 20, borderwidth = 5)
track_wt.grid(row = 2, column = 1)
P_inp = Entry(frame, width = 20, borderwidth = 5)
P_inp.grid(row = 3, column = 1)
vel = Entry(frame, width= 20, borderwidth=5)
vel.grid(row = 4, column = 1)

lbl1= Label(frame, text = "Rear wheel dia in inches").grid(row=0, column=0)
lbl2= Label(frame, text = "Turning radius in meters").grid(row=1, column=0)
lbl3= Label(frame, text = "Track width in inches").grid(row=2, column=0)
lbl4= Label(frame, text = "Power in kW").grid(row=3, column=0)
lbl5= Label(frame, text = "Vehicle velocity in kmph").grid(row=4, column=0)
material={'15Ni2Cr1Mo15':{'BHN': 500, 'sb': 320, 'sc': 950},'40Ni2Cr1Mo28':{'BHN': 600, 'sb': 400, 'sc': 1100},
    'C45':{'BHN': 195, 'sb': 140, 'sc': 500}}


options = [
    "15Ni2Cr1Mo15",
    "40Ni2Cr1Mo28",
    "C45"
    ]
clicked1 = StringVar()
clicked1.set(options[0])
clicked2 = StringVar()
clicked2.set(options[0])

drop1 = OptionMenu(frame, clicked1, *options)
drop1.grid(row = 5, column = 1)
lbl9 = Label(frame, text = "Select pinion mat").grid(row = 5, column = 0)
drop2 = OptionMenu(frame, clicked2, *options)
drop2.grid(row = 6, column = 1)
lbl10 = Label(frame, text = "Select gear mat").grid(row = 6, column = 0)

Btn1 = Button(frame, text = "Submit", padx = 10, pady= 10, command = take_inp).grid(row = 7, column = 0, columnspan = 2)

root.mainloop()