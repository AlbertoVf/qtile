# Arco Qtile

Configuracion personalizada para Qtile en ArcoLinux.

![wall](./wall.jpg)

## Instalacion

```bash
git clone https://github.com/AlbertoVf/qtile ~/.config/qtile
```

## Personalizacion de tema

1. Agregar al fichero **themes/themes.toml** un nuevo con el formato:

    ```toml
    [tema]
        background = ""
        foreground = ""
        active     = ""
        inactive   = ""
        color1     = ""
        color2     = ""
        color3     = ""
        color4     = ""
    ```

2. Modificar el archivo **qtile.conf** y substituir el valor de la propiedad **theme**.

## Configurar entorno

Usa qtile_manager para configurar las demas caracteristicas de qtile

```bash
qtile_manager -t [nombre]
```

```bash
qtile_manager -h
```
