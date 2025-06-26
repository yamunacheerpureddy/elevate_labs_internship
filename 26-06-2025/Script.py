import requests
from bs4 import BeautifulSoup


def scrape_news_headlines(url, output_file):
    try:
        # Send a GET request to the website with headers to mimic a browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # To Raise an error for bad status

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        headlines = soup.find_all(['h2', 'h3'],
                                  class_=lambda x: x and ('title' in x.lower() or 'headline' in x.lower()))

        # If no headlines found with class filter, try more general approach
        if not headlines:
            headlines = soup.find_all(['h2', 'h3'])

        # Extract text from headlines and clean it
        cleaned_headlines = []
        seen_headlines = set()  #To avoid duplicates we'll use set set never allow duplicates
        for headline in headlines:
            text = headline.get_text().strip()
            if text and text not in seen_headlines:
                cleaned_headlines.append(text)
                seen_headlines.add(text)

        # Save to file
        with open(output_file, 'w', encoding='utf-8') as f:
            for i, headline in enumerate(cleaned_headlines, 1):
                f.write(f"{i}. {headline}\n")

        print(f"Successfully scraped {len(cleaned_headlines)} headlines to {output_file}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    news_url = input("Enter the url of the website=")
    output_filename = "indian_express_headlines.txt"
    # Run the scraper
    scrape_news_headlines(news_url, output_filename)
