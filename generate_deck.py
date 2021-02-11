import genanki as ga
import os

MODEL_ID = 1170336229
DECK_ID = 1850966276
RESOURCES_DIR = 'files'
RESOURCE_PREFIX = 'Italian_Core'
CARDS_FILE = 'cards.txt'

# Define model.

my_model = ga.Model(
  MODEL_ID,
  'Italian Core 100',
  fields = [
    {'name': 'Index'},
    {'name': 'Word'},
    {'name': 'Example'},
    {'name': 'Word-English'},
    {'name': 'Example-English'},
    {'name': 'Image'},
    {'name': 'Audio-Word'},
    {'name': 'Audio-Example'},
  ],
  templates = [
    {
      'name': 'Reading',
      'qfmt': '{{Word}} <br> <br> {{Example}} <br> {{Image}}',
      'afmt': '{{FrontSide}} <hr id=answer> {{Word-English}} <br> <br> {{Example-English}} <br> {{Audio-Word}} {{Audio-Example}}',
    },
    {
      'name': 'Production',
      'qfmt': '{{Word-English}} <br> <br> {{Example-English}} <br> {{Image}}',
      'afmt': '{{FrontSide}} <hr id=answer> {{Word}} <br> <br> {{Example}} <br> {{Audio-Word}} {{Audio-Example}}',
    },
  ],
  css = """.card {
  font-family: arial;
  font-size: 20px;
  text-align: center;
  color: black;
  background-color: white; }"""
)

# Define deck.

my_deck = ga.Deck(
  DECK_ID,
  'Italian Core 100 (sentences + media)')

# Retrive notes from file and add them to the deck.

with open(CARDS_FILE, 'r') as file:
    for line in file:
        card = line.split('__')
        img = '<img src="{}_{}.jpg">'.format(RESOURCE_PREFIX, card[0])
        audioWord = '[sound:{}_{}.mp3]'.format(RESOURCE_PREFIX, card[0])
        audioExample = ''
        if bool(card[5]):
            audioExample = '[sound:{}_{}-example.mp3]'.format(RESOURCE_PREFIX, card[0])

        my_note = ga.Note(
            model = my_model,
            fields = [
                card[0], card[1], card[2], card[3], card[4],
                img, audioWord, audioExample])
        my_deck.add_note(my_note)

# Define package and media files.

my_package = ga.Package(my_deck)

with os.scandir(RESOURCES_DIR) as files:
    my_package.media_files = [file.path for file in files]

my_package.write_to_file('italian_core_100.apkg')
