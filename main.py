import os
import re
import json
import xmltodict 

#se abre el archivo xml como un string
with open("SAPGW_Error_Log_20201123145005.xml","r",encoding="utf-8") as archivo:
    XmlString=archivo.read()
    
#se elimina caracteres invalidos del string    
XmlString= XmlString.replace("&","&amp;") 
XmlString= XmlString.replace('<?xml version="1.0" encoding="utf-8"?>',"")

#se convierte a objeto XML
Xml = xmltodict.parse(XmlString)
JsonString =str( Xml["SAPGW_ERROR_LOG"]["item"]["REQUEST_DATA"]["HTTP_BODY"]) #Se extra el Json del Xml

#se deshace el cambio en del caracter invalido y se crea el objeto json
JsonString = JsonString.replace("&amp;","&")
JsonSap = json.loads(JsonString)


#se guarda el json en disco 
with open("JsonSap.json","w",encoding="utf-8") as file:
			 json.dump(JsonSap,file,indent=4)

#print(JsonSap["jobReports"][2]["report"][0]["Type"])
print("success!")
input()