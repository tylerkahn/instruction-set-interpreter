What is this?
=============

An interpreter of a very simple instruction set I made up. Instructions are run on a virtual machine that exists within the Python runtime.


Usage
------------------

    python lc1.py <sourcefile.lc1> 


Virtual Machine Info
----------

There are 8 general purpose 16 bit registers `r0` through `r7`.


Syntax for LC1
------------

    <mnemonic> <arg1> <arg2> ... <argn> ; <comment>

 - arguments are separated by spaces
 - everything is case insensitive
 - non-negative decimal and hexadecimal numbers are valid
 - hexadecimal numbers are denoted by perpending an '0x' to the number as in 0xF = 15 in base 10
 - comments, whitespace, and blank lines are ignored during interpretation 

Instruction Set
----------------

    MOV <register1:int> <register2>

       MOV r1 r2  ; set r2 to value of r1
       MOV 5 r2   ; set r2 to 5

    ADD <register1:int1> <register2:int2> <register3>

       ADD r1 0xF r3 ; add 15 to value of r1 and store it in r3
       ADD r1 r2 r3  ; add value of r1 to value of r2 and store it in r3

    NOT <register1:int> <register2>

       NOT r0 r1  ; invert bits of r0 and store result in r1
       NOT 0x5 r0 ; invert bits representing 5 and store result in r0

    AND <register1:int1> <register2:int2> <register3>
       
       AND r0 r1 r2 ; bitwise and of r0 and r1, store result in r2

    DSP <register:int>
       
       DSP 65 ; write ascii value to stdout, this outputs 'A'

    PRINT <register:int>
       
       PRINT 20 ; prints hexadecimal value of r0 to screen, this outputs '0x14'
