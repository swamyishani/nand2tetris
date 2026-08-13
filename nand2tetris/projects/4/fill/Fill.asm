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
@PIXELS
M=16384
(WHITE)
  @SCREEN
  D=M
  (LOOP)
  @PIXELS
  M=M+1
  D=M
  @SCREEN
  M=0
  @DIFF
  M=24576-D
  @END
  M;JEQ
  @LOOP
  0;JMP
@BLACK
  @SCREEN
  D=M
  (LOOP)
  @PIXELS
  M=M+1
  D=M
  @SCREEN
  M=-1
  @DIFF
  M=24576-D
  @END
  M;JEQ
  @LOOP
  0;JMP
(END)
@END
0;JMP

