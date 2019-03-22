import matplotlib.pyplot as plt
from math import exp

# Plot, for first resistor (1.817): Wdot against time, Th against time, Tc against time.
# And also Qh against time and Qc against time
# Wdot = 

# First column: Time / s, Second: Th / C, Third: Tc / C, Fourth: Current / A

Rin = 2.131
RL = 1.817

data = open("data/main.dat", 'r')
rows = [line.split() for line in data]

Times = [float(line[0]) for line in rows]
Ths = [float(line[1]) for line in rows]
Tcs = [float(line[2]) for line in rows]
Currents = [float(line[3]) for line in rows]

Wdots = [I**2 * RL for I in Currents]

def plot(y, overlay=None, olabel='', ylabel='', title='', save=False, lab=''):
    plt.plot(Times, y, color='black', label=lab)
    if overlay: plt.plot(Times, overlay, color='black', linestyle='--', label=olabel)
    plt.grid(color='black', linestyle='--', linewidth=0.5)
    plt.xlabel('Time / s')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend(loc='upper left')
    if save:
        plt.savefig('{}.png'.format(title), dpi=1000)
        plt.close()
    else:
        plt.show()
        
def eqnc(t):
    return 19.5 + 20 * exp(-(t+19)/25)

def eqnh(t):
    return 41.5 - 20 * exp(-(t+12)/40)
    
