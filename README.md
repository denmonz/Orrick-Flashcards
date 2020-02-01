Firebase deployed website: https://orrick-flashcards.firebaseapp.com

LexNLP:
Paper: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3192101
Code: https://github.com/LexPredict/lexpredict-lexnlp



----------------
How I got NLTK working on Mac:

download python 3.6
Use pip3 to install pipenv
Download LexNLP from https://github.com/LexPredict/lexpredict-lexnlp
Use pipenv to make a python 3.6 environment in your downloaded LexNLP folder
use pipenv to install dependencies from python-requirements-full.txt
manually install any dependencies which pipenv failed to install (for me that was sklearn)
launch python in your virtual environment
    in python interactive terminal execute two commands: 
        import nltk
        nltk.download( )
        (This launches an interactive downloader program: I got some connection error: to fix I went to my machine's python 3.6 install location and "$ sudo ./Install\ Certificates.command" )
    download "all" in the nltk.download(  ) interactive window
