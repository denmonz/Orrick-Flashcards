# Orrick Flashcards
Firebase Deployed Website: https://orrick-flashcards.firebaseapp.com <br>
Heroku Deployed Website: https://orrick-flashcards.herokuapp.com/

## To-do's
- [ ] Grammar/Styling filter
    - [ ] Or get a better, purely-python-implemented question generator
- [ ] Finalize a main.py or pipeline to automate connections between our back and front-end components
- [ ] Test our pipeline on a brand new environment
    - [ ] A .sh script to automate set-up procedures as much as possible
- [ ] Self-defined  questions
- [ ] AWS deployment

Clients' Wishlist:
- [ ] Customize sections
- [ ] Password Protection of the site  

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
### "SSL: CERTIFICATE_VERIFY_FAILED" When Installing NLTK<br>
Navigate to the intallation location of Python 3.6, open a terminal, and run the command `sudo ./Install\ Certificates.command`.

