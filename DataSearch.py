#import libararies (these are needed to run program)
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import tkinter as tk
from tkinter import *


#function for scraping url
def get_data(url):
    # get current date
    today = datetime.now()

    # list headers from the website
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0'
    }
    # can be changed baed on website for raw data
    base_url = url

    #create table
    table = []
    #loop through scraping the url
    for i in range(1, 4):
        print('Searching Page {0}'.format(i))
        params = {
            'Page': i
        }
        r = requests.get(base_url, headers=headers, params=params)
        soup = BeautifulSoup(r.content, 'html.parser')
        table.append(pd.read_html(str(soup))[0])
    ##apply data to table and export as csv
    master = pd.concat(table)
    master = master.loc[:, master.columns[1:-1]]
    filename = today.strftime("%b-%d-%Y") + ' Crypto Table.csv'
    master.to_csv(filename, index=False)
    print('done')

def get_key_words():
    search = GoogleSearch({
        "q": "coffee",
        "api_key": "a045f0d008d3dc3c58fcfdacf218bb6d9891607b2f1a5b4facdbc6d3b1a724d9"
    })
    result = search.get_dict()

if __name__ == "__main__":
    #get_data("https://www.coingecko.com/en")
    window = tk.Tk()
    window.title('Results')
    window.geometry("300x300")
    lbl = Label(window, text="Enter URL", fg='red', font=("Helvetica", 16))
    lbl.place(x=90, y=40)
    txtfld = Entry(window, text="Enter URL", bd=5)
    txtfld.place(x=90, y=80)
    btn = Button(window,height=5,width=10, text="Run",command = lambda :get_data(txtfld.get()))
    btn.place(x=90, y=110)
    window.mainloop()
