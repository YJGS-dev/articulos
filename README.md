
# Artículos

Una pequeña aplicación para alta, baja, cambio y consulta de articulos.


## Ejecutar manualmente

Clonar el proyecto

```bash
  git clone https://github.com/YJGS-dev/articulos.git
```

Ir al directorio del proyecto

```bash
  cd articulos
```

Crear entorno virtual

```bash
  python -m virtualenv env
```

Activar entorno

```bash
  source env/bin/activate
```

Instalar dependencias

```bash
  pip install -r requirements.txt
```

Crear el archivo .env y agregar las siguientes variables de entorno

`SECRET_KEY`

`DEBUG` true o false

`DB_NAME`

`DB_USER`

`DB_PASSWORD`

`DB_HOST`

`DB_PORT`

Ejecutar migraciones

```bash
  python manage.py migrate
```

Iniciar el servidor

```bash
  python manage.py runserver
```


## License

[MIT](https://choosealicense.com/licenses/mit/)