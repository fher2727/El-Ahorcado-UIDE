[INICIO]
   |
   v
[Elegir palabra aleatoria]
   |
   v
[Inicializar intentos y letras usadas]
   |
   v
(MIENTRAS intentos > 0)
   |
   v
[Mostrar palabra oculta e intentos]
   |
   v
[¿Palabra completada?]
   |          \
  SI           NO
   |            \
   v             v
[GANAR]      [Pedir letra]
                |
                v
           [Validar letra]
                |
                v
         [¿Letra está en palabra?]
             |           \
            SI            NO
             |             \
             v              v
[Actualizar aciertos]   [Restar intento]
             \             /
              v           v
          [Continuar bucle]
   |
   v
[PERDER: mostrar palabra]
   |
   v
[FIN]
