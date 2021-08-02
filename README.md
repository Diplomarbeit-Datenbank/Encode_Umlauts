# Encode_Umlauts
![image](https://user-images.githubusercontent.com/87471423/127822984-3d1ac518-224d-432c-ad97-cbd4602ef8c0.png)

Eine Library, um Umlaute aus einem Textfile richtig auszulesen


## Funktionen:
    o Richtiges einlesen von Umlauten in einem Textdokument
    o Einfache inplementierung in eigenen Code durch encode() Funktion
    o Richtiges anzeigen von Umlauten und nicht ä = ae


## Benötigte Librarys:
    o re:  -> Für die einfache Herausfilterung der Umlaute
           -> pip install re

## Verwendung:
    -> Einfach starten der main Funktion im File: encode.py und schon hat man ein 
       ausführliches Beispiel der Funktionen parat.
       
    Main:
    def main():
    """

    : -> to test the class Encode_umlauts()
    """
    data = open('text_file.txt', 'r')
    string = data.read()
    data.close()
    encoded = Encode_umlauts(string)
    print('with encode: \n', encoded.encode())

    return 0
