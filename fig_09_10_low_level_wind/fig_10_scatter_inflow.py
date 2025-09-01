import numpy as np
import matplotlib.pyplot as plt
import sys, os
sys.path.insert(1,'../')
import config
from netCDF4 import Dataset
import matplotlib as mpl
from mpi4py import MPI
import util_draw as udraw
from util.vvmLoader import VVMLoader, VVMGeoLoader
import util.tools as tools
from matplotlib.collections import LineCollection
import matplotlib.patheffects as mpl_pe
from scipy import stats

comm = MPI.COMM_WORLD
nproc = comm.Get_size()
cpuid = comm.Get_rank()

center_flag='czeta0km_positivemean'
datdir=config.dataPath+f"/axisy_lowlevel/{center_flag}/"

fname = f'{datdir}/lowlevel_inflow_0-500m.npz'
data  = np.load(fname)
explist = data['expList']
rday_1d = data['restart_day']
var_1d  = data['var_1d']
radius_1d = data['radius_1d']
method_1d = data['method_1d']
rwind_init = data['rwind_init']
twind_init = data['twind_init']
rwind_last = data['rwind_last']
twind_last = data['twind_last']
nmet, nexp, nvar, nradius = data['rwind_init'].shape

nexp = len(config.expList)
exp0 = config.expdict[config.expList[0]]

method_dict = {'inflow_daily':{'imet':1,\
                         'ur_text':'{exp0} {txtstr}-{rday} day',\
                         'scatter_x_label':'restart day average'
                        },\
               'inflow_snapshot':{'imet':0,\
                         'ur_text':'{exp0} {rday} day (snapshot)',\
                         'scatter_x_label':'restart day snapshot',\
                        },\
              }
iswhite = True
tag = 'inflow_daily'
#tag = 'inflow_snapshot'
mdict = method_dict[tag]
if iswhite:
  figdir = f'./{center_flag}_white/{tag}/'
else:
  figdir = f'./{center_flag}/{tag}/'
os.system(f'mkdir -p {figdir}')

udraw.set_figure_defalut() 
if not iswhite:
  udraw.set_black_background()

bounds=np.array('0 10 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31'.split()).astype(int)

newcolors = np.vstack((
                       [[0.8,0.8,0.8,1]],\
                       [[0.5,0.5,0.5,1]],\
                       #plt.cm.Reds(np.linspace(0.2,0.9,1)),
                       plt.cm.Greens(np.linspace(0.2,0.9,5)),
                       plt.cm.Oranges(np.linspace(0.2,0.9,5)),
                       plt.cm.Blues(np.linspace(0.2,0.9,5)),
                       plt.cm.Purples(0.7),
                     ))
cmap = mpl.colors.ListedColormap(newcolors, name='OrangeBlue')
cmap.set_under((0.7,0.7,0.7))
cmap.set_over(plt.cm.Purples(0.7))
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)



###### maximum radius ##########
nsen   = 2
x_data = np.min(rwind_init[mdict['imet'],1:,0,:], axis=1)
y_data = np.max(twind_last[mdict['imet'],1:,0,:], axis=1)
c_data = rday_1d[1:]
x_data = x_data[:nexp]
y_data = y_data[:nexp]
c_data = c_data[:nexp]

nsen   = 1
x_data = np.min(rwind_init[mdict['imet'],1:,0,:], axis=1)
y_data = np.max(twind_last[mdict['imet'],1:,0,:], axis=1)
c_data = rday_1d[1:]
x_data = x_data[:nexp-2]
y_data = y_data[:nexp-2]
c_data = c_data[:nexp-2]

udraw.set_figure_defalut() 
if not iswhite:
  udraw.set_black_background()
fig = plt.figure(figsize=(10,8))
#ax  = fig.add_axes([0.13, 0.15, 0.8, 0.8])
#cax = fig.add_axes([0.83, 0.3, 0.03, 0.5])
ax  = fig.add_axes([0.15, 0.15, 0.72, 0.75])
cax = fig.add_axes([0.89, 0.15, 0.03, 0.7])
plt.sca(ax)

idx=c_data<=25
res = stats.linregress(x_data[idx], y_data[idx])
x=np.arange(-10,10)
plt.plot(x, res.intercept + res.slope*x, 'k', lw=1)

#plt.plot([-100,100],[100,-100],c='0.5',lw=3)
#plt.scatter(x_data, y_data, s=300, c=c_data, norm=norm, cmap=cmap,zorder=10)
plt.scatter(x_data[:-nsen], y_data[:-nsen], s=300, c=c_data[:-nsen], norm=norm, cmap=cmap,zorder=10)
plt.scatter(x_data[-nsen:], y_data[-nsen:], s=300, c=c_data[-nsen:], norm=norm, cmap=cmap,zorder=10, marker='X')
CB=fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap),
       cax=cax, orientation='vertical', extend='neither', extendrect=True)

bc=(bounds[:-1]+bounds[1:])/2
CB.ax.set_title('D'+r'$xx$'+'_on', loc='left', fontsize=20)
ticks = bc
ticklabels = np.array([f'{i:02.0f}' for i in bounds[:-1]])
idx=[0,1,2,7,12,17]
CB.set_ticks(ticks[idx])
CB.set_ticklabels(ticklabels[idx])
CB.ax.tick_params(width=2.2,        # line thickness of the ticks
                  length=7,         # length of the tick lines
                  direction='out')  # optional: point ticks outward

plt.sca(ax)
#plt.xlim(-3.5, 0.5)
plt.yticks(np.arange(0,9.01,1.5))
plt.xticks(np.arange(-3,0.01,0.5))
plt.ylim(-0.3, 9)
plt.xlim(0.1, -3)
plt.grid(True)
plt.xlabel(f'maximum radial wind\n{mdict["scatter_x_label"]} [m/s]')
plt.ylabel('maximum tangential wind\nlast day average [m/s]')
plt.savefig(f'{figdir}/scatter_max_radi.png', dpi=200)
plt.show()

