from bs4 import BeautifulSoup
import requests

base_link = "https://scholar.google.com"

def search_user(username):
    users_links = []
    users = []

    url = f"{base_link}/citations?hl=es&view_op=search_authors&mauthors={username}&btnG="
    response = requests.get(url=url)
    html = BeautifulSoup(response.text, 'html.parser')
    users_blocks = html.find_all(class_="gsc_1usr")
    for user in users_blocks:
        user_link = user.div.a['href']
        profile_link = base_link + user_link
        new_user = get_user(profile_link)
        users.append(new_user)

    return users


def get_user(user_link):
    response = requests.get(url=user_link)
    html = BeautifulSoup(response.text, 'html.parser')
    name = html.find(id="gsc_prf_in").text
    photo = html.find(id="gsc_prf_pua").img['src']

    books = []

    books_blocks = html.find_all(class_="gsc_a_tr")
    for book in books_blocks:
        book_el = book.a
        books.append({
            "name": book_el.text,
            "link": base_link + book_el['data-href']
        })

    user = {
        "name": name,
        "books": books,
        "photo": photo,
        "books_number": len(books)
    }
    return user