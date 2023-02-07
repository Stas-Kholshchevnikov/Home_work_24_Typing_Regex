#Файл со значениями "по умолчанию"

import os
from classes.procedure import filter_proc, map_proc, unique_proc, sort_proc, limit_proc

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data", "apache_logs.txt")

DEF_TYPE_COMMAND = {'filter': filter_proc,
                    'map': map_proc,
                    'unique': unique_proc,
                    'sort': sort_proc,
                    'limit': limit_proc}

