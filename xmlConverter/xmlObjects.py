from unicodedata import name
import xml.etree.cElementTree as ET
from time import sleep

class XML:
    '''This class will create an xml in default format'''
    root = ET.Element("product-import")

    item = ET.SubElement(root, "products")

    def generateXml(infos, name):
        '''This function needs the list of products and he name of the xml file'''

        ET.SubElement(XML.root, "date").text = "2020-11-30T15:15:58-03:00"

        print("-------------------------------")
        #loop que irá converter os item da lista infos

        for x in range(len(infos)):

            print("convertendo o item {}".format(x))
            print("-------------------------------")
            # sleep(0.5)
        
            produto = ET.SubElement(XML.item, "product")

            #loop que cadastra as infos do produto x
            for key in infos[x].keys():

                #pular o date
                if(infos[x][key] == "date"):

                    continue

                #preenche os campos do xml
                ET.SubElement(produto, key).text = infos[x][key]
            
        tree = ET.ElementTree(XML.root)

        tree.write("{}.xml".format(name))

        print("Concluido")
        print("-------------------------------")