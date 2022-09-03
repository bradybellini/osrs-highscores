import httpx
import re
from bs4 import BeautifulSoup

with httpx.Client() as client:
    r = client.get("https://secure.runescape.com/m=hiscore_oldschool_hardcore_ironman/group-ironman/?groupName=gamers+grove")

bs = BeautifulSoup(r.text, 'html.parser')
# groups = bs.find_all('tbody', attrs={"data-test": ''})
# groups = bs.find_all('tr', class_='uc-scroll__table-row')
groups = bs.find_all('tr',class_='uc-scroll__table-row')

formatted_groups = []

for group in groups:
    data = {
        'group_id': group['data-test'],
        'group_name': group.find_all('td')[1].text,
        'group_rank': group.find_all('td')[0].text,
        'group_total_level': group.find_all('td')[2].text,
        'group_total_xp': group.find_all('td')[3].text
    }
    formatted_groups.append(data)


print(formatted_groups)
