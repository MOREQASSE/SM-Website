import numpy as np
import matplotlib.pyplot as plt

# Paramètres pour les simulations
R = 20e3  # Résistance en ohms
C = 47e-9  # Capacité en farads
Vcc = 5  # Tension d'alimentation (V)
t = np.linspace(0, 0.002, 1000)  # Temps (s) sur 2 ms

# Calcul des tensions
Vc = Vcc * (1 - np.exp(-t / (R * C))) * (t < R * C) + Vcc * np.exp(-t / (R * C)) * (t >= R * C)  # Tension du condensateur
Vs = Vcc * np.sign(np.sin(2 * np.pi * t / (2 * R * C)))  # Signal carré de sortie
V_plus = np.where(Vs > 0, Vcc / 2, -Vcc / 2)  # Tension de référence

# Tracé des courbes individuellement
# Vs(t)
plt.figure(figsize=(8, 4))
plt.plot(t * 1e3, Vs, color='blue')
plt.title("Vs(t) (Signal carré)")
plt.xlabel("Temps (ms)")
plt.ylabel("Tension (V)")
plt.grid(True)
plt.show()

# Vc(t)
plt.figure(figsize=(8, 4))
plt.plot(t * 1e3, Vc, color='red')
plt.title("Vc(t) (Tension du condensateur)")
plt.xlabel("Temps (ms)")
plt.ylabel("Tension (V)")
plt.grid(True)
plt.show()

# V+(t)
plt.figure(figsize=(8, 4))
plt.plot(t * 1e3, V_plus, color='green', linestyle='--')
plt.title("V+(t) (Tension de référence)")
plt.xlabel("Temps (ms)")
plt.ylabel("Tension (V)")
plt.grid(True)
plt.show()
