# Generador de Mazo de Vocabulario

Este script en Python carga una lista de palabras desde un archivo JSON y genera un mazo de tarjetas en formato XML para su uso en plataformas de estudio de vocabulario. Cada tarjeta contiene información como la palabra, definición, oración de vocabulario, sinónimo y antónimo.

## Uso

1. Asegúrate de tener un archivo JSON con la información de las palabras. Puedes utilizar el formato proporcionado en el ejemplo `words.json`.

2. Ejecuta el script `generate_deck.py` para generar el mazo en formato XML.

    ```bash
    python generate_deck.py
    ```

3. El script creará un archivo llamado `vocabulary_deck.xml` con el mazo de tarjetas.

## Estructura del Proyecto

- `generate_deck.py`: El script principal que carga las palabras desde un archivo JSON y genera el mazo de tarjetas en XML.

- `words.json`: Archivo de ejemplo con la información de las palabras.

- `vocabulary_deck.xml`: Archivo de salida que contiene el mazo de tarjetas en formato XML.

## Requisitos

- Python 3.x
