from imports import *

start = time.time()

print(f"📂 Origen: {CARPETA_ORIGEN.resolve()}")
print(f"📂 Trabajo: {CARPETA_TRABAJO.resolve()}")
print(f"📄 Consolidado: {ARCHIVO_CONSOLIDADO.name}\n")

limpiar_archivos_previos(CARPETA_TRABAJO, ARCHIVO_CONSOLIDADO)

xlsx_files = list(CARPETA_ORIGEN.glob("*.xlsx"))
csv_paths = []

for file in tqdm(xlsx_files, desc="🔄 Convertir XLSX a CSV"):
    nombre = file.stem
    destino = CARPETA_TRABAJO / f"{nombre}.csv"
    xlsx_to_csv_limpio(file, destino, separador=SEPARADOR)
    csv_paths.append(destino)

with open(ARCHIVO_ESQUEMA, "r", encoding="utf-8") as f:
    esquema = {col: pl.Utf8 for col in json.load(f)}

dataframes = []
for archivo in tqdm(csv_paths, desc="📥 Cargando CSVs"):
    df = pl.read_csv(archivo, separator=SEPARADOR, schema=esquema, ignore_errors=True)
    dataframes.append(normalizar(df))

df_final = pl.concat(dataframes, how="vertical")
df_final.write_csv(ARCHIVO_CONSOLIDADO, separator=SEPARADOR)
print(f"\n✅ Consolidado guardado: {ARCHIVO_CONSOLIDADO.name}")

# 📝 Log de ejecución
end = time.time()
with open(ARCHIVO_LOG, 'w', encoding='utf-8') as f:
    f.write(f"🕒 Tiempo total: {round(end - start, 2)} segundos\n")
    f.write(f"✅ Archivos procesados: {len(csv_paths)}\n")
    f.write(f"🔢 Registros consolidados: {df_final.shape[0]}\n")