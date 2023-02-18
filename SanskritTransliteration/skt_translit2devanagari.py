# skt_translit2devanagari.py - 
# convert from Sanskrit transliterated text to native Devanagari script 

from indic_transliteration import sanscript

# Define the input and output scripts
input_scripts = {
    'IAST': sanscript.IAST,
    'ITRANS': sanscript.ITRANS,
    'Kolkata': sanscript.KOLKATA,
    'SLP1': sanscript.SLP1,
    'Velthuis': sanscript.VELTHUIS,
}
output_script = sanscript.DEVANAGARI

# Define the input texts
IAST = """
itihaasam imaṃ śrutvā purāṇaṃ śaśvad uttamam
yadā yadā hi dharmasya glānir bhavati bhārata
sukha-duḥkhe same kṛtvā labhā-lābhau jayā-jayau
"""

ITRANS = """
itihaasam imaM shrutvaa puraaNam shashvad uttamam
yadaa yadaa hi dharmasya glaanir bhavati bhaarata
sukhaduHkhe same kRRitvaa labhaalabhau jayajayau
"""

Kolkata = """
itihaasam imaM Srutva puraaNam Sashvad uttamam
yadaa yadaa hi Dharmasya glaanir bhavati Bhaarata
sukhaduHkhe same kRRitva labhaalabhau jayajayau
"""

SLP1 = """
itihaasam imaM zrutvA purANaM zazvad uttamam
yadA yadA hi dharmasya glAnir bhavati bhArata
sukhaduHkhe same kRRitvA labhAlabhau jayajayau
"""

Velthuis = """
itihaasam ima.m zrutvaa puraa.nam shashvad uttamam
yadaa yadaa hi dharmasya glaanir bhavati bhaarata
sukhaduHkhe same kRitvaa labhaalabhau jayajayau
"""

# Define a dictionary to store the input texts
input_texts = {
    'IAST': IAST,
    'ITRANS': ITRANS,
    'Kolkata': Kolkata,
    'SLP1': SLP1,
    'Velthuis': Velthuis,
}

# Loop through each input text and transliterate to Devanagari script
for input_name, input_text in input_texts.items():
    # Transliterate the input text to Devanagari script
    output_text = sanscript.transliterate(input_text, input_scripts[input_name], output_script)

    # Write the output to a file with UTF-8 encoding
    with open(f'{input_name}_to_Devanagari.txt', 'w', encoding='utf-8') as f:
        f.write(input_text + '\n') 
        f.write(output_text)
