# Import the required module for text 
# to speech conversion 
from gtts import gTTS 

# This module is imported so that we can 
# play the converted audio 
import os 
# importing required modules 
from pypdf import PdfReader 
# import remove

# defining audio converter function:
def audio_converter(text,lang="en",tld="co.in",name="audio"):
    ## Whenever needed uncomment the two below lines.....
    # lang=input("Enter the language code  of converted audio [referrence:https://shorturl.at/bfJNO ]: ")
    # tld=input("Enter your top level domain [referrence: https://shorturl.at/bfJNO]:") 
    
    
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed 

    myobj = gTTS(text=text,lang=lang,tld=tld, slow=False) 

    # Saving the converted audio in a mp3 file named whatever user enters

    # print("Warning: Don't put space in file name inorder to play it automatically........")
    # name=input("Enter the converted file name: ")
    

    # if same name file exists then instead of overwriting the file it makes another file named as e.g. Atrajit1, Atrajit2, etc.
    i=1
    if not os.path.exists(f"{name}.mp3"):
        myobj.save(f"{name}.mp3")
        return f"{name}.mp3"
    else:
        while True:
            if not os.path.exists(f"{name}{i}.mp3"):
                myobj.save(f"{name}{i}.mp3")
                break
            i=i+1
        return f"{name}{i}.mp3"
    

if __name__=="main":
    Consent=input('''What you want to do?:
                0. Delete audio files. [Write del]
                1. Convert text to voice. [Write ttv]
                2. Convert pdf to voice. [write ptv]
                3. Greet members in bulk. [write gmb]
                \n Give your consent here: ''')
    if Consent=="ptv":
        dir=input("Enter your directory: ")
        list=os.listdir(dir)
        for i in list:
            if i.endswith(".pdf"):
                print(i)
        item=input("Enter the pdf you want to read: ")

        # creating a pdf reader object                                
        reader = PdfReader(f"{dir}\\{item}") 

        # printing number of pages in pdf file 
        print(len(reader.pages)) 

        # getting a specific page from the pdf file 
        pageno=int(input("Enter the no. of page you want to read out: "))
        page = reader.pages[pageno] 

        # extracting text from page 
        text = page.extract_text()
        audio_file=audio_converter(text)
        play=input("Do you want to play the audio (y/n): ")
        if play=="y":
            os.system(audio_file)
        elif play=="n":
            print("Thanks for using our app!")
        else:
            raise TypeError(f" you entered {play} which is neiter y nor n!")

        


    elif Consent=="gmb":
        # The text that you want to convert to audio 
        # mytext =input("Enter your text!")
        text=input("Enter names here (csv format): ")
        text=text.split(",")
        s=""
        wish=input("Enter what to wish: ")
        for i in text:
            s=s+ f"{wish} {i}"+"\n"
        audio_file=audio_converter(s)
        play=input("Do you want to play the audio (y/n): ")
        if play=="y":
            os.system(audio_file)
        elif play=="n":
            print("Thanks for using our app!")
        else:
            raise TypeError(f" you entered {play} which is neiter y nor n!")

    elif Consent=="ttv":
        text=input("Enter your text to convert into audio:\n")
        audio_file=audio_converter(text)
        print(audio_file)
        play=input("Do you want to play the audio (y/n): ")
        if play=="y":
            os.system(audio_file)
        elif play=="n":
            print("Thanks for using our app!")
        else:
            raise TypeError(f" you entered {play} which is neiter y nor n!")
        

    elif Consent=="del":
        atrajit=input("Want to delete all/some specific mp3 files/skip?[all/spec/skip] ")
        if atrajit=="all":
            x=input("Want to delete files of current directory?(y/n): ")
            if x=="y":
                remove.remove_audioes()
            elif x=="n":
                remove.remove_audioes(input("Enter your directory: "))
            else:
                raise TypeError(f"You entered {x} which is neither y nor n! ")
            
        elif atrajit=="spec":
            x=input("Want to delete files of current directory?(y/n): ")
            if x=="y":
                remove.remove_spec_files()
            elif x=="n":
                remove.remove_spec_files(input("Enter your directory: "))
            else:
                raise TypeError(f"You entered {x} which is neither y nor n! ")
        elif atrajit=="skip":
                print("Thanks for using our app!")
        else:
            raise TypeError("Wrong Command!")

    else:
        raise TypeError(f'''You entered {Consent} which is not: 
                                            0.del
                                            1.ttv
                                            2.ptv
                                            3.gmb  ''')

    
