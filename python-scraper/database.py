import pyodbc 

server = 'DESKTOP-RS7QS73' 
database = 'WEB_SCRAPING' 
username = 'root' 
password = 'root' 
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

def insert_user(user):
    user_id = user['user_id']
    user_name = user['name']
    photo = user['photo']
    papers = user['papers']

    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = '{user_id}'")
    row = cursor.fetchone()

    if row == None:
        cursor.execute(f"INSERT INTO users (id, name, image) VALUES ('{user_id}', '{user_name}', '{photo}')")
        for paper in papers:
            name = paper['name']
            year = paper['year']
            cit = paper['cit']
            link = paper['link']
            cursor.execute(f"INSERT INTO papers (name, year, cit, url, user_id) VALUES ('{name}', {year}, {cit}, '{link}', '{user_id}')")
    else:
        cursor.execute(f"UPDATE users SET name='{user_name}', image='{photo}' WHERE id='{user_id}'")
        cursor.execute(f"DELETE FROM papers WHERE user_id='{user_id}'")
        for paper in papers:
            name = paper['name']
            year = paper['year']
            cit = paper['cit']
            link = paper['link']
            cursor.execute(f"INSERT INTO papers (name, year, cit, url, user_id) VALUES ('{name}', {year}, {cit}, '{link}', '{user_id}')")

    conn.commit()

