# Arco Qtile

Configuracion personalizada para Qtile en ArcoLinux.

![wall](./wall.jpg)

## Personalizacion de thema

1. Agregar al fichero **themes/themes.json** una nueva propiedad con el formato:

    ```json
    "tema":{
        "active"     : "",
        "background" : "",
        "color1"     : "",
        "color2"     : "",
        "color3"     : "",
        "color4"     : "",
        "foreground" : "",
        "inactive"   : ""
    }
    ```

    ```python
    # actualiza previews.md y crea .json para cada thema
    python settings/manager.py
    ```

2. Modificar el archivo **.env** y substituir el valor de la propiedad **theme**.

    ```python
    # actualiz el valor de la propiedad
    python scripts/change_environment.sh "property" "value"
    ```

3. Reiniciar Qtile para aplicar los cambios.

    ```python
    # Generar captura de pantallas con cada tema
    python scripts/qtile_theme_screenshots.py
    ```

## Instalacion

```bash
git clone https://github.com/AlbertoVf/qtile ~/.config/qtile
```
