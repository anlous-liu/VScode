import numpy as np
import functions
import os

imput = functions.read_json("InputParameter.json")

DecayConstant_A = np.log(2)/imput["Half_life_A"]
DecayConstant_B = np.log(2)/imput["Half_life_B"]
Initial_Partical_Number_A = imput["Initial_Partical_Number_A"]
Initial_Partical_Number_B = imput["Initial_Partical_Number_B"]
Initial_Partical_Number_C = imput["Initial_Partical_Number_C"]
DeltaT = imput["delta_t"]
Tfinal = imput["Tfinal"]

N_output = functions.Numerical_solution(Initial_Partical_Number_A,Initial_Partical_Number_B,Initial_Partical_Number_C,DecayConstant_A,DecayConstant_B,DeltaT,Tfinal)
A_output = functions.Analitical_solutions(Initial_Partical_Number_A,Initial_Partical_Number_B,Initial_Partical_Number_C,DecayConstant_A,DecayConstant_B,DeltaT,Tfinal)
np.savetxt("Noutput.csv",
        N_output,
        delimiter =", ",
        fmt ='% s')
np.savetxt("Aoutput.csv",
        A_output,
        delimiter =", ",
        fmt ='% s')

def Main ():
    imput = functions.read_json("InputParameter.json")

    DecayConstant_A = np.log(2)/imput["Half_life_A"]
    DecayConstant_B = np.log(2)/imput["Half_life_B"]
    Initial_Partical_Number_A = imput["Initial_Partical_Number_A"]
    Initial_Partical_Number_B = imput["Initial_Partical_Number_B"]
    Initial_Partical_Number_C = imput["Initial_Partical_Number_C"]
    DeltaT = imput["delta_t"]
    Tfinal = imput["Tfinal"]

    N_output = functions.Numerical_solution(Initial_Partical_Number_A,Initial_Partical_Number_B,Initial_Partical_Number_C,DecayConstant_A,DecayConstant_B,DeltaT,Tfinal)
    A_output = functions.Analitical_solutions(Initial_Partical_Number_A,Initial_Partical_Number_B,Initial_Partical_Number_C,DecayConstant_A,DecayConstant_B,DeltaT,Tfinal)
    np.savetxt("Noutput.csv",
            N_output,
            delimiter =", ",
            fmt ='% s')
    np.savetxt("Aoutput.csv",
            A_output,
            delimiter =", ",
            fmt ='% s')
    return True




