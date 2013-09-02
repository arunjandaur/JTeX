JTeX (JSON to LaTeX transpiler written in Python 2.7.5)
=======================================================
Author: Arun Jandaur (https://github.com/arunjandaur)
--------------------

Description:
------------
Takes up to 9 files and/or directories at the command line, expands the directories, and then translates all the .json files it finds into .tex files, placing the .tex files into the same directories their JSON counterparts were found. JTeX can also parse .py files that only contain lists and dicts.

Setup:
------
1. Open the terminal
2. Clone the repository:
        git clone https://github.com/arunjandaur/JTeX.git
3. Go into the repository:
        cd JTeX/
4. Run the setup file (this will copy everything into the appropriate /usr/local/bin,share,lib folders):
        bash setup

Usage:
------
    jtex [FILE_OR_DIR] [FILE_OR_DIR] [FILE_OR_DIR] ...

It should put a .tex file with the same name in the same directory the .json or .py counterpart was found. Enjoy!

Like it? I hope so. :)
Tell me what you think on my GitHub: github.com/arunjandaur/JTeX (I always appreciate the feedback)

Credits:
1. Python API
2. I got the connection.json file in the local/lib/tests/ folder from draw2d.org, a website that provides an amazing 2D drawing software. Check it out sometime!
