'''
Created on 19/05/2012

@author: PractiquesIATeam
'''
import sys
from PyQt4 import QtCore, QtGui
from CForm import Ui_widget
import Image
from CAlgorisme import *
import random
from CColors import *
import time


class Principal(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.__finestra = Ui_widget()
        self.__finestra.setupUi(self)
        self.__llista_pixels = []
        self.__llista_centres = []
        self.connect(self.__finestra.bsortir,QtCore.SIGNAL('clicked()'),QtCore.SLOT('close()'))
        self.connect(self.__finestra.baplicar,QtCore.SIGNAL('clicked()'),self.aplica_algorisme)
        self.connect(self.__finestra.bbuscar,QtCore.SIGNAL('clicked()'),self.__navega)
        self.__algorisme = CAlgorisme()
        
    def __mostrar_imatge(self,fn): 
        self.__finestra.escena.clear()
        img = QtGui.QImage()
        img.load(fn)                                           
        self.__finestra.escena.addPixmap((QtGui.QPixmap(img)))
        #print "S'ha carregat la imatge!"
        
    def __carregapixels(self,fn):
        self.__llista_pixels = []
        pic = Image.open(fn)
        for i in range(pic.size[0]):
            for j in range(pic.size[1]):
                self.__llista_pixels.append(pic.getpixel((i,j)))
        #print self.__llista_pixels
        #print "Pixels carregats!"
        self.__mostrar_imatge(fn)
            
    def __navega(self):
        name = self.__finestra.explora.getOpenFileName(self, "Open image file", "Open image file")
        self.__carregapixels(str(name))
        #print "S'ha seleccionat la imatge!"
        
    def __pintar_rectangles(self, colors):
        self.__finestra.escena_colors.clear()
        pen = QtGui.QPen(QtCore.Qt.black, 0, QtCore.Qt.SolidLine)
        for i in range(len(colors)):
            if colors[i][2] >= 5.00:
                self.__finestra.escena_colors.addRect(i*85, 40, 60, 30, pen, QtGui.QColor(colors[i][0][0],colors[i][0][1],colors[i][0][2]))
                text = QtGui.QGraphicsTextItem()
                text.setPos(float(i*85), float(20))
                text.setPlainText(colors[i][3]+" "+str("%.2f" % colors[i][2])+"%")
                self.__finestra.escena_colors.addItem(text)
            #self.__finestra.escena_colors.addText(colors[i][3])
        #print "rectangles pintats!"
    
    def __generar_centres(self,k):
        for x in range(k):
            y = random.randint(1,len(self.__llista_pixels))
            self.__llista_centres.append(self.__llista_pixels[y])
    
    def aplica_algorisme(self):
        t = time.clock()
        self.__llista_centres = []
        k = int(self.__finestra.TextField.text())
        self.__generar_centres(k)
        llista = self.__algorisme.K_means(self.__llista_pixels, self.__llista_centres)
        #print "Print de K-means: ", llista
        color = CColors()
        color.diu_colors(llista)
        #print "Diu Colors: ", llista
        self.__pintar_rectangles(llista)
        print "Temps promig: %.2f sec" % (time.clock() - t)


def main():
    app = QtGui.QApplication(sys.argv)
    finestra = Principal()
    finestra.setVisible(True)
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
