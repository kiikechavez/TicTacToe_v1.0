# Dobot TicTacToe Proyect
![TicTacToeImage](https://user-images.githubusercontent.com/36646104/161598775-3843ba89-24a2-4a3b-9927-12a3a9313f7f.png)

 tres en raya_v1.0
Proyecto final de robótica industrial Universidad de Antioquia, el juego Tic-Tac-Toe se gana completando una fila o diagonal usando X u O

La robótica aplicada a juegos interactivos constituye un excelente problema para explorar la colaboración humano-robot, ya que presenta una estructura cuya complejidad (al menos en términos de software) es fácil de ser incrementada.

En este trabajo se presenta un sistema basado en un robot capaz de jugar al triqui con un oponente humano de forma natural.

La interacción con el humano se lleva a cabo mediante visión artificial, la principal ventaja de este sistema mecatrónico frente a otros similares es que opera con una estructura general, por lo que podrá ser adaptado para realizar otras tareas.

### Pasos a seguir del juego

1. El humano hace un movimiento (coloque una ficha en el tablero de juego).
2. Se captura una imagen del tablero de juego.
3. Se procesa la imagen para determinar el movimiento realizado por el humano
4. Determina en qué posición mover su ficha
5. El robot utiliza su brazo para hacer el movimiento.
6. Determina si hay victoria o empate.
7. Le solicita al jugador que se mueva de nuevo o bien indica un empate o victoria del robot.

<i>Este conjunto de acciones continúa hasta que se completa el juego o el humano indica el deseo de abandonar.</i>

## Para poder llevar a cabo los pasos anteriores es necesario utilizar tres archivos .py los cuales son:
  * <b>Funciones_del_robot:</b> <br>En este archivo se encuentran las funciones con las cuales se podrá mover el robot, se inicializa el puerto serial, se inicializan los movimientos en x, y, z, y también velocidad, aceleración de los motores de cada articulación,
  * <b>Funciones_tres_en_raya:</b> <br>Por medio de este archivo encontramos funciones que nos ayudarán para el movimiento del robot donde podrá validar si es ganador o hacia dónde debería realizar el próximo movimiento, también como validación el tablero se irá creando en la pantalla del PC y en este archivo también se encuentra la forma de dibujar este tablero.
  * <b>Identifique_jugador:</b> <br>Por medio de este archivo, se hace el reconocimiento de imágenes, las áreas para dibujar el tablero digitalmente, se identifican los centroides de cada uno de las imágenes y el área del tablero en la que se encuentra, de esta manera nos indica , en qué posición del tablero se ha hecho alguna de las jugadas.

Los archivos contienen los experimentos anteriores
