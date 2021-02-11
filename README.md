# italian-core-100
Python scripts for scrapping ItalianPod101's [Italian Core 100 Word List](https://www.italianpod101.com/italian-word-lists/?page=1) and generating an Anki deck from it.

## Dependencies

* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [genanki](https://pypi.org/project/genanki/)

## Instructions

After installing the dependencies, run the run_scrapper.py script to generate a cards.txt file and a "files" directory containing the media. You can then run the generate_deck.py script to generate an italian_core_100.apkg file that can be imported into Anki.
