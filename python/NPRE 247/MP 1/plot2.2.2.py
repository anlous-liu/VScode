import functions
import Main
import matplotlib.pyplot as plt
import numpy as np

#getting a smooth enough numerical solution
functions.write_json("InputParameter.json","delta_t",0.05)
Main.Main()
imput = np.array(functions.read_csv("Noutput.csv"))
#creating sum array
sum_ = imput[1]+imput[2]+imput[3]
#plotting
plt.figure(figsize=(5, 2.7), layout='constrained')
plt.plot(imput[0], imput[1], label='Substance A')  
plt.plot(imput[0], imput[2], label='Substance B')  
plt.plot(imput[0], imput[3], label='Substance C')
plt.plot(imput[0], sum_, "r-.",label='Sum')
plt.xlabel('time (h)')
plt.ylabel('particle number')
plt.legend()
plt.savefig('result_2.2.2.png',dpi=300)
#output parameters used
parameters = functions.read_json("InputParameter.json")
output =  parameters
functions.new_json("output_2.2.2.json",output)
