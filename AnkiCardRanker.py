import io
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs


#Create Web Driver
driver = webdriver.Chrome(executable_path='C:/Users/Parker/Documents/Kanshudo Scrape/chromedriver-win64/chromedriver.exe')

#log in credentials
email = "" #INSERT USERNAME FOR KANSHUDO
password = "" #INSERT PASSWORD FOR KANSHUDO

#Log in to Kanshudo
driver.get('https://www.kanshudo.com/users/sign_in')
driver.find_element("id", "user_email").send_keys(email)
driver.find_element("id", "user_password").send_keys(password)
driver.find_element("name", "commit").click()

#Open Files
file1 = open('MiscVocabCards.txt', 'r', encoding="utf-8")
file2 = open('MiscVocabCardsUpdated.txt', 'w', encoding="utf-8")
file3 = open('test.txt', 'w', encoding="utf-8")



#Initialize the array, intro string, and isolated word string
strings = []
isolated_word = ""

#Add each line of the file to an array
for line in file1:
    strings.append(line)

#Iterate through the array of lines, and isolate each keyword
for i in strings:
    if "kanshudo-checked" not in i:
        isolated_word = ""
        jlpt_tag = ""
        common_tag = ""
        irregular_tag = ""
        no_match_tag = ""

        j = 0
        while i[j] != "\"":
            isolated_word += i[j]
            j+=1
        
        file3.write(isolated_word)

        #Search Kanshudo for the word
        driver.get('https://www.kanshudo.com/searchq?q=' + isolated_word)

        #Get Search Results
        search_results = driver.find_element("class name", "jr_inner")
        
        #Extract HTML
        kanji = search_results.get_attribute('innerHTML')
        
        #Identify Word
        beginning_index = kanji.find("onclick=\"wordDetails")
        while kanji[beginning_index] != '\'':
            beginning_index += 1
        end_index = beginning_index+1
        while kanji[end_index] != '\'': 
            end_index += 1

        result_word = kanji[beginning_index+1:end_index]

        #Compare result word with flashcard word

        #Get JLPT tag
        ######## Try to implement for loop by using i value in strings
        if (result_word.strip() == isolated_word.strip() and "ja-jlpt_1" in kanji):
            jlpt_tag = "jlpt-N1"
        elif (result_word.strip() == isolated_word.strip() and "ja-jlpt_2" in kanji):
            jlpt_tag = "jlpt-N2"
        elif (result_word.strip() == isolated_word.strip() and "ja-jlpt_3" in kanji):
            jlpt_tag = "jlpt-N3"
        elif (result_word.strip() == isolated_word.strip() and "ja-jlpt_4" in kanji):
            jlpt_tag = "jlpt-N4"
        elif (result_word.strip() == isolated_word.strip() and "ja-jlpt_5" in kanji):
            jlpt_tag = "jlpt-N5"
        
        #Get Common tag
        ######## Try to implement for loop by using i value in strings
        if (result_word.strip() == isolated_word.strip() and "ja-ufn_1" in kanji):
            common_tag = "common-1"
        elif (result_word.strip() == isolated_word.strip() and "ja-ufn_2" in kanji):
            common_tag = "common-2"
        elif (result_word.strip() == isolated_word.strip() and "ja-ufn_3" in kanji):
            common_tag = "common-3"
        elif (result_word.strip() == isolated_word.strip() and "ja-ufn_4" in kanji):
            common_tag = "common-4"
        elif (result_word.strip() == isolated_word.strip() and "ja-ufn_5" in kanji):
            common_tag = "common-5"
        elif (result_word.strip() == isolated_word.strip() and "ja-ufn_6" in kanji):
            common_tag = "common-6"
        elif (result_word.strip() == isolated_word.strip() and "ja-ufn_7" in kanji):
            common_tag = "common-7"
        elif (result_word.strip() == isolated_word.strip() and "ja-ufn_8" in kanji):
            common_tag = "common-8"
        elif (result_word.strip() == isolated_word.strip() and "ja-ufn_9" in kanji):
            common_tag = "common-9"
        elif (result_word.strip() == isolated_word.strip() and "ja-ufn_10" in kanji):
            common_tag = "common-10"
        elif (result_word.strip() == isolated_word.strip() and "ja-ufn_11" in kanji):
            common_tag = "common-11"
        elif (result_word.strip() == isolated_word.strip() and "ja-ufn_12" in kanji):
            common_tag = "common-12"

        #Get Irregular Tag
        if (result_word.strip() == isolated_word.strip() and "sd off" in kanji):
            irregular_tag = "irregular-form"

        #Tag for no matches
        if (result_word.strip() != isolated_word.strip()):
            no_match_tag = "no-match"
        

        i = i.strip("\n")
        i += (" " + jlpt_tag + " " + common_tag + " " + irregular_tag + " " + no_match_tag + " kanshudo-checked \n")

    #Write the updated line to the updated file
    file2.write(i)

file1.close()
file2.close()