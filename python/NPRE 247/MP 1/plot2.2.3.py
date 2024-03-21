import functions
import Main
import matplotlib.pyplot as plt
import numpy as np

dt_used = functions.read_json('dt_used_in_2.2.3.json')

Data = np.zeros((2,len(dt_used)))
for i in range(0,len(dt_used)):
    functions.write_json("InputParameter.json","delta_t",dt_used[i])
    Main.Main()
    Nout = functions.read_csv("Noutput.csv")
    time_Max = float(functions.Numerical_Max_NB(Nout))
    Data[0][i]=1/dt_used[i]
    Data[1][i]=time_Max
Parameters = functions.read_json('InputParameter.json')
decay_A = np.log(2)/Parameters["Half_life_A"]
decay_B = np.log(2)/Parameters["Half_life_B"]
N0_A = Parameters["Initial_Partical_Number_A"]
N0_B = Parameters["Initial_Partical_Number_B"]

Analytical_Max_B = functions.Highest_B_t(decay_A,decay_B,N0_A,N0_B)
list_A_Max_B= np.ones_like(Data[1])
list_A_Max_B = Analytical_Max_B*list_A_Max_B       

plt.figure(figsize=(5, 2.7), layout='constrained')
plt.plot(Data[0], Data[1],"bo")
plt.plot(Data[0], list_A_Max_B,"r-.", label='Analytical')  
plt.xlabel(r'$ 1/\Delta t$')
plt.ylabel(r'Max Time for $N_B$')
plt.legend()
plt.savefig('result_2.2.3.png',dpi=300)        
        