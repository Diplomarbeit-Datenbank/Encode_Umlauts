# Encode_Umlauts
![image](https://user-images.githubusercontent.com/87471423/129373157-7f3e1ac8-3752-46fc-b7a2-d16ec4f305d8.png)



Eine Library, um Umlaute aus einem Textfile richtig auszulesen


## Funktionen:
    o Richtiges einlesen von Umlauten in einem Textdokument
    o Einfache Implementierung in eigenen Code durch encode() Funktion
    o Richtiges anzeigen von Umlauten und nicht ä = ae


## Benötigte Librarys:
    o re:  -> Für die einfache Herausfilterung der Umlaute
           -> pip install re

## Entwickler Verwendung:
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
   
   
# Eigenschaften:
    o Copyright Christof Haidegger
    o Erstellt von Christof Haidegger
    o Debugging von Christof Haidegger
    
    o Geschriebene Zeilen Python-Code: 164
    o Geschriebene Zeilen README-Code: 47
    
   
    
