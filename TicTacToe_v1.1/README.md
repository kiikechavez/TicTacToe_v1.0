# Dobot TicTacToe Proyect

<figure>
 <img src="https://user-images.githubusercontent.com/36646104/161598775-3843ba89-24a2-4a3b-9927-12a3a9313f7f.png" alt="TicTacToeImage" style="width:100%">
 <figcaption><i>Fig.1 - Final project of the industrial robotics course at University of Antioquia, the Tic-Tac-Toe game is won by completing a row or diagonal using X or O</i></figcaption>
</figure>

<br>Robotics applied to interactive games constitutes an excellent problem to explore human-robot collaboration, since it presents a structure whose complexity (at least in terms of software) is easy to increase.

In this work, a system based on a robot capable of playing triqui with a human opponent in a natural way is presented.

Interaction with the human is carried out through artificial vision. The main advantage of this mechatronic system over other similar ones is that it operates with a general structure, so it can be adapted to perform other tasks.

### Game steps

1. The human makes a move (place a token on the game board).
2. An image of the game board is captured.
3. The image is processed to determine the movement made by the human.
4. Determines in which position to move his piece.
5. The robot uses its arm to make the movement.
6. Determine if there is a win or tie.
7. Prompts the player to move again or indicates a tie or robot win.

<i>This set of actions continues until the game is completed or the human indicates a desire to quit.</i>

## Machine requirements
<br>For the proper functioning of the project. It is necessary to have python and the following libraries:
1. <b>cv2:</b> if this library is not available, it can be installed with the command pip install opencv-python
2. <b>serial:</b> if this library is not available, it can be installed with the command pip install pyserial
3. <b>struct:</b> si no se cuenta con esta libreria se puede instalar con el comando pip install supyr-struct
4. Other libraries to consider are: time and Numpy

## In order to carry out the previous steps, it is necessary to use three .py files, which are:
  * <b>Funciones_del_robot:</b> <br>In this file are the functions with which the robot can move, the serial port is initialized along with the movements in x, y, z. Also the speed and acceleration of the motors of each joint.
  * <b>Funciones_tres_en_raya:</b> <br>Through this file we find functions that will help us with the movement of the robot where it can validate if it is a winner or where it should make the next movement, as a validation method, the board will be created on the computer screen, the code of this function is also found in this file.
  * <b>Identifique_jugador:</b> <br>Through this file, the image recognition is done, the areas to draw the board digitally, the centroids of each of the images and the area of the board in which it is located are identified, in this way it tells us in what position some of the moves have been made on the board.

