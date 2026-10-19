import numpy as np


for dt in [0.5 , 1, 2, 5, 10]:

    ttot = 30
    diag = 2

    nn = int(ttot/dt)

    print(10*'*', ' tempo total de intergação = ', ttot, 10*'*')
    print(10*'*', ' passo de tempo = ', dt, 10*'*')
    print(10*'*', ' numero total de passos de tempo = ', nn, 10*'*')
    print(10*'*', ' intervalo de tempo para diagnostico = ', diag, 10*'*')

    f = -9.81 # gravidade

    ci = 2 # condicao inicial

    u = [ci]
    a = [ci]

    u_c = ci

    for t in range(1, nn+1):
        u_p = u_c + f * dt  
        tempo = t * dt
        a_p = ci + f * tempo
        
        if np.isclose(tempo % diag,0) or np.isclose(tempo % diag, diag):
            u.append(u_p)
            a.append(a_p)

        u_c = u_p



    print(dt)
    print(a==u)
    print(a)
    print(u)

