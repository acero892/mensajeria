### 1. Instalar el ambiente virtual y luego actrivarlo

``` bash
python -m venv venv
```

Then, activate the environment in your Terminal:
``` bash
venv/Scripts/activate
```



### 2. Instalar el archivo de requerimientos
``` bash
pip install -r requirements.txt
```

### 3. Se debe abrir la aplicación de docker desktop y luego ejecutar para levantar los servicios


``` bash

docker-compose up
```

### 3. Se debe de abrir una terminal para cada producer y se ejecuta de la siguiente manera


``` bash
cd src
python Cliente1.py
python Cliente2.py
python Cliente3.py
```

### 4. Se debe de abrir una terminal y ejecutar el consumer para recibir los datos

``` bash
cd src
python consumer.py
```

### 5. Se ejecuta la logica del analisis de sentimientos abriendo el archivo

``` bash

python src/sentimientos.ipynb
```
