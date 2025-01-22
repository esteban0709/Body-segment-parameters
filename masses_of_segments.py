import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#Just change this part
#Enter the height (talla) and weight (peso) of each participant in cm and kg
data = {
    "Talla (cm)": [174, 175, 180, 165, 182, 157, 175, 176, 178, 163, 168, 171, 166, 174, 169, 165], #height in cm
    "Peso (kg)": [102, 65.9, 75, 55, 74, 67, 65, 66, 82.5, 52.1, 68.1, 67, 66.3, 75, 65, 71.2], #weight in kg
}

# Do not change nothing from here
df = pd.DataFrame(data)


talla = df.loc[:, "Talla (cm)"].tolist()
talla_meters=[0]*len(talla)
for i in range(len(talla)):
    talla_meters[i]=talla[i]*0.01
peso = df.loc[:, "Peso (kg)"].tolist()
peso_pounds=[0]*len(peso)
for i in range(len(peso)):
    peso_pounds[i]= peso[i]*2.20462

a=len(talla)

def calcular_pendiente(x1, y1, x2, y2):

    try:
        pendiente = (y2 - y1) / (x2 - x1)
        return pendiente
    except ZeroDivisionError:
        return 


x1_hand, y1_hand = 1.028,1.091
x2_hand, y2_hand = 1.099,1.215

x1_forearm, y1_forearm = 1.029,1.084
x2_forearm, y2_forearm =  1.098,1.181

x1_arm, y1_arm = 1.028,1.059
x2_arm, y2_arm = 1.099,1.129


x1_shank, y1_shank= 1.03,1.066
x2_shank, y2_shank = 1.097,1.121

x1_thigh, y1_thigh = 1.031,1.037
x2_thigh, y2_thigh=  1.095,1.088

m_hand = calcular_pendiente(x1_hand, y1_hand, x2_hand, y2_hand)
m_forearm = calcular_pendiente(x1_forearm, y1_forearm, x2_forearm, y2_forearm)
m_arm = calcular_pendiente(x1_arm, y1_arm, x2_arm, y2_arm)
m_shank = calcular_pendiente(x1_shank, y1_shank, x2_shank, y2_shank)
m_thigh = calcular_pendiente(x1_thigh, y1_thigh, x2_thigh, y2_thigh)

def obtener_ecuacion_recta(m, x1, y1):
   
    b = y1 - m * x1

    ecuacion = f"y = {m}x + {b}"
    #print(f"La ecuación de la recta es: {ecuacion}")
    
    def ecuacion_recta(x):
        return m * x + b

    return ecuacion_recta




recta_hand = obtener_ecuacion_recta(m_hand, x1_hand, y1_hand)
recta_forearm = obtener_ecuacion_recta(m_forearm, x1_forearm, y1_forearm)
recta_arm = obtener_ecuacion_recta(m_arm, x1_arm, y1_arm)
recta_shank= obtener_ecuacion_recta(m_shank, x1_shank, y1_shank)
recta_thigh = obtener_ecuacion_recta(m_thigh, x1_thigh, y1_thigh)
"""
# Probar la ecuación con otro valor de x
x = 5
y = recta_hand(x)
print(f"Para x = {x}, y = {y}")
"""


rectas = {
    "Hand": recta_hand,
    "Forearm": recta_forearm,
    "Arm": recta_arm,
    "Shank": recta_shank,
    "Thigh": recta_thigh
}


rangos_x = {
    "Hand": (x1_hand, x2_hand),
    "Forearm": (x1_forearm, x2_forearm),
    "Arm": (x1_arm, x2_arm),
    "Shank": (x1_shank, x2_shank),
    "Thigh": (x1_thigh, x2_thigh)
}


plt.figure(figsize=(10, 6))
for name, recta in rectas.items():
    x_min, x_max = rangos_x[name]
    x_vals = np.linspace(x_min, x_max, 100)
    y_vals = recta(x_vals)
    
    
    plt.plot(x_vals, y_vals, label=name)
    
    
    mid_x = (x_min + x_max) / 2
    mid_y = recta(mid_x)
    
    
    plt.text(mid_x, mid_y + 0.5, name, fontsize=10, ha='center')


plt.xlabel("Body density (kg/l)")
plt.ylabel("Segment density (kg/l)")
plt.legend()
plt.grid(True)
plt.show()

c=[0]*a
for i in range(a):
    c[i]=talla_meters[i]/(peso[i]**(1/3))
d=[0]*a
for i in range(a):
    d[i]=0.69+0.9*c[i]
    
hand_density=[0]*a
for i in range(a):
    hand_density[i]=recta_hand(d[i])


forearm_density=[0]*a
for i in range(a):
    forearm_density[i]=recta_forearm(d[i])


arm_density=[0]*a
for i in range(a):
    arm_density[i]=recta_arm(d[i])

shank_density=[0]*a
for i in range(a):
    shank_density[i]=recta_shank(d[i])

thigh_density=[0]*a
for i in range(a):
    thigh_density[i]=recta_thigh(d[i])

hand_density_metrics=[0]*a
forearm_density_metrics=[0]*a
arm_density_metrics=[0]*a
shank_density_metrics=[0]*a
thigh_density_metrics=[0]*a
head_density_metrics=[1110]*a
trunk_density_metrics=[1030]*a

for i in range(a):
    hand_density_metrics[i]=hand_density[i]*1000
    forearm_density_metrics[i]=forearm_density[i]*1000
    arm_density_metrics[i]=arm_density[i]*1000
    shank_density_metrics[i]=shank_density[i]*1000
    thigh_density_metrics[i]=thigh_density[i]*1000

volumen_hand_right=[0]*a
volumen_forearm_right=[0]*a
volumen_arm_right=[0]*a
volumen_shank_right=[0]*a
volumen_thigh_right=[0]*a
volumen_head=[0]*a
volumen_trunk=[0]*a

for i in range(a):
    volumen_hand_right[i]= 1.69*talla[i]+1.60*peso_pounds[i]-62
    volumen_forearm_right[i]=-2.06*talla[i]+8.40*peso_pounds[i]+329
    volumen_arm_right[i]=-2.14*talla[i]+13.25*peso_pounds[i]+76
    volumen_shank_right[i]=26.72*talla[i]+11.84*peso_pounds[i]-2.912
    volumen_thigh_right[i]=58.34*talla[i]+17.84*peso_pounds[i]-6.949
    volumen_head[i]=6.84*talla[i]+2.05*peso_pounds[i]+2806
    volumen_trunk[i]=-22.71*talla[i]+163.68*peso_pounds[i]+524
    
volumen_hand_right_m3=[0]*a
volumen_forearm_right_m3=[0]*a
volumen_arm_right_m3=[0]*a
volumen_shank_right_m3=[0]*a
volumen_thigh_right_m3=[0]*a
volumen_head_m3=[0]*a
volumen_trunk_m3=[0]*a

for i in range(a):
    volumen_hand_right_m3[i]= volumen_hand_right[i]*0.000001
    volumen_forearm_right_m3[i]=volumen_forearm_right[i]*0.000001
    volumen_arm_right_m3[i]=volumen_arm_right[i]*0.000001
    volumen_shank_right_m3[i]=volumen_shank_right[i]*0.000001
    volumen_thigh_right_m3[i]=volumen_thigh_right[i]*0.000001
    volumen_head_m3[i]=volumen_head[i]*0.000001
    volumen_trunk_m3[i]=volumen_trunk[i]*0.000001

hand_mass=[0]*a
forearm_mass=[0]*a
arm_mass=[0]*a
shank_mass=[0]*a
thigh_mass=[0]*a
head_mass=[0]*a
trunk_mass=[0]*a

for i in range(a):
    hand_mass[i]= hand_density_metrics[i]*volumen_hand_right_m3[i]
    forearm_mass[i]=forearm_density_metrics[i]*volumen_forearm_right_m3[i]
    arm_mass[i]=arm_density_metrics[i]*volumen_arm_right_m3[i]
    shank_mass[i]=shank_density_metrics[i]*volumen_shank_right_m3[i]
    thigh_mass[i]=thigh_density_metrics[i]*volumen_thigh_right_m3[i]
    head_mass[i]=head_density_metrics[i]*volumen_head_m3[i]
    trunk_mass[i]=trunk_density_metrics[i]*volumen_trunk_m3[i]

b=a+1

participante = list(range(1, b))

data = {
    "Participante": participante,
    "Hand Mass": hand_mass,
    "Forearm Mass": forearm_mass,
    "Arm Mass": arm_mass,
    "Shank Mass": shank_mass,
    "Thigh Mass": thigh_mass,
    "Head Mass": head_mass,
    "Trunk Mass": trunk_mass
}

df = pd.DataFrame(data)


output_file = "masses.xlsx"
df.to_excel(output_file, index=False)
