CREATE DATABASE WEB_SCRAPING;

create table users(
id varchar(20) primary key,
name varchar(200),
image varchar(500)
)

create table papers(
id int IDENTITY(1,1) primary key,
name varchar(200),
year int,
cit int,
url varchar(500),
user_id varchar(20),
foreign key (user_id) references users(id)
)