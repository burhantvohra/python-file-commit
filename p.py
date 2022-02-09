import matplotlib.pyplot as mb
import numpy as np

G_ref = 1000 #input('Enter Reference Solar Irradiation')
U_isc = 0.005 #input('Enter the Temperature co-efficient of cell short circuited')
Isc = 11.37 # input('Enter the Short circuit  current at 25C')
Ta = 34 #input('Enter the Ambient Temperature in Celsius')
Noct = 25 # input('Enter the Nominal cell temp')
Tc_ref = 25
i =0
a =np.array([])
#Iph=np.array([])
#Tc =np.array([])
G= np.array([0,0,0,0,0,0,0,38,143,276,387,445,439,370,252,120,24,0,0,0,0,0,0,0])
print(G)
for i in range(len(G)):
   Tc = Ta + ((G[i] / 800) * ((Noct) - 20))
   Iph = (G[i]/ (G_ref)) * (Isc + (U_isc) * (Tc - Tc_ref))
   #print(Tc)
  # print(Iph)

mb.plot(Iph,Tc)
mb.show()

