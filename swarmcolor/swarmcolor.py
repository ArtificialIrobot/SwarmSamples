import numpy as np
import matplotlib
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

gradient = ['#D207ED','#D107EC','#D007EB','#D007EA','#CF07E9','#CE07E9','#CE08E8','#CD08E7','#CC08E6','#CC08E5','#CB08E5','#CA09E4','#CA09E3','#C909E2','#C809E1','#C809E1','#C709E0','#C60ADF','#C60ADE','#C50ADD','#C40ADD','#C40ADC','#C30BDB','#C20BDA','#C20BD9','#C10BD9','#C00BD8','#C00CD7','#BF0CD6','#BE0CD5','#BE0CD5','#BD0CD4','#BC0CD3','#BC0DD2','#BB0DD1','#BA0DD1','#BA0DD0','#B90DCF','#B80ECE','#B80ECE','#B70ECD','#B60ECC','#B60ECB','#B50FCA','#B40FCA','#B40FC9','#B30FC8','#B20FC7','#B20FC6','#B110C6','#B010C5','#B010C4','#AF10C3','#AE10C2','#AE11C2','#AD11C1','#AC11C0','#AC11BF','#AB11BE','#AA12BE','#AA12BD','#A912BC','#A812BB','#A812BA','#A712BA','#A613B9','#A613B8','#A513B7','#A413B6','#A413B6','#A314B5','#A214B4','#A214B3','#A114B3','#A014B2','#A014B1','#9F15B0','#9E15AF','#9E15AF','#9D15AE','#9C15AD','#9C16AC','#9B16AB','#9A16AB','#9A16AA','#9916A9','#9817A8','#9817A7','#9717A7','#9617A6','#9617A5','#9517A4','#9418A3','#9418A3','#9318A2','#9218A1','#9218A0','#91199F','#90199F','#90199E','#8F199D','#8E199C','#8E1A9B','#8D1A9B','#8C1A9A','#8C1A99','#8B1A98','#8A1A98','#8A1B97','#891B96','#881B95','#881B94','#871B94','#861C93','#861C92','#851C91','#841C90','#841C90','#831D8F','#821D8E','#821D8D','#811D8C','#801D8C','#801D8B','#7F1E8A','#7E1E89','#7E1E88','#7D1E88','#7C1E87','#7C1F86','#7B1F85','#7A1F84','#7A1F84','#791F83','#782082','#782081','#772080','#762080','#76207F','#75207E','#74217D','#74217D','#73217C','#72217B','#72217A','#712279','#702279','#702278','#6F2277','#6E2276','#6E2275','#6D2375','#6C2374','#6C2373','#6B2372','#6A2371','#6A2471','#692470','#68246F','#68246E','#67246D','#66256D','#66256C','#65256B','#64256A','#642569','#632569','#622668','#622667','#612666','#602665','#602665','#5F2764','#5E2763','#5E2762','#5D2762','#5C2761','#5C2860','#5B285F','#5A285E','#5A285E','#59285D','#58285C','#58295B','#57295A','#56295A','#562959','#552958','#542A57','#542A56','#532A56','#522A55','#522A54','#512B53','#502B52','#502B52','#4F2B51','#4E2B50','#4E2B4F','#4D2C4E','#4C2C4E','#4C2C4D','#4B2C4C','#4A2C4B','#4A2D4A','#492D4A','#482D49','#482D48','#472D47','#472E47']
# Make data.
X = np.arange(-3, 3, 0.01)
Y = np.arange(-3, 3, 0.01)
X, Y = np.meshgrid(X, Y)
#declaring z value
Z = -((1.0+np.cos(12.0*np.sqrt((X**2.0)+(Y**2.0))))/(0.5*((X**2)+(Y**2))+2))

num_func_params = 2
num_swarm = 100
position = -3 + 6 * np.random.rand(num_swarm, num_func_params)
temp = -3 + 6 * np.random.rand(num_swarm, num_func_params)
posx= [[0 for xx in range(100)] for yy in range(200)]
posy = [[0 for xx in range(100)] for yy in range(200)]
velocity = np.zeros([num_swarm, num_func_params])
personal_best_position = np.copy(position)
personal_best_value = np.zeros(num_swarm)

for i in range(num_swarm):
    # Z = (1-X)**2 + 1 *(Y-X**2)**2
    #personal_best_value[i] = (1 - position[i][0]) ** 2 + 1 * (position[i][1] - position[i][0] ** 2) ** 2
	personal_best_value[i] = -((1.0+np.cos(12.0*np.sqrt((position[i][0]**2.0)+(position[i][1]**2.0))))/(0.5*((position[i][0]**2)+(position[i][1]**2))+2))
	
tmax = 200
c1 = 0.001
c2 = 0.002
levels = np.linspace(-1, 35, 100)
global_best = np.min(personal_best_value)
global_best_position = np.copy(personal_best_position[np.argmin(personal_best_value)])

for t in range(tmax):
	for i in range(num_swarm):
		error = -((1.0+np.cos(12.0*np.sqrt((position[i][0]**2.0)+(position[i][1]**2.0))))/(0.5*((position[i][0]**2)+(position[i][1]**2))+2))
		if personal_best_value[i] > error:
			personal_best_value[i] = error
			personal_best_position[i] = position[i]
	best = np.min(personal_best_value)
	best_index = np.argmin(personal_best_value)
	if global_best < best:
		global_best = best
		global_best_position = np.copy(personal_best_position[best_index])

	for i in range(num_swarm):
        # update velocity
		velocity[i] += c1 * np.random.rand() * (personal_best_position[i] - position[i]) \
						+ c2 * np.random.rand() * (global_best_position - position[i])
		temp[i] = position[i]
		position[i] += velocity[i]
	for i in range(num_swarm):

		posx[t][i] = position[i][0]
		posy[t][i] = position[i][1]


	fig = plt.figure()
	ax1 = plt.axes()
	CS = plt.contour(X, Y, Z, levels=levels, cmap=cm.gist_stern)
	plt.gca().set_xlim([-3, 3])
	plt.gca().set_ylim([-3, 3])
    # setting color
	fig.colorbar(CS, shrink=0.5, aspect=5)
	for i in range(t+1):
		for j in range (num_swarm):
			ax1.scatter(posx[i][j],posy[i][j],color=gradient[(tmax-1)-(t-i)], s=50,zorder=100)
	for i in range(num_swarm):
		ax = plt.axes()
		ax.arrow(temp[i][0],temp[i][1], position[i][0]-temp[i][0], position [i][1]-temp[i][1], head_width=0.2, head_length=0.1, zorder=100)
		ax1.scatter(position[i][0],position[i][1],color= 'black',s=50,zorder=110)
	ax.scatter(global_best_position[0], global_best_position[1],color='red',s=50,zorder=1200)
	plt.title('{0:03d}'.format(t))
	filename = 'frame{0:03d}.png'.format(t)
	plt.savefig(filename, bbox_inches='tight')
	plt.close(fig)