# Arco Qtile

Configuracion personalizada para QTile en ArcoLinux

![wall](./wall.jpg)

## Personalizacion de colores

1. Agregar a themes.themes una funcion con los colores a utilizar

```python
def name():
  return [
    "#", #00 - dark
    "#", #01 - grey
    "#", #02 - light
    "#", #03 - text
    "#", #04 - focus
    "#", #05 - active
    "#", #06 - inactive
    "#", #07 - urgent
    "#", #08 - color1
    "#", #09 - color2
    "#", #10 - color3
    "#", #11 - color4
  ]
```

2. Modificar en el archivo config.py la variable colors asignandole la funcion con los colores deseados.
3. Reiniciar Qtile para aplicar los cambios.