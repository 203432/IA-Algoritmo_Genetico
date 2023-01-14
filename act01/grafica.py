from matplotlib import pyplot 
import algoritmo_genetico
import math
# Función cuadrática.
def f1(x):
    return (x**2)*(math.e**x) *(math.cos(10*x))

def graficar(POBLACION,generacion):
    pyplot.title('Grafica de la funcion: f(x) = (x**2)*(math.e**x) *(math.cos(10*x)\n Generacion:'+str(generacion+1),color='red',size=10, family='arial')
    print(POBLACION[0].x)
    # Valores del eje X que toma el gráfico.
    x = range(-70, 70)
    # Graficar ambas funciones.
    pyplot.plot(x, [f1(i) for i in x])
    # Establecer el color de los ejes.
    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="red")
    # Limitar los valores de los ejes.
    pyplot.xlim(-14, 20)
    pyplot.ylim(-10, 30)
    pyplot.xlabel('X_axis\nIndividuo mas apto de esta generacion'+str(POBLACION[0].x)+' tiene una aptitud de: '+str(POBLACION[0].aptitud), size = 6)
    pyplot.ylabel('Y_axis', size = 14)

    dots = []
    for individuo in POBLACION:
        pyplot.annotate("Individuo: "+str(individuo.cromosoma), (individuo.x, individuo.aptitud))
        dot = pyplot.scatter(individuo.x, individuo.aptitud)

    # Guardar gráfico como imágen PNG.
    pyplot.savefig("output.png")

    # Mostrarlo.
    pyplot.show()