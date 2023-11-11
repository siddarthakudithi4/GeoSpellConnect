import mysql.connector


from autocorrect import Speller

sen=input("enter the sentence : ")
words=[]
b=sen.split()
for i in b:
    spell=Speller(lang='en')
    k=spell(i)
    words.append(k)
c=' '.join(words)
print(c)



sos = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlaccount",
    database='gameo'
)
mycursor = sos.cursor()

# Execute a query for each corrected word
for i in words:
    sql = "SELECT * FROM mytable WHERE city = %s"
    val = (i,)

    mycursor.execute(sql, val)

    result = mycursor.fetchall()

    for row in result:
        print(row)







import spacy
# Load the English language model
nlp = spacy.load('en_core_web_sm')

# Define your sentence
sentence = c

# Process the sentence
doc = nlp(sentence)

# Extract city names
city_names = []

for ent in doc.ents:
    if ent.label_ == "GPE":  # "GPE" stands for Geopolitical Entity (often includes cities)
        city_names.append(ent.text)

# Print the extracted city names
print(city_names)