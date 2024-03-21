import numpy as np
import matplotlib.pyplot as plt
import csv
import json

   
def Numerical_next (current,Decay_Constant,delta_t):
    Next_value = 0
    Next_value =current-delta_t*Decay_Constant*current
    change_due_to_decay = delta_t*Decay_Constant*current
    return Next_value, change_due_to_decay
def Partical_number_WRO_Time_A (decayconstant,N0,time):
    P_n = N0*np.exp(-decayconstant*time)
    return P_n
def Partical_number_WRO_Time_B (decayconstant_A,decayconstant_B,N0_A,N0_B,time):
    C_A = (decayconstant_A*N0_A)/(decayconstant_B-decayconstant_A)
    C_B = N0_B - C_A
    A_exp = np.exp(-decayconstant_A*time)
    B_exp = np.exp(-decayconstant_B*time)
    PB_n = C_B*B_exp + C_A*A_exp
    return PB_n
def Partical_number_WRO_Time_C (decayconstant_A,decayconstant_B,N0_A,N0_B,N0_C,time):
    C_A = (decayconstant_A*N0_A)/(decayconstant_B-decayconstant_A)
    C_B = N0_B - C_A
    A_exp = np.exp(-decayconstant_A*time)
    B_exp = np.exp(-decayconstant_B*time)
    C_B = C_B*(-1)/(decayconstant_B)
    C_A = C_A*(-1)/(decayconstant_A)
    PC_n = decayconstant_B*(C_B*B_exp+C_A*A_exp)+N0_A+N0_B+N0_C
    return PC_n
def Highest_B_t (decayconstant_A,decayconstant_B,N0_A,N0_B):
    k=(decayconstant_A*decayconstant_B*N0_A)/(decayconstant_B-decayconstant_A)
    A_c = decayconstant_A*N0_A-k
    B_c = decayconstant_B*N0_B-k
    time = (np.log(B_c/A_c))/(decayconstant_B-decayconstant_A)
    return time 
def Numerical_solution (NA_0,NB_0,NC_0,Decay_Constant_A,Decay_Constant_B,delta_t,final_t):
    Step_number  = int(final_t/delta_t)
    Time = np.zeros(Step_number+1)
    Partical_Number_A = np.zeros(Step_number+1)
    Partical_Number_B = np.zeros(Step_number+1)
    Partical_Number_C = np.zeros(Step_number+1)
    Partical_Number_A[0]=NA_0
    Partical_Number_B[0]=NB_0
    Partical_Number_C[0]=NC_0
    for i in range(1,Step_number+1):
        Time[i] = delta_t*i
        Partical_Number_A[i],change_A= Numerical_next(Partical_Number_A[i-1],Decay_Constant_A,delta_t)
        Partical_Number_B[i],change_B = Numerical_next(Partical_Number_B[i-1]+change_A,Decay_Constant_B,delta_t)
        Partical_Number_C[i] = Partical_Number_C[i-1]+change_B
    N_output = np.zeros((4,Step_number+1))
    N_output[0]=Time
    N_output[1]=Partical_Number_A
    N_output[2]=Partical_Number_B
    N_output[3]=Partical_Number_C
    return N_output
def Analitical_solutions (NA_0,NB_0,NC_0,Decay_Constant_A,Decay_Constant_B,delta_t,final_t):
    Step_number  = int(final_t/delta_t)
    Time = np.zeros(Step_number+1)
    Partical_Number_A = np.zeros(Step_number+1)
    Partical_Number_B = np.zeros(Step_number+1)
    Partical_Number_C = np.zeros(Step_number+1)
    for i in range (0,Step_number+1):
        Time[i] = delta_t*i
        Partical_Number_A[i]=Partical_number_WRO_Time_A(Decay_Constant_A,NA_0,i*delta_t)
        Partical_Number_B[i]=Partical_number_WRO_Time_B(Decay_Constant_A,Decay_Constant_B,NA_0,NB_0,i*delta_t)
        Partical_Number_C[i]=Partical_number_WRO_Time_C(Decay_Constant_A,Decay_Constant_B,NA_0,NB_0,NC_0,i*delta_t)
    A_output = np.zeros((4,Step_number+1))
    A_output[0]=Time
    A_output[1]=Partical_Number_A
    A_output[2]=Partical_Number_B
    A_output[3]=Partical_Number_C
    return A_output
def read_csv (filename):
    file = open(filename,"r")
    data = list(csv.reader(file,delimiter=","))
    file.close
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = float(data[i][j])
    return data
def write_json (filename,dict_directory,value):
    with open(filename) as file:
        data = json.load(file)
        data[dict_directory] = value
        Modified = json.dumps(data, indent=4)
    with open(filename,"w") as file:
        file.write(Modified)
    return True
def new_json (filename, new_dic):
    new_dic = json.dumps(new_dic, indent=4)
    with open(filename,"w") as file:
        file.write(new_dic)
    return True
def read_json(filename):
    f = open(filename)
    imput = json.load(f)
    return imput
def Numerical_Max_NB (Nout):
    Nout = np.array(Nout)
    index = np.where(Nout[2] == Nout[2].max())
    return Nout[0][index]