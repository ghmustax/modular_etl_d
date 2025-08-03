
from imports import *

# ⬇️ Detectar extensión desde headers HTTP
def obtener_extension(headers):
    if "Content-Disposition" in headers:
        match = re.search(r'filename="?([^"]+)"?', headers["Content-Disposition"])
        if match:
            return Path(match.group(1)).suffix
    content_type = headers.get("Content-Type", "")
    return mimetypes.guess_extension(content_type) or ".bin"

# 🧼 Limpieza de texto
def limpiar_valor(valor):
    if isinstance(valor, str):
        valor = valor.replace(",", "").replace("\n", " ").replace("\r", " ").replace("\t", " ").strip()
        valor = ' '.join(valor.split())
    return valor

# 🧽 Normalización masiva con Polars
def normalizar(df: pl.DataFrame):
    return df.select([
        pl.col(col).cast(str).str.strip_chars().str.replace_all(r"\s+", " ")
        for col in df.columns
    ])

# 📚 Lectura adaptativa por extensión
def leer_archivo(path: Path):
    ext = path.suffix.lower()

    if ext == ".csv":
        return pl.read_csv(path, ignore_errors=True)
    elif ext == ".txt":
        return pl.read_csv(path, separator="\t", ignore_errors=True)
    elif ext == ".xlsx":
        wb = load_workbook(path)
        ws = wb.active
        filas = [
            [limpiar_valor(cell) for cell in row]
            for row in ws.iter_rows(values_only=True)
        ]
        return pl.DataFrame(filas)
    elif ext == ".json":
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return pl.DataFrame(data)
    return None

# 🧹 Limpieza de archivos previos
def limpiar_archivos_previos(carpeta_trabajo: Path, archivo_consolidado: Path):
    for archivo in carpeta_trabajo.glob("*.csv"):
        try:
            archivo.unlink()
            print(f"🗑️ Eliminado: {archivo.name}")
        except Exception as e:
            print(f"⚠️ No se pudo eliminar {archivo.name}: {e}")
    if archivo_consolidado.exists():
        try:
            archivo_consolidado.unlink()
            print(f"🗑️ Consolidado eliminado: {archivo_consolidado.name}")
        except Exception as e:
            print(f"⚠️ Error al eliminar consolidado: {e}")

# 🔄 Conversión XLSX → CSV limpio
def xlsx_to_csv_limpio(xlsx_path: Path, csv_path: Path, separador='|'):
    wb = load_workbook(xlsx_path)
    ws = wb.active
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=separador)
        for row in ws.iter_rows(values_only=True):
            row_limpia = [
                str(cell).replace(",", "").replace("\n", " ").replace("\r", " ").replace("\t", " ").strip()
                if isinstance(cell, str) else cell
                for cell in row
            ]
            writer.writerow(row_limpia)

# 📦 Consolidación final
def consolidate_and_save(dataframes: list, output_path: Path, sep='|'):
    df = pl.concat(dataframes, how='vertical', rechunk=True)
    df.write_csv(output_path, separator=sep)
    print(f"✅ Consolidado exportado en: {output_path.name}")