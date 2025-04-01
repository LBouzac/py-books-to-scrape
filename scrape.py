import csv
import requests
import bs4

def scrape_website(url):
    # Send an HTTP GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page with BeautifulSoup
        soup = bs4.BeautifulSoup(response.text, 'html.parser')

        # List to store book information
        books = []

        # Find all book containers on the page
        book_containers = soup.find_all('article', class_='product_pod')
        for book in book_containers:
            # Extract the necessary information for each book
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text
            price_without_tax = book.find('p', class_='price_color').text  # Adjust this selector if necessary
            product_page_link = book.h3.a['href']
            universal_product_code = book.find('p', class_='instock availability').text.strip()  # Adjust this selector if necessary
            number_available = book.find('p', class_='instock availability').text.strip()  # Adjust this selector if necessary
            product_description = book.find('p', class_='instock availability').text.strip()  # Adjust this selector if necessary
            category = book.find('p', class_='instock availability').text.strip()  # Adjust this selector if necessary
            review_rating = book.p['class'][1]
            image_url = book.img['src']

            # Add the book information to the list
            books.append([title, price, price_without_tax, product_page_link, universal_product_code, number_available, product_description, category, review_rating, image_url])

        # Write the book information to a CSV file
        with open('books.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Write the header of the CSV file
            writer.writerow(['Title', 'Price', 'Price without tax', 'Product page link', 'Universal product code', 'Number available', 'Product description', 'Category', 'Review rating', 'Image URL'])
            # Write the book data rows
            writer.writerows(books)

    else:
        # Print an error message if the request failed
        print(f"failed {url}. Status code: {response.status_code}")