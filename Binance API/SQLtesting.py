import sqlite3
from sqlite3 import Error
from openpyxl import Workbook #pip install openpyxl
from openpyxl.utils import get_column_letter
import requests
import time
import urllib
import csv
import sys
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime
import json

binance_url = 'https://api.binance.com/api/v3/ticker/price'
binance_time_url = 'https://api.binance.com/api/v1/time'

current_time_request = requests.get(binance_time_url).content

response = requests.get(binance_url).content
print(json.loads(response))
# dict_keys = list(response[0].keys())

# def create_connection(db_file=':memory:'):
#     try:
#         conn = sqlite3.connect(db_file) 
#         return conn
#     except Error as e:
#         print(e)

#     return None

# def create_table(conn, create_table_sql):
#     try:
#         c = conn.cursor()
#         c.execute(create_table_sql)
#     except Error as e:
#         print(e)

# if __name__ == '__main__':

#     sql_create_employees_table = """ CREATE TABLE IF NOT EXISTS employees (
#         id integer PRIMARY KEY,
#         plan_code integer NOT NULL,
#         race text NOT NULL,
#         gender text NOT NULL,
#         eeo_code string NOT NULL,
#         annual_salary float NOT NULL,
#         annual_hours_worked integer NOT NULL ) """
    
#     conn = create_connection(f'eeocCounter.sqlite3')

#     if conn is not None:
#         create_table(conn, sql_create_employees_table)
#     else:
#         print("Failed to create database connection.")


# conn.close()
# conn = create_connection(f'eeocCounter.sqlite3')
# sql = """
# INSERT INTO employees (
#     id,
#     plan_code,
#     race,
#     gender,
#     eeo_code,
#     annual_salary,
#     annual_hours_worked)
# VALUES (?,?,?,?,?,?,?);
# """