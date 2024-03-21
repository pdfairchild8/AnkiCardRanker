# Anki Card Ranker for Japanese Learning

This is a Python program that is meant to be used in conjunction with the free, open-source flashcard program, Anki. In addition, this program requires an account for the Japanese dictionary wesbite, [Kanshudo](https://www.kanshudo.com/).

With program, one can automatically tag the vocabulary on their Anki flashcards with two different kinds of rankings, obtained from Kanshudo:
- ***Usefullness ranking*** (A numerical value from **1-12** that represents how common the word is in typical Japanese speech or writing with **1** being the most common.)
- ***JLPT Level*** (The approximate level of the [Japanese Language Proficiency Test](https://www.jlpt.jp/e/about/levelsummary.html#:~:text=The%20JLPT%20has%20five%20levels,most%20difficult%20level%20is%20N1.) that corresponds to this word)

To use the code, the log in credentials must be edited into the following section of the **AnkiCardRanker.py** file:
```
#log in credentials
email = "" #INSERT E-MAIL ADDRESS FOR KANSHUDO ACCOUNT
password = ""  #INSERT PASSWORD FOR KANSHUDO ACCOUNT
```

In order to read through a selected set of cards in the Anki Browser, they must be saved as a text file by navigating to **Notes > Export Notes** in the broswer, and exporting them with the following conditions:

- **Export format:** Notes in Plain Text (*.txt)
- **Include:** Selected notes
- [x] **Include HTML and media references**
- [x] **Include tags**

The text file should be named **"MiscVocabCards.txt"**. After running the code, the updated, tagged cards are saved in a file named **MiscVocabCardsUpdated.txt**. 

This program was built with the [Selenium WebDriver](https://www.selenium.dev/).
