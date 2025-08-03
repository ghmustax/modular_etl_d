from imports import *

load_dotenv()

CARPETA_ORIGEN = Path(os.getenv("CARPETA_ORIGEN"))
CARPETA_TRABAJO = Path(os.getenv("CARPETA_TRABAJO"))
ARCHIVO_CONSOLIDADO = Path(os.getenv("ARCHIVO_CONSOLIDADO"))
ARCHIVO_LOG = Path(os.getenv("ARCHIVO_LOG"))
ARCHIVO_ESQUEMA = Path(os.getenv("ARCHIVO_ESQUEMA"))
SEPARADOR = os.getenv("SEPARADOR", "|")