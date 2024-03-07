from threading import Thread
import requests
import time

rates = ['eur','jpy','usd','rub','cad']
bases = ['eur','jpy','usd','rub','cad']

threads = []
a=0
def main():
    threads = []
    

def fetch_rate(bases,symbols):
        a = time.time()
        web = "http://www.floatrates.com/daily/"+str(bases)+".json"
        
        response = requests.get(web)
        response.raise_for_status()
        rate = response.json()
        
        rate[bases]= {'rate':1}
        rates_line = ", ".join(
            [f"{symbol}: {float(rate[symbol]['rate']):2.04}" for symbol in symbols]
        )
        
        print(f"{bases} = {rates_line}")
        print("Time in Thread:  {:.2f}s".format(time.time()-a))
        print()
a = time.time()
for base in bases:
    thread = Thread(target=fetch_rate, args=[base,rates])
    thread.start()
    threads.append(thread)
    
while threads:    
    threads.pop().join()

b=time.time()-a
print("Time Elapsed:  {:.2f}s".format(b))
  
    
