# 🔌 Sistema
import os
import re
import csv
import json
import mimetypes
import time
import logging
from pathlib import Path
from datetime import datetime

# 📦 Entorno y descarga
from dotenv import load_dotenv
import requests
from urllib.parse import urlsplit
import shutil

# 📊 Dataframes
import polars as pl
import pandas as pd

# 📁 Excel
from openpyxl import load_workbook

# ⏱️ Progreso
from tqdm import tqdm



