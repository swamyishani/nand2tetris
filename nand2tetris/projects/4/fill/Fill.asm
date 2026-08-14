// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

(LOOP)
@KBD
D=M
@WHITE
D;JNE
@BLACK
D;JEQ
@LOOP
0;JMP
(WHITE)
  (LOOP2)
  @SCREEN
  M=0
  D=D+A
  @LOOP2
  0;JMP
(BLACK)
  (LOOP3)
  @SCREEN
  M=-1
  D=D+A
  @LOOP3
  0;JMP
(END)
@END
0;JMP

