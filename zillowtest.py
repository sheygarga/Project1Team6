#dependencies
import requests as req
import json
import xmltodict
from bs4 import BeautifulSoup
from xml.etree.ElementTree import fromstring
#import xml.etree.ElementTree as ET
from xmljson import Parker, parker

#api call urls
url1 = "http://www.zillow.com/webservice/GetRegionChildren.htm?zws-id=X1-ZWz1g600175l3f_18y6r&state=ca&city=ojai&childtype=zipcode"
url2 = "http://www.zillow.com/webservice/GetRegionChildren.htm?zws-id=X1-ZWz1g600175l3f_18y6r&state=ca&city=sylmar&childtype=zipcode"
url3 = "http://www.zillow.com/webservice/GetRegionChildren.htm?zws-id=X1-ZWz1g600175l3f_18y6r&state=ca&city=beverlyhills&childtype=zipcode"
url4 = "http://www.zillow.com/webservice/GetRegionChildren.htm?zws-id=X1-ZWz1g600175l3f_18y6r&state=ca&city=crescenta-montrose&childtype=zipcode"
url5 = "http://www.zillow.com/webservice/GetRegionChildren.htm?zws-id=X1-ZWz1g600175l3f_18y6r&state=ca&city=longbeach&childtype=zipcode"
url6 = "http://www.zillow.com/webservice/GetRegionChildren.htm?zws-id=X1-ZWz1g600175l3f_18y6r&state=ca&city=santabarbara&childtype=zipcode"

#list of urls from above
urls = [url1,url2,url3,url4,url5,url6]


#will become a list of list of zindex values for each place
zindex_list = []

#loops through the list of api calls
for url in urls:
    
    #gets the info from the api call
    zillow_response = req.get(url)
    #will hold the zindex values found for the current api call
    temp_zindex = []

    #part of the xml to json conversion 
    with open('zillow_response.xml', 'w') as f:
        f.write(zillow_response.text)

    #xml to json conversion    
    def parse_xml(xml):
        soup = BeautifulSoup(xml)
        return soup
    
    #xml to json conversion with reading
    if __name__ == '__main__':
        with open('zillow_response.xml', 'r') as zillow_xml:
            xml_contents = zillow_xml.read()
        #soup = parse_xml(xml_contents)
        #print(soup.prettify())
        temp_file = json.dumps(parker.data(fromstring(xml_contents)), indent=4 )
        temp2_file = json.loads(temp_file)

        #loops through the responses 
        for loc in temp2_file['response']['list']['region']:
            #finds the zindex value for the result if it exists
            if 'zindex' in loc:
                #adds it to the list of zindex values for this location
                temp_zindex.append(loc['zindex'])
        
        #adds it to the list of lists
        zindex_list.append(temp_zindex)
        #print(temp2_file['response']['list']['region'])


#calculates average zindex value for each area
avg_list= []
for list in zindex_list:
    avg = sum(list)/len(list)
    avg_list.append(avg)

#urls for api calls to census 
ojai_call = "https://api.census.gov/data/2010/sf1?get=H0060001,NAME&for=place:53476&in=state:06"
san_call = "https://api.census.gov/data/2010/sf1?get=H0060001,NAME&for=place:66140&in=state:06"
bev_call = "https://api.census.gov/data/2010/sf1?get=H0060001,NAME&for=place:06308&in=state:06"
cres_call = "https://api.census.gov/data/2010/sf1?get=H0060001,NAME&for=place:30000&in=state:06"
lb_call = "https://api.census.gov/data/2010/sf1?get=H0060001,NAME&for=place:43000&in=state:06"
sb_call = "https://api.census.gov/data/2010/sf1?get=H0060001,NAME&for=place:69070&in=state:06"

#list of the calls
cen_calls = [ojai_call, san_call, bev_call, cres_call, lb_call, sb_call]

#empty list to be populated with the population
pop_list = []

#goes through each census call 
for cen_loc in cen_calls:   
    #gets population and adds it to the pop_list
    census_response = req.get(cen_loc).json()
    pop = int(census_response[1][0])
    pop_list.append(pop)


print(pop_list)