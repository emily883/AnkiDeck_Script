import json

with open("words.json", "r", encoding="utf-8") as json_file:
    words_to_study = json.load(json_file)

def create_card(words):
    return f"""
        <card tags="definition">
            <text name="Front">{words['word']} | {words['palabra']}</text>
            <text name="Back">{words['definition']} | {words['definicion']}</text>
        </card>
        <card tags="sentence">
            <text name="Front">{words['word']} | {words['palabra']}</text>
            <text name="Back">{words['vocabulary_sentence']} | {words["oracion_vocabulario"]}</text>
        </card>
        <card tags="synonym">
            <text name="Front">{words['word']} | {words['palabra']}</text>
            <text name="Back">{words['synonym']} | {words["sinonimo"]}</text>
        </card>
        <card tags="antonym">
            <text name="Front">{words['word']} | {words['palabra']}</text>
            <text name="Back">{words['antonym']}| {words["antonimo"]}</text>
        </card>
    """

def generate_deck(words):
    return f"""
        <deck name="WK_6th_Unit_1">
            <fields>
                <text lang="en-US" name="Front" sides="11"></text>
                <text lang="en-US" name="Back" sides="01"></text>
            </fields>
            <cards>
                {''.join(create_card(word_info) for word_info in words)}
            </cards>
        </deck>
    """

xml_content = generate_deck(words_to_study)
# print(xml_content)

with open("vocabulary_deck.xml", "w") as file:
    file.write(xml_content)

print("File created")

# Si me lees manda saludos :)
