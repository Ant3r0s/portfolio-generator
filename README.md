# Portfolio Generator

Portfolio Generator es una aplicación web que permite a los usuarios generar un portfolio online de manera sencilla. Los usuarios solo tienen que introducir sus datos profesionales, y la aplicación generará automáticamente una página de portfolio personalizable.

## Características

- Formulario para introducir datos de currículum: nombre, profesión, experiencia, educación y habilidades.
- Generación automática de una página HTML con el portfolio.
- Plantillas personalizables para que el usuario pueda descargar o compartir su portfolio online.

## Tecnologías Utilizadas

- [Flask](https://flask.palletsprojects.com/): Un micro-framework para Python que facilita el desarrollo web.
- [Flask-WTF](https://flask-wtf.readthedocs.io/): Extensión para manejar formularios de forma más sencilla en Flask.
- HTML/CSS para el frontend.

## Requisitos

Para ejecutar este proyecto en tu entorno local, necesitarás:

- Python 3.7 o superior.
- pip para instalar las dependencias del proyecto.

## Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/Ant3r0s/portfolio-generator.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd portfolio-generator
    ```

3. Crea un entorno virtual e instálalo:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

4. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Inicia la aplicación Flask:

    ```bash
    python app.py
    ```

2. Abre tu navegador y ve a `http://127.0.0.1:5000/`.

3. Introduce tus datos en el formulario para generar tu portfolio.

4. La aplicación generará automáticamente una página HTML con tu información.

## Personalización

Puedes personalizar la apariencia del portfolio modificando los archivos de la carpeta `templates/` y los estilos en `static/css/styles.css`.

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar el proyecto o agregar nuevas funcionalidades, por favor, sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature-nueva-funcionalidad`).
3. Haz un commit de tus cambios (`git commit -m 'Añadir nueva funcionalidad'`).
4. Sube tu rama al repositorio (`git push origin feature-nueva-funcionalidad`).
5. Abre un Pull Request para que podamos revisarlo.

## Licencia

Este proyecto está bajo la licencia MIT. Para más información, consulta el archivo [LICENSE](LICENSE).
