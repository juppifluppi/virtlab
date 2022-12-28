import random

print('''
Willkommen zum Übungsprogramm für die theoretischen Analysen im 1. Sem. Pharmazie!
---------------------------------------------------------------------------------------------------
Sie können im Folgenden für sechs verschiedene Analysen mit randomisierten Salzmischungen Nachweise
durchführen, indem Sie die jeweilige Nummer aus der Liste eingeben, die Ihnen angezeigt wird.
Daraufhin wird Ihnen eine Beobachtung geschildert und nach Dücken auf "Enter"
können Sie den nächsten Nachweis durchführen. Mit "Ansage" können Sie eine Abgabe durchführen, bei
der Sie die gefundenen Ionen, mit Leertaste getrennt und so wie in der Liste angegeben, aufschreiben.
Mit "Führe Entstörung durch..." können Sie einzelne Ionen aus der Analyse entfernen, sofern Sie
enthalten sind. Diese Entstörung kann mit "Beginne mit frischer Substanz" wieder aufgehoben werden.
Ist die Analyse beendet, so können Sie das Programm mit einem Klick auf "Run" in der oberen Leiste
neustarten. Viel Spaß!
---------------------------------------------------------------------------------------------------
Version 1.04 (Letztes Update: 01.03.2021)
---------------------------------------------------------------------------------------------------
''')

input("Drücke Enter zum Starten...")

def let_user_pick(options):
    print("---------------------")
    print("Wähle eine Analyse:")
    print("---------------------")
    for idx, element in enumerate(options):
        print("{}) {}".format(idx+1,element))
    k = input("Gib eine Nummer ein: ")
    try:
        if -1 < int(k) <= len(options):
            return int(k)
    except:
        pass
    return None
    
analysen = ["Einzelsalzanalyse", \
            "Anionen: Zwei (Pseudo-)halogenide", \
            "Anionen: Zwei schwefel- oder kohlenstoffhaltige Anionen", \
            "Analyse einer schwerlöslichen Verbindung", \
            "Kationen: Zwei Vertreter aus der HCl- und H2S-Gruppe", \
            "Kationen: Zwei Vertreter aus der Ammoniumsulfid-Gruppe"]
    
g = 1
while g == 1:












##################
### ANALYSE  1 ###
##################

    k=let_user_pick(analysen)
    if k == 1:
      
      print('''
-----------------------------------------------------------------------------------------------------------
Deine Analyse enthält ein Kation und ein Anion aus der folgenden Auswahl:
- Calcium        - Chlorid
- Strontium      - Bromid
- Barium         - Iodid
- Natrium        - Fluorid
- Kalium         - Thiocyanat
- Lithium        - Hexacyanoferrat(II)
- Magnesium      - Hexacyanoferrat(III)
- Ammonium       - Carbonat
                 - Oxalat
                 - Acetat
                 - Sulfid
                 - Sulfit
                 - Sulfat
                 - Thiosulfat
                 - Nitrit
                 - Nitrat
                 - Phosphat
Es sind jedoch keine schwer löslichen Erdalkalisulfate enthalten. Es wird ebenfalls vorausgesetzt, dass
schlecht lösliche Salze in Lösung gebracht wurden bzw. störende Kationen zur Anionenanalyse per Sodaauszug
entfernt wurden.
-----------------------------------------------------------------------------------------------------------
''')

      kationen = ["Calcium", "Strontium", "Barium", "Natrium", "Kalium", "Lithium", "Magnesium", "Ammonium"]
      anionen = ["Fluorid", "Chlorid", "Bromid", "Iodid", "Thiocyanat", "Hexacyanoferrat(II)", "Hexacyanoferrat(III)",\
      "Carbonat", "Oxalat", "Acetat", "Sulfid", "Sulfit", "Sulfat", "Thiosulfat", "Nitrit", "Nitrat", "Phosphat"]
      
      nachweise = ["Flammenfärbung", \
      "Fällung mit Silber im Salpetersauren", \
      "Vorprobe: Erhitzen mit konz. Schwefelsäure", \
      "Prüfung auf reduzierende Substanzen mit Kaliumtriiodid-Lösung", \
      "Wassertropfenprobe", \
      "Thiocyanatnachweis", \
      "Hexacyanoferrat(II) als Berliner Blau", \
      "Hexacyanoferrat(III) als Turnbulls Blau", \
      "Gärröhrchenprobe", \
      "Oxalatnachweis", \
      "Acetatnachweis mit Kaliumhydrogensulfat", \
      "Sulfidnachweis mit Bleiacetatpapier", \
      "Sulfitnachweis mit Fuchsin", \
      "Sulfatnachweis per Bariumsulfatfällung", \
      "Nitritnachweis mittels Lunges Reagenz", \
      "Nitratnachweis mit Zinkstaub und Lunges Reagenz", \
      "Phosphatnachweis als Ammoniumdodecamolybdatophosphat", \
      "Magnesiumnachweis mit Titangelb", \
      "Ammoniumnachweis", \
      "Erdalkalimetalle: Fällung mit Natriumcarbonat", \
      "Lösung anzeigen (Analyse beenden)"]
      
      x = 1
      while x == 1:
        analysebeginn1 = random.sample(kationen, 1)
        analysebeginn2 = random.sample(anionen, 1)
        if ((analysebeginn1 == "Calcium") or (analysebeginn1 == "Strontium") or (analysebeginn1 == "Barium")) and (analysebeginn2 == "Sulfat") :
          continue
        else:
          break
        
      analyse = analysebeginn1+analysebeginn2
      analysebeginn = analyse
      
      def flamme():
        if ("Natrium" in analyse) :
          print("-----------------------------------------------------")
          print("Eine langanhaltend grellgelbe Flamme ist zu erkennen.")
          print("-----------------------------------------------------")

        elif ("Calcium" in analyse) :
          print("---------------------------------------")
          print("Eine orangerote Flamme ist zu erkennen.")
          print("---------------------------------------")

        elif ("Strontium" in analyse) :
          print("-------------------------------------")
          print("Eine tiefrote Flamme ist zu erkennen.")
          print("-------------------------------------")

        elif ("Barium" in analyse) :
          print("----------------------------------")
          print("Eine grüne Flamme ist zu erkennen.")
          print("----------------------------------")

        elif ("Kalium" in analyse) :
          print("-------------------------------------")
          print("Eine violette Flamme ist zu erkennen.")
          print("-------------------------------------")

        elif ("Lithium" in analyse) :
          print("-------------------------------------")
          print("Eine tiefrote Flamme ist zu erkennen.")
          print("-------------------------------------")

        else :
          print("------------------------------------------------")
          print("Es ist keine Veränderung der Flamme zu erkennen.")
          print("------------------------------------------------")
      
      def silberfaellung():
        if ("Chlorid" in analyse) or ("Thiocyanat" in analyse):
          print("----------------------------------------------------------------------------------")
          print("Es bildet sich ein weißer Niederschlag, der in verd. Ammoniak komplett löslich ist")
          print("----------------------------------------------------------------------------------")
        
        elif ("Hexacyanoferrat(II)" in analyse) :
          print("----------------------------------------------------------------------------------")
          print("Es bildet sich ein weißer Niederschlag, der sich nicht in konz. Ammoniak löst ist.")
          print("----------------------------------------------------------------------------------")
      
        elif ("Bromid" in analyse) :
          print("---------------------------------------------------------------------------------------")
          print("Es bildet sich ein hellgelber Niederschlag, der in konz. Ammoniak komplett löslich ist.")
          print("---------------------------------------------------------------------------------------")
      
        elif ("Iodid" in analyse) :
          print("------------------------------------------------------------------------------")
          print("Es bildet sich ein gelber Niederschlag, der sich nicht in konz. Ammoniak löst.")
          print("------------------------------------------------------------------------------")

        elif ("Sulfit" in analyse) :
          print("----------------------------------------------------------------------------")
          print("Es bildet sich ein weißer Niederschlag, der sich in konz. Ammoniak löst ist.")
          print("----------------------------------------------------------------------------")

        elif ("Sulfat" in analyse) :
          print("------------------------------------------------------------------------")
          print("Es bildet sich ein weißer Niederschlag, der sich in konz. Ammoniak löst.")
          print("------------------------------------------------------------------------")

        elif ("Sulfid" in analyse) :
          print("---------------------------------------------------------------------------------")
          print("Es bildet sich ein schwarzer Niederschlag, der sich nicht in konz. Ammoniak löst.")
          print("---------------------------------------------------------------------------------")

        elif ("Thiosulfat" in analyse) :
          print("-----------------------------------------------------------------------------------")
          print("Es bildet sich ein weißer Niederschlag, der sich nach kurzer Zeit schwarz verfärbt.")
          print("-----------------------------------------------------------------------------------")

        else:
          print("---------------------------------")
          print("Es bildet sich kein Niederschlag.")
          print("---------------------------------")
      
      def konzh2so4():
        if ("Nitrit" in analyse) or ("Nitrat" in analyse) or ("Bromid" in analyse):
          print("------------------------------------")
          print("Es sind braune Dämpfe zu beobachten.")
          print("------------------------------------")
      
        elif ("Iodid" in analyse) :
          print("--------------------------------------")
          print("Es sind violette Dämpfe zu beobachten.")
          print("--------------------------------------")
          
        elif ("Chlorid" in analyse) or ("Sulfit" in analyse) or ("Thiosulfat" in analyse) :
          print("--------------------------------------")
          print("Es sind farblose Dämpfe zu beobachten.")
          print("--------------------------------------")

        elif ("Carbonat" in analyse) or ("Sulfid" in analyse) :
          print("---------------------------------------")
          print("Es ist ein farbloses Gas zu beobachten.")
          print("---------------------------------------")

        else:
          print("----------------------------")
          print("Es bilden sich keine Dämpfe.")
          print("----------------------------")
      
      def reduzierend():
        if ("Sulfid" in analyse) or ("Sulfit" in analyse) or ("Thiosulfat" in analyse) or ("Oxalat" in analyse) or ("Hexacyanoferrat(II)" in analyse) :
          print("-------------------------------------------------------")
          print("Eine Entfärbung der Kaliumtriiodid-Lösung ist zu sehen.")
          print("-------------------------------------------------------")

        else:
          print("----------------------------------------")
          print("Die Kaliumtriiodid-Lösung bleibt dunkel.")
          print("----------------------------------------")
          
      def wassertropfen():
        if ("Fluorid" in analyse) :
          print("-------------------------------------------------------")
          print("Es ist ein weißer Fleck auf dem Filterpapier erkennbar.")
          print("-------------------------------------------------------")
          
        else:
          print("--------------------------------")
          print("Das Filterpapier bleibt schwarz.")
          print("--------------------------------")  
      
      def thiocyanat():
        if ("Thiocyanat" in analyse) and ("Fluorid" not in analyse) and ("Iodid" not in analyse) and ("Hexacyanoferrat(II)" not in analyse) :
          print("--------------------------------")
          print("Es kommt zu einer roten Färbung.")
          print("--------------------------------")
      
        elif ("Fluorid" in analyse) :
          print("-----------------------")
          print("Die Lösung bleibt klar.")
          print("-----------------------")
          
        elif ("Iodid" in analyse) :
          print("----------------------------------")
          print("Es kommt zu einer braunen Färbung.")
          print("----------------------------------")
          
        elif ("Hexacyanoferrat(II)" in analyse) :
          print("---------------------------------")
          print("Es kommt zu einer blauen Färbung.")
          print("---------------------------------")   
          
        else:
          print("----------------------------------")
          print("Es ist keine Rotfärbung erkennbar.")
          print("----------------------------------")  
          
      def berliner():
        if ("Thiocyanat" in analyse) :
          print("--------------------------------")
          print("Es kommt zu einer roten Färbung.")
          print("--------------------------------")   
        
        elif ("Hexacyanoferrat(II)" in analyse) :
          print("-----------------------------")
          print("Es bildet sich Berliner Blau.")
          print("-----------------------------")
          
        else:
          print("-------------------------------")
          print("Es ist keine Färbung erkennbar.")
          print("-------------------------------")  
          
      def turnbulls():
        if ("Thiocyanat" in analyse) :
          print("--------------------------------")
          print("Es kommt zu einer roten Färbung.")
          print("--------------------------------")     
        
        elif ("Hexacyanoferrat(III)" in analyse) :
          print("------------------------------")
          print("Es bildet sich Turnbulls Blau.")
          print("------------------------------")
          
        else:
          print("-------------------------------")
          print("Es ist keine Färbung erkennbar.")
          print("-------------------------------")  

      def carbonat():
        if (("Carbonat" in analyse) or ("Sulfit" in analyse)) and ("Thiosulfat" not in analyse) :
          print("------------------------------------------------------------------------------------")
          print("Es ist eine Gasentwicklung und ein weißer Niederschlag im Gärröhrchen festzustellen.")
          print("------------------------------------------------------------------------------------")

        elif ("Thiosulfat" in analyse) :
          print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
          print("Es ist eine Gasentwicklung und ein weißer Niederschlag im Gärröhrchen festzustellen. Ebenfalls hat sich ein gelber Niederschlag im Reagenzglas gebildet.")
          print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

        else:
          print("----------------------------")
          print("Das Gärröhrchen bleibt klar.")
          print("----------------------------")

      def oxalat():
        if (("Oxalat" in analyse) or ("Sulfit" in analyse)) and ("Sulfat" not in analyse) :
          print("--------------------------------------------------------------------------------------------------------")
          print("Es entsteht ein weißer Niederschlag. Nach Zugabe von verd. Kaliumpermanganat-Lösung wird diese entfärbt.")
          print("--------------------------------------------------------------------------------------------------------")

        elif ("Sulfat" in analyse) :
          print("------------------------------------------------------------------------------------------------------------------")
          print("Es entsteht ein weißer Niederschlag. Nach Zugabe von verd. Kaliumpermanganat-Lösung kommt es zu keiner Entfärbung.")
          print("------------------------------------------------------------------------------------------------------------------")

        else:
          print("------------------------------")
          print("Es entsteht kein Niederschlag.")
          print("------------------------------")

      def acetatkhso4():
        if ("Acetat" in analyse) and ("Sulfid" not in analyse) and ("Sulfit" not in analyse) and ("Thiosulfat" not in analyse) :
          print("------------------------------")
          print("Es riecht intensiv nach Essig.")
          print("------------------------------")

        elif ("Sulfid" in analyse) or ("Sulfit" in analyse) or ("Thiosulfat" in analyse) :
          print("-------------------------------------------------")
          print("Es ist ein stark stechender Geruch festzustellen.")
          print("-------------------------------------------------")

        else:
          print("-------------------------------")
          print("Es ist kein Geruch wahrnehmbar.")
          print("-------------------------------")

      def sulfidblei():
        if ("Sulfid" in analyse) :
          print("---------------------------------------------------")
          print("Es kommt zu einer Schwarzfärbung des Filterpapiers.")
          print("---------------------------------------------------")

        else:
          print("-------------------------------")
          print("Es ist keine Färbung erkennbar.")
          print("-------------------------------")

      def sulfitfuchsin():
        if ("Sulfit" in analyse) or ("Sulfid" in analyse) :
          print("----------------------------------------")
          print("Es kommt zu einer Entfärbung der Lösung.")
          print("----------------------------------------")

        else:
          print("--------------------------")
          print("Die Lösung bleibt gefärbt.")
          print("--------------------------")
          
      def baso4():
        if ("Sulfat" in analyse) or ("Sulfit" in analyse) or ("Thiosulfat" in analyse) :
          print("---------------------------------------")
          print("Es bildet sich ein weißer Niederschlag.")
          print("---------------------------------------")

        else:
          print("---------------------------------------")
          print("Es ist keine Veränderung festzustellen.")
          print("---------------------------------------")          

      def nitrit():
        if ("Nitrit" in analyse) :
          print("----------------------------------")
          print("Es bildet sich ein roter Farblack.")
          print("----------------------------------")

        else:
          print("--------------------------------------")
          print("Es ist keine Verfärbung festzustellen.")
          print("--------------------------------------")

      def nitrat():
        if ("Nitrit" in analyse) or ("Nitrat" in analyse) :
          print("----------------------------------")
          print("Es bildet sich ein roter Farblack.")
          print("----------------------------------")

        else:
          print("--------------------------------------")
          print("Es ist keine Verfärbung festzustellen.")
          print("--------------------------------------")

      def phosphat():
        if ("Phosphat" in analyse) :
          print("-----------------------------------------------------------------------")
          print("Es bildet sich ein gelber Niederschlag, der in Natronlauge löslich ist.")
          print("-----------------------------------------------------------------------")

        else:
          print("---------------------------------------")
          print("Es ist kein Niederschlag festzustellen.")
          print("---------------------------------------")

      def magnesium():
        if ("Magnesium" in analyse) :
          print("--------------------------------------------")
          print("Es bildet sich ein intensiv gelber Farblack.")
          print("--------------------------------------------")

        else:
          print("-----------------------------------")
          print("Es ist kein Farblack festzustellen.")
          print("-----------------------------------")

      def ammonium():
        if ("Ammonium" in analyse) :
          print("-----------------------------------------------------------------------")
          print("Es ist eine Blaufärbung des pH-Papiers am oberen Uhrglas festzustellen.")
          print("-----------------------------------------------------------------------")

        else:
          print("---------------------------------------")
          print("Das pH-Papier ändert seine Farbe nicht.")
          print("---------------------------------------")

      def erdalkali():
        if ("Strontium" in analyse) or ("Barium" in analyse) :
          print("---------------------------------------")
          print("Es bildet sich ein weißer Niederschlag.")
          print("---------------------------------------")

        elif ("Calcium" in analyse) or ("Lithium" in analyse) :
          print("--------------------------------------------------------------------")
          print("Es bildet sich nach anschließendem Erhitzen ein weißer Niederschlag.")
          print("--------------------------------------------------------------------")

        else:
          print("----------------------------------------")
          print("Es kommt zu keiner Niederschlagsbildung.")
          print("----------------------------------------")

      def let_user_pick(options):
          print("---------------------")
          print("Wähle ein Experiment:")
          print("---------------------")
          print("0) Ansage")
          for idx, element in enumerate(options):
              print("{}) {}".format(idx+1,element))
          i = input("Gib eine Nummer ein: ")
          try:
              if -1 < int(i) <= len(options):
                  return int(i)
          except:
              pass
          return None
          
      x = 1
      while x == 1:
          input("Drücke Enter zum Fortfahren...")
          i=let_user_pick(nachweise)
          if i == 0:
              print('''Möglichkeiten:
- Calcium        - Chlorid
- Strontium      - Bromid
- Barium         - Iodid
- Natrium        - Fluorid
- Kalium         - Thiocyanat
- Lithium        - Hexacyanoferrat(II)
- Magnesium      - Hexacyanoferrat(III)
- Ammonium       - Carbonat
                 - Oxalat
                 - Acetat
                 - Sulfid
                 - Sulfit
                 - Sulfat
                 - Thiosulfat
                 - Nitrit
                 - Nitrat
                 - Phosphat
        ''')
              guess = input("Welche zwei Ionen werden gesucht (mit Leertaste getrennt aufschreiben)?\n")
              if (len(str.split(guess)) != 2) :
                  print("----------------------------")
                  print("Angabe von zwei Ionen nötig!")
                  print("----------------------------")
              elif (analysebeginn[0] in guess) and (analysebeginn[1] in guess) :
                  print("--------")
                  print("RICHTIG!")
                  print("--------")
                  quit()
              elif (analysebeginn[0] in guess) or (analysebeginn[1] in guess) :
                  print("---------------------------")
                  print("+1/-1 - Versuch es nochmal!")
                  print("---------------------------")
              else:
                  print("---------------------------")
                  print("+2/-2 - Versuch es nochmal!")
                  print("---------------------------")
                  
          if i == 1:
            flamme()
          
          if i == 2:
            silberfaellung()
          
          if i == 3:
            konzh2so4()

          if i == 4:
            reduzierend()

          if i == 5:
            wassertropfen()
      
          if i == 6:
            thiocyanat()
      
          if i == 7:
            berliner()
      
          if i == 8:
            turnbulls()

          if i == 9:
            carbonat()

          if i == 10:
            oxalat()

          if i == 11:
            acetatkhso4()

          if i == 12:
            sulfidblei()

          if i == 13:
            sulfitfuchsin()

          if i == 14:
            baso4()

          if i == 15:
            nitrit()

          if i == 16:
            nitrat()

          if i == 17:
            phosphat()

          if i == 18:
            magnesium()

          if i == 19:
            ammonium()

          if i == 20:
            erdalkali()

          if i == 21:
            print("---------------")
            print("Enthalten war: "+analysebeginn[0])
            print("Enthalten war: "+analysebeginn[1])
            print("---------------")
            quit()




















##################
### ANALYSE 3A ###
##################

    elif k == 2:
      
      print('''
-----------------------------------------------------------------------------------------------------------
Deine Analyse enthält zwei unbekannte Anionen aus der Gruppe der (Pseudo-)halogenide:
- Fluorid
- Chlorid
- Bromid
- Iodid
- Thiocyanat
- Hexacyanoferrat(II)
- Hexacyanoferrat(III)
Von den Hexacyanoferraten kann immer nur eine Art in der Analyse enhalten sein. In diesem Programm wird 
vorausgesetzt, dass Du diese beiden Anionen eindeutig mithilfe der Nachweise unterscheiden kannst 
(im Praktikum ist dies nicht notwendig).
-----------------------------------------------------------------------------------------------------------
''')

      anionen = ["Fluorid", "Chlorid", "Bromid", "Iodid", "Thiocyanat", "Hexacyanoferrat(II)", "Hexacyanoferrat(III)"]
      
      nachweise = ["Führe Entstörung durch...", \
      "Beginne mit frischer Substanz", \
      "Silberfällung im Salpetersauren", \
      "Vorprobe: Erhitzen mit konz. Schwefelsäure", \
      "Chloramin-T-Nachweis", \
      "Wassertropfenprobe", \
      "Kriechprobe", \
      "Thiocyanatnachweis", \
      "Hexacyanoferrat(II) als Berliner Blau", \
      "Hexacyanoferrat(III) als Turnbulls Blau", \
      "Lösung anzeigen (Analyse beenden)"]
      
      x = 1
      while x == 1:
        analysebeginn = random.sample(anionen, 2)
        if ("Hexacyanoferrat(II)" in analysebeginn) and ("Hexacyanoferrat(III)" in analysebeginn) :
          continue
        else:
          break
      
      analyse = analysebeginn[:]
      
      def silberfaellung():
        if (("Chlorid" in analyse) or ("Thiocyanat" in analyse)) and ("Hexacyanoferrat(II)" not in analyse) and ("Bromid" not in analyse) and ("Iodid" not in analyse) :
          print("----------------------------------------------------------------------------------")
          print("Es bildet sich ein weißer Niederschlag, der in verd. Ammoniak komplett löslich ist")
          print("----------------------------------------------------------------------------------")
        
        elif ("Hexacyanoferrat(II)" in analyse) and ("Iodid" not in analyse) and ("Bromid" not in analyse) :
          print("----------------------------------------------------------------------------------")
          print("Es bildet sich ein weißer Niederschlag, der sich nicht in konz. Ammoniak löst ist.")
          print("----------------------------------------------------------------------------------")
      
        elif ("Hexacyanoferrat(II)" in analyse) and ("Iodid" not in analyse) and ("Bromid" in analyse) :
          print("----------------------------------------------------------------------------------")
          print("Es bildet sich ein hellgelber Niederschlag, der sich teilweise in konz. Ammoniak löst. Zurück bleibt ein weißer Niederschlag.")
          print("----------------------------------------------------------------------------------")
      
        elif ("Bromid" in analyse) and ("Iodid" not in analyse) and ("Hexacyanoferrat(II)" not in analyse) :
          print("---------------------------------------------------------------------------------------")
          print("Es bildet sich ein hellgelber Niederschlag, der in konz. Ammoniak komplett löslich ist.")
          print("---------------------------------------------------------------------------------------")
      
        elif ("Iodid" in analyse) :
          print("------------------------------------------------------------------------------")
          print("Es bildet sich ein gelber Niederschlag, der sich nicht in konz. Ammoniak löst.")
          print("------------------------------------------------------------------------------")
          
        else:
          print("---------------------------------")
          print("Es bildet sich kein Niederschlag.")
          print("---------------------------------")
      
      def konzh2so4():
        if ("Chlorid" in analyse) and ("Bromid" not in analyse) and ("Iodid" not in analyse) :
          print("--------------------------------------")
          print("Es sind farblose Dämpfe zu beobachten.")
          print("--------------------------------------")
      
        elif ("Bromid" in analyse) and ("Iodid" not in analyse) :
          print("------------------------------------")
          print("Es sind braune Dämpfe zu beobachten.")
          print("------------------------------------")
          
        elif ("Iodid" in analyse) :
          print("--------------------------------------")
          print("Es sind violette Dämpfe zu beobachten.")
          print("--------------------------------------")
          
        else:
          print("----------------------------")
          print("Es bilden sich keine Dämpfe.")
          print("----------------------------")
      
      def chloramin():
        if ("Bromid" in analyse) and ("Iodid" not in analyse) :
          print("--------------------------------------")
          print("Die organische Phase färbt sich braun.")
          print("--------------------------------------")
          
        elif ("Iodid" in analyse) :
          print("----------------------------------------")
          print("Die organische Phase färbt sich violett.")
          print("----------------------------------------")
          
        else:
          print("------------------------------------")
          print("Die organische Phase bleibt farblos.")
          print("------------------------------------")
      
      def wassertropfen():
        if ("Fluorid" in analyse) or ("Silikat" in analyse) :
          print("-------------------------------------------------------")
          print("Es ist ein weißer Fleck auf dem Filterpapier erkennbar.")
          print("-------------------------------------------------------")
          
        else:
          print("--------------------------------")
          print("Das Filterpapier bleibt schwarz.")
          print("--------------------------------")  
      
      def kriechprobe():
        if ("Fluorid" in analyse) :
          print("---------------------------------------")
          print("Der Objektträger aus Glas ist angeätzt.")
          print("---------------------------------------")
          
        else:
          print("-----------------------------------------------")
          print("Es ist keine Veränderung am Glas festzustellen.")
          print("-----------------------------------------------")    
      
      def thiocyanat():
        if ("Thiocyanat" in analyse) and ("Fluorid" not in analyse) and ("Iodid" not in analyse) and ("Hexacyanoferrat(II)" not in analyse) :
          print("--------------------------------")
          print("Es kommt zu einer roten Färbung.")
          print("--------------------------------")
      
        elif ("Fluorid" in analyse) :
          print("-----------------------")
          print("Die Lösung bleibt klar.")
          print("-----------------------")
          
        elif ("Iodid" in analyse) :
          print("----------------------------------")
          print("Es kommt zu einer braunen Färbung.")
          print("----------------------------------")
          
        elif ("Hexacyanoferrat(II)" in analyse) :
          print("---------------------------------")
          print("Es kommt zu einer blauen Färbung.")
          print("---------------------------------")   
          
        else:
          print("----------------------------------")
          print("Es ist keine Rotfärbung erkennbar.")
          print("----------------------------------")  
          
      def berliner():
        if ("Thiocyanat" in analyse) :
          print("--------------------------------")
          print("Es kommt zu einer roten Färbung.")
          print("--------------------------------")   
        
        elif ("Hexacyanoferrat(II)" in analyse) :
          print("-----------------------------")
          print("Es bildet sich Berliner Blau.")
          print("-----------------------------")
          
        else:
          print("-------------------------------")
          print("Es ist keine Färbung erkennbar.")
          print("-------------------------------")  
          
      def turnbulls():
        if ("Thiocyanat" in analyse) :
          print("--------------------------------")
          print("Es kommt zu einer roten Färbung.")
          print("--------------------------------")     
        
        elif ("Hexacyanoferrat(III)" in analyse) :
          print("------------------------------")
          print("Es bildet sich Turnbulls Blau.")
          print("------------------------------")
          
        else:
          print("-------------------------------")
          print("Es ist keine Färbung erkennbar.")
          print("-------------------------------")  
      
      
      def let_user_pick(options):
          print("---------------------")
          print("Wähle ein Experiment:")
          print("---------------------")
          print("0) Ansage")
          for idx, element in enumerate(options):
              print("{}) {}".format(idx+1,element))
          i = input("Gib eine Nummer ein: ")
          try:
              if -1 < int(i) <= len(options):
                  return int(i)
          except:
              pass
          return None
          
      def entstoerung(options):
          print("--------------------------------------------------------")
          print("Für welches Ion möchtest Du eine Entstörung durchführen?")
          print("--------------------------------------------------------")
          for idx, element in enumerate(options):
              print("{}) {}".format(idx+1,element))
          b = input("Gib eine Nummer ein: ")
          try:
              if -1 < int(b) <= len(options):
                  return int(b)
          except:
              pass
          return None
          
      x = 1
      while x == 1:
          input("Drücke Enter zum Fortfahren...")
          i=let_user_pick(nachweise)
          if i == 0:
              print('''Möglichkeiten:
- Fluorid
- Chlorid
- Bromid
- Iodid
- Thiocyanat
- Hexacyanoferrat(II)
- Hexacyanoferrat(III)
              ''')
              guess = input("Welche zwei Anionen werden gesucht (mit Leertaste getrennt aufschreiben)?\n")
              if (len(str.split(guess)) != 2) :
                  print("----------------------------")
                  print("Angabe von zwei Ionen nötig!")
                  print("----------------------------")
              elif (analysebeginn[0] in guess) and (analysebeginn[1] in guess) :
                  print("--------")
                  print("RICHTIG!")
                  print("--------")
                  quit()
              elif (analysebeginn[0] in guess) or (analysebeginn[1] in guess) :
                  print("---------------------------")
                  print("+1/-1 - Versuch es nochmal!")
                  print("---------------------------")
              else:
                  print("---------------------------")
                  print("+2/-2 - Versuch es nochmal!")
                  print("---------------------------")
                  
          if i == 1:
            b = entstoerung(anionen)
            if anionen[b-1] in analyse :
              analyse.remove(anionen[b-1])
            ax = str(anionen[b-1])+" entstört!"
            print("-"*len(ax))
            print(ax)
            print("-"*len(ax))
            
          if i == 2:
            analyse = analysebeginn[:]
            print("-----------------------------------------------------------------------")
            print("Neue Substanz aus dem Analysengefäß genommen (Entstörungen aufgehoben)!")
            print("-----------------------------------------------------------------------")   
            
          if i == 3:
            silberfaellung()
          
          if i == 4:
            konzh2so4()
          
          if i == 5:
            chloramin()
          
          if i == 6:
            wassertropfen()
      
          if i == 7:
            kriechprobe()
      
          if i == 8:
            thiocyanat()
      
          if i == 9:
            berliner()
      
          if i == 10:
            turnbulls()
            
          if i == 11:
            print("---------------")
            print("Enthalten war: "+analysebeginn[0])
            print("Enthalten war: "+analysebeginn[1])
            print("---------------")
            quit()































##################
### ANALYSE 3B ###
##################

    elif k == 3:

      print('''
-----------------------------------------------------------------------------------------------------------
Deine Analyse enthält zwei unbekannte Vertreter aus der Gruppe der schwefel- und kohlenstoffhaltigen Anionen:
- Sulfid
- Sulfit
- Sulfat
- Thiosulfat
- Carbonat
- Oxalat
- Acetat
-----------------------------------------------------------------------------------------------------------
''')

      anionen = ["Sulfid", "Sulfit", "Sulfat", "Thiosulfat", "Carbonat", "Oxalat", "Acetat"]

      nachweise = ["Führe Entstörung durch...", \
      "Beginne mit frischer Substanz", \
      "Vorprobe auf schwefelhaltige Anionen", \
      "Vorprobe auf reduzierende Substanzen mit Kaliumtriiodid-Lösung", \
      "Carbonatnachweis", \
      "Oxalatnachweis", \
      "Acetatnachweis mit Kaliumhydrogensulfat", \
      "Acetatnachweis mit Ethanol", \
      "Sulfidnachweis mit Bleiacetatpapier", \
      "Sulfidnachweis mit Pentacyanothionitroferrat(II)", \
      "Sulfitnachweis mit Kaliumhydrogensulfat", \
      "Sulfitnachweis mit Nitroprussid-Natrium + Zinksulfat-Lsg. + K4[Fe(CN)6]-Lsg. im Neutralen", \
      "Sulfitnachweis mit Fuchsin", \
      "Bariumsulfatfällung", \
      "Sonnenuntergangsreaktion", \
      "Thiosulfatnachweis durch Freisetzen von Schwefel", \
      "Lösung anzeigen (Analyse beenden)"]

      x = 1
      while x == 1:
        analysebeginn = random.sample(anionen, 2)
        break
        
      analyse = analysebeginn[:]

      def vorprobeschwefel():
        if ("Sulfid" in analyse) or ("Sulfit" in analyse) or ("Thiosulfat" in analyse) or ("Thiocyanat" in analyse) :
          print("------------------------------------------------------")
          print("Das entweichende Gas färbt Bleiactetat-Papier schwarz.")
          print("------------------------------------------------------")

        else:
          print("-----------------------------------------------")
          print("Das Bleiacetat-Papier ändert seine Farbe nicht.")
          print("-----------------------------------------------")

      def reduzierend():
        if ("Sulfid" in analyse) or ("Sulfit" in analyse) or ("Thiosulfat" in analyse) or ("Oxalat" in analyse) :
          print("-------------------------------------------------------")
          print("Eine Entfärbung der Kaliumtriiodid-Lösung ist zu sehen.")
          print("-------------------------------------------------------")

        else:
          print("----------------------------------------")
          print("Die Kaliumtriiodid-Lösung bleibt dunkel.")
          print("----------------------------------------")

      def carbonat():
        if (("Carbonat" in analyse) or ("Sulfit" in analyse)) and ("Thiosulfat" not in analyse) :
          print("------------------------------------------------------------------------------------")
          print("Es ist eine Gasentwicklung und ein weißer Niederschlag im Gärröhrchen festzustellen.")
          print("------------------------------------------------------------------------------------")

        elif ("Thiosulfat" in analyse) :
          print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
          print("Es ist eine Gasentwicklung und ein weißer Niederschlag im Gärröhrchen festzustellen. Ebenfalls hat sich ein gelber Niederschlag im Reagenzglas gebildet.")
          print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

        else:
          print("----------------------------")
          print("Das Gärröhrchen bleibt klar.")
          print("----------------------------")

      def oxalat():
        if (("Oxalat" in analyse) or ("Sulfit" in analyse)) and ("Sulfat" not in analyse) :
          print("--------------------------------------------------------------------------------------------------------")
          print("Es entsteht ein weißer Niederschlag. Nach Zugabe von verd. Kaliumpermanganat-Lösung wird diese entfärbt.")
          print("--------------------------------------------------------------------------------------------------------")

        elif ("Sulfat" in analyse) :
          print("------------------------------------------------------------------------------------------------------------------")
          print("Es entsteht ein weißer Niederschlag. Nach Zugabe von verd. Kaliumpermanganat-Lösung kommt es zu keiner Entfärbung.")
          print("------------------------------------------------------------------------------------------------------------------")

        else:
          print("------------------------------")
          print("Es entsteht kein Niederschlag.")
          print("------------------------------")

      def acetatkhso4():
        if ("Acetat" in analyse) and ("Sulfid" not in analyse) and ("Sulfit" not in analyse) and ("Thiosulfat" not in analyse) :
          print("------------------------------")
          print("Es riecht intensiv nach Essig.")
          print("------------------------------")

        elif ("Sulfid" in analyse) or ("Sulfit" in analyse) or ("Thiosulfat" in analyse) :
          print("-------------------------------------------------")
          print("Es ist ein stark stechender Geruch festzustellen.")
          print("-------------------------------------------------")

        else:
          print("-------------------------------")
          print("Es ist kein Geruch wahrnehmbar.")
          print("-------------------------------")

      def acetatetoh():
        if ("Acetat" in analyse) and ("Sulfid" not in analyse) and ("Sulfit" not in analyse) and ("Thiosulfat" not in analyse) :
          print("-------------------------------")
          print("Es riecht intensiv nach Kleber.")
          print("-------------------------------")

        elif ("Sulfid" in analyse) or ("Sulfit" in analyse) or ("Thiosulfat" in analyse) :
          print("-------------------------------------------------")
          print("Es ist ein stark stechender Geruch festzustellen.")
          print("-------------------------------------------------")

        else:
          print("-------------------------------")
          print("Es ist kein Geruch wahrnehmbar.")
          print("-------------------------------")

      def sulfidblei():
        if ("Sulfid" in analyse) :
          print("---------------------------------------------------")
          print("Es kommt zu einer Schwarzfärbung des Filterpapiers.")
          print("---------------------------------------------------")

        else:
          print("-------------------------------")
          print("Es ist keine Färbung erkennbar.")
          print("-------------------------------")

      def sulfidpentacyano():
        if ("Sulfid" in analyse) :
          print("----------------------------------------")
          print("Es kommt zu einer blauvioletten Färbung.")
          print("----------------------------------------")

        else:
          print("-------------------------------")
          print("Es ist keine Färbung erkennbar.")
          print("-------------------------------")

      def sulfitkhso4():
        if ("Sulfit" in analyse) or ("Thiosulfat" in analyse) :
          print("----------------------------------------")
          print("Es kommt zur Entfärbung des mit Kaliumtriiodid getränkten Filterpapiers.")
          print("----------------------------------------")

        else:
          print("----------------------------------")
          print("Es ist keine Entfärbung erkennbar.")
          print("----------------------------------")

      def sulfitnitro():
        if ("Sulfit" in analyse) :
          print("-------------------------------------")
          print("Es bildet sich eine tiefrote Färbung.")
          print("-------------------------------------")

        else:
          print("-----------------------------------")
          print("Es ist keine Veränderung erkennbar.")
          print("-----------------------------------")

      def sulfitfuchsin():
        if ("Sulfit" in analyse) or ("Sulfid" in analyse) :
          print("----------------------------------------")
          print("Es kommt zu einer Entfärbung der Lösung.")
          print("----------------------------------------")

        else:
          print("--------------------------")
          print("Die Lösung bleibt gefärbt.")
          print("--------------------------")

      def baso4():
        if ("Sulfat" in analyse) or ("Sulfit" in analyse) or ("Thiosulfat" in analyse) :
          print("---------------------------------------")
          print("Es bildet sich ein weißer Niederschlag.")
          print("---------------------------------------")

        else:
          print("---------------------------------------")
          print("Es ist keine Veränderung festzustellen.")
          print("---------------------------------------")

      def sonne():
        if ("Thiosulfat" in analyse) and ("Sulfid" not in analyse) :
          print("--------------------------------------------------------------------------")
          print("Es bildet sich ein weißer Niederschlag, der sich schnell schwarz verfärbt.")
          print("--------------------------------------------------------------------------")

        elif ("Sulfid" in analyse) :
          print("------------------------------------------")
          print("Es bildet sich ein schwarzer Niederschlag.")
          print("------------------------------------------")

        else:
          print("---------------------------------")
          print("Es bildet sich kein Niederschlag.")
          print("---------------------------------")

      def thioschwefel():
        if ("Thiosulfat" in analyse) and ("Sulfid" not in analyse) :
          print("---------------------------------------------------------------------------------------------")
          print("Farblose Dämpfe führen zur Entfärbung von Iod-Papier. Es bildet sich ein gelber Niederschlag.")
          print("---------------------------------------------------------------------------------------------")

        elif ("Sulfid" in analyse) :
          print("-----------------------------------------------------------------------------")
          print("Es bildet sich ein farbloses Gas. Kein gelber Niederschlag ist zu beobachten.")
          print("-----------------------------------------------------------------------------")

        else:
          print("---------------------------------------")
          print("Es ist keine Veränderung festzustellen.")
          print("---------------------------------------")

      def let_user_pick(options):
          print("---------------------")
          print("Wähle ein Experiment:")
          print("---------------------")
          print("0) Ansage")
          for idx, element in enumerate(options):
              print("{}) {}".format(idx+1,element))
          i = input("Gib eine Nummer ein: ")
          try:
              if -1 < int(i) <= len(options):
                  return int(i)
          except:
              pass
          return None

      def entstoerung(options):
          print("--------------------------------------------------------")
          print("Für welches Ion möchtest Du eine Entstörung durchführen?")
          print("--------------------------------------------------------")
          for idx, element in enumerate(options):
              print("{}) {}".format(idx+1,element))
          b = input("Gib eine Nummer ein: ")
          try:
              if -1 < int(b) <= len(options):
                  return int(b)
          except:
              pass
          return None

      x = 1
      while x == 1:
          input("Drücke Enter zum Fortfahren...")
          i=let_user_pick(nachweise)
          if i == 0:
              print('''Möglichkeiten:
- Sulfid
- Sulfit
- Sulfat
- Thiosulfat
- Carbonat
- Oxalat
- Acetat
''')
              guess = input("Welche zwei Anionen werden gesucht (mit Leertaste getrennt aufschreiben)?\n")
              if (len(str.split(guess)) != 2) :
                  print("----------------------------")
                  print("Angabe von zwei Ionen nötig!")
                  print("----------------------------")
              elif (analysebeginn[0] in guess) and (analysebeginn[1] in guess) :
                  print("--------")
                  print("RICHTIG!")
                  print("--------")
                  quit()
              elif (analysebeginn[0] in guess) or (analysebeginn[1] in guess) :
                  print("---------------------------")
                  print("+1/-1 - Versuch es nochmal!")
                  print("---------------------------")
              else:
                  print("---------------------------")
                  print("+2/-2 - Versuch es nochmal!")
                  print("---------------------------")

          if i == 1:
            b = entstoerung(anionen)
            if anionen[b-1] in analyse :
              analyse.remove(anionen[b-1])
            ax = str(anionen[b-1])+" entstört!"
            print("-"*len(ax))
            print(ax)
            print("-"*len(ax))

          if i == 2:
            analyse = analysebeginn[:]
            print("-----------------------------------------------------------------------")
            print("Neue Substanz aus dem Analysengefäß genommen (Entstörungen aufgehoben)!")
            print("-----------------------------------------------------------------------")

          if i == 3:
            vorprobeschwefel()

          if i == 4:
            reduzierend()

          if i == 5:
            carbonat()

          if i == 6:
            oxalat()

          if i == 7:
            acetatkhso4()

          if i == 8:
            acetatetoh()

          if i == 9:
            sulfidblei()

          if i == 10:
            sulfidpentacyano()

          if i == 11:
            sulfitkhso4()

          if i == 12:
            sulfitnitro()

          if i == 13:
            sulfitfuchsin()

          if i == 14:
            baso4()

          if i == 15:
            sonne()

          if i == 16:
            thioschwefel()

          if i == 17:
            print("---------------")
            print("Enthalten war: "+analysebeginn[0])
            print("Enthalten war: "+analysebeginn[1])
            print("---------------")
            quit()























##################
### ANALYSE  4 ###
##################

    elif k == 4:

      print('''
-----------------------------------------------------------------------------
Deine Analyse enthält eine schwerlösliche Verbindung aus der folgenden Liste:
- Calciumsulfat
- Strontiumsulfat
- Bariumsulfat
- Siliciumdioxid
- Magnesiumsilikat
- Aluminiumsilikat
- Aluminiumoxid
- Eisenoxid
- Titandioxid
- Zinnoxid
- Mangandioxid
-----------------------------------------------------------------------------
''')

      salze = ["Calciumsulfat", "Strontiumsulfat", "Bariumsulfat", "Siliciumdioxid", "Magnesiumsilikat", "Aluminiumsilikat", \
      "Aluminiumoxid", "Eisenoxid", "Titandioxid", "Zinnoxid", "Mangandioxid"]

      nachweise = ["Basischer Aufschluss mit anschließenden Nachweisen auf Erdalkalimetalle und Aluminium", \
      "Saurer Aufschluss mit anschließenden Nachweisen auf Eisen und Aluminium", \
      "Freiberger Aufschluss mit anschließender Leuchtprobe", \
      "Oxidationsschmelze", \
      "Titandioxid-Nachweis mit konz. Schwefelsäure", \
      "Thermochromie", \
      "Wassertropfenprobe", \
      "Lösung anzeigen (Analyse beenden)"]

      x = 1
      while x == 1:
        analysebeginn = random.sample(salze, 1)
        break
        
      analyse = analysebeginn[:]

      def basisch():
        if ("Calciumsulfat" in analyse) :
          print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
          print("Der mit Wasser gewaschene Schmelzkuchen löst sich mit Salzsäure auf. Im Anschluss wird eine orangerote Flamme erhalten. Ebenso kommt es mit konz. Schwefelsäure zu einem weißen Niederschlag.")
          print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        elif ("Strontiumsulfat" in analyse) :
          print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
          print("Der mit Wasser gewaschene Schmelzkuchen löst sich mit Salzsäure auf. Im Anschluss wird eine tiefrote Flamme erhalten. Ebenso kommt es mit konz. Schwefelsäure zu einem weißen Niederschlag.")
          print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        elif ("Bariumsulfat" in analyse) :
          print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
          print("Der mit Wasser gewaschene Schmelzkuchen löst sich mit Salzsäure auf. Im Anschluss wird eine leicht grüne Flamme erhalten. Ebenso kommt es mit konz. Schwefelsäure zu einem weißen Niederschlag.")
          print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        elif ("Siliciumdioxid" in analyse) :
          print("--------------------------------------------------------------------------------------------------------------------------------------------------------------")
          print("Der mit Wasser gewaschene Schmelzkuchen löst sich mit Salzsäure auf. Die nachfolgenden Nachweise auf Erdalkalimetalle und Aliuminium verlaufen jedoch negativ.")
          print("--------------------------------------------------------------------------------------------------------------------------------------------------------------")

        elif ("Magnesiumsilikat" in analyse) :
          print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
          print("Der mit Wasser gewaschene Schmelzkuchen löst sich mit Salzsäure auf. Im Anschluss wird keine Flammenfärbung beobachtet. Es wird jedoch ein blauer Farblack mit Magneson II erhalten.")
          print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        elif ("Aluminiumsilikat" in analyse) :
          print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
          print("Der mit Wasser gewaschene Schmelzkuchen löst sich mit Salzsäure auf. Im Anschluss wird keine Flammenfärbung beobachtet. Mit Morin wird jedoch eine Fluoreszenz und mit verd. Natronlauge ein weißer Niederschlag beobachtet.")
          print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        elif ("Aluminiumoxid" in analyse) :
          print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
          print("Der mit Wasser gewaschene Schmelzkuchen löst sich mit Salzsäure auf. Im Anschluss wird keine Flammenfärbung beobachtet. Mit Morin wird jedoch eine Fluoreszenz und mit verd. Natronlauge ein weißer Niederschlag beobachtet.")
          print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        else:
          print("--------------------------------------------------------------------------------------------")
          print("Der Schmelzkuchen löst sich nicht auf und keine weiterführenden Nachweise verlaufen positiv.")
          print("--------------------------------------------------------------------------------------------")

      def sauer():
        if ("Aluminiumoxid" in analyse) :
          print("----------------------------------------------------------------------------------------------------------------------------------------------------")
          print("Mit Morin wird eine Fluoreszenz im Waschwasser beobachtet. Ebenso kommt es zur Bildung eines farblosen Niederschlags durch Zugabe verd. Natronlauge.")
          print("----------------------------------------------------------------------------------------------------------------------------------------------------")

        elif ("Eisenoxid" in analyse) :
          print("---------------------------------------------------------------------------------------------")
          print("Das Waschwasser wird mit Ammoniumthiocyanat versetzt, wodurch eine blutrote Färbung entsteht.")
          print("---------------------------------------------------------------------------------------------")

        else:
          print("-----------------------------------------------")
          print("Im Waschwasser werden keine Ionen nachgewiesen.")
          print("-----------------------------------------------")

      def freiberger():
        if ("Zinnoxid" in analyse) :
          print("---------------------------------")
          print("Die Leuchtprobe verläuft positiv.")
          print("---------------------------------")

        else:
          print("-------------------------------------------------")
          print("Die Leuchtprobe nach Aufschluss verläuft negativ.")
          print("-------------------------------------------------")

      def oxidation():
        if ("Mangandioxid" in analyse) :
          print("----------------------------------------------------------------------------------------------------------------------")
          print("Es wird nach Zugabe von verd. Essigsäure zum Schmelzkuchen eine violette Lösung und ein brauner Niederschlag erhalten.")
          print("----------------------------------------------------------------------------------------------------------------------")

        else:
          print("--------------------------------------")
          print("Es wird keine farbige Lösung erhalten.")
          print("--------------------------------------")

      def titan():
        if ("Titandioxid" in analyse) :
          print("-------------------------------------------------------------------------------------------------------------------")
          print("Die nach Behandlung mit konz. Schwefelsäure erhaltene Lösung verfärbt sich durch Zugabe von Zink-Granalien violett.")
          print("-------------------------------------------------------------------------------------------------------------------")
          
        else:
          print("------------------------------------------")
          print("Die Nachweise auf Titan verlaufen negativ.")
          print("------------------------------------------")

      def thermochromie():
        if ("Titandioxid" in analyse) :
          print("----------------------------------------------------------------------------------------")
          print("Nach Erhitzen des Salzes in der Bunsenbrennerflamme bleibt das Salz für kurze Zeit gelb.")
          print("----------------------------------------------------------------------------------------")

        else:
          print("-----------------------------------------------")
          print("Es ist keine Verfärbung des Salzes zu erkennen.")
          print("-----------------------------------------------")

      def wassertropfen():
        if ("Siliciumdioxid" in analyse) or ("Aluminiumsilikat" in analyse) or ("Magnesiumsilikat" in analyse) :
          print("-------------------------------------------------------")
          print("Es ist ein weißer Fleck auf dem Filterpapier erkennbar.")
          print("-------------------------------------------------------")
          
        else:
          print("--------------------------------")
          print("Das Filterpapier bleibt schwarz.")
          print("--------------------------------")  

      def let_user_pick(options):
          print("---------------------")
          print("Wähle ein Experiment:")
          print("---------------------")
          print("0) Ansage")
          for idx, element in enumerate(options):
              print("{}) {}".format(idx+1,element))
          i = input("Gib eine Nummer ein: ")
          try:
              if -1 < int(i) <= len(options):
                  return int(i)
          except:
              pass
          return None

      x = 1
      while x == 1:
          input("Drücke Enter zum Fortfahren...")
          i=let_user_pick(nachweise)
          if i == 0:
              print('''Möglichkeiten:
- Calciumsulfat
- Strontiumsulfat
- Bariumsulfat
- Siliciumdioxid
- Magnesiumsilikat
- Aluminiumsilikat
- Aluminiumoxid
- Eisenoxid
- Titandioxid
- Zinnoxid
- Mangandioxid
''')
              guess = input("Welches Salz wird gesucht?\n")
              if (len(str.split(guess)) != 1) :
                  print("------------------------------")
                  print("Angabe nur eines Salzes nötig!")
                  print("------------------------------")
              elif (analysebeginn[0] in guess) :
                  print("--------")
                  print("RICHTIG!")
                  print("--------")
                  quit()
              else:
                  print("---------------------------")
                  print("+1/-1 - Versuch es nochmal!")
                  print("---------------------------")

          if i == 1:
            basisch()

          if i == 2:
            sauer()

          if i == 3:
            freiberger()

          if i == 4:
            oxidation()

          if i == 5:
            titan()

          if i == 6:
            thermochromie()

          if i == 7:
            wassertropfen()
            
          if i == 8:
            print("---------------")
            print("Enthalten war: "+analysebeginn[0])
            print("---------------")
            quit()















##################
### ANALYSE 5A ###
##################

    elif k == 5:

      print('''
---------------------------------------------------------------------------
Deine Analyse enthält zwei unbekannte Kationen aus der HCl- und H2S-Gruppe:
- Silber
- Blei
- Zinn
- Kupfer
- Bismut
---------------------------------------------------------------------------
''')

      kationen = ["Silber", "Blei", "Zinn", "Kupfer", "Bismut"]

      nachweise = ["Führe Entstörung durch...", \
      "Beginne mit frischer Substanz", \
      "Kationentrennungsgang", \
      "Fällung mit Chlorid", \
      "Fällung mit TAA im HCl-Sauren", \
      "Fällung mit Schwefelsäure", \
      "Zugabe von Kaliumiodid-Lösung", \
      "Bismutrutsche", \
      "Zugabe von Natronlauge", \
      "Zugabe von Ammoniak", \
      "Zugabe von Dithionit", \
      "Eisennagelprobe", \
      "Leuchtprobe", \
      "Lösung anzeigen (Analyse beenden)"]

      x = 1
      while x == 1:
        analysebeginn = random.sample(kationen, 2)
        break
        
      analyse = analysebeginn[:]

      def trennungsgang():
        if (("Silber" in analyse) or ("Blei" in analyse)) and ("Zinn" not in analyse) and ("Kupfer" not in analyse) and ("Bismut" not in analyse)  :
          print("------------------------------------------------------")
          print("Der Trennungsgang deutet auf Ionen der HCl-Gruppe hin.")
          print("------------------------------------------------------")

        elif ("Silber" not in analyse) and ("Blei" not in analyse) and (("Zinn" in analyse) or ("Kupfer" in analyse) or ("Bismut" in analyse))  :
          print("------------------------------------------------------")
          print("Der Trennungsgang deutet auf Ionen der H2S-Gruppe hin.")
          print("------------------------------------------------------")         

        elif (("Silber" in analyse) or ("Blei" in analyse)) and (("Zinn" in analyse) or ("Kupfer" in analyse) or ("Bismut" in analyse))  :
          print("-------------------------------------------------------------------")
          print("Der Trennungsgang deutet auf Ionen der HCl- und der H2S-Gruppe hin.")
          print("-------------------------------------------------------------------")         

        else:
          print("-----------------------------------------")
          print("Der Trennungsgang liefert keine Hinweise.")
          print("-----------------------------------------")

      def chloridfaellung():
        if ("Silber" in analyse)  :
          print("----------------------------------------------------------------------------------------------------")
          print("Es kommt zur Bildung eines weißen Niederschlags. Beim Erwärmen löst sich der Niederschlag nicht auf.")
          print("----------------------------------------------------------------------------------------------------")

        elif ("Blei" in analyse) and ("Silber" not in analyse) :
          print("------------------------------------------------------------------------------------------------------------------------------------------")
          print("Es kommt zur Bildung eines weißen Niederschlags. Beim Erwärmen löst sich der Niederschlag auf. Es kommt zur Kristallbildung beim Abkühlen.")
          print("------------------------------------------------------------------------------------------------------------------------------------------")

        else:
          print("---------------------------------")
          print("Es bildet sich kein Niederschlag.")
          print("---------------------------------")

      def taa():
        if ("Blei" in analyse) or ("Bismut" in analyse) or ("Kupfer" in analyse) :
          print("---------------------------------------------------")
          print("Es kommt zur Bildung eines schwarzen Niederschlags.")
          print("---------------------------------------------------")

        elif ("Zinn" in analyse) :
          print("------------------------------------------------")
          print("Es kommt zur Bildung eines gelben Niederschlags.")
          print("------------------------------------------------")

        else:
          print("---------------------------------")
          print("Es bildet sich kein Niederschlag.")
          print("---------------------------------")

      def schwefelsaeure():
        if ("Blei" in analyse) :
          print("------------------------------------------------------------------------------------------")
          print("Es kommt zur Bildung eines weißen Niederschlags, der in Ammoniumacetat-Lösung löslich ist.")
          print("------------------------------------------------------------------------------------------")

        else:
          print("-------------------")
          print("Es passiert nichts.")
          print("-------------------")

      def kaliumiodid():
        if ("Blei" in analyse) and ("Bismut" not in analyse) :
          print("------------------------------------------------")
          print("Es kommt zur Bildung eines gelben Niederschlags.")
          print("------------------------------------------------")

        elif ("Bismut" in analyse) :
          print("-------------------------------------------------")
          print("Es kommt zur Bildung eines braunen Niederschlags.")
          print("-------------------------------------------------")

        else:
          print("-------------------")
          print("Es passiert nichts.")
          print("-------------------")

      def bismutrutsche():
        if ("Bismut" in analyse) :
          print("--------------------------------")
          print("Es bildet sich ein gelber Fleck.")
          print("--------------------------------")

        else:
          print("-------------------")
          print("Es passiert nichts.")
          print("-------------------")

      def natronlauge():
        if ("Kupfer" in analyse) :
          print("------------------------------------------------")
          print("Es kommt zur Bildung eines blauen Niederschlags.")
          print("------------------------------------------------")

        elif ("Bismut" in analyse) and ("Kupfer" not in analyse) :
          print("----------------------------------------------------------------------------------------")
          print("Es kommt zur Bildung eines weißen Niederschlags. Dieser verfärbt sich in der Hitze gelb.")
          print("----------------------------------------------------------------------------------------")

        else:
          print("-------------------")
          print("Es passiert nichts.")
          print("-------------------")

      def ammoniak():
        if ("Kupfer" in analyse) :
          print("---------------------------------------------")
          print("Es kommt zur Bildung einer tiefblauen Lösung.")
          print("---------------------------------------------")
          
        elif ("Bismut" in analyse) and ("Kupfer" not in analyse) :
          print("----------------------------------------------------------------------------")
          print("Es kommt zur Bildung eines weißen Niederschlags, der in der Hitze gelb wird.")
          print("----------------------------------------------------------------------------")

        else:
          print("-------------------")
          print("Es passiert nichts.")
          print("-------------------")

      def dithionit():
        if ("Kupfer" in analyse) :
          print("----------------------------------------------------")
          print("Es kommt zur Bildung eines rotbraunen Niederschlags.")
          print("----------------------------------------------------")

        else:
          print("-------------------")
          print("Es passiert nichts.")
          print("-------------------")

      def eisennagel():
        if ("Kupfer" in analyse) :
          print("----------------------------------------------------")
          print("Es bildet sich eine rotbraune Schicht auf dem Nagel.")
          print("----------------------------------------------------")

        else:
          print("-------------------")
          print("Es passiert nichts.")
          print("-------------------")

      def leuchtprobe():
        if ("Zinn" in analyse) :
          print("-------------------------------------")
          print("Es kommt zu einer blauen Fluoreszenz.")
          print("-------------------------------------")

        else:
          print("---------------------------------")
          print("Die Leuchtprobe verläuft negativ.")
          print("---------------------------------")

      def let_user_pick(options):
          print("---------------------")
          print("Wähle ein Experiment:")
          print("---------------------")
          print("0) Ansage")
          for idx, element in enumerate(options):
              print("{}) {}".format(idx+1,element))
          i = input("Gib eine Nummer ein: ")
          try:
              if -1 < int(i) <= len(options):
                  return int(i)
          except:
              pass
          return None

      def entstoerung(options):
          print("--------------------------------------------------------")
          print("Für welches Ion möchtest Du eine Entstörung durchführen?")
          print("--------------------------------------------------------")
          for idx, element in enumerate(options):
              print("{}) {}".format(idx+1,element))
          b = input("Gib eine Nummer ein: ")
          try:
              if -1 < int(b) <= len(options):
                  return int(b)
          except:
              pass
          return None

      x = 1
      while x == 1:
          input("Drücke Enter zum Fortfahren...")
          i=let_user_pick(nachweise)
          if i == 0:
              print('''Möglichkeiten:
- Silber
- Blei
- Zinn
- Kupfer
- Bismut
''')
              guess = input("Welche zwei Kationen werden gesucht (mit Leertaste getrennt aufschreiben)?\n")
              if (len(str.split(guess)) != 2) :
                  print("----------------------------")
                  print("Angabe von zwei Ionen nötig!")
                  print("----------------------------")
              elif (analysebeginn[0] in guess) and (analysebeginn[1] in guess) :
                  print("--------")
                  print("RICHTIG!")
                  print("--------")
                  quit()
              elif (analysebeginn[0] in guess) or (analysebeginn[1] in guess) :
                  print("---------------------------")
                  print("+1/-1 - Versuch es nochmal!")
                  print("---------------------------")
              else:
                  print("---------------------------")
                  print("+2/-2 - Versuch es nochmal!")
                  print("---------------------------")

          if i == 1:
            b = entstoerung(kationen)
            if kationen[b-1] in analyse :
              analyse.remove(kationen[b-1])
            ax = str(kationen[b-1])+" entstört!"
            print("-"*len(ax))
            print(ax)
            print("-"*len(ax))

          if i == 2:
            analyse = analysebeginn[:]
            print("-----------------------------------------------------------------------")
            print("Neue Substanz aus dem Analysengefäß genommen (Entstörungen aufgehoben)!")
            print("-----------------------------------------------------------------------")

          if i == 3:
            trennungsgang()

          if i == 4:
            chloridfaellung()
            
          if i == 5:
            taa()
            
          if i == 6:
            schwefelsaeure()
            
          if i == 7:
            kaliumiodid()
            
          if i == 8:
            bismutrutsche()
            
          if i == 9:
            natronlauge()
            
          if i == 10:
            ammoniak()
            
          if i == 11:
            dithionit()
            
          if i == 12:
            eisennagel()
            
          if i == 13:
            leuchtprobe()
            
          if i == 14:
            print("---------------")
            print("Enthalten war: "+analysebeginn[0])
            print("Enthalten war: "+analysebeginn[1])
            print("---------------")
            quit()


















##################
### ANALYSE 5B ###
##################

    elif k == 6:
      
      print('''
-----------------------------------------------------------------------------
Deine Analyse enthält zwei unbekannte Kationen aus der Ammoniumsulfid-Gruppe:
- Cobalt
- Mangan
- Eisen
- Zink
- Aluminium
-----------------------------------------------------------------------------
''')

      kationen = ["Cobalt", "Mangan", "Eisen", "Zink", "Aluminium"]

      nachweise = ["Führe Entstörung durch...", \
      "Beginne mit frischer Substanz", \
      "Phosphorsalzperle", \
      "Fällung mit TAA im Ammoniakalischen", \
      "Cobalt-Nachweis mit Ammoniumthiocyanat und Pentanol", \
      "Eisen-Nachweis mit Ammoniumthiocyanat", \
      "Zugabe von Natronlauge", \
      "Bildung von Berliner Blau", \
      "Oxidationsschmelze", \
      "Oxidation zu Permanganat", \
      "Bildung von Thenards Blau oder Rinnmanns Grün", \
      "Fluoreszenz mit Morin", \
      "Thermochromie", \
      "Lösung anzeigen (Analyse beenden)"]

      x = 1
      while x == 1:
        analysebeginn = random.sample(kationen, 2)
        break
        
      analyse = analysebeginn[:]

      def perle():
        if ("Eisen" in analyse) and ("Mangan" not in analyse) and ("Cobalt" not in analyse) :
          print("-----------------------------------------------")
          print("Oxidationsflamme: gelb. Reduktionsflamme: grün.")
          print("-----------------------------------------------")

        elif ("Mangan" in analyse) and ("Eisen" not in analyse) and ("Cobalt" not in analyse) :
          print("-----------------------------------------------------")
          print("Oxidationsflamme: violett. Reduktionsflamme: farblos.")
          print("-----------------------------------------------------")

        elif ("Zink" in analyse) and ("Eisen" not in analyse) and ("Mangan" not in analyse) and ("Cobalt" not in analyse) :
          print("--------------------------------------------------")
          print("Oxidationsflamme: farblos. Reduktionsflamme: grau.")
          print("--------------------------------------------------")

        elif ("Cobalt" in analyse) and ("Eisen" not in analyse) and ("Mangan" not in analyse) :
          print("-----------------------------------------------")
          print("Oxidationsflamme: blau. Reduktionsflamme: blau.")
          print("-----------------------------------------------")

        elif ("Cobalt" in analyse) and ("Eisen" in analyse) :
          print("-----------------------------------------------")
          print("Oxidationsflamme: grün. Reduktionsflamme: cyan.")
          print("-----------------------------------------------")

        elif ("Cobalt" in analyse) and ("Mangan" in analyse) :
          print("--------------------------------------------------")
          print("Oxidationsflamme: violett. Reduktionsflamme: blau.")
          print("--------------------------------------------------")

        elif ("Eisen" in analyse) and ("Mangan" in analyse) :
          print("------------------------------------------------")
          print("Oxidationsflamme: braun. Reduktionsflamme: grün.")
          print("------------------------------------------------")

        else:
          print("-----------------------------------------------------")
          print("Oxidationsflamme: farblos. Reduktionsflamme: farblos.")
          print("-----------------------------------------------------")

      def taa():
        if ("Eisen" in analyse) or ("Cobalt" in analyse):
          print("------------------------------------------")
          print("Es bildet sich ein schwarzer Niederschlag.")
          print("------------------------------------------")

        elif ("Mangan" in analyse) and ("Eisen" not in analyse) and ("Cobalt" not in analyse) :
          print("-----------------------------------------------")
          print("Es bildet sich ein rosa gefärbter Niederschlag.")
          print("-----------------------------------------------")

        elif ("Zink" in analyse) and ("Eisen" not in analyse) and ("Mangan" not in analyse) and ("Cobalt" not in analyse) :
          print("---------------------------------------")
          print("Es bildet sich ein weißer Niederschlag.")
          print("---------------------------------------")

        elif ("Aluminium" in analyse) and ("Eisen" not in analyse) and ("Mangan" not in analyse) and ("Cobalt" not in analyse) and ("Zink" not in analyse) :
          print("------------------------------------------")
          print("Es bildet sich ein farbloser Niederschlag.")
          print("------------------------------------------")
          
        else:
          print("---------------------------------")
          print("Es bildet sich kein Niederschlag.")
          print("---------------------------------")
          
      def cobaltpentanol():
        if ("Cobalt" in analyse) :
          print("-------------------------------------")
          print("Die organische Phase färbt sich blau.")
          print("-------------------------------------")

        else:
          print("------------------------------------")
          print("Die organische Phase bleibt farblos.")
          print("------------------------------------")

      def eisenthiocyanat():
        if ("Eisen" in analyse) :
          print("-------------------------------------")
          print("Es bildet sich ein blutroter Komplex.")
          print("-------------------------------------")

        else:
          print("--------------------------")
          print("Die Lösung bleibt farblos.")
          print("--------------------------")

      def natronlauge():
        if ("Eisen" in analyse) or ("Mangan" in analyse) :
          print("----------------------------------------")
          print("Es bildet sich ein brauner Niederschlag.")
          print("----------------------------------------")

        elif ("Aluminium" in analyse) and ("Eisen" not in analyse) and ("Mangan" not in analyse) and ("Zink" not in analyse) :
          print("------------------------------------------------------------------------------")
          print("Es bildet sich ein farbloser Niederschlag, der sich im Überschuss wieder löst.")
          print("------------------------------------------------------------------------------")          

        elif ("Zink" in analyse) and ("Eisen" not in analyse) and ("Mangan" not in analyse) :
          print("---------------------------------------------------------------------------")
          print("Es bildet sich ein weißer Niederschlag, der sich im Überschuss wieder löst.")
          print("---------------------------------------------------------------------------")   

        else:
          print("---------------------------------")
          print("Es bildet sich kein Niederschlag.")
          print("---------------------------------")

      def berliner():
        if ("Eisen" in analyse) :
          print("----------------------------------")
          print("Es bildet sich ein blauer Komplex.")
          print("----------------------------------")

        else:
          print("-----------------------")
          print("Die Lösung bleibt klar.")
          print("-----------------------")

      def oxidation():
        if ("Mangan" in analyse) :
          print("----------------------------------------------------------------------------------------------------------------------")
          print("Es wird nach Zugabe von verd. Essigsäure zum Schmelzkuchen eine violette Lösung und ein brauner Niederschlag erhalten.")
          print("----------------------------------------------------------------------------------------------------------------------")

        else:
          print("--------------------------------------")
          print("Es wird keine farbige Lösung erhalten.")
          print("--------------------------------------")

      def permanganat():
        if ("Mangan" in analyse) :
          print("------------------------------------")
          print("Es bildet sich eine violette Lösung.")
          print("------------------------------------")

        else:
          print("--------------------------------------")
          print("Es wird keine farbige Lösung erhalten.")
          print("--------------------------------------")

      def spinell():
        if ("Aluminium" in analyse) and ("Zink" in analyse) :
          print("--------------------------------------")
          print("Es bildet sich ein blaugrüner Spinell.")
          print("--------------------------------------")

        elif ("Aluminium" in analyse) and ("Zink" not in analyse) :
          print("----------------------------------")
          print("Es bildet sich ein blauer Spinell.")
          print("----------------------------------")

        elif ("Zink" in analyse) and ("Aluminium" not in analyse) :
          print("----------------------------------")
          print("Es bildet sich ein grüner Spinell.")
          print("----------------------------------")
          
        else:
          print("---------------------------")
          print("Es kommt zu keiner Färbung.")
          print("---------------------------")

      def morin():
        if ("Aluminium" in analyse) or ("Zink" in analyse) :
          print("-------------------------------------")
          print("Es zeigt sich eine grüne Fluoreszenz.")
          print("-------------------------------------")

        else:
          print("-------------------------------")
          print("Es kommt zu keiner Fluoreszenz.")
          print("-------------------------------")

      def thermochromie():
        if ("Aluminium" in analyse) or ("Zink" in analyse) :
          print("--------------------------------------")
          print("Das Salz färbt sich in der Hitze gelb.")
          print("--------------------------------------")

        else:
          print("---------------------------")
          print("Es kommt zu keiner Färbung.")
          print("---------------------------")
          
      def let_user_pick(options):
          print("---------------------")
          print("Wähle ein Experiment:")
          print("---------------------")
          print("0) Ansage")
          for idx, element in enumerate(options):
              print("{}) {}".format(idx+1,element))
          i = input("Gib eine Nummer ein: ")
          try:
              if -1 < int(i) <= len(options):
                  return int(i)
          except:
              pass
          return None

      def entstoerung(options):
          print("--------------------------------------------------------")
          print("Für welches Ion möchtest Du eine Entstörung durchführen?")
          print("--------------------------------------------------------")
          for idx, element in enumerate(options):
              print("{}) {}".format(idx+1,element))
          b = input("Gib eine Nummer ein: ")
          try:
              if -1 < int(b) <= len(options):
                  return int(b)
          except:
              pass
          return None

      x = 1
      while x == 1:
          input("Drücke Enter zum Fortfahren...")
          i=let_user_pick(nachweise)
          if i == 0:
              print('''Möglichkeiten:
- Cobalt
- Mangan
- Eisen
- Zink
- Aluminium
''')
              guess = input("Welche zwei Kationen werden gesucht (mit Leertaste getrennt aufschreiben)?\n")
              if (len(str.split(guess)) != 2) :
                  print("----------------------------")
                  print("Angabe von zwei Ionen nötig!")
                  print("----------------------------")
              elif (analysebeginn[0] in guess) and (analysebeginn[1] in guess) :
                  print("--------")
                  print("RICHTIG!")
                  print("--------")
                  quit()
              elif (analysebeginn[0] in guess) or (analysebeginn[1] in guess) :
                  print("---------------------------")
                  print("+1/-1 - Versuch es nochmal!")
                  print("---------------------------")
              else:
                  print("---------------------------")
                  print("+2/-2 - Versuch es nochmal!")
                  print("---------------------------")

          if i == 1:
            b = entstoerung(kationen)
            if kationen[b-1] in analyse :
              analyse.remove(kationen[b-1])
            ax = str(kationen[b-1])+" entstört!"
            print("-"*len(ax))
            print(ax)
            print("-"*len(ax))

          if i == 2:
            analyse = analysebeginn[:]
            print("-----------------------------------------------------------------------")
            print("Neue Substanz aus dem Analysengefäß genommen (Entstörungen aufgehoben)!")
            print("-----------------------------------------------------------------------")

          if i == 3:
            perle()

          if i == 4:
            taa()

          if i == 5:
            cobaltpentanol()

          if i == 6:
            eisenthiocyanat()

          if i == 7:
            natronlauge()

          if i == 8:
            berliner()

          if i == 9:
            oxidation()

          if i == 10:
            permanganat()

          if i == 11:
            spinell()

          if i == 12:
            morin()

          if i == 13:
            thermochromie()

          if i == 14:
            print("---------------")
            print("Enthalten war: "+analysebeginn[0])
            print("Enthalten war: "+analysebeginn[1])
            print("---------------")
            quit()
