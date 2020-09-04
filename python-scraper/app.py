from scrapper import get_user
from database import insert_user

links = [
    "https://scholar.google.com/citations?user=CDt8mKsAAAAJ&hl=es&oi=ao",
    "https://scholar.google.com/citations?user=c9ZEN0YAAAAJ&hl=es&oi=ao",
    "https://scholar.google.com/citations?user=CfFNecwAAAAJ&hl=es&oi=ao",
    "https://scholar.google.com/citations?user=VREZXUYAAAAJ&hl=es&oi=ao",
    "https://scholar.google.com/citations?user=NxtJVCgAAAAJ&hl=es&oi=ao",
    "https://scholar.google.com/citations?user=NKRP2VEAAAAJ&hl=es&oi=ao",
    "https://scholar.google.com/citations?user=POQ1BD0AAAAJ&hl=es&oi=ao"
]

for link in links:
    user = get_user(link)
    insert_user(user)