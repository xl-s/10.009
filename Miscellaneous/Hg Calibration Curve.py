from numpy import arange, unique, poly1d, polyfit
import matplotlib.pyplot as plt

x = [436, 546, 579]
y = [3.25, 4.5, 4.825]

m, c = polyfit(x, y, 1)
xe = arange(410, 690)
ye = m * xe + c

plt.plot(unique(xe), poly1d(polyfit(xe, ye, 1))(unique(xe)), color='black', label='y = {}x - {}'.format(round(m, 4),round(-c, 2)))
plt.scatter([436, 546, 579], [3.25, 4.5, 4.825], marker='x', color='black')
plt.xlabel("Wavelength / nm")
plt.ylabel("Spectroscope Reading / cm")
plt.grid(color='black', linestyle='--', linewidth=0.5)
plt.ylim(2.5, 6.5)
plt.xlim(400, 700)
plt.title("Hg Emission Spectrum Calibration Curve")
plt.legend(loc='upper left')
 
plt.savefig('Calibration.png', dpi = 1000)
plt.close()
plt.show() # Place this before the above two lines to see the graph
