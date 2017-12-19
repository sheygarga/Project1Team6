import requests as req
import json
import xmltodict
from bs4 import BeautifulSoup
from xml.etree.ElementTree import fromstring
#import xml.etree.ElementTree as ET
from xmljson import Parker, parker

api_key = "X1-ZWz1g600175l3f_18y6r"
endpoint = "http://www.zillow.com/webservice/GetRegionChildren.htm?"
state = "ca"
child_type1 = "neighborhood"
child_type2 = "zipcode"

params = {
    "zws-id" : api_key,
    "state" : state,
    "childtype": child_type2


}

url1 = "http://www.zillow.com/webservice/GetRegionChildren.htm?zws-id=X1-ZWz1g600175l3f_18y6r&state=ca&city=ojai&childtype=zipcode"
url2 = "http://www.zillow.com/webservice/GetRegionChildren.htm?zws-id=X1-ZWz1g600175l3f_18y6r&state=ca&city=sylmar&childtype=zipcode"
url3 = "http://www.zillow.com/webservice/GetRegionChildren.htm?zws-id=X1-ZWz1g600175l3f_18y6r&state=ca&city=beverlyhills&childtype=zipcode"
url4 = "http://www.zillow.com/webservice/GetRegionChildren.htm?zws-id=X1-ZWz1g600175l3f_18y6r&state=ca&city=crescenta-montrose&childtype=zipcode"
url5 = "http://www.zillow.com/webservice/GetRegionChildren.htm?zws-id=X1-ZWz1g600175l3f_18y6r&state=ca&city=longbeach&childtype=zipcode"
url6 = "http://www.zillow.com/webservice/GetRegionChildren.htm?zws-id=X1-ZWz1g600175l3f_18y6r&state=ca&city=santabarbara&childtype=zipcode"

urls = [url1,url2,url3,url4,url5,url6]

#url = "http://www.zillow.com/webservice/GetRegionChildren.htm?zws-id=X1-ZWz1g600175l3f_18y6r&state=wa&city=seattle&childtype=neighborhood"

for url in urls:
    zillow_response = req.get(url)

    with open('zillow_response.xml', 'w') as f:
        f.write(zillow_response.text)
        
    def parse_xml(xml):
        soup = BeautifulSoup(xml)
        return soup

    if __name__ == '__main__':
        with open('zillow_response.xml', 'r') as zillow_xml:
            xml_contents = zillow_xml.read()
        #soup = parse_xml(xml_contents)
        #print(soup.prettify())
        temp_file = json.dumps(parker.data(fromstring(xml_contents)), indent=4 )
        temp2_file = json.loads(temp_file)
        print(temp2_file['response']['list']['region'][0])




#print(tree.tag)