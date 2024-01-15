import requests
from bs4 import BeautifulSoup
import csv

urls = [
    'https://distribution.giftlov.com/api/Orders/95ccc5cc-dec2-480f-a0b9-37233c064133/49f5520479158e085a8d10000cc7740a0834bbde49493a0493415cae2a57ad6a/o/15642927?r=5.611925132178843'
]

claim_codes = []

while len(urls) != 0:
    current_url = urls.pop()

    response = requests.get(current_url)

    soup = BeautifulSoup(response.content, "html.parser")

    card_elements = soup.select('#card-number')

    claim_code = {}


    if len(card_elements) == 1 :
        claim_code['url'] = current_url
        claim_code['code'] = card_elements[0].getText()
        claim_codes.append(claim_code)

print(claim_codes)

with open('codes.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)

    for claim_code in claim_codes:
        writer.writerow(claim_code.values())