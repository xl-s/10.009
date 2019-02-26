import matplotlib.pyplot as plt

Se = 1
lambd = 10
Rin = 10
DT = 100
VSe = Se * DT

def wdot(RL):
    return (VSe**2 * RL)/((Rin + RL)**2)

step = 0.1
highest = 61

x = [val * step for val in range(0, int(highest/step))]
y = [wdot(val) for val in x]

plt.plot(x, y, color='black')
plt.grid(color='black', linestyle='--', linewidth=0.5)
plt.xlabel('Load Resistance, $R_L\ /\ \Omega$')
plt.ylabel('Work Output, $\dot{W}\ /\ W$')
plt.title('Work Output $(\dot{W})$ against Resistance $(R_L)$')

plt.savefig('Work Output.png', dpi=1000)
plt.close()
plt.show() # Place this before the above two lines to see the graph
