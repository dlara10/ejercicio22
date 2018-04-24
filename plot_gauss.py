import numpy as np
import matplotlib.pyplot as plt

d = np.loadtxt('gauss.txt')

min_t = d[:,0].min()
max_t = d[:,0].max()

i_x = d[d[:,0]==min_t, 1]
i_u = d[d[:,0]==min_t, 2]

f_x = d[d[:,0]==max_t, 1]
f_u = d[d[:,0]==max_t, 2]

plt.plot(i_x, i_u, label='inicial')
plt.plot(f_x, f_u, '--', label='final')
plt.legend()
plt.xlabel("x")
plt.ylabel("u")
plt.title('Gauss')
plt.savefig('gauss.png')
