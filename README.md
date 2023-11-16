# Arco Qtile

Configuracion personalizada para Qtile en ArcoLinux.

![wall](./wall.jpg)

## Instalacion

```bash
git clone https://github.com/AlbertoVf/qtile ~/.config/qtile
```

```bash
# Descargar manager
curl -o qtile_manager https://raw.githubusercontent.com/AlbertoVf/shell-scripts/main/system/qtile_manager
```

## Personalizacion de tema

1. Agregar al fichero **themes/themes.yml** una nueva propiedad con el formato:

    ```yaml
    tema:
        background : ""
        foreground : ""
        active     : ""
        inactive   : ""
        color1     : ""
        color2     : ""
        color3     : ""
        color4     : ""
    ```

2. Modificar el archivo **.env** y substituir el valor de la propiedad **theme**.

    ```bash
    qtile_manager -t [theme]
    ```

## Configurar entorno

Usa qtile_manager para configurar las demas caracteristicas de qtile

```bash
qtile_manager -h
```
