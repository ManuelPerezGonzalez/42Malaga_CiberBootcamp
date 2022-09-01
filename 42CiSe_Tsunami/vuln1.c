/* ************************************************************************** */
/*   vulnt1.c                                                                */
/*   By: maperez-                                                             */
/*   Created: 2022/08/02                                                      */
/* ************************************************************************** */

#include <stdio.h> 

int main(int argc, char **argv)
{           
    char buffer[5]; // Declaramos un array con 5 bytes de espacio,

    if  (argc < 2) // y si los argumentos son menores que 2,
    {
        printf("\nIntroduzca un argumento al programa\n"); // escribimos
        return (0); // y retornamos 0 a la función main (programa acaba).
    }
    strcpy(buffer, argv[1]); // Aquí es donde está el fallo.

    return (0); // Devolvemos 0 a main.
}
