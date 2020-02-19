from sko.PSO import PSO
import numpy as np
import matplotlib.pyplot as plt



def same(l, u, O, a, r):
    return ((a * u + (l + O) * (r * a)) / (a * O * u))


def lambda_0(N, l, u, R, C, O, a, r):
    if R < C * ((same(l, u, O, a, r) * (N + 1) / 2) + (N - 1) / (2 * l)):
        return 0
    else:
        return l


def lambda_1(N, l, u, R, C, O, a, r):
    if R <= C * ((same(l, u, O, a, r) * (N + 1)) / 2 + same(l, u, O, a, r) - (1 / (l + O))):
        return 0
    elif  C * ((same(l, u, O, a, r) * (N + 1)) / 2 + same(l, u, O, a, r) - (1 / (l + O))) < R <= \
        C * \
        ((same(l, u, O, a, r) * (N + 1)) / 2 + (a * u + (l + O) *(r * a)) / (a * O * u - l * (l + O)) - (1 / (l + O))):
        return (a * O * u) / (l + O) - ((a * u + (l + O) * (r * a)) / (l + O)) * \
               ((R / C) - (same(l, u, O, a, r) * (N + 1) / 2) + (1 / (l + O))) ** (-1)
    elif R > C * \
        ((same(l, u, O, a, r) * (N + 1) / 2) + (a * u + (l + O) * (r * a)) / (a * O * u - l * (l + O)) - (1 / (l + O))):
        return l


def social(l_0, l_1, N, l, u, R, C, O, a, r):
    if l_0 != 0:
        return ((a * l_0 * u * R * (l + O)) / (a * u * O - l_1 * a * (l + O) + l_0 * (a * (l + O) + a * u + r * (l + O)))) - \
               (C / (a * u * O - l_1 * a * (l + O) + l_0 * (a * (l + O) + a * u + r * (l + O)))) * \
               ((l_0 * (a * u + (l + O) * (r + a)) * (N + 1) / 2) + (a * (u * O - l_1 * (l + O)) * (N - 1) / 2) + \
                ((a * l_0 * l_1 * (l + O) * (a * u + (l + O) * (r + a))) / (a * O * u - l_1 * (l + O))) - \
                a * l_0 * l_1 + (a * r) * l * l_0)
    else:
        return 0


'''关于a'''
M = np.arange(0.5, 1.9, 0.05)
x1 = []
y1 = []
for i in range(len(M)):
    x1.append(lambda_0(N=4, l=1, u=3, R=8, C=2, O=3, a=M[i], r=1))
    y1.append(lambda_1(N=4, l=1, u=3, R=8, C=2, O=3, a=M[i], r=1))
# print(x1)
# print('\n')
# print(y1)

x2 = []
y2 = []
for i in range(len(M)):
    def social1(l_0, l_1):
        N = 4
        l = 1
        u = 3
        R = 8
        C = 2
        O = 3
        a = M[i]
        r = 1
        if l_0 != 0:
            return ((a * l_0 * u * R * (l + O)) / (a * u * O - l_1 * a * (l + O) + l_0 * (a * (l + O) + a * u + r * (l + O)))) - \
                   (C / (a * u * O - l_1 * a * (l + O) + l_0 * (a * (l + O) + a * u + r * (l + O)))) * \
                   ((l_0 * (a * u + (l + O) * (r + a)) * (N + 1) / 2) + (a * (u * O - l_1 * (l + O)) * (N - 1) / 2) + \
                    ((a * l_0 * l_1 * (l + O) * (a * u + (l + O) * (r + a))) / (a * O * u - l_1 * (l + O))) - \
                    a * l_0 * l_1 + (a * r) * l * l_0)
        else:
            return 0

    def test(l_0, l_1):
        return -social1(l_0, l_1)
    pso = PSO(func=test, dim=2, pop=100, max_iter=2000, lb=[0, 0], ub=[1, 1], w=0.9, c1=2, c2=2)
    pso.run()
    x2.append(pso.gbest_x[0])
    y2.append(pso.gbest_x[1])

y2 = np.where(np.array(x2) == 0, np.array(x2), np.array(y2))
# print(x2)
# print(y2)

s1 = []
s2 = []
for i in range(len(M)):
    s1.append(social(l_0=x1[i], l_1=y1[i], N=4, l=1, u=3, R=8, C=2, O=3, a=M[i], r=1))
    s2.append(social(l_0=x2[i], l_1=y2[i], N=4, l=1, u=3, R=8, C=2, O=3, a=M[i], r=1))
s1 = np.where(np.array(s1) < 0, 0, np.array(s1))
# print(s1)
# print(s2)

'''关于r'''
P = np.arange(0.1, 3.1, 0.1)
x3 = []
y3 = []
for i in range(len(P)):
    x3.append(lambda_0(N=4, l=1, u=3, R=8, C=2, O=3, a=1, r=P[i]))
    y3.append(lambda_1(N=4, l=1, u=3, R=8, C=2, O=3, a=1, r=P[i]))


x4 = []
y4 = []
for i in range(len(P)):
    def social1(l_0, l_1):
        N = 4
        l = 1
        u = 3
        R = 8
        C = 2
        O = 3
        a = 1
        r = P[i]
        if l_0 != 0:
            return ((a * l_0 * u * R * (l + O)) / (a * u * O - l_1 * a * (l + O) + l_0 * (a * (l + O) + a * u + r * (l + O)))) - \
                   (C / (a * u * O - l_1 * a * (l + O) + l_0 * (a * (l + O) + a * u + r * (l + O)))) * \
                   ((l_0 * (a * u + (l + O) * (r + a)) * (N + 1) / 2) + (a * (u * O - l_1 * (l + O)) * (N - 1) / 2) + \
                    ((a * l_0 * l_1 * (l + O) * (a * u + (l + O) * (r + a))) / (a * O * u - l_1 * (l + O))) - \
                    a * l_0 * l_1 + (a * r) * l * l_0)
        else:
            return 0

    def test(l_0, l_1):
        return -social1(l_0, l_1)
    pso = PSO(func=test, dim=2, pop=100, max_iter=2000, lb=[0, 0], ub=[1, 1], w=0.9, c1=2, c2=2)
    pso.run()
    x4.append(pso.gbest_x[0])
    y4.append(pso.gbest_x[1])
y4 = np.where(np.array(x4) == 0, np.array(x4), np.array(y4))


s3 = []
s4 = []
for i in range(len(P)):
    s3.append(social(l_0=x3[i], l_1=y3[i], N=4, l=1, u=3, R=8, C=2, O=3, a=1, r=P[i]))
    s4.append(social(l_0=x4[i], l_1=y4[i], N=4, l=1, u=3, R=8, C=2, O=3, a=1, r=P[i]))
s3 = np.where(np.array(s3) < 0, 0, np.array(s3))


plt.rcParams['figure.dpi'] = 110 # 图片分辨率
fig = plt.figure(figsize=(9,8))
ax1 = fig.add_subplot(1, 2, 1)
# ax1.plot(M, x1, color = 'red', linestyle = '-', marker = 'o', markerfacecolor='none', label = r'$\lambda_0^e$')
# ax1.plot(M, y1, color = 'limegreen', linestyle = '-', marker = '^', markerfacecolor='none', label = r'$\lambda_1^e$')
ax1.plot(M, x2, color = 'red', linestyle = '-', marker = 's', markerfacecolor='none', label = r'$\lambda_0^*$')
ax1.plot(M, y2, color = 'green', linestyle = '-', marker = '.', label = r'$\lambda_1^*$')
ax1.set_xlabel(r'$\alpha$')
ax1.set_ylabel( r'$\lambda_0^*\ and\ \lambda_1^*$')
ax1.set_title('(a)')
ax1.legend(loc = 'best')


ax3 = fig.add_subplot(1, 2, 2)
# ax3.plot(M, s1, color = 'red', linestyle = '-', marker = 's', markerfacecolor='none', \
#          label = r'S($\lambda_0^e$, $\lambda_1^e$)')
ax3.plot(M, s2, color = 'red', linestyle = '-', marker = '^',  markerfacecolor='none', label = r'S($\lambda_0^*$, $\lambda_1^*$)')
ax3.set_xlabel(r'$\alpha$')
ax3.set_ylabel(r'$S(\lambda_0^*,\lambda_1^*)$')
ax3.set_title('(b)')
ax3.legend(loc = 'best')


fig = plt.figure(figsize=(9,8))
ax2 = fig.add_subplot(1, 2, 1)
# ax2.plot(P, x3, color = 'red', linestyle = '-', marker = 'o', markerfacecolor='none', label = r'$\lambda_0^e$')
# ax2.plot(P, y3, color = 'limegreen', linestyle = '-', marker = '^', markerfacecolor='none', label = r'$\lambda_1^e$')
ax2.plot(P, x4, color = 'red', linestyle = '-', marker = 's', markerfacecolor='none', label = r'$\lambda_0^*$')
ax2.plot(P, y4, color = 'green', linestyle = '-', marker = '.', label = r'$\lambda_1^*$')
ax2.set_xlabel(r'$\gamma$')
ax2.set_ylabel( r'$\lambda_0^*\ and\ \lambda_1^*$')
ax2.set_title('(a)')
ax2.legend(loc = 'best')


ax4 = fig.add_subplot(1, 2, 2)
# ax4.plot(P, s3, color = 'red', linestyle = '-', marker = 's', markerfacecolor='none', \
#          label = r'S($\lambda_0^e$, $\lambda_1^e$)')
ax4.plot(P, s4, color = 'red', linestyle = '-', marker = '^', markerfacecolor='none', label = r'S($\lambda_0^*$, $\lambda_1^*$)')
ax4.set_xlabel(r'$\gamma$')
ax4.set_ylabel(r'$S(\lambda_0^*,\lambda_1^*)$')
ax4.set_title('(b)')
ax4.legend(loc = 'best')

plt.show()