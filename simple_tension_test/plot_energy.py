import matplotlib
import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.ticker as mtick


time, strain_energy, crack_energy, total_energy = np.loadtxt('Energy.hist',
                                                              delimiter='\t', unpack=True)                                                    

font = {'size': 12}
matplotlib.rc('font', **font)

labels = []
labels.append('Strain energy')
labels.append('Crack energy dissipation')
labels.append('Total energy')

symbols = ['-k', '--m', '-.b^', ':gx', '-rD', 'bx']

fig = plt.figure()
ax = fig.add_subplot(111)

plt.plot(time, strain_energy, symbols[0],
         linewidth=2.0, label=labels[0], fillstyle='none', markersize=8)   
plt.plot(time, crack_energy, symbols[1],
         linewidth=2.0, label=labels[1], fillstyle='none', markersize=8)   
plt.plot(time, total_energy, symbols[2],
         linewidth=2.0, label=labels[2], fillstyle='none', markersize=8)   
# plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 3))
# ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))

plt.xlabel('Displacement (mm)')
plt.ylabel('Energy (J)', multialignment='center')
#plt.xlim(0,0.014)
# plt.xticks(np.arange(0, 6, step=1))
#plt.ylim(0.0, 0.003)
# plt.legend( bbox_to_anchor=(2.4, 1.1),prop={'size':10})
plt.grid()
plt.legend()
# ax.set_aspect('equal')
# plt.subplots_adjust(top = 0.95, bottom = 0.125,
#                     right = 0.95, left = 0.125, hspace = 0, wspace = 0)
plt.savefig("Energy_history.eps", bbox_inches='tight', pad_inches=0.1)
