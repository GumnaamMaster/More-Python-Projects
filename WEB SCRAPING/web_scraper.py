
# coding: utf-8

# In[20]:


import requests, pandas
from bs4 import BeautifulSoup

r = requests.get("https://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c = r.content
soup = BeautifulSoup(c,"html.parser")

base = "https://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="

values = []

last = soup.find_all("a",{"class":"Page"})[-1].text

for page in range(0,int(last)*10,10):

    print(base + str(page) + ".html")
    r = requests.get(base + str(page) + ".html")
    c = r.content
    soup = BeautifulSoup(c,"html.parser")
    all = soup.find_all("div",{"class":"propertyRow"})

    for one in all:

        craps = {}

        prices = one.find_all("h4")

        if not prices:
            craps.update({"Price":"None"})

        for price in prices:
            craps.update({"Price":price.text.replace("\n","")})

        addresses = one.find_all("span",{"class":"propAddressCollapse"})

        if not addresses:
            craps.update({"Address":"None"})

        for address in addresses:
            craps.update({"Address":address.text})

        beds = one.find_all("span",{"class":"infoBed"})

        if not beds:
            craps.update({"Beds":"None"})

        for bed in beds:

            bed = bed.find("b")
            craps.update({"Beds":bed.text})

        fullbaths = one.find_all("span",{"class":"infoValueFullBath"})

        if not fullbaths:
            craps.update({"Full Baths":"None"})

        for fullbath in fullbaths:

            fullbath = fullbath.find("b")
            craps.update({"Full Baths":fullbath.text})

        areas = one.find_all("span",{"class":"infoSqFt"})

        if not areas:
            craps.update({"Area":"None"})

        for area in areas:
            craps.update({"Area":area.text})

        halfbaths = one.find_all("span",{"class":"infoValueHalfBath"})

        if not halfbaths:
            craps.update({"Half Baths":"None"})

        for halfbath in halfbaths:

            halfbath = halfbath.find("b")
            craps.update({"Half Baths":halfbath.text})

        temp = 0
        lotscolumns = one.find_all("div",{"class":"columnGroup"})

        for lotscolumn in lotscolumns:

            lotsgroups = lotscolumn.find_all("span",{"class":"featureGroup"})

            for lotsgroup in lotsgroups:

                if "Lot Size" in lotsgroup.text:
                    temp = 1
                    lots = lotscolumn.find_all("span",{"class":"featureName"})

                    for lot in lots:
                        craps.update({"Lot Size":lot.text})

        if temp == 0:
            craps.update({"Lot Size":"None"})

        values.append(craps)

df = pandas.DataFrame(values) 
df.to_csv("Output.csv")


# In[10]:


df

