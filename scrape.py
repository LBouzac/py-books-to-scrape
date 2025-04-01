import requests
import bs4

# scrap de https://books.toscrape.com

def scrape_website(url):
    # Envoie de la requête HTTP GET
    response = requests.get(url)

    # Vérification du statut de la réponse
    if response.status_code == 200:
        # Parsing HTML content
        soup = bs4.BeautifulSoup(response.text, 'html.parser')

        # Trouver les titres de livres
        book_titles = soup.find_all('h3')
        for title in book_titles:
            print(title.get_text())
    else:
        print(f"Echec {url}. Status code: {response.status_code}")