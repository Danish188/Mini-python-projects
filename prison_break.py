import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# function to scrap data from the url 
def data_from_url(url , tagname , class_name):
    response = requests.get(url)
    if response.status_code != 200:
        print("HTTP 404: Page not found!")
        
    else:
        # getting data in form of html
        soup = BeautifulSoup(response.text , "html.parser")
        # find the data according to tag
        html_output = soup.find(tagname , {"class":class_name})
        # read the html string using pandas
        output = pd.read_html(str(html_output))
        
    return output[0]

url = "https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes"

data = data_from_url(url , "table" , "wikitable")
# convert Date column from string to datetime
data["Date"] = pd.to_datetime(data["Date"])

print(data.info())
# plot the graph of the data
data_plot = data["Date"].dt.year.value_counts().plot(kind= "bar" ,
                                                     xlabel = "Year" ,
                                                     ylabel = "No. of Escapes" ,
                                                     title = "prison Breaks" ,
                                                     figsize = (12,6))
# show the plot
plt.show()