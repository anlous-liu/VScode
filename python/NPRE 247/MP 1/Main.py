import json
import numpy as np
import matplotlib.pyplot as plt

# with open ("InputStandard.json") as json_file:
#     imput = json_file.read()
    
# print(imput)
imput = { 
    "DecayConstant_A": 0.2739712176126266045127399689558, 
    "DecayConstant_B": 0.0627282516343841908974870698152, 
    "Initial_Partical_Number_A": 100,
    "Initial_Partical_Number_B":0,
    "Initial_Partical_Number_C":0,
    "Tfinal": 60
}
DecayConstant_A = imput["DecayConstant_A"]
DecayConstant_B = imput["DecayConstant_B"]
DecayConstant_C=0
Initial_Partical_Number_A = imput["Initial_Partical_Number_A"]
Initial_Partical_Number_B = imput["Initial_Partical_Number_B"]
Initial_Partical_Number_C = imput["Initial_Partical_Number_C"]
Tfinal = imput["Tfinal"]


def Numerical_next (current,Decay_Constant,delta_t):
    Next_value = 0
    Next_value =current-delta_t*Decay_Constant*current
    change_due_to_decay = delta_t*Decay_Constant*current
    return Next_value, change_due_to_decay
def draw_graph (A_output,title):
    plt.figure(figsize=(5, 2.7), layout='constrained')
    plt.plot(A_output[0], A_output[1], label='Substance A')  # Plot some data on the (implicit) axes.
    plt.plot(A_output[0], A_output[2], label='Substance B')  # etc.
    plt.plot(A_output[0], A_output[3], label='Substance C')
    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.title(title)
    plt.legend()
    plt.show()
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
    C_C = (1/decayconstant_A)*C_A+(1/decayconstant_B)*C_B
    PC_n = decayconstant_B*(C_B*B_exp+C_A*A_exp)+N0_A+N0_C
    return PC_n

DeltaT = 0.05
Step_number  = int(Tfinal/DeltaT)
Time = np.zeros(Step_number)
Partical_Number_A = np.zeros(Step_number)
Partical_Number_B = np.zeros(Step_number)
Partical_Number_C = np.zeros(Step_number)
Partical_Number_A[0]=Initial_Partical_Number_A

for i in range(1,Step_number):
    Time[i] = DeltaT*i
    Partical_Number_A[i],change_A= Numerical_next(Partical_Number_A[i-1],DecayConstant_A,DeltaT)
    Partical_Number_B[i],change_B = Numerical_next(Partical_Number_B[i-1]+change_A,DecayConstant_B,DeltaT)
    Partical_Number_C[i] = Partical_Number_C[i-1]+change_B
N_output = np.zeros((4,Step_number))
N_output[0]=Time
N_output[1]=Partical_Number_A
N_output[2]=Partical_Number_B
N_output[3]=Partical_Number_C

for i in range (1,Step_number):
    Partical_Number_A[i]=Partical_number_WRO_Time_A(DecayConstant_A,100,i*DeltaT)
    Partical_Number_B[i]=Partical_number_WRO_Time_B(DecayConstant_A,DecayConstant_B,100,0,i*DeltaT)
    Partical_Number_C[i]=Partical_number_WRO_Time_C(DecayConstant_A,DecayConstant_B,100,0,0,i*DeltaT)
A_output = np.zeros((4,Step_number))
A_output[0]=Time
A_output[1]=Partical_Number_A
A_output[2]=Partical_Number_B
A_output[3]=Partical_Number_C


print(Partical_Number_A[100]+Partical_Number_B[100]+Partical_Number_C[100])
print(Partical_Number_C[10])
np.savetxt("Noutput.csv",
        N_output,
        delimiter =", ",
        fmt ='% s')

draw_graph(A_output,"Analytic")
draw_graph(N_output,"Numerical")

print(Partical_Number_A[100]+Partical_Number_B[100]+Partical_Number_C[100])
print(Partical_Number_C[10])
np.savetxt("Aoutput.csv",
        A_output,
        delimiter =", ",
        fmt ='% s')


