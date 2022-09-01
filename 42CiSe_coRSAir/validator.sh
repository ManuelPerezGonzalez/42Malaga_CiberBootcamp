+--------------------------------------------------+

vim ~/.zshrc
export LDFLAGS="-L/System/Volumes/Data/sgoinfre/goinfre/Perso/maperez-/homebrew/opt/openssl@1.1/lib"
export CPPFLAGS="-I/System/Volumes/Data/sgoinfre/goinfre/Perso/maperez-/homebrew/opt/openssl@1.1/include"

Compilador: gcc $LDFLAGS $CPPFLAGS corsair.c -lssl -lcrypto && ./a.out && rm -rf a.out

+--------------------------------------------------+

Comprobar clave privada: openssl rsa -check -in privkey.pem

+--------------------------------------------------+
