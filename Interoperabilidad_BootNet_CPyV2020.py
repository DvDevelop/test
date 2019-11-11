import concurrent.futures
import requests
import threading
import time

thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

def download_site(url):
    session = get_session()
    print(f"downloading {url}")
    with session.get(url,verify=False) as response:
        print(f"Content {response.content} read {len(response.content)} from {url} status_code {response.status_code}")

def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)

if __name__ == "__main__":
    print("Crawling")
    sites = [
        #"http://intranet.censo2020.inegi.org.mx/integra/api/integracion/integrar?paquete=Lenvio_011111110_20190704_120101010_VOLUMEN2019.zip&idPaquete=10000&idEvento=2&nombreEvento=CENSOLAB",
        #"https://intranet.censo2020.inegi.org.mx/status.html",
        #"http://10.210.100.147:8081/integra/api/integracion/integrar?paquete=Lenvio_011111110_20190704_120101010_VOLUMEN2019.zip&idPaquete=10000&idEvento=2&nombreEvento=CENSOLAB",
        #"http://10.153.2.189:8300/siatl/",
        #"http://10.210.100.147:8081/integra/api/integracion/integrar?paquete=Lenvio_021111110_20190704_120102010_volumen2019.zip&idPaquete=10000&idEvento=1&nombreEvento=CENSOLAB",

        # Referencia 19 de agosto 2019
        #"http://intranet.censo2020.inegi.org.mx/integra/api/integracion/integrar?paquete=Lenvio_091111110_20190704_120109010_volumen2019.zip&idPaquete=10000&idEvento=1&nombreEvento=CENSOLAB",
        #"http://10.210.100.146:8081/integra/api/integracion/integrar?paquete=Lenvio_091111110_20190704_120109010_volumen2019.zip&idPaquete=10000&idEvento=1&nombreEvento=CENSOLAB",

        # URL con paquete sin encriptación
        #"http://intranet.censo2020.inegi.org.mx/integra/api/integracion/integrar?paquete=Lenvio_041111110_20190704_120104010_volumen2019.zip&idPaquete=10000&idEvento=1&nombreEvento=CENSOLAB",

        # Prueba 26 de agosto 2019
        #"http://intranet.censo2020.inegi.org.mx/integra/api/integracion/integrar?paquete=Lenvio_041111110_20190704_120104010_volumen2019.zip&idPaquete=10000&idEvento=1&nombreEvento=CENSOLAB",

        #Prueba 4 de septiembre 2019
        "https://www.google.com"
        #"http://intranet.censo2020.inegi.org.mx/integra/api/integracion/integrar?paquete=Lenvio_011111110_20190704_121001100_volumen2019.zip&idPaquete=10000&idEvento=192&nombreEvento=VOLUMEN2019",
    ] * 5
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Crawling downloaded {len(sites)} in {duration} seconds")
