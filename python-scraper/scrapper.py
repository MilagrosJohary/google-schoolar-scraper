from bs4 import BeautifulSoup
import requests

base_link = "https://scholar.google.com"

# Scrapear usuario por link
# Devuelve un usuario con su detalle
def get_user(user_link):
    
    # Obtener el id de usuario del link
    query_params = user_link.split("?")[1]

    user_id = ""
    for param in query_params.split("&"):
        splited_param = param.split("=")
        if (splited_param[0] == "user"):
            user_id = splited_param[1]


    response = requests.get(url=user_link)

    html = BeautifulSoup(response.text, 'html.parser')
    user_name = html.find(id="gsc_prf_in").text
    photo = html.find(id="gsc_prf_pua").img['src']
    if photo.split('/')[1] == "citations":
        photo = base_link + photo

    books = []

    books_blocks = html.find_all(class_="gsc_a_tr")
    for book in books_blocks:
        block_info = book.find(class_="gsc_a_t")
        block_cit = book.find(class_="gsc_a_c")
        block_year = book.find(class_="gsc_a_y")

        name = block_info.a.text
        link = base_link + block_info.a['data-href']
        cit = int(block_cit.a.text) if block_cit.a.text != "" else 0
        year = int(block_year.span.text) if block_year.span.text != "" else 0

        books.append({
            "name": name,
            "cit": cit,
            "year": year,
            "link": link
        })


    user = {
        "user_id": user_id,
        "name": user_name.upper(),
        "papers": books,
        "photo": photo
    }
    return user