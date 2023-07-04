import requests,json,time,os
api_url = "http://www.omdbapi.com/?"
api_key = "660d3d37" # MyKey
print()
print(" Developed by the 1st year students at : ")
print(" Indraprastha Institute of Information Technology Delhi (IIITD)")
print()
while True:
    print()
    print("-+"*50+"-")
    print("-"*38+" MOVIE INFO API PROGRAM "+"-"*39)
    print("-+"*50+"-")
    print()
    print()
    print(" Choose one of your favourite movies from here : ")
    print()
    print(" Choice no.  |   Movie             |   Year")
    print(" ------------|---------------------|------------")
    print("     1.      |   3 Idiots          |   2009")
    print("     2.      |   Housefull         |   2010")
    print("     3.      |   Foothpath         |   2003")
    print("     4.      |   Garam Masala      |   2005")
    print("     5.      |   Taarzan           |   2004")
    print("     6.      |   Heropanti         |   2014")
    print("     7.      |   Radhe             |   2021")
    print("     8.      |   Kick              |   2014")
    print("     9.      |   Baby              |   2015")
    print("     10.     |   Rowdy Rathore     |   2012")
    print(" ------------|---------------------|------------")
    print("     11.     |   The Killer        |   2006")
    print("     12.     |   Main hoon na      |   2004")
    print("     13.     |   Welcome           |   2007")
    print("     14.     |   Race              |   2008")
    print("     15.     |   Don               |   2006")
    print("     16.     |   Toilet            |   2017")
    print("     17.     |   Kesari            |   2019")
    print("     18.     |   Gold              |   2018")
    print("     19.     |   Junooniyat        |   2016")
    print("     20.     |   Airlift           |   2016")
    print(" ------------|---------------------|------------")
    print("     21.     |   Munna Bhai MBBS   |   2003")
    print("     22.     |   Golmaal           |   2006")
    print("     23.     |   Tubelight         |   2017")
    print("     24.     |   Rustom            |   2016")
    print("     25.     |   Dhoom             |   2004")
    print("     26.     |   Shaandaar         |   2015")
    print("     27.     |   Tees Maar Khan    |   2010")
    print("     28.     |   Dabangg           |   2010")
    print("     29.     |   Aladdin           |   2009")
    print("     30.     |   Mimi              |   2021")
    print(" ------------|---------------------|------------")
    print("     31.     |   Bhagam Bhag       |   2006")
    print("     32.     |   Showbiz           |   2007")
    print("     33.     |   Veer Zaara        |   2004")
    print("     34.     |   Rocky Handsome    |   2016")
    print("     35.     |   Happy Ending      |   2014")
    print("     36.     |   Roy               |   2015")
    print("     37.     |   Luka Chuppi       |   2019")
    print("     38.     |   The Train         |   2007")
    print("     39.     |   De Dana Dan       |   2009")
    print("     40.     |   Baazigar          |   1993")
    print(" ------------|---------------------|------------")
    print("     41.     |   Sandwich          |   2006")
    print("     42.     |   Sholay            |   1975")
    print("     43.     |   Partner           |   2007")
    print("     44.     |   The Lunchbox      |   2013")
    print("     45.     |   Hera Pheri        |   2000")
    print("     46.     |   Kaal              |   2005")
    print("     47.     |   Happy New Year    |   2014")
    print("     48.     |   Chennai Express   |   2013")
    print("     49.     |   36 China Town     |   2006")
    print("     50.     |   Jannat            |   2008")
    print(" ------------|---------------------|------------")
    print("     51.     |   Exit the program :)")
    print()
    choice=int(input(" Enter your choice number (integer format only) : "))
    print()
    print("-"*101)
    print()
    #----------------------------------------------------
    if choice==1: # 3 Idiots
        imdb_id = "1187043"
    elif choice==2: # Housefull
        imdb_id = "1573072"
    elif choice==3: # Footpath
        imdb_id = "0374660"
    elif choice==4: # Garam Masala
        imdb_id = "0453671"
    elif choice==5: # Taarzan
        imdb_id = "0435437"
    elif choice==6: # Heropanti
        imdb_id = "3142232"
    elif choice==7: # Radhe
        imdb_id = "10888594"
    elif choice==8: # Kick
        imdb_id = "2372222"
    elif choice==9: # Baby
        imdb_id = "3848892"
    elif choice==10: # Rowdy Rathore
        imdb_id = "2077833"
    #----------------------------------------------------
    elif choice==11: # The Killer
        imdb_id = "0833484"
    elif choice==12: # Main Hoon Na
        imdb_id = "0347473"
    elif choice==13: # Welcome
        imdb_id = "0488798"
    elif choice==14: # Race
        imdb_id = "1017456"
    elif choice==15: # Don
        imdb_id = "0461936"
    elif choice==16: # Toilet
        imdb_id = "5785170"
    elif choice==17: # Kesari
        imdb_id = "6264938"
    elif choice==18: # Gold
        imdb_id = "6173990"
    elif choice==19: # Junooniyat
        imdb_id = "3840534"
    elif choice==20: # Airlift
        imdb_id = "4387040"
    #----------------------------------------------------
    elif choice==21: # Munna Bhai MBBS
        imdb_id = "0374887"
    elif choice==22: # Golmaal
        imdb_id = "0495034"
    elif choice==23: # Tubelight
        imdb_id = "5882970"
    elif choice==24: # Rustom
        imdb_id = "5165344"
    elif choice==25: # Dhoom
        imdb_id = "0422091"
    elif choice==26: # Shaandaar
        imdb_id = "4007558"
    elif choice==27: # Tees Maar Khan
        imdb_id = "1572311"
    elif choice==28: # Dabangg
        imdb_id = "1620719"
    elif choice==29: # Aladdin
        imdb_id = "1227762"
    elif choice==30: # Mimi
        imdb_id = "10895576"
    #----------------------------------------------------
    elif choice==31: # Bhagam Bhag
        imdb_id = "0805184"
    elif choice==32: # Showbiz
        imdb_id = "1152845"
    elif choice==33: # Veer Zaara
        imdb_id = "0420332"
    elif choice==34: # Rocky Handsome
        imdb_id = "3410408"
    elif choice==35: # Happy Ending
        imdb_id = "3017412"
    elif choice==36: # Roy
        imdb_id = "2976182"
    elif choice==37: # Luka Chuppi
        imdb_id = "8908002"
    elif choice==38: # The Train
        imdb_id = "0995827"
    elif choice==39: # De Dana Dan
        imdb_id = "1255951"
    elif choice==40: # Baazigar
        imdb_id = "0106333"
    #----------------------------------------------------
    elif choice==41: # Sandwich
        imdb_id = "0430202"
    elif choice==42: # Sholay
        imdb_id = "0073707"
    elif choice==43: # Partner
        imdb_id = "0807758"
    elif choice==44: # The Lunchbox
        imdb_id = "2350496"
    elif choice==45: # Hera Pheri
        imdb_id = "0242519"
    elif choice==46: # Kaal
        imdb_id = "0415908"
    elif choice==47: # Happy New Year
        imdb_id = "2461132"
    elif choice==48: # Chennai Express
        imdb_id = "2112124"
    elif choice==49: # 36 China Town
        imdb_id = "0477252"
    elif choice==50: # Jannat
        imdb_id = "1216300"
    #----------------------------------------------------
    elif choice==51: # exit
        print("  Thank you !! :)")
        print()
        print("-+"*50+"-")
        print()
        time.sleep(5)
        os.system('cls')
        print()
        print()
        print()
        print("  Exiting the program ....")
        time.sleep(3)
        break
#----------------------------------------------------
    else:
        time.sleep(2)
        os.system('cls')
        print()
        print()
        print("  Sorry !! Please enter a valid number next time.")
        print()
        print()
        print("  Directing to home page ....")
        print("\n\n\n\n\n\n\n\n\n")
        print("  IIITD - Indraprastha Institute of Information Technology Delhi")
        print()
        time.sleep(4)
        os.system('cls')
        continue
    #----------------------------------------------------
    time.sleep(2)
    os.system('cls')
    print()
    print()
    print("  Loading the data ....")
    print()
    print()
    print("  (: Please have some patience :)")
    print("\n\n\n\n\n\n\n\n\n")
    print("  IIITD - Indraprastha Institute of Information Technology Delhi")
    print()
    time.sleep(3)
    os.system('cls')
    print()
    print()
    print()
    url = api_url+f'i=tt{imdb_id}&apikey={api_key}'
    resp = requests.get(url)
    if resp.status_code == 200:
        data = json.loads(resp.text)
        print(f" Title        : {data['Title']}\n")
        print("-+"*50+"-\n")
        print(f" Language     : {data['Language']}\n")
        print(f" Released     : {data['Released']}\n")
        print(f" Genre        : {data['Genre']}\n")
        print(f" Writers      : {data['Writer']}\n")
        print(f" Actors       : {data['Actors']}\n")
        print(f" Plot         : {data['Plot']}\n")
        print(f" Runtime      : {data['Runtime']}\n")
        print(f" Ratings      :\n")
        for i in data['Ratings']:
            for j in i:
                print(f"\t{j}\t: {i[j]}")
            print("\n")
        print(f" IMDB Rating  : {data['imdbRating']}\n")
        print(f" Metascore    : {data['Metascore']}\n")
    else:
        print("Request failed, status code: ", resp.status_code)
    print()
    print("-+"*50+"-")
    print()
    ask_again=input(" Want to choose another movie ? (Y/N) : ")
    print()
    if ask_again=="Y" or ask_again=="y":
        time.sleep(2)
        os.system('cls')
        print()
        print()
        print("  Directing to home page ....")
        print("\n\n\n\n\n\n\n\n\n")
        print("  IIITD - Indraprastha Institute of Information Technology Delhi")
        print()
        time.sleep(3)
        os.system('cls')
    elif ask_again=="N" or ask_again=="n":
        print("  Thank you !! :)")
        print()
        print("-+"*50+"-")
        print()
        time.sleep(5)
        os.system('cls')
        print()
        print()
        print()
        print("  Exiting the program ....")
        time.sleep(3)
        break
    else:
        time.sleep(2)
        os.system('cls')
        print()
        print()
        ask_again=input(" Please enter either Y or N : ")
        if ask_again=="Y" or ask_again=="y":
            time.sleep(2)
            os.system('cls')
            print()
            print()
            print("  Directing to home page ....")
            print("\n\n\n\n\n\n\n\n\n")
            print("  IIITD - Indraprastha Institute of Information Technology Delhi")
            print()
            time.sleep(3)
            os.system('cls')
        elif ask_again=="N" or ask_again=="n":
            print()
            print()
            print("  Thank you !! :)")
            print()
            print("-+"*50+"-")
            print()
            time.sleep(5)
            os.system('cls')
            print()
            print()
            print()
            print("  Exiting the program ....")
            time.sleep(3)
            break
        else:
            break