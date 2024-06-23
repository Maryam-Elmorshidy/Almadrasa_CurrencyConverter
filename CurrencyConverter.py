import requests 

initial_currency = input("enter initial currency : ") 
target_currency = input("enter target currency : ") 

while True :
    try : 
        amount = float(input("enter amount that you want : "))
    except: 
        print("amount should be a numeric value")
        continue

    if amount == 0 :
        print("your amount should be bigger than zero")
        continue
    else:
        break


url = ("https://api.apilayer.com/fixer/convert?to="+ 
       target_currency +"&from="+ initial_currency 
       +"&amount="+ str(amount))

payload = {}
headers= {
  "apikey": "Jw9aSaIPHBznauuHDYs0FVPA18bICpL3"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code

if (status_code != 200) :
    print("there was a problem , try again")
    quit()


result = response.json()

print(f'{amount} {initial_currency} = {result['result']} {target_currency}')