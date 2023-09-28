#lyberis
import getpass



convert={
    "Q":"/",
    "W":"'",
    "E":"ק",
    "R":"ר",
    "T":"א",
    "Y":"ט",
    "U":"ו",
    "I":"ן",
    "O":"ם",
    "P":"פ",

    "A":"ש",
    "S":"ד",
    "D":"ג",
    "F":"כ",
    "G":"ע",
    "H":"י",
    "J":"ח",
    "K":"ל",
    "L":"ך",
    ";":"ף",

    "Z":"ז",
    "X":"ס",
    "C":"ב",
    "V":"ה",
    "B":"נ",
    "N":"מ",
    "M":"צ",
    ",":"ת",
    ".":"ץ",
    "/":"."
}

stri=""
print("******************************************************")
print("----------Welcome to the Terminal Translator----------")
print("******************************************************")
print("--------- after inputing a char press enter ----------")
print("--------------  to end session enter: ~ --------------")
print("----------------- to delete enter: - -----------------")
print("******************************************************")
while True:
    #geting input
        # Print the current string without a newline
    print(stri)
    add = getpass.getpass(":")
    if add!="":
        add=add[0]
        add=add.upper()
        if add in convert:
            add=add[0]
            add=add.upper()
            add = convert[add]
            stri = stri+add
        elif add=="~":
            break
        elif add=="-":
            stri=stri[:-1]
        else:
            stri = stri+add
    else:{}

# Reverse the order of words
words = stri.split()
reversed_words = " ".join(reversed(words))
print("******************************************************")
print("--------------------- END SESSION --------------------")
print("*************************Y4Z**************************")
print(stri)
print("******************************************************")
