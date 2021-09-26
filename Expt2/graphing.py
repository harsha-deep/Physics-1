import matplotlib.pyplot as plt

time = [] # fill values
theta = [] # fill values

for i in range(len(theta)):
    theta[i] = theta[i] + 5.1
    
# plt.plot(time, theta)
# plt.title('theta v/s time')
# plt.show()          #uncomment these two lines to get plot of theta vs time

dtheta = []
for i in range(len(theta)-1):
    dtheta.append(theta[i+1]-theta[i]/(time[i+1]-time[i]))
dtheta.append(0)
plt.plot(theta, dtheta)
plt.title('phase portrait')
plt.show()
