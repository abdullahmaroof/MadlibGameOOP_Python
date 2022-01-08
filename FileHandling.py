import datetime
currentDataAndTime = datetime.datetime.now()
dateAndTime = currentDataAndTime.strftime("%Y.%m.%d--%H.%M.%S")

class file:
    @staticmethod
    def makingfile(name,age):
        myfile = open("userdata.txt", "a")
        myfile.write("Nmae: "+name+"\n")
        myfile.write("Age: "+age+"\n")
        myfile.write("Date & Time: "+dateAndTime+ "\n\n")
        myfile.close()

class forbeglevel(file):
    @staticmethod
    def makingfile():
        myfile = open("beglevel.txt","a")
        myfile.write("level: Beginner level\n\n")
        myfile.write("A \'Curious\' (Adjective) Child asked his Mother:\n\'Mommy\' (Noun 1), Why are some of Your Hairs \'Turning\' (Noun 2) Grey?\nThe Mother Tried to Use\nThis \'Occasion\' (Noun 3) to Teach her Child: \nIt is Because of \'You\' (Pronoun), Dear.\nEvery Bad \'Action\' (Noun 4) of Yours will Turn one of My \'Hair\' (Noun 5) Grey!.\nThe child replied \'Innocently\' (Adverb):\nNow I know why Grandmother has only Grey Hairs on Her Head.\n")
        myfile.write("Date & Time: " + dateAndTime+ "\n\n")
        myfile.close()

class formodlevel(file):
    @staticmethod
    def makingfile():
        myfile = open("modlevel.txt","a")
        myfile.write("level: Moderate level\n\n")
        myfile.write("After a long night of \'making\' (Noun 1) love, the guy notices a photo\n of another man, on the wall.\n He \'begins\' (Verb 1) to worry\n\"Is this your husband?\" he \'nervously\' (adverb) asks.\nShe replies, \'snuggling\' (Verb 2) up to him.\n\"Your boyfriend then?\" he \'continues\' (Verb 3). \"No, not at all,\"\nShe says, nibbling away at his \'ear\' (Noun 2).\n\"Is it your dad or your brother?\" he \'inquires\' (verb 4),  hoping to be reassured.\n\"No, no, no! You are so \'hot\' (Adjective) when you\'re\n")
        myfile.write("Date & Time: " + dateAndTime+ "\n\n")
        myfile.close()
class foradvlevel(file):
    @staticmethod
    def makingfile():
        myfile = open("advlevel.txt","a")
        myfile.write("level: Advance level\n\n")
        myfile.write("A \'Curious\' (Adjective) Child asked his Mother:\n\'Mommy\' (Noun 1), Why are some of Your Hairs \'Turning\' (Noun 2) Grey?\nThe Mother Tried to Use\nThis \'Occasion\' (Noun 3) to Teach her Child: \nIt is Because of \'You\' (Pronoun), Dear.\nEvery Bad \'Action\' (Noun 4) of Yours will Turn one of My \'Hair\' (Noun 5) Grey!.\nThe child replied \'Innocently\' (Adverb):\nNow I know why Grandmother has only Grey Hairs on Her Head.\n")
        myfile.write("Date & Time: " + dateAndTime+ "\n\n")
        myfile.close()

