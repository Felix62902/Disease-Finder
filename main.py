import sqlite3
import tkinter
import time
import webbrowser  # this only triggers if you do one certain thing

# Set up
connection = sqlite3.connect("Diseases.db")
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS diseases (ID Primary key, name Text, coughing Boolean, Sneezing  Boolean, Fever Boolean, Rash Boolean
, Insomnia Boolean, Vomiting Boolean, Pneumonia Boolean, Fatigue Boolean, Spots Boolean, Diarrhoa Boolean, Convulsions Boolean)""")

# ID,name,coughing,Sneezing,Fever,Rash,Insomnia,Vomiting,Pneumonia,Fatigue,Spots
# ,diarrhoea,convulsions
cursor.execute("""SELECT* FROM diseases""")
test = cursor.fetchall()
if len(test) < 2: #check if there are fewer than 2 records in the table, if there are indeed fewer than 2, insert rows
    cursor.execute("""INSERT INTO diseases VALUES
        (0,'Common Cold',1,1,1,0,0,0,0,1,0,0,0)""")
    cursor.execute("""INSERT INTO diseases VALUES
        (1,'The Flu',1,1,1,0,0,0,1,1,0,0,0)""")
    cursor.execute("""INSERT INTO diseases VALUES
        (2,'The Coronavirus (COVID-19)',1,0,1,0,0,0,1,0,0,0,0)""")
    cursor.execute("""INSERT INTO diseases VALUES
        (3,'Chicken pox',0,0,1,1,0,0,1,0,1,0,0)""")
    cursor.execute("""INSERT INTO diseases VALUES
        (4,'Malaria',0,0,1,0,0,1,1,0,0,1,1)""")
    cursor.execute("""INSERT INTO diseases VALUES
        (5,'Tetanus',0,0,1,0,0,1,0,1,0,0,1)""")
    cursor.execute("""INSERT INTO diseases VALUES
        (6,'Meningitis',0,0,1,1,0,1,0,1,0,0,0)""")
    cursor.execute("""INSERT INTO diseases VALUES
        (7,'Cholera',0,0,0,0,0,1,0,1,0,1,0)""")
    cursor.execute("""INSERT INTO diseases VALUES
        (8,'Typhoid',0,0,1,1,0,1,0,0,0,1,0)""")
    cursor.execute("""INSERT INTO diseases VALUES
        (9,'Measles/rubeola',1,1,1,1,0,0,0,1,1,0,0)""")
    cursor.execute("""INSERT INTO diseases VALUES
        (10,'Smallpox',0,0,1,0,1,1,0,0,1,0,0)""")
    cursor.execute("""INSERT INTO diseases VALUES
        (11,'SARS',1,0,1,0,0,1,1,1,0,0,0)""")
    cursor.execute("""INSERT INTO diseases VALUES
        (12,'E-coli',0,0,1,0,0,1,0,0,0,1,1)""")  # remove
    cursor.execute("""INSERT INTO diseases VALUES
        (13,'XX',1,1,1,1,1,1,1,1,1,1,1)""")
    cursor.execute("""INSERT INTO diseases VALUES
        (14,'Ebola',1,0,1,1,0,1,0,0,0,1,1)""")
    cursor.execute("""INSERT INTO diseases VALUES
        (15,'Zika',0,0,1,1,1,1,0,1,0,0,0)""")
    cursor.execute("""INSERT INTO diseases VALUES
        (16,'The black death',1,1,1,0,0,0,1,1,1,1,1)""")
    cursor.execute("""INSERT INTO diseases VALUES
        (17,'Pertussis',1,1,1,0,0,1,1,1,0,0,0)""")
    cursor.execute("""INSERT INTO diseases VALUES
        (18,'Salmonella',0,0,1,0,0,1,0,1,0,1,0)""")
    cursor.execute("""INSERT INTO diseases VALUES
        (19,'Acne',0,0,0,0,0,0,0,0,1,0,0)""")
    cursor.execute("""INSERT INTO diseases VALUES
        (20,'Alergies',0,1,0,1,0,0,0,0,0,0,0)""")
    cursor.execute("""INSERT INTO diseases VALUES
        (21,'Screen eyes',0,0,1,0,1,0,0,0,0,0,0)""")
    cursor.execute("""INSERT INTO diseases VALUES
        (22,'AIDS(HIV)',0,0,1,1,0,1,0,1,1,1,0)""")
    cursor.execute("""INSERT INTO diseases VALUES
        (23,'Skin cancer',0,0,0,1,0,0,1,0,1,0,0)""")
    cursor.execute("""INSERT INTO diseases VALUES
        (24,'Lung cancer',1,0,0,0,0,1,1,1,0,0,1)""")
    cursor.execute("""INSERT INTO diseases VALUES
        (25,'Undernutrition',0,0,1,1,0,0,0,1,0,0,0)""")
    cursor.execute("""INSERT INTO diseases VALUES
        (26,'Diabeties',0,0,1,0,1,1,0,1,1,0,0)""")
    connection.commit()
    connection.close()


def coughing():
    if cough['bg'] == '#FF0000':
        cough['bg'] = '#55FF55'  #if its already red, set to green, elif it is not red, set to red
    else:
        cough['bg'] = '#FF0000'


def sneezing():
    if sneeze['bg'] == '#FF0000':
        sneeze['bg'] = '#55FF55'
    else:
        sneeze['bg'] = '#FF0000'


def fevering():
    if fever['bg'] == '#FF0000':
        fever['bg'] = '#55FF55'
    else:
        fever['bg'] = '#FF0000'


def rashing():
    if rash['bg'] == '#FF0000':
        rash['bg'] = '#55FF55'
    else:
        rash['bg'] = '#FF0000'


def insomning():
    if insomnia['bg'] == '#FF0000':
        insomnia['bg'] = '#55FF55'
    else:
        insomnia['bg'] = '#FF0000'


def vomiting():
    if vomit['bg'] == '#FF0000':
        vomit['bg'] = '#55FF55'
    else:
        vomit['bg'] = '#FF0000'


def pneumoning():
    if pneumonia['bg'] == '#FF0000':
        pneumonia['bg'] = '#55FF55'
    else:
        pneumonia['bg'] = '#FF0000'


def fatiguing():
    if fatigue['bg'] == '#FF0000':
        fatigue['bg'] = '#55FF55'
    else:
        fatigue['bg'] = '#FF0000'


def spotting():
    if spots['bg'] == '#FF0000':
        spots['bg'] = '#55FF55'
    else:
        spots['bg'] = '#FF0000'


def pooping():
    if diarrhoa['bg'] == '#FF0000':
        diarrhoa['bg'] = '#55FF55'
    else:
        diarrhoa['bg'] = '#FF0000'


def seizing():
    if convulsions['bg'] == '#FF0000':
        convulsions['bg'] = '#55FF55'
    else:
        convulsions['bg'] = '#FF0000'


def sub():
    #This funciton checks the bg colour of multiple elements, if it is green,it sets a corresponding variable to 1, else 0.
    # symtom's present (1) or absent (0) .
    connection = sqlite3.connect("Diseases.db")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS diseases (ID Primary key, name Text, coughing Boolean, Sneezing  Boolean, Fever Boolean, Rash Boolean
, Insomnia Boolean, Vomiting Boolean, Pneumonia Boolean, Fatigue Boolean, Spots Boolean, Diarrhoa Boolean, Convulsions Boolean)""")
    if cough[
        'bg'] == '#55FF55':  # its a shame I can only use if statements for this bit. (There might be a way around it).
        vcoughing = 1
    else:
        vcoughing = 0
    if sneeze['bg'] == '#55FF55':
        vsneezing = 1
    else:
        vsneezing = 0
    if fever['bg'] == '#55FF55':
        vfever = 1
    else:
        vfever = 0
    if rash['bg'] == '#55FF55':
        vrash = 1
    else:
        vrash = 0
    if insomnia['bg'] == '#55FF55':
        vinsomnia = 1
    else:
        vinsomnia = 0
    if vomit['bg'] == '#55FF55':
        vvomit = 1
    else:
        vvomit = 0
    if pneumonia['bg'] == '#55FF55':
        vpneumonia = 1
    else:
        vpneumonia = 0
    if fatigue['bg'] == '#55FF55':
        vfatigue = 1
    else:
        vfatigue = 0
    if spots['bg'] == '#55FF55':
        vspots = 1
    else:
        vspots = 0
    if diarrhoa['bg'] == '#55FF55':
        vdiarrhoa = 1
    else:
        vdiarrhoa = 0
    if convulsions['bg'] == '#55FF55':
        vconvulsions = 1
    else:
        vconvulsions = 0
    one.configure(text='')  #a label used to display the 1 % likely hood of disease, clear it here to refresh
    five.configure(text='')
    twenty.configure(text='')
    fifty.configure(text='')
    connection.commit()  #save modification to the database
    calculate(connection, cursor, vcoughing, vsneezing, vfever, vrash, vinsomnia, vvomit, vpneumonia, vfatigue, vspots,
              vdiarrhoa, vconvulsions, fifty, twenty, five, one)
    check()


def calculate(connection, cursor, vcoughing, vsneezing, vfever, vrash, vinsomnia, vvomit, vpneumonia, vfatigue, vspots,
              vdiarrhoa, vconvulsions, fifty, twenty, five, one):
    symptoms = [vcoughing, vsneezing, vfever, vrash, vinsomnia, vvomit, vpneumonia, vfatigue, vspots, vdiarrhoa,
                vconvulsions]
    cursor.execute(
        "SELECT name FROM diseases WHERE coughing=? AND Sneezing=? AND  Fever=? AND Rash=? AND Insomnia=? AND Vomiting=? AND Pneumonia=? AND Fatigue=? AND Spots=? AND Diarrhoa=? AND Convulsions=?",
        (vcoughing, vsneezing, vfever, vrash, vinsomnia, vvomit, vpneumonia, vfatigue, vspots, vdiarrhoa, vconvulsions)) # provides value for the placeholders ?
    Most = cursor.fetchall()
    print("\n---------------------------------------------------\n")
    print("\nMost likely disease(s) you have (>50% sure): \n")
    for i in range(0, len(Most)):
        print(Most[i][0])
        fifty.configure(text=fifty['text'] + Most[i][0] + ',\n')
    # cursor.execute("SELECT name FROM diseases WHERE coughing=? AND Sneezing=? AND  Fever=? AND Rash=?",   (vcoughing, vsneezing, vfever, vrash,))
    # Common=cursor.fetchall()
    # print("Common disease(s) you may have: \n")
    # for i in range(0,len(Common)):
    # print(Common[i])
    # --------------------------50%
    probably = []
    for i in range(0, len(symptoms)):
        temp = symptoms[i]
        symptoms[i] = 1 - symptoms[i]
        cursor.execute(
            "SELECT name FROM diseases WHERE coughing=? AND Sneezing=? AND  Fever=? AND Rash=? AND Insomnia=? AND Vomiting=? AND Pneumonia=? AND Fatigue=? AND Spots=? AND Diarrhoa=? AND Convulsions=?",
            (symptoms[0], symptoms[1], symptoms[2], symptoms[3], symptoms[4], symptoms[5], symptoms[6], symptoms[7],
             symptoms[8], symptoms[9], symptoms[10]))
        Possible = cursor.fetchall()
        for j in range(0, len(Possible)):
            if duplication_check(Possible[j], probably) == False and duplication_check(Possible[j], Most) == False:
                probably.append(Possible[j])
        symptoms[i] = temp
    print("\nProbable diseases you may have (>20% sure): \n")
    for i in range(0, len(probably)):
        print(probably[i][0])
        twenty.configure(text=twenty['text'] + probably[i][0] + ',\n')
    # --------------------------20%
    possibly = []
    for i in range(0, len(symptoms)):
        for j in range(0, len(symptoms)):
            if i != j:
                temp = symptoms[i]
                tempa = symptoms[j]
                symptoms[i] = 1 - symptoms[i]
                symptoms[j] = 1 - symptoms[j]
                cursor.execute(
                    "SELECT name FROM diseases WHERE coughing=? AND Sneezing=? AND  Fever=? AND Rash=? AND Insomnia=? AND Vomiting=? AND Pneumonia=? AND Fatigue=? AND Spots=? AND Diarrhoa=? AND Convulsions=?",
                    (symptoms[0], symptoms[1], symptoms[2], symptoms[3], symptoms[4], symptoms[5], symptoms[6],
                     symptoms[7], symptoms[8], symptoms[9], symptoms[10]))
                Possible = cursor.fetchall()
                for k in range(0, len(Possible)):
                    if duplication_check(Possible[k], probably) == False and duplication_check(Possible[k],
                                                                                               possibly) == False and duplication_check(
                            Possible[k], Most) == False:
                        possibly.append(Possible[k])
                symptoms[i] = temp
                symptoms[j] = tempa
    print("\nPossible diseases you may have (>5% sure): \n")
    for i in range(0, len(possibly)):
        print(possibly[i][0])
        five.configure(text=five['text'] + possibly[i][0] + ',\n')
    # --------------------------50%
    nah = []
    for i in range(0, len(symptoms)):
        for j in range(0, len(symptoms)):
            for k in range(0, len(symptoms)):
                if i != j and i != k and k != j:
                    temp = symptoms[i]
                    tempa = symptoms[j]
                    tempb = symptoms[k]
                    symptoms[i] = 1 - symptoms[i]
                    symptoms[j] = 1 - symptoms[j]
                    symptoms[k] = 1 - symptoms[k]
                    cursor.execute(
                        "SELECT name FROM diseases WHERE coughing=? AND Sneezing=? AND  Fever=? AND Rash=? AND Insomnia=? AND Vomiting=? AND Pneumonia=? AND Fatigue=? AND Spots=? AND Diarrhoa=? AND Convulsions=?",
                        (symptoms[0], symptoms[1], symptoms[2], symptoms[3], symptoms[4], symptoms[5], symptoms[6],
                         symptoms[7], symptoms[8], symptoms[9], symptoms[10]))
                    doubt = cursor.fetchall()
                    for l in range(0, len(doubt)):
                        if duplication_check(doubt[l], nah) == False and duplication_check(doubt[l],
                                                                                           probably) == False and duplication_check(
                                doubt[l], possibly) == False and duplication_check(doubt[l], Most) == False:
                            nah.append(doubt[l])
                    symptoms[i] = temp
                    symptoms[j] = tempa
                    symptoms[k] = tempb
    print("\nDiseases theres a small chance you have(>1% sure): \n")
    for i in range(0, len(nah)):
        print(nah[i][0])
        one.configure(text=one['text'] + nah[i][0] + ',\n')
    diagnosis(symptoms)
    return (one, five, twenty, fifty, Chance, this)


def duplication_check(element, table):
    for i in range(0, len(table)):
        if element == table[i]:
            return (True)
    return (False)


def diagnosis(symptoms):
    count = 0
    for i in range(0, len(symptoms)):
        if symptoms[i] == 1:
            if i > 8:
                count = count + 5  # 10
            elif i == 5 or i == 6 or i == 8:
                count = count + 3  # 9
            elif i == 2 or i == 3 or i == 7:
                count = count + 2  # 6
            else:
                count = count + 1  # 3
    if count == 0:
        this.configure(text="You're healthy, stop wasting time")
    elif count < 1:
        this.configure(text='You should be fine.')
    elif count < 2:
        this.configure(text='Be more careful.')
    elif count < 4:
        this.configure(text='Take a day off to get better.')
    elif count < 8:
        this.configure(text='Take a day off and get advice/healthcare.')
    elif count < 14:
        this.configure(text='Isolate, get a doctors advice.')
    elif count < 20:
        this.configure(text='Call a doctor for immediate help.')
    elif count < 28:
        this.configure(text='Get immediate healthcare now.')
    else:
        this.configure(text='Find a grave.')
    # count=((count/28*100)//2)
    count = (((count ** 2) * 100) // 784)
    Chance.configure(text=(str(count) + '%'))
    return (Chance, this)


def check():
    print(fifty['text'])
    if fifty['text'] == 'XX,\n':
        webbrowser.open("https://www.youtube.com/watch?v=sbCUP85vIHI")


print("loading...")
z = tkinter.Tk()
z.geometry("1200x700")
x = tkinter.Label(z, bg='#EEEEEE')
x.grid(row=0, column=0)
y = tkinter.Label(z, bg='#DDDDDD', height=45, width=30)
y.grid(row=0, column=1)
d = tkinter.Label(z, bg='#DDDDDD', height=45, width=30)
d.grid(row=0, column=2)
# init_______________________________________________
cough = tkinter.Button(x, text='Coughing?', command=coughing, bg='#FF0000', height=3, width=25)
cough.grid(row=0, column=0)
coughadvice = tkinter.Label(x, bg='#DDDDFF', height=3, width=80, wraplength=300,
                            text='Any: soreness or discomfort in the throat. Could be from just a soreness to persistant coughing.')
coughadvice.grid(row=0, column=1)
sneeze = tkinter.Button(x, text='Sneezing?', command=sneezing, bg='#FF0000', height=3, width=25)
sneeze.grid(row=1, column=0)
sneezeadvice = tkinter.Label(x, bg='#DDDDFF', height=3, width=80, wraplength=300,
                             text='From any blockage, runnyness or bleeding in the nose to frequent fluid discharges (sneezes).')
sneezeadvice.grid(row=1, column=1)
fever = tkinter.Button(x, text='Fever/Headache?', command=fevering, bg='#FF0000', height=3, width=25)
fever.grid(row=2, column=0)
feveradvice = tkinter.Label(x, bg='#DDDDFF', height=3, width=80, wraplength=300,
                            text='Any: head or neck discomfort,headache or sensitivity to light or sound.High forehead temperatures also count.')
feveradvice.grid(row=2, column=1)
rash = tkinter.Button(x, text='Rash?', command=rashing, bg='#FF0000', height=3, width=25)
rash.grid(row=3, column=0)
rashadvice = tkinter.Label(x, bg='#DDDDFF', height=3, width=80, wraplength=300,
                           text='Any: blemishes or itchyness on the skin. Is typically red/pink and scratched.')
rashadvice.grid(row=3, column=1)
insomnia = tkinter.Button(x, text='Insomnia?', command=insomning, bg='#FF0000', height=3, width=25)
insomnia.grid(row=4, column=0)
insomniaadvice = tkinter.Label(x, bg='#DDDDFF', height=3, width=80, wraplength=300,
                               text='A Significant difficulty sleeping or staying asleep. Includes discomfort as a cause.')
insomniaadvice.grid(row=4, column=1)
vomit = tkinter.Button(x, text='Nausea/Vomiting?', command=vomiting, bg='#FF0000', height=3, width=25)
vomit.grid(row=5, column=0)
vomitadvice = tkinter.Label(x, bg='#DDDDFF', height=3, width=80, wraplength=300,
                            text='Any: mild stomach discomfort or vomiting.')
vomitadvice.grid(row=5, column=1)
pneumonia = tkinter.Button(x, text='Pneumonia/lack of breath?', command=pneumoning, bg='#FF0000', height=3, width=25)
pneumonia.grid(row=6, column=0)
pneumoniaadvice = tkinter.Label(x, bg='#DDDDFF', height=3, width=80, wraplength=300,
                                text='Any: shortness of breath or coughing/choking due to fluid/blood.')
pneumoniaadvice.grid(row=6, column=1)
fatigue = tkinter.Button(x, text='Fatigue/Muscle-pain?', command=fatiguing, bg='#FF0000', height=3, width=25)
fatigue.grid(row=7, column=0)
fatigueadvice = tkinter.Label(x, bg='#DDDDFF', height=3, width=80, wraplength=300,
                              text='Any: Significant tiredness, loss of appetite.')
fatigueadvice.grid(row=7, column=1)
spots = tkinter.Button(x, text='Spots/Cysts?', command=spotting, bg='#FF0000', height=3, width=25)
spots.grid(row=8, column=0)
spotsadvice = tkinter.Label(x, bg='#DDDDFF', height=3, width=80, wraplength=300,
                            text='Any: spots, blisters or lumps on the body.')
spotsadvice.grid(row=8, column=1)
diarrhoa = tkinter.Button(x, text='Diarrhea?', command=pooping, bg='#FF0000', height=3, width=25)
diarrhoa.grid(row=9, column=0)
diarrhoaadvice = tkinter.Label(x, bg='#DDDDFF', height=3, width=80, wraplength=300,
                               text='Any: Large stomach discomfort, discoloured or sloppy poos.')
diarrhoaadvice.grid(row=9, column=1)
convulsions = tkinter.Button(x, text='Convulsions/seizures?', command=seizing, bg='#FF0000', height=3, width=25)
convulsions.grid(row=10, column=0)
convulsionsadvice = tkinter.Label(x, bg='#DDDDFF', height=3, width=80, wraplength=300,
                                  text='Any: Joint pain, Sudden jerks, froth, Extreme shaking')
convulsionsadvice.grid(row=10, column=1)
# --------------------------------------------------------------
Diseases = tkinter.Label(y, bg='#BBBBDD', height=4, width=30, wraplength=300, text='Diseases')
Diseases.grid(row=0, column=0)
fiftyframe = tkinter.Label(y, bg='#FFD0D0', height=3, width=30, wraplength=200,
                           text='Most likely disease(s) you have (>50% sure): ')
fiftyframe.grid(row=1, column=0)
fifty = tkinter.Label(y, bg='#FFE0E0', height=6, width=30, wraplength=200, text='')
fifty.grid(row=2, column=0)
twentyframe = tkinter.Label(y, bg='#FFEED0', height=3, width=30, wraplength=200,
                            text='Probable diseases you may have (>20% sure): ')
twentyframe.grid(row=3, column=0)
twenty = tkinter.Label(y, bg='#FFF0E0', height=6, width=30, wraplength=200, text='')
twenty.grid(row=4, column=0)
fiveframe = tkinter.Label(y, bg='#FFFFDD', height=3, width=30, wraplength=200,
                          text='Possible diseases you may have (>5% sure): ')
fiveframe.grid(row=5, column=0)
five = tkinter.Label(y, bg='#FFFFEE', height=6, width=30, wraplength=200, text='')
five.grid(row=6, column=0)
oneframe = tkinter.Label(y, bg='#DDFFDD', height=3, width=30, wraplength=200,
                         text='Diseases theres a small chance you have(>1% sure): ')
oneframe.grid(row=7, column=0)
one = tkinter.Label(y, bg='#EEFFEE', height=6, width=30, wraplength=200, text='')
one.grid(row=8, column=0)
# --------------------------------------------------------------
Diagnosis = tkinter.Label(d, bg='#AAAAAA', height=6, width=30, wraplength=300, text='Statistics')
Diagnosis.grid(row=0, column=0)
Survival = tkinter.Label(d, bg='#CCCCCC', height=4, width=30, wraplength=300, text="Rough chance you'll die:")
Survival.grid(row=1, column=0)
Chance = tkinter.Label(d, bg='#EEEEEE', height=6, width=30, wraplength=300, text='')
Chance.grid(row=2, column=0)
whattodo = tkinter.Label(d, bg='#CCCCCC', height=4, width=30, wraplength=300, text="Diagnosis:")
whattodo.grid(row=3, column=0)
this = tkinter.Label(d, bg='#EEEEEE', height=6, width=30, wraplength=200, text='')
this.grid(row=4, column=0)
block = tkinter.Label(d, bg='#DDDDDD', height=16, width=30, wraplength=300, text='')
block.grid(row=5, column=0)

# --------------------------------------------------------------
submit = tkinter.Button(x, text='Submit symptoms', command=sub, bg='#FFFF00', height=3, width=50)
submit.grid(row=11, column=1)
Death = tkinter.Label(x, bg='#EEEEFF', height=3, width=25, wraplength=200, text='What disease have you got? ---->')
Death.grid(row=11, column=0)
print("Ready! see results here")
time.sleep(1)

tkinter.Tk().mainloop()
