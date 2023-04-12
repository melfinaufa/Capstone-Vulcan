from flask import Flask, render_template
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from bs4 import BeautifulSoup 
import requests

#don't change this
matplotlib.use('Agg')
app = Flask(__name__) #do not change this

#insert the scrapping here
url_get = requests.get('https://www.exchange-rates.org/history/IDR/USD/T')
soup = BeautifulSoup(url_get.content,"html.parser")

#find your right key here
table = soup.find('tbody')
row = table.find_all('a', attrs={'class':'w'})

row_length = len(row)

temp = [] #initiating a list 

for i in range(1, row_length):
#insert the scrapping process here
    #scrapping process
    #get date 
    date = table.find_all('a', attrs={'class':'w'})[i].text
    
    #get price
    price = table.find_all('span', attrs={'class':'w'})[i].text
    price = price.strip().replace('$1 = Rp','')#to remove excess white space and symbols, sehingga menjadi angka
    
    
    temp.append((date,price)) 

    

#temp = temp[::-1]

#change into dataframe
df = pd.DataFrame(temp, columns = ('Date','Dolar to Rupiah'))


#insert data wrangling here

df['Date'] = df['Date'].astype('datetime64')
df['Dolar to Rupiah'] = df['Dolar to Rupiah'].str.replace(',','.')
df['Dolar to Rupiah'] = df['Dolar to Rupiah'].astype('float64')

#reindexing to fill the missing value
exchange_rate = df.set_index('Date')
periode = pd.date_range(start= '2022-10-12', end = '2023-04-07')
exchange_rate = exchange_rate.reindex(periode).ffill().bfill()

#end of data wranggling 

@app.route("/")
def index(): 
	
	card_data = f'{exchange_rate["Dolar to Rupiah"].mean().round(2)}' #be careful with the " and ' 

	# generate plot
	ax = exchange_rate.plot(figsize = (15,8)) 
	
	# Rendering plot
	# Do not change this
	figfile = BytesIO()
	plt.savefig(figfile, format='png', transparent=True)
	figfile.seek(0)
	figdata_png = base64.b64encode(figfile.getvalue())
	plot_result = str(figdata_png)[2:-1]

	# render to html
	return render_template('index.html',
		card_data = card_data, 
		plot_result=plot_result
		)


if __name__ == "__main__": 
    app.run(debug=True)