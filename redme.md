# Proyecto Coder

## Instrucciones para instalar proyecto en local
+ Crea una carpeta contenedora madre
+ Abre la consola y ubicate en la carpeta madre.
+ Clona este proyecto en la carpeta madre
+ Entra a la carpeta que acabas de clonar
+ Para instalar las dependencias corre el siguiente comando:
```
pip install -r requirements.txt
```
## Instrucciones para crear un superuser
+ En la consola, crear un superuser
```
python manage.py createsuperuser
```
+ Acceder con user y password via
```
http://127.0.0.1:8000/admin/
```
## Superuser de pruebas
username:admin
password:admin

## Otros usuarios
username:pepe
password:contra123

## Proyecto:
+ El proyecto se basa en un blog en el cual se puede crear/aditar un usuario, crear/editar/eliminar un post y en caso de ser admin, crear una categorias. Para esto, se crearon dos aplicaciones que manejan todo: "theblog" y "members". "theblog" cuenta con los modelos del proyecto y se encarga de todo lo relacionado a posteos y sus categorias. Mientras que "members", se encarga de utilizar el manejo de users por default para administrar los usuarios del postal.
+ Modelos de clases en "models.py" te "theblog"
+ + Post: Clase que contiene la data de los posteos realizado por los usuarios. Cada posteo cuenta con un titulo, imagen de cabecera, un titulo para la cabecera del posteo, el usuario autor, un cuerpo del post, la fecha en que se subio, la categoria a la que pertenece, la cantidad de likes que cuenta y un breve descripcion descripcion del mismo.
+ + Category: Clase que tiene un campo titulo que sirve para relacionar los posteos y agruparlos en (como bien dice su nombre) una categoria.
+ + UserProfile: Clase que contiene todos los campos por defecto de User que vienen implementados en django sumados a una pequeña biografia, una imagen de perfi y links de contacto.
+ + Comments: Clase que contiene la data de los comentarios realizados por los usuarios en cada posteo. Los mismos se pueden editar y eliminar.