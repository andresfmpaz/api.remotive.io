import requests
import json
import database_operation as db_ops
from datetime import datetime
import format_util

#/Users/andresmeneses/Documents/Proyectos_AM/PythonProjects/remotiveApp
def fetch_data(url):
    # Hace una petición GET a la url especificada y retorna el texto de la
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def json_process(text):
    #print(text)
    data = json.loads(text)
    # Obtener el timestamp actual
    collection_date = datetime.now()
    job_count = data["job-count"]
    for job in data["jobs"]:
        conn = connect()
        xml = format_util.fix_xml(job['description'])
        publication_date = job['publication_date']
        pub_date = format_util.fix_date_hh24(publication_date)
        db_ops.insert(conn, job['url'], job['title'], job['company_name'], job['company_logo'], job['category'], job['job_type'], pub_date, job['candidate_required_location'], job['salary'], xml, job_count, collection_date )
    print(job_count)
    conn.close()
    
    
def connect():
    conn = db_ops.connect()
    return conn


if __name__ == "__main__":
    json_process(fetch_data("https://remotive.com/api/remote-jobs"))