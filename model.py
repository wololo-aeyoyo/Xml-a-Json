# model.py
# D. Thiebaut
# This is the model part of the Model-View-Controller
# The class holds the name of a text file and its contents.
# Both the name and the contents can be modified in the GUI
# and updated through methods of this model.
# 
from Xml import Transformar
import json
class Model:
    def __init__( self ):
        '''
        Initializes the two members the class holds:
        the file name and its contents.
        '''
        self.fileName = None
        self.fileContent = ""
        self.Json=[]
    def isValid( self, fileName ):
        '''
        returns True if the file exists and can be
        opened.  Returns False otherwise.
        '''
        try: 
            file = open( fileName, 'r' )
            file.close()
            return True
        except:
            return False

    def setFileName( self, fileName ):
        '''
        Se encarga de actualizar el campo del json y ademas de parcearlo
        '''
        if self.isValid( fileName ):
            self.fileName = fileName
            with open(self.fileName,"r",encoding="utf-8") as archivo:
                XmlString=archivo.read()
            self.Json = Transformar.XmltoJson(XmlString)
            self.fileContents=self.Json[0]
            
            print(self.fileContents)
            
            #self.fileContents = open( fileName, 'r' ).read()
            
        else:
            self.fileContents = ""
            self.fileName = ""
            
    def getFileName( self ):
        '''
        Returns the name of the file name member.
        '''
        return self.fileName

    def getFileContents( self ):
        '''
        Returns the contents of the file if it exists, otherwise
        returns an empty string.
        
        '''
        return self.fileContents
    
    def writeDoc( self, text,rutaCuadro ):
        '''
        checkea si el xml era valido y luego manda a ecribir en disco el jonson
        ademas manda el pop up respectivo
        '''
        print(rutaCuadro)
        if self.isValid( self.fileName ):
            if self.Json[0] != "":
                with open("JsonSap.json","w",encoding="utf-8") as file:
                    json.dump(self.Json[1],file,indent=4)
                return True
            else: return False
            """
            with open(self.fileName,"r",encoding="utf-8") as archivo:
                XmlString=archivo.read()
            Status = Transformar.XmltoJson(XmlString)
            print(Status)
            

            fileName = self.fileName + ".bak"
            file = open( fileName, 'w' )
            file.write( text )
            file.close()"""
            