class CAlgorisme(object):
    
    def Calcular_distancia(self,x,y):
        z = []
        dist = 0
        for i in range (len(x)):
            z.append(x[i]-y[i])
            dist += z[i]*z[i]
            return dist

    def Recalcular_centres(self,Con, Col, Cen):
        Nous = []
        for x in range (len(Cen)):
            Nous.append([0,0,0])
            CenR = 0
            CenG = 0
            CenB = 0
            count = 0
            i = 0
            for y in Con:
                #print x, "==", y
                if (x==y) :
                    CenR += Col[i][0]
                    #print CenR
                    #print i
                    CenG += Col[i][1]
                    CenB += Col[i][2]
                    count +=1
                    #print count
                i+=1
            if count != 0:
                Nous[x][0] = CenR/count
                Nous[x][1] = CenG/count
                Nous[x][2] = CenB/count
        return Nous

    def Comprovar_final(self,Cen1,Cen2):
        trobat = True
        for x in range(len(Cen1)):
            if (trobat):
                trobat = (Cen1[x]==Cen2[x])
        return trobat
    
    def K_means(self,Colors,Centres):
        #print "Entro a K_means"
        Contadors = []
        Centres2 =[]
        for i in range (len(Colors)):
            Contadors.append(0)
        for j in range (len(Centres)):
            Centres2.append([0,0,0])
        final = False
        while(not final):
            for i in range (len(Centres)):
                for j in range (3):
                    Centres2[i][j]=Centres[i][j]
                
            for x in range (len(Colors)):
                con = 0
                minim = 0
                dist = 0
                for y in range(len(Centres)):
                    dist = self.Calcular_distancia(Colors[x],Centres[y])
                    if (y==0):
                        minim = dist
                    else:
                        if(dist < minim):
                            minim = dist
                            con = y

                Contadors[x] = con
            Centres = self.Recalcular_centres(Contadors,Colors,Centres)
            final = self.Comprovar_final(Centres,Centres2)
        Centres_i_pixels = [[]]
        #print "PASSA EL WHILE"
        for x in range (len(Centres)):
            #print Centres[x]
            #print Centres_i_pixels
            if (x == 0):
                Centres_i_pixels[x].append(Centres[x])
            else:
                Centres_i_pixels.append([Centres[x]])
            cont = 0
            for y in Contadors:
                if (y==x):
                    cont += 1
            Centres_i_pixels[x].append(cont)
        return Centres_i_pixels

