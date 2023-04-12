# Web-Scrapping using Beautifulsoup

Projek ini dikembangkan sebagai salah satu capstone project dari Algoritma Academy Data Analytics Specialization. Deliverables yang diharapkan dari projek ini adalah melakukan simple webscrapping untuk mendapatkan informasi dengan menggunakan salah satu library dari python yaitu BeautifulSoup4. Adapun website yang diambil adalah berasal dari https://www.exchange-rates.org/history/IDR/USD/T. Website tersebut berisikan data time series mengenai  pergerakan harga Kurs US Dolar ke Rupiah. Adapun range waktu yang diambil kurang lebih selama 6 bulan, yaitu mulai dari 12-Oktober-2022 hingga 7-April 2023. Setelah dilakukan web crapping, juga mengaplikasikan EDA dan Wrangling Data dan Visualisasi menggunakan jupyter notebook untuk mendapatkan insight dan menarik kesimpulan. Pada projek ini juga akan memanfaatkan flask dashboard sederhana untuk menampilkan hasil scrap dan visualisasi data movement exchange rate USD to IDR.

## Tahap awal

yaitu dengan membuat environment baru yang berisikan requirement-requirement library yang dibutuhkan dalam projek ini

## Dependencies yang dibutuhkan

- beautifulSoup4
- pandas
- flask
- matplotlib

Atau bisa dengan menginstall requirements.txt dengan cara berikut

```python
pip install -r requirements.txt
```

## Rubics

- Environment preparation (2 points)
- Finding the right key to scrap the data  & Extracting the right information (5 points)
- Creating data frame & Data wrangling (5 points)
- Creating a tidy python notebook as a report. (2 points)
- Implement it on flask dashboard (2 points)


## Syntax-syntax untuk menjalankan projek


```python
table = soup.find(___)
tr = table.find_all(___)
```


```python
df = pd.DataFrame(name of your tupple, columns = (name of the columns))
```


```python
df = scrap(___) #insert url here
```




### Sumber Data


(Medium) Data kurs US Dollar ke rupiah dari `https://www.exchange-rates.org/history/IDR/USD/T`

    * Dari halaman tersebut carilah `harga harian`, dan `tanggal`
    * Bualah plot pergerakan kurs USD 
    



Thanks !
