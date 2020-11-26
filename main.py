import os
import re
import json
from xml.dom.minidom import parse, parseString


with open("SAPGW_Error_Log_20201123145005.xml","r",encoding="utf-8") as archivo:
    XmlString=archivo.read()
XmlString= XmlString.replace("&","&amp;") 
XmlString= XmlString.replace('<?xml version="1.0" encoding="utf-8"?>',"")
Xml = parseString(XmlString)
print(Xml)
