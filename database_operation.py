import psycopg2
from psycopg2 import sql
from datetime import datetime

# Configuración de los parámetros de conexión
hostname = 'localhost'  # o la IP si es remota
database = 'remotive'
username = 'remotive_usr'
password = 'admin1234'  # Sustituye 'tu_contraseña' con la contraseña real
port_id = 5432  # Asegúrate de usar el puerto correcto en el que PostgreSQL está escuchando

def connect():
    """Create a connection to the database."""
    conn = psycopg2.connect(
        dbname=database, 
        user=username, 
        password=password, 
        host=hostname,
        port=port_id
    )
    return conn

def consult(conn, query):
    """Execute a query and return the results."""
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()  # or fetchone() if you are retrieving a single row

def insert(conn, url, title, company_name, company_logo, category, job_type,
           publication_date, candidate_required_location, salary, description, job_counting, collection_date):
    """Insert a new listing into the rmt_job_listings table."""
    try:
        with conn.cursor() as cur:
            cur.execute(sql.SQL("""
                INSERT INTO rmt_job_listings (
                    url, title, company_name, company_logo, category, job_type, 
                    publication_date, candidate_required_location, salary, 
                    description, job_counting, collection_date)
                VALUES (
                    %s, %s, %s, %s, %s, %s,to_timestamp(%s,'YYYY-MM-DD HH24:MI:SS') , %s, %s, %s, %s, %s)
                """), 
                (url, title, company_name, company_logo, category, job_type,
                publication_date, candidate_required_location, salary, description,job_counting, collection_date ))
            conn.commit()
    except psycopg2.errors.InvalidDatetimeFormat as e:
        print("Error de formato de fecha:", e)
    except psycopg2.IntegrityError as e:
        print("Error de integridad:", e)
    except Exception as e:
        print("Ocurrió un error al insertar el registro:", e)
    finally:
        cur.close()       

def update(conn, job_id, salary):
    """Update the salary for a listing."""
    with conn.cursor() as cur:
        cur.execute("UPDATE rmt_job_listings SET salary = %s WHERE id_remotive = %s", (salary, job_id))
        conn.commit()

def delete(conn, job_id):
    """Delete a listing from the rmt_job_listings table."""
    with conn.cursor() as cur:
        cur.execute("DELETE FROM rmt_job_listings WHERE id_remotive = %s", (job_id,))
        conn.commit()

