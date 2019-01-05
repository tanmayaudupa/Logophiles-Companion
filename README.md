# Logophiles-Companion
### A Customized Vocabulary Assistant


[![Python 3](https://img.shields.io/badge/python-3-blue.svg)](https://www.python.org/download/releases/3.0/)
[![Tkinter](https://img.shields.io/badge/tkinter-interface-green.svg)](https://docs.python.org/2/library/tkinter.html)


The task of pausing a video everytime you hear a complex words and searching up its meaning is both arduous and time consuming. Wouldn't it be a lot easier to automate this process, but at the same time ensuring that you learn the word and its usage.
*Logophiles Companion* is a Vocabulary Learning assistant which annotates non-trivial words with their corresponding definitions on a real time basis as it occurs in a video. Every tough word which comes up frequently assumes the user to have learned its meaning and usage and becomes trivial over time. The model makes use of an Artificial Neural Net to classify words based on its complexity and uses wordnet to get their meanings.

Quick Start
---------------

![Introduction](introduction.gif)


Downloading and Installing
----

1. Clone the code repositories
```
 $ git clone https://github.com/tanmayaudupa/Logophiles-Companion 
 $ cd Logophiles-Companion
 ```
2. Run `dragdropinterface.py`.
3. Minimize pop up tab to see interface window.
4. Drop subtitle file into the above window.
5. The old subtitle file has been replaced.
6. Add it as subtitle file through the video viewer of your choice.

Drag and drop the subtitle file in the window titled `dragdropinterface.py` by running the script.
The old subtitle file has now been replaced by a new subtitle file containing meanings to those non-trivial words.
Add the new subtitle file in the video player of your choice. 
Enjoy!

