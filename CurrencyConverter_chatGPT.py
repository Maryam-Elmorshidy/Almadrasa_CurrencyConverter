import requests

def get_currency_input(prompt):
    return input(prompt).strip().upper()

def get_amount_input():
    while True:
        try:
            amount = float(input("Enter the amount to convert: "))
            if amount <= 0:
                print("Amount must be greater than zero. Please try again.")
            else:
                return amount
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def fetch_conversion_rate(initial_currency, target_currency, amount, api_key):
    url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={initial_currency}&amount={amount}"
    headers = {"apikey": api_key}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json().get('result')
    else:
        print(f"Error: Unable to fetch conversion rate (status code: {response.status_code})")
        return None

def main():
    initial_currency = get_currency_input("Enter the initial currency (e.g., USD): ")
    target_currency = get_currency_input("Enter the target currency (e.g., EUR): ")
    amount = get_amount_input()
    
    api_key = "Jw9aSaIPHBznauuHDYs0FVPA18bICpL3"
    
    result = fetch_conversion_rate(initial_currency, target_currency, amount, api_key)
    
    if result is not None:
        print(f"{amount} {initial_currency} = {result} {target_currency}")

if __name__ == "__main__":
    main()
