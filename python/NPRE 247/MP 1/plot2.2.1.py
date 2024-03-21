import matplotlib.pyplot as plt
import functions
import numpy as np
import Main
import os
dict_of_dt =  functions.read_json("dt_type.json")

# running to get 3 sets of data for three types of dt
for i in range(0,3):
    for j in range(0,len(list(dict_of_dt.values()))):
        functions.write_json("InputParameter.json","delta_t",list(dict_of_dt.values())[j])
        Main.Main()
        Nout = functions.read_csv("Noutput.csv")
        temp = np.zeros((2,len(Nout[0])))
        temp[0]=Nout[0]
        temp[1]=Nout[2]
        np.savetxt(f"Noutput{j}.csv",temp,delimiter =", ",fmt ='% s')
#running to get a fine enough analytical solution        
functions.write_json("InputParameter.json","delta_t",0.05)        
Main.Main()
#read the three outputs
Aout = functions.read_csv("Aoutput.csv")
N1 = functions.read_csv("Noutput0.csv")
N2 = functions.read_csv("Noutput1.csv")
N3 = functions.read_csv("Noutput2.csv")
#removing output files to make directory cleaer
for i in range(0,3):
    os.remove(f"Noutput{i}.csv")
#plot and save the graph    
plt.figure(figsize=(5, 2.7), layout='constrained')
plt.plot(N1[0], N1[1], label='Coarse')  
plt.plot(N2[0], N2[1], label='Medium')  
plt.plot(N3[0], N3[1], label='Fine')
plt.plot(Aout[0], Aout[2],"r-.", label="Analytical")
plt.xlabel('time (h)')
plt.ylabel('particle number')
plt.legend()
plt.savefig('result_2.2.1.png',dpi=300)
#output parameters used
parameters = functions.read_json("InputParameter.json")
del parameters["delta_t"]
dts = functions.read_json("dt_type.json")
dts["analytic_dt"]=0.05
output =  {**parameters,**dts}
functions.new_json("output_2.2.1.json",output)
