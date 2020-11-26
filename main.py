import os
import re
import json
import xmltodict


with open("SAPGW_Error_Log_20201123145005.xml","r",encoding="utf-8") as archivo:
    XmlString=archivo.read()
XmlString= XmlString.replace("&","&amp;") 
XmlString= XmlString.replace('<?xml version="1.0" encoding="utf-8"?>',"")
Xml = xmltodict.parse(XmlString)
JsonString =str( Xml["SAPGW_ERROR_LOG"]["item"]["REQUEST_DATA"]["HTTP_BODY"])
JsonString = JsonString.replace("&amp;","&")
JsonSap = json.loads(JsonString)



with open("JsonSap.json","w",encoding="utf-8") as file:
			 json.dump(JsonSap,file,indent=4)

print(JsonSap["jobReports"][2]["report"][0]["Type"])