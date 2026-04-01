import pyodbc

def obtener_conexion():
    return pyodbc.connect(
        "DRIVER={SQL Server};"
        "SERVER=CLEIUSS\\SQLEXPRESS;"
        "DATABASE=Nexelyion;"
        "Trusted_Connection=yes;"
    )