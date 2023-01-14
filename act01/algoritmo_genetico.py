import random
import itertools
import math
import grafica
import graf_aptos

class Individuo:
    def __init__(self,cromosoma,x,aptitud,id,cromosomaBinario):
        self.cromosoma = cromosoma
        self.x = x
        self.aptitud = aptitud
        self.id = id
        self.cromosomaBinario = cromosomaBinario

class Genes():
    def __init__(self,id,gen,probMuta,muta):
        self.gen = gen
        self.probMuta = probMuta
        self.id = id
        self.muta = muta


class Pareja:
    def __init__(self,idParejas,probCruza):
        self.idParejas = idParejas
        self.probCruza = probCruza


def probabilidad_cruza(pob):
    listID = []
    for x in range(0,len(pob)):
        listID.append(pob[x].cromosoma)
    parejas = list(itertools.combinations(listID, 2))
    return parejas
    
 
def decimal_a_binario(decimal):
    if decimal <= 0:
        return "0"
    # Aquí almacenamos el resultado
    binario = ""
    # Mientras se pueda dividir...
    while decimal > 0:
        # Saber si es 1 o 0
        residuo = int(decimal % 2)
        # E ir dividiendo el decimal
        decimal = int(decimal / 2)
        # Ir agregando el número (1 o 0) a la izquierda del resultado
        binario = str(residuo) + binario
    return binario

def binario_a_decimal(binario):
    posicion = 0
    decimal = 0
    # Invertir la cadena porque debemos recorrerla de derecha a izquierda
    # https://parzibyte.me/blog/2019/06/26/invertir-cadena-python/
    binario = binario[::-1]
    for digito in binario:
        # Elevar 2 a la posición actual
        multiplicador = 2**posicion
        decimal += int(digito) * multiplicador
        posicion += 1
    return decimal

def calcularX(xmin,i,intervalo):
    return xmin + i * intervalo

# Función cuadrática.
def f1(x):
    return (x**2)*(math.e**x) *(math.cos(10*x))

def porcentaje():
    valor = random.randint(0,100)
    valor = valor/100
    return valor



#ESTOS METODOS SE ESTARAN REPITIENDO HASTA QUE EL ALGORITMO RECIBA SU VALOR PARA PARAR
def nuevosIndividuos(POBLACION, numBits, xmin, xinterval,xmax,id_ind,PMAX):
    #AQUI EMPIEZA LA CRUZA
    #Seleccion de parejas que pueden cruzar
    PC = 0.60
    parejas = probabilidad_cruza(POBLACION) #todas las posibles parejas para cruza
    print(str(parejas))

    paresCruzas = []
    for x in parejas:
        probCruza = porcentaje()
        if probCruza <= PC:
            temp = list(tuple(x))
            paresCruzas.extend(temp) #Aqui se almacenan las parejas que si van a poder cruzarse

    print("ARR: ParesCruza:")
    print(paresCruzas)
    #Cruza
    cruzBin = []
    for x in paresCruzas:
        for i in range(0,len(POBLACION)):
            if x == POBLACION[i].cromosoma:
                cruzBin.append(POBLACION[i].cromosomaBinario) #CONVIERTE A BINARIO EL VALOR DE LOS INDIVIDUO A CRUZAR
                break
    print("CRUZBIN")
    print(cruzBin)

    #Se define el punto de cruza de todos los individuos que se cruzaran
    puntoCruza =  round(5/2)
    newPob = []
    #Se generan los nuevos individuos, que pasaran a la mutacion
    for x in range(0,len(cruzBin),2):
        val1 = cruzBin[x]
        val2 = cruzBin [x+1]
        cruzBin[x] = val1
        cruzBin[x+1] = val2
        newVal1 = val1[0:puntoCruza] + val2[puntoCruza:]
        newVal2 = val2[0:puntoCruza] + val1[puntoCruza:]
        newPob.append(newVal1)
        newPob.append(newVal2)

    print("Poblacion antes de mutar:")
    print(newPob)

    #MUTACION
    PMI = 0.60
    PMG = 0.50

    ##MUTA EL INDIVIDUO?
    arrGenes = []

    for x in range(0,len(newPob)):
        PMI_ind = porcentaje()
        print("PROBABILIDAD QUE MUTE EL INDIVIDUO:"+str(PMI_ind))
        if PMI_ind <=  PMI:
            genes = newPob[x]
            print("El valor "+newPob[x]+" mutara")
            newPob[x]='x'
            for i in range(0,len(genes)):
                PMG_ind = porcentaje()
                muta = False
                if PMG_ind <= PMG:
                    muta = True 
                arrGenes.append(Genes(x,genes[i], PMG_ind,muta))
            #MUTA POR GEN

    c = 0
    for x in arrGenes:
        print("El gen le pertenece al nuevo individuo "+ str(x.id)+" gen num "+str(c)+ " : "+str(x.gen) + " probabilidad de mutar:"+ str(x.probMuta)+" ¿Muta?"+str(x.muta))
        c = c+1
    c = 0

            
    for gen in arrGenes:
        if gen.muta == True:
            if gen.gen == '0':
                gen.gen = '1'
            else:
                gen.gen = '0'


    individuoNuevo = 0
    genmutado = ''
    genesmutados = []
    
    for gen in arrGenes:
        genmutado = genmutado+gen.gen
        if len(genmutado) == numBits:
            genesmutados.append(genmutado)
            genmutado = ''



        

    c = 0
    for x in arrGenes:
        print("El gen le pertenece al nuevo individuo "+ str(x.id)+" gen num "+str(c)+ " gen despues de mutar: "+str(x.gen) )
        c = c+1
    c = 0

    y = 0
    print("NEWPOB")
    print(newPob)
    print("GENESMUTADOS")
    print(genesmutados)
    for x in range(0,len(newPob)):
        if newPob[x] == 'x':
            newPob[x] = genesmutados[y]
            y = y+1
    y = 0
    print("poblacion despues de mutar")
    print(newPob)

    PoblacionNueva = []
    for x in newPob:
        cromosoma = binario_a_decimal(x)
        xPob = calcularX(xmin, cromosoma, xinterval)
        funcion = f1(xPob)
        if xPob < xmin or xPob>xmax:
            xPob = "OUT"
            funcion = "OUT"
        PoblacionNueva.append(Individuo(cromosoma,xPob,funcion,id_ind,x)) 
        id_ind = id_ind +1

    print("POSIBLES POBLADORES NUEVOS")
    for poblador in PoblacionNueva:
        print("Individuo "+str(poblador.cromosoma) + " x del individuo "+str(poblador.x)+" Ind en binario "+str(poblador.cromosomaBinario)+ " y su aptitud es de:"+str(poblador.aptitud))
        if poblador.x != "OUT":
            POBLACION.append(poblador)
            

    print("POBLACION DESPUES DE AGREGAR LOS NUEVOS INDIVIDUOS")

    POBLACION = sorted(POBLACION,key=lambda poblador: poblador.aptitud, reverse=True)
    for poblador in POBLACION:
        print("ID:"+str(poblador.id)+"| Individuo "+str(poblador.cromosoma) + " x del individuo "+str(poblador.x)+" Ind en binario "+str(poblador.cromosomaBinario)+ " y su aptitud es de:"+str(poblador.aptitud))

    #PODA
    while len(POBLACION) > PMAX:
        POBLACION.pop()
    print("Nueva poblacion despues de la poda")
    for poblador in POBLACION:
        print("Individuo "+str(poblador.cromosoma) + " x del individuo "+str(poblador.x)+" Ind en binario "+str(poblador.cromosomaBinario)+ " y su aptitud es de:"+str(poblador.aptitud))
    
    return POBLACION







#CONFIGURAACIONES INICIALES DEL ALGORITMO

if __name__ == '__main__':
    id_ind = 0
    PMAX = random.randint(3,7)
    numGeneraciones = 5
    PINICIAL = (random.randint(2,5))
    xmin = -20 #DADO POR EL USUARIO
    xmax = 20 #DADO POR EL USUARIO
    rango = xmax - xmin
    xinterval = 1
    numpuntos = (rango/xinterval) + 1
    numPuntosBi = str(decimal_a_binario(numpuntos))
    numBits = len(numPuntosBi)
    POBLACION = []


    for x in range(PINICIAL):
        POBLACION.append(Individuo(random.randint(0,10),0,0,id_ind,''))
        id_ind = id_ind + 1
    print("El rango es = "+str(rango))
    print("La cantidad de puntos es = "+ str(numpuntos))
    print("La cantidad de bits es = "+ str(numBits))
    print("Poblacion Inicial: "+str(PINICIAL))
    print('La poblacion maxima es:'+str(PMAX))


#IMPRIME EL CROMOSOMA DE LOS INDIVIDUOS
    for x in range(0,len(POBLACION)):
        print("EL cromosoma del individuo "+str(POBLACION[x].id) +" es: "+str(POBLACION[x].cromosoma))

#SE CALCULA X DE LOS INDIVIDUOS, SU APTITUD Y SU BINARIO
    for i in range(0,len(POBLACION)):
        x = calcularX(xmin, POBLACION[i].cromosoma, xinterval)
        POBLACION[i].x = x
        POBLACION[i].aptitud = f1(POBLACION[i].x)
        POBLACION[i].cromosomaBinario = decimal_a_binario(POBLACION[i].cromosoma)
        while len(POBLACION[i].cromosomaBinario) < numBits:
            POBLACION[i].cromosomaBinario = "0"+ POBLACION[i].cromosomaBinario
        print("Individuo:"+str(POBLACION[i].id)+"Con cromosoma:" +str(POBLACION[i].cromosoma)+"- x: "+str(POBLACION[i].x)+" su aptitud es "+str(POBLACION[i].aptitud)+" y su binario es "+str(POBLACION[i].cromosomaBinario))

#AQUI EMPIEZA LA CRUZA
    masApto = []
    for generacion in range(numGeneraciones):
        POBLACION = nuevosIndividuos(POBLACION, numBits, xmin, xinterval,xmax,id_ind,PMAX)
        masApto.append(POBLACION[0])
        grafica.graficar(POBLACION,generacion)
    for apto in masApto:
        print(apto.x)
    
    graf_aptos.graficar_aptos(masApto)
    




