import json
import os
from pymongo import MongoClient



if __name__ == '__main__':
    client = MongoClient('localhost', 27017)
    #db name is dic
    db = client.dic
    #collection name is endic
    endic = db.endic

    while True:
        word=input("Please input the word:")
        # input "##",the script shutdown
        if word == "##":
            client.close()
            print("The script shutdown")
            break;
        #use "cl" to clear the Terminal
        elif word == "cl" :
            os.system('clear')

        else:
            rs=endic.find({"word_name":word},{"_id":0})#Attention: remember reomve "_id" column
            for tmp in rs:
                #word,explain,phonetic
                part=tmp["symbols"][0]["parts"][0]["part"]
                means=tmp["symbols"][0]["parts"][0]["means"]
                ph_en=tmp["symbols"][0]["ph_en"]
                ph_am=tmp["symbols"][0]["ph_am"]
                ph_en_mp3=tmp["symbols"][0]["ph_en_mp3"]
                print("[%s][%s]\n%s\n%s\n%s" % (ph_en,ph_am,part,means,ph_en_mp3))
