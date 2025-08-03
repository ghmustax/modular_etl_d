from imports import *

def setup_logger(log_name="pipeline_log", log_dir="logs"):
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, f"{log_name}_{datetime.now().strftime('%Y-%m-%d')}.log")

    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format="%(asctime)s — %(levelname)s — %(message)s",
        filemode="a"
    )
    return logging.getLogger()

# Ejemplo de uso desde cualquier script
# from logger import setup_logger
# logger = setup_logger()
# logger.info("Inicio de pipeline")