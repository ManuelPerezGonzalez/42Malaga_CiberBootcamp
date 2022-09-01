
+------------------ HELP LINKS ------------------+

Guía inicial:

https://wiki.elhacker.net/bugs-y-exploits/overflows-y-shellcodes/exploits-y-stack-overflows-en-windows

https://github.com/42Cyber/Vagrantfiles

+---------- SHELLCODE.C ----------+

En primer lugar creamos el shellcode.c (que devuelve el payload), con el que, mediante el uso de la librería msvcrt.dll, usaremos el calc.exe, y al compilarlo obtendremos el shellcode.obj, el cual solo seremos capaces de comprender si lo leemos con "xxd -i shellcode.obj".

Una vez compilado, en /debug (carpeta creada al compilar):
xxd -i shellcode.obj

Cuando veamos la ristra de carácteres en hexadecimal representados, debemos buscar los correspondientes al "push ebp, mov ebp" y al "mov ebx, call ebx", que serían "0x55, 0x8b" y "0xff, 0xd3" respectivamente, para saber desde dónde empezar y dónde terminar de copiar.

+---------- EXPLOIT.C ----------+

Lo segundo sería crear el programa que llamará a la vulnerabilidad, nuestro exploit.c, que recibiendo una serie de argumentos, los usará para hacer fallar a nuestro programa vulnerable, mediante el uso de una variable que excede su capacidad de almacenamiento, concatenando un buffer máximo, un offset que contendrá la dirección de la librería kernel32.dll, que en todo momento sabe dónde se encuentra la cima de la pila (jmp esp kernel32..dll). Una vez apuntemos a esa dirección, añadimos la ristra obtenida mediante el compilado del shellcode.c

+---------- VULN1.C ----------+

Este será un programa simple que usaremos como vulnerabilidad del sistema en el que una variable buffer sufrirá un overflow (brecha/puerta trasera/comoquierasllamarlo) que aprovecharemos para introducirnos en el sistema. En este caso lo único que hacemos es ejecutar el programa de la calculadora (calc.exe) pero podríamos llegar a hacer cosas bastante más destructivas.
