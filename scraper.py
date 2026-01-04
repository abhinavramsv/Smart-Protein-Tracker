import requests
from bs4 import BeautifulSoup
import random

def get_market_price(item_name):
    """
    Attempts to scrape Google. 
    Returns: (Price, True) if connection succeeds.
    Returns: (Estimated_Price, False) if connection is blocked.
    """
    
    # 1. Setup - Pretend to be a real browser
    url = f"https://www.google.com/search?q={item_name}+price+india+1kg"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        # 2. Try to Connect
        response = requests.get(url, headers=headers, timeout=5) # 5 second timeout
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Google often puts the main answer in this class
        price_div = soup.find("div", class_="BNeawe iBp4i AP7Wnd")
        
        if price_div:
            # Clean the text (e.g., "₹ 240.00" -> 240.0)
            price_text = price_div.get_text()
            clean_price = float(''.join(filter(str.isdigit, price_text.split('.')[0])))
            
            # SUCCESS: Return Price AND "True" for Live Status
            return clean_price, True 
            
    except Exception as e:
        print(f"⚠️ Connection blocked or failed for {item_name}. Switching to Offline Mode.")

    # 3. Fallback (Simulation)
    # Returns estimated data so the app doesn't crash
    if "egg" in item_name.lower():
        price = random.randint(6, 9)
    else:
        price = random.randint(220, 260)
    
    # FAILURE: Return Price AND "False" for Live Status
    return price, False