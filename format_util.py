from bs4 import BeautifulSoup
from datetime import datetime


def fix_xml(xml):
    # Tu HTML mal formado
    #html_content = "<div><br></div>badly formatted html<br></div>"

    # Usar BeautifulSoup para 'arreglar' el HTML
    soup = BeautifulSoup(xml, "html.parser")
    well_formed_html = str(soup)

    return well_formed_html

def fix_date_hh24(date):
    formatted_date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
    return formatted_date