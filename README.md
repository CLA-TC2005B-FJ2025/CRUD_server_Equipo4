# CRUD_server_Equipo4

Este es el sistema de CRUD (create, read, delete, update) del equipo 4 para el proyecto con el socio formador Lienzo. El equipo esta conformado por: 

- Fernando Sigala Rascón A01563650
- Jesús Alexander Herrera Acevedo A01563465
- Nadia Susana Soto Juarez A01563655
- Mauricio Balbuena Martinez A01563331


## Prerequisitos

Antes de comenzar, asegúrate de tener:

- **GitHub Codespaces** habilitado.
- **Docker** ejecutándose en tu Codespace.
- **Python 3** instalado.
- **pymssql** instalado en tu entorno Python.

### Iniciar la instancia de SQL Server en Docker

Para iniciar una instancia de **SQL Server** en un contenedor Docker, ejecuta el siguiente comando en la terminal de tu **GitHub Codespace**:

```sh
docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=YourPassword123!' \
   -p 1433:1433 --name sqlserver -d mcr.microsoft.com/mssql/server:2022-latest
```

### Instalar sqlcmd
```sh
sudo apt update
sudo apt install mssql-tools unixodbc-dev
echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
source ~/.bashrc
```
### Iniciamos la base de datos 
```sh
sqlcmd -S localhost -U SA -P "YourPassword123!"
```
### Probamos que la base de datos se haya creado correctamente
```sh
sqlcmd -S localhost -U SA -P "YourPassword123!" -i "init_db.sql"
SELECT TABLE_SCHEMA, TABLE_NAME  
FROM INFORMATION_SCHEMA.TABLES  
WHERE TABLE_TYPE = 'BASE TABLE';  
GO
```

### Abra **otra** terminal (no cierre la terminal que está ejecutando el servidor), y ejecute el siguiente comando:
```sh
cd servicios\ WEB/
python WEBservices.py
```
