
class CColors(object):

    def __init__(self):
        pass
    
    def __lee(self, cadena):
        if cadena[-1]=='\n':
            cadena=cadena[:-1]
        cadena=cadena.split(' ')
        for i in range(len(cadena)):
            cadena[i]=eval(cadena[i])
        return cadena
    
    def __lee_cadenas(self, cadena):
        if cadena[-1]=='\n':
            cadena=cadena[:-1]
        cadena=cadena.split(' ')
        return cadena
    
    def __leer(self, fitxer):
        contenido=[]
        linia=fitxer.readline()
        contenido.append(self.__lee_cadenas(linia))    
        while True:
            linia=fitxer.readline()
            if not linia:
                fitxer.close()
                break
            contenido.append(self.__lee(linia))
        return contenido
    
    def __probabilitat(self, centre,colors):
        distancia=[]
        for i in range(len(colors)):
            R=centre[0]-colors[i][0]
            G=centre[1]-colors[i][1]
            B=centre[2]-colors[i][2]
            distancia.append(R*R+G*G+B*B)
        cerca=distancia[0]
        fila=0
        #print "Distancies: " ,distancia
        for i in range(1,len(distancia)):
            if (distancia[i]<cerca):
                fila=i
                cerca = distancia[i]
        return fila+1
    
    def __ordena(self, x, y):
        if x[2] < y[2] :
            rst = 1
        elif x[2] > y[2] :
            rst = -1
        else :
            rst = 0
        return rst
    
    
    ##suponent que centres=[[[centre0],num_pixels],[[centre1],num_pixels1]...]
    def diu_colors(self, centres):
        fitxer=open("colors.txt","r")
        colors=self.__leer(fitxer)
        num_pixels=0
        for i in range (len (centres)):
            num_pixels+=centres[i][1]
        taula_centres_prob=[colors[0][3:],[0,0,0,0,0,0,0,0,0,0,0]]
        pixels = []
        for i in range (len(centres)):
            fila=self.__probabilitat(centres[i][0],colors[1:])
            prob = colors[fila][3:]
            #print "Distancia desde ",centres[i][0], "fins a " , pixels, ": ", fila
            pixels.append(colors[fila][:3])                         #Obtens el codi RGB del color que es!!
            ponderacio=(float(centres[i][1])/num_pixels)*100
            #print "Ponderacio: " , centres[i][1] ,"/", num_pixels ," = ", ponderacio
            centres[i].append(ponderacio)
            max = [0,0]
            for j in range(len(prob)):
                taula_centres_prob[1][j]+=prob[j]
                if prob[j] > max[0]:
                    max[0] = prob[j]
                    max[1] = j
            centres[i].append(taula_centres_prob[0][max[1]])       
            #print "Taula Centres: " , taula_centres_prob
        #print "Llista de centres: ", centres
        centres.sort(self.__ordena)
        #print "Colors taula: ", pixels
        #print "LLista de centres O : ", centres
        #print "Taula_centres_prob :" , taula_centres_prob
        return centres          
        
        
