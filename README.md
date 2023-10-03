# Detector cambios de ip

Sencillo algoritmo creado con python y librerias como:
- Tkinter
- Sys
- Request
- Threading
- datatime

## Funcionamiento

1. Realiza una comprobración en el directorio, si existe el archivo `lockfile.lock`, no se ejecuta y termina el algoritmo.
2. Si el archivo no existe, lo crea y su vida util es hasta que finalice el algoritmo.
3. Se usa la libreria **request** para consumir una API, la cual me facilita la dirección IPV4 Pública.
4. El algoritmo trabaja en conjunto con un archivo.txt (`ip_historial.txt`). Con la función `obtener_historial()` obtendremos el archivo .txt con el historial que mostrará en pantalla.
    _**Siempre y cuando el archivo exista, caso contraio lo crea y se comienza uno nuevo.**_
5. La función `actualizar_y_mostrar()` Realiza dos funciones: La primera es que detecte algún cambio en la dirección IP y si la IP no coincide con la que se guardó en el archivo de texto genera un aviso que se plasma en el `ip_historial.txt`

![Muestra](https://media.discordapp.net/attachments/1116592460009852971/1158766859475238942/image.png?ex=651d713c&is=651c1fbc&hm=94cf751d112482c0d4d483d698a1ab11deeb9f5e36d3c1429ed9cd4fbbb672e2&=&width=626&height=660)
![Muestra2](https://media.discordapp.net/attachments/1116592460009852971/1158766859726884974/image.png?ex=651d713c&is=651c1fbc&hm=e21252a27c4ac161f8e428d56804652c807de369642e7805c2ee085f2b5bd562&=&width=621&height=662)