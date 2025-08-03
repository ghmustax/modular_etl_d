# Proyecto ETL Snowflake - Nueva Versión

Este proyecto contiene un pipeline ETL modular que permite consolidar archivos `.xlsx` en formato `.csv` y subirlos a Snowflake.

## 🔧 Tecnologías utilizadas
- Snowflake SQL
- Python (módulos reutilizables con logging personalizado)
- Pandas / Polars (opcional)
- Git para versionamiento

## 🎯 Objetivo
Centralizar información contenida en múltiples fuentes Excel, transformarla, limpiar formatos de fechas, y cargarla de forma eficiente a Snowflake usando credenciales seguras.

## 📦 Estructura del proyecto
etl_nuevo_proyecto/ 
│ 
├── README.md
├── src/ │  
├── extractor.py 
│   
├── transformer.py 
│   
├── loader.py 
│   └── logger.py 
├── data/ 
│   └── raw/ 
├── config/ 
│   └── .env


## 🛡️ Seguridad
El archivo `.env` no se sube al repositorio. Contiene tus credenciales y debe estar en el `.gitignore`.

## 🧠 Autor
Diego – Cloud Intelligence & Data Engineer  

## repositorio git 
diego.hincapie.s
https://github.com/ghmustax/modular_etl_d.git

