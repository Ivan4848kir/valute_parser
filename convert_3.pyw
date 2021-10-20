import requests
import json
import tkinter as tk
from datetime import date
data=0
adr='https://www.cbr-xml-daily.ru/daily_json.js'
def req(link):
    try:
        s=requests.get(link)
        data=s.json()
        status='Связь установлена'
        usd=data['Valute']['USD']['Value']
        eur=data['Valute']['EUR']['Value']
    except:
        status='Сбой связи'
        usd=0
        eur=0
    tx='Курсы валют на %10s\nUSD: %5.2f\nEUR: %5.2f\nMy USD: %10.2f\nMy EUR: %10.2f\nAll money: %10.2f' % (date.today(),usd,eur,usd*2000,eur*2000,(eur*2000)+(usd*2000))
    return status, tx
def ref():
    mon=req(adr)
    label_st['text']=mon[0]
    label_val['text']=mon[1]
mon=req(adr)
window=tk.Tk()
frame_st=tk.Frame()
label_st=tk.Label(master=frame_st, text=mon[0])
frame_st.pack()
frame_val=tk.Frame()
label_val=tk.Label(master=frame_val, text=mon[1])
frame_val.pack()
label_st.pack()
label_val.pack()
button_st=tk.Button(master=frame_st, text='Обновить', command=ref)
button_st.pack()
window.mainloop()


    



      
            




