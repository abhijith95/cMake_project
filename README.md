# Introduction
Welcome to my repository on how to write batch script and CMake script. We know it is being done at Scania and we
are enjoying the fruits of some engineers' labor. The idea behind this is to learn to work with batch files and
cmake files. This small project is a result of my curiosity. I hope it is worthwhile for you all to read as well!

# Project description
This is a very simple project where two numbers are set by the user and a mathematical operation is carried out
between them. The user gets to choose one among the four operations: Addition, subtraction, multiplcation and division.
All the source codes are in C and are placed under src/ folder. The project uses only one header file which can be
found under /lib.

# Build.bat
The batch file runs in a similar fashion to what we do at work. It takes in user input from the command line interface
and builds the project accordingly. The batch file is relatively easy to read and understand. It has enough comments
to follow through. When it comes to using double quotes around the expressions I do not have a reason why it works that
way.

# CMakeLists.txt
This is the heart of the project which builds a "dll" file that is used for python testing. At Scania it is done in a
similar way I presume. I can show you which file is built to create the dll file. This file also contains a lot of 
comments and some useful web links to understand how to build a software.

# Before you begin
Make sure to create a folder called out/ in the root.