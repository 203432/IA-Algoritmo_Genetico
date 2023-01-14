import matplotlib.pyplot as plt



def graficar_aptos(aptos):
    x=[]
    y=[]
    i = 1
    for apto in aptos:
        x.append(i)
        i = i+1
        y.append(apto.aptitud)
    plt.title('Evolucion del individuo mas apto a traves de las generaciones',color='red',size=10, family='arial')

    plt.plot(x,y,linestyle='solid',color='blue')
    plt.plot(x,y,'o',color='r')
    plt.xlabel('Numero de la generacion')
    plt.ylabel('Aptitud')
    plt.show()
