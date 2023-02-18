import matplotlib.pyplot as plt
import numpy as np
# print(plt.rcParams.keys())
plt.rcParams['font.sans-serif']=['SimHei']

plt.figure()
plt.subplot(2,2,1)
x=[0,1]
y=[2,3]
plt.xlabel('x轴')
plt.plot(x,y)

plt.subplot(2,2,2)
x1=np.arange(-1,5,0.5)
y1=x1**2+1
plt.plot(x1,y1)

plt.subplot(2,2,3)
x=np.linspace(0.2,6,15)
y=x**3+np.log(x)
plt.plot(x,y)

plt.subplot(2,2,4)
x=[0,1]
y=[2,3]
plt.plot(x,y)

plt.show()






