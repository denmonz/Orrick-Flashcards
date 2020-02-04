<<<<<<< HEAD
Firebase deployed website: https://orrick-flashcards.firebaseapp.com

LexNLP:
Paper: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3192101
Code: https://github.com/LexPredict/lexpredict-lexnlp



----------------
How I got LexNLP working on Mac:

download python 3.6<br>
Use pip3 to install pipenv<br>
Download LexNLP from https://github.com/LexPredict/lexpredict-lexnlp<br>
Use pipenv to make a python 3.6 environment in your downloaded LexNLP folder<br>
use pipenv to install dependencies from python-requirements-full.txt<br>
manually install any dependencies which pipenv failed to install (for me that was sklearn)<br>
launch python in your virtual environment<br>
    in python interactive terminal execute two commands: <br>
        import nltk<br>
        nltk.download()<br>
        (This launches an interactive downloader program: I got some connection error: to fix I went to my machine's python 3.6 install location and "$ sudo ./Install\ Certificates.command" )<br>
    download "all" in the nltk.download() interactive window<br>
=======
# Orrick Flashcards
Firebase Deployed Website: https://orrick-flashcards.firebaseapp.com

## LexNLP<br>
[Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3192101) | [Code](https://github.com/LexPredict/lexpredict-lexnlp)<br>

----------------
## Setup Instructions
### The Essentials
Be sure to have Python version 3.6 and PipEnv installed on your machine.

### How To Get LexNLP Working Using Pipenv and the Pipfile Files<br>
1. Start a terminal at the Flashcard Generator folder.<br>
2. Use the command `pipenv shell`.<br>
    <t>This will launch a new Pipenv environment using the Pipfile files.<br>
3. Launch the python console and use the command `import nltk` followed by `nltk.download()`.<br>
4. In the pop-up window, install "all".<br>

### How I got LexNLP working on Mac From Scratch<br>
1. Download [LexNLP](https://github.com/LexPredict/lexpredict-lexnlp).<br>
2. Use Pipenv to make a Python 3.6 environment in your downloaded LexNLP folder<br>
3. Use pipenv to install dependencies from python-requirements-full.txt<br>
4. Manually install any dependencies which PipEnv failed to install (for me that was sklearn)<br>
5. Launch the python console and use the command `import nltk` followed by `nltk.download()`.<br>
6. In the pop-up window, install "all".<br>
    
## Common Errors<br>
### "SSL Connection Error" When Installing NLTK<br>
Navigate to the intallation location of Python 3.6, open a terminal, and run the command `sudo ./Install\ Certificates.command`.
>>>>>>> 2eeb157a4cea4a94c20cb7b095ac6f5f28e0cfbc
