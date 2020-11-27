import os
import re
import json
import xmltodict 

#se abre el archivo xml como un string
#with open("SAPGW_Error_Log_20201123145005.xml","r",encoding="utf-8") as archivo:
#    XmlString=archivo.read()
class Transformar:
    
    def XmltoJson(Objecto):   
        #se elimina caracteres invalidos del string 
        XmlString=str(Objecto)   
        XmlString= XmlString.replace("&","&amp;") 
        XmlString= XmlString.replace('<?xml version="1.0" encoding="utf-8"?>',"")

        #se convierte a objeto XML
        try:
            Xml = xmltodict.parse(XmlString)
            JsonString =str( Xml["SAPGW_ERROR_LOG"]["item"]["REQUEST_DATA"]["HTTP_BODY"]) #Se extra el Json del Xml
        except:
            print("failed to parsed XML") 
            return [""]
               

        #se deshace el cambio en del caracter invalido y se crea el objeto json
        JsonString = JsonString.replace("&amp;","&")
        JsonSap = json.loads(JsonString)
        print("epale")
        return JsonString,JsonSap

#print(JsonSap["jobReports"][2]["report"][0]["Type"])
#print("success!")
#input()