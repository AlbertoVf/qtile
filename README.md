# Arco Qtile

Configuracion personalizada para Qtile en ArcoLinux.

![wall](./wall.jpg)

## Personalizacion de thema

1. Agregar al fichero __themes/themes.json__ una nueva propiedad con el formato:

    ```json
    "tema":{
        "background" : "",
        "foreground" : "",
        "active"     : "",
        "inactive"   : "",
        "color1"     : "",
        "color2"     : "",
        "color3"     : "",
        "color4"     : ""
    }
    ```

    ```python
    python settings/manager.py # actualiza previews.md y crea .json para cada thema
    ```

2. Modificar el archivo __manager.json__ y substituir el valor de la propiedad **theme**.
3. Reiniciar Qtile para aplicar los cambios.

## Instalacion

```bash
git clone https://github.com/AlbertoVf/qtile ~/.config/qtile
```
