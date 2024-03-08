# Vocabulary Deck Generator

This Python script loads a list of words from a JSON file, inspired by the content from the [VocabTest](https://www.vocabtest.com/) platform, specifically focusing on sixth-grade Unit 1 words. It generates a deck of cards in XML format for use on vocabulary study platforms, such as [Anki](https://www.ankiapp.com/).

## Usage

1. Ensure you have a JSON file with word information. You can use the format provided in the example `words.json`.

2. Run the `generate_deck.py` script to generate the deck in XML format.

    ```bash
    python generate_deck.py
    ```

3. The script will create a file named `vocabulary_deck.xml` containing the deck of cards.

## Project Structure

- `generate_deck.py`: The main script that loads words from a JSON file and generates the card deck in XML.

- `words.json`: Example file with word information, inspired by the [VocabTest](https://www.vocabtest.com/) platform for sixth-grade Unit 1. The information is translated into Spanish.

- `vocabulary_deck.xml`: Output file containing the deck of cards in XML format.

## Requirements

- Python 3.x
