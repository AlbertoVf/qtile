# Arco Qtile

![arcolinux](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Arcolinux.svg/240px-Arcolinux.svg.png)
![qtile](https://docs.qtile.org/en/stable/_images/qtile-logo.svg)

Configuracion personalizada para [Qtile](https://docs.qtile.org/en/stable/) en ArcoLinux.

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
qtile_manager -c console -v <valor>
qtile_manager -c font -v <valor>
qtile_manager -c mail -v <valor>
qtile_manager -c theme -v <valor>
```

```bash
qtile_manager -s # toma captura de pantalla con cada tema
qtile_manager -r # reinicia qtile
qtile_manager -l # muestra logs
qtile_manager -h # imprime ayuda
```
