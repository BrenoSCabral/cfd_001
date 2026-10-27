import numpy as np
import matplotlib.pyplot as plt

ttot = 30
diag = 2
f = -9.81 # gravidade
ci = 2

dts = [0.5, 1, 2, 5, 10]

def sol_analitica(t):
    return ci + f * t

t_fino = np.linspace(0, ttot, 500)

fig, axes = plt.subplots(2, 3, figsize=(15, 7))
ax_dif = axes.flat[-1]

for dt, ax in zip(dts, axes.flat):

    nn = int(round(ttot / dt))

    u = [ci] # solução numérica
    tt = [0.0] # tempos salvos

    u_c = ci
    for n in range(1, nn + 1):
        u_p = u_c + f * dt
        tempo = n * dt

        resto = tempo % diag
        if np.isclose(resto, 0) or np.isclose(resto, diag):
            u.append(u_p)
            tt.append(tempo)

        u_c = u_p

    tt = np.array(tt)
    u = np.array(u)

    # analítica contínua + numérica com pontos
    ax.plot(t_fino, sol_analitica(t_fino), color='k', lw=1.5, label='Sol. Analítica')
    ax.plot(tt, u, marker='o', ms=5, lw=1, ls='--', color='tab:red', label='Sol. Numérica')
    ax.set_title(f'dt = {dt} s')
    ax.set_xlabel('tempo (s)')
    ax.set_ylabel('u (m/s)')
    ax.grid(True)
    ax.legend()

    # diferença nos tempos de diagnóstico
    dif = sol_analitica(tt) - u
    ax_dif.plot(tt, dif, marker='o', ms=4, label=f'dt = {dt} s')

ax_dif.axhline(0, color='k', lw=0.8)
ax_dif.set_title('Analítica - Numérica')
ax_dif.set_xlabel('tempo (s)')
ax_dif.set_ylabel('diferença (m/s)')
ax_dif.grid(True)
ax_dif.legend(fontsize=8)
ax_dif.set_ylim(-1, 1)

plt.tight_layout()
# plt.show()

plt.savefig("/Users/breno/doutorado/cfd_amb_oce/cfd_001/result.png", dpi=300)