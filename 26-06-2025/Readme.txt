 
Objective:
Scrape top headlines from a news website (Indian Express) and save them in a `.txt` file.  

Tools Used:
- Python (via **PyCharm IDE**)  
- 'requests' (for fetching HTML content)  
- `BeautifulSoup` (for parsing HTML and extracting headlines)  

---


How to Run the Script  
  Prerequisites 
  1. Python 3.13 installed  
  2. Required libraries:  
     pip install requests beautifulsoup4
  3. PyCharm(or any Python IDE)
                       
Steps to Execute  
1. Clone or download the script (`indian_express_scraper.py`).  
2. Run the script  in PyCharm (or via terminal):  
  
   python indian_express_scraper.py
   
3. Output:
   - The script fetches headlines from [Indian Express](https://indianexpress.com/).  
   - Saves them in `indian_express_headlines.txt`.  
   - Prints success message with the number of headlines scraped.  

input:
    https://www.thehindu.com/news/national/ or your choice                   

Expected Output (`indian_express_headlines.txt`)
    1. India refuses to sign joint statement in SCO summit
    2. Himachal flash floods: Several rescued as search operation to find missing people intensified
    3. Ahmedabad Air India flight crash probe: AAIB yet to appoint lead investigator; delay is 'inexplicable and inexcusable', says Congress leader Jairam Ramesh
    4. Two women Maoists killed in Narayanpur
    5. Ahmedabad plane crash: Government says data extraction from black boxes underway
    6. Russia assures timely delivery of remaining S-400 air defence system during bilateral meeting with Rajnath
    7. Operation Sindhu: 272 Indians, 3 Nepalese nationals evacuated from Iran
    8. Encounter between terrorists, security forces breaks out in Jammu and Kashmir’s Udhampur
    9. ‘Language is the soul of a nation, not merely a medium of communication,’ says Union Minister Amit Shah
    10. Navy staffer held for leaking Operation Sindoor details, other classified info to Pakistani handler
    11. Ahmedabad Air India plane crash: Government says data extraction from black boxes under way
    12. India calls out Pakistan unwarranted aspersions, attempts to deflect attention from atrocities against children at UN
    13. Can India push Pakistan into FATF’s ‘Grey list’
    14. Ministry of Railways introduces key reforms for train controllers
    15. Poor deprived of their right to dream: Rahul Gandhi flags rising costs of houses
    16. Two killed, 10 missing after vehicle carrying pilgrims falls into Alaknanda river in Uttarakhand
    17. We must unite in our fight against terrorism for our collective safety, security: Rajnath Singh in SCO meet in China


Troubleshooting
  Error: `ModuleNotFoundError` (missing `requests` or `bs4`)  
     Fix: Run `pip install requests beautifulsoup4`.  
  
  Error:-Website blocking the request  
     Fix: Update `headers` in the script with a newer User-Agent.  
  
  No headlines found
        Fix:Check if the website structure changed (update `soup.find_all()` selectors).  


Conclusion:-
This script automates the extraction of news headlines from **Indian Express**, demonstrating **web scraping** with Python. It can be extended for other websites or data analysis tasks.  
