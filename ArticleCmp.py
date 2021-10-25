import pandas as pd
import ArticleInp
T = ArticleInp
df = pd.read_csv('cmp.csv')
""""
 Column reading
print(df['Twinspires'][0:5])

 Row reading
first4 = df.head(4)

print(first4)

print(df.iloc[0,1])
"""


#for index, row in df.iterrows():
#    print(index, row[T.FSNA])


# Overall, RS Values
RSA = df.loc[1, T.FSNA]
RSB = df.loc[1, T.FSNB]

SSNA = df.loc[0, T.FSNA]
SSNB = df.loc[0, T.FSNB]

# Overall comparison
if RSA > RSB:
    Ovr = (SSNA + " is a better option than " + SSNB + " in our opinion")
elif RSB > RSA:
    Ovr = (SSNB + " is a better option than " + SSNA + " in our opinion")
elif RSA == RSB:
    Ovr = (SSNA + " and " + SSNB + " are pretty much equal according to our analysis.")

# Round stars into phrases
RTAv = float(RSA)
RTBv = float(RSB)
RTAv = round(RTAv)
RTBv = round(RTBv)

if RTAv == 5:
    RTA = "'Best'"
elif RTAv == 4:
    RTA = "'Great'"
elif RTAv == 3:
    RTA = "'Average'"
elif RTAv == 2:
    RTA = "'Below Average'"
elif RTAv == 1:
    RTA = "'Poor'"
else:
    RTA = "'Couldn't compute overall value'"

if RTBv == 5:
    RTB = "'Best'"
elif RTBv == 4:
    RTB = "'Great'"
elif RTBv == 3:
    RTB = "'Average'"
elif RTBv == 2:
    RTB = "'Below Average'"
elif RTBv == 1:
    RTB = "'Poor'"
else:
    RTB = "Couldn't compute overall value"

# Available States
x = 12
states_available = []
for i in range(0, 15):
    state = df.iloc[x,0]
    if df.loc[x, T.FSNA] == "Yes":
        res = df.iloc[x, 0]
        states_available.append(res)
    else:
        pass
    x += 1

x = 12
states_available_2 = []
for i in range(0, 15):
    state = df.iloc[x,0]
    if df.loc[x, T.FSNB] == "Yes":
        res = df.iloc[x, 0]
        states_available_2.append(res)
    else:
        pass
    x += 1

# Intro Promo overalls
ipA = df.loc[3,T.FSNA]
ipB = df.loc[3,T.FSNB]

# Intro promo description
ipdescA = df.loc[29, T.FSNA]
ipdescB = df.loc[29, T.FSNB]

# Credit type
ipcredA = df.loc[30, T.FSNA]
ipcredB = df.loc[30, T.FSNB]

# Time to use the credit
ipcredtimeA = df.loc[31, T.FSNA]
ipcredtimeB = df.loc[31, T.FSNB]

# Playthrough requirement
ipplayreqA = df.loc[32, T.FSNA]
ipplayreqB = df.loc[32, T.FSNB]

# odds
oddscompA = df.loc[2,T.FSNA]
oddscompB = df.loc[2,T.FSNB]

if oddscompA > oddscompB:
    Ocmp = (SSNA + " is a better option than " + SSNB + " according to our data.")
elif oddscompB > oddscompA:
    Ocmp = (SSNB + " is a better option than " + SSNA + " according to our data.")
elif oddscompA == oddscompB:
    Ocmp = (SSNA + " and " + SSNB + " are pretty much equal according to our data.")
else:
    Ocmp = ("There isnt sufficient data available.")

# Promotions and Odds Boosts
pobA = df.loc[4, T.FSNA]
pobB = df.loc[4, T.FSNB]

if pobA > pobB:
    Pobdesc = (SSNA + " is a better option than " + SSNB + " according to our data.")
elif pobB > pobA:
    Pobdesc = (SSNB + " is a better option than " + SSNA + " according to our data.")
elif pobA == pobB:
    Pobdesc = (SSNA + " and " + SSNB + " are pretty much equal according to our data.")
else:
    Pobdesc = ("There isnt sufficient data available.")

# User interface
uiA = df.loc[6,T.FSNA]
uiB = df.loc[6,T.FSNB]

# UI comparison
if uiA > uiB:
    uidesc = (SSNA + " is a better option than " + SSNB + " according to our data.")
elif uiB > uiA:
    uidesc = (SSNB + " is a better option than " + SSNA + " according to our data.")
elif uiA == uiB:
    uidesc = (SSNA + " and " + SSNB + " are pretty much equal according to our data.")
else:
    uidesc = ("There isnt sufficient data available.")

# UI rounding


uiAv = float(uiA)
uiBv = float(uiB)
uiAv = round(uiAv)
uiBv = round(uiBv)

if uiAv == 5:
    uiRTA = "'Best'"
elif uiAv == 4:
    uiRTA = "'Great'"
elif uiAv == 3:
    uiRTA = "'Average'"
elif uiAv == 2:
    uiRTA = "'Below Average'"
elif uiAv == 1:
    uiRTA = "'Poor'"
else:
    uiRTA = "Couldn't compute overall value"

if uiBv == 5:
    uiRTB = "'Best'"
elif uiBv == 4:
    uiRTB = "'Great'"
elif uiBv == 3:
    uiRTB = "'Average'"
elif uiBv == 2:
    uiRTB = "'Below Average'"
elif uiBv == 1:
    uiRTB = "'Poor'"
else:
    uiRTB = "Couldn't compute overall value"

# Bet Types
# Has to be Yes or No otherwise gives error
ParlA = df.loc[79, T.FSNA]
ParlB = df.loc[79, T.FSNB]

if ParlA == 'Yes' and ParlB == 'Yes':
    Betdesc = SSNA + " and " + SSNB + " both offer same game parlays."
elif ParlA == 'Yes' and ParlB == 'No':
    Betdesc = SSNA + " does offer same game parlays but " + SSNB + " does not."
elif ParlB == 'Yes' and ParlA == 'No':
    Betdesc = SSNB + " does offer same game parlays but " + SSNA + " does not."
else:
    boline = ("We dont have sufficient data at this point in time.")

# Deposits and Withdrawals
DepA = df.loc[7, T.FSNA]
DepB = df.loc[7, T.FSNB]
# Deposit Methods
DepmetA = df.loc[90, T.FSNA]
DepmetB = df.loc[90, T.FSNB]
# Min Deposit
MindepA = df.loc[89, T.FSNA]
MindepB = df.loc[89, T.FSNB]

# Withdrawal Methods
WimetA = df.loc[99, T.FSNA]
WimetB = df.loc[99, T.FSNB]

# Min Withdrawal
MinwitA = df.loc[98, T.FSNA]
MinwitB = df.loc[98, T.FSNB]

# bottom line comparison
if RSA > RSB:
    boline = (SSNA + " is a better option than " + SSNB + ",")
elif RSB > RSA:
    boline = (SSNB + " is a better option than " + SSNA + ",")
elif RSA == RSB:
    boline = (SSNA + " and " + SSNB + " are pretty much equal,")
else:
    boline = ("We dont have sufficient data at this point in time.")