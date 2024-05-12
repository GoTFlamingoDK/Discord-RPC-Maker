from pypresence import Presence
import time

#Husk og Install pypresence & time
#Skriv dette i din terminal "pip install pypresence" & "pip install time"

#Step 1
#opret en Dsicord bot på https://discord.com/developers/applications/

#HUSK AT NAVNGI NOGET "FAMILY FRIENDLY" OG NOGET FEDT SOM "Ostepops" ELLER SÅ NOGET

#Step 2
#Gå til Oauth2 ude i siden og kopier "Client ID"

#Step 3
#Sæt det ind ved "Client_ID"

Client_ID = 12345678

RPC = Presence(Client_ID,pipe=0)
RPC.connect()

#Step 4
#Skriv nu Noget Fedt i Text og Text1

Text = "Hej Med Dig"
Text1 = "Farvel"

while True:
    RPC.update(state=Text1, details=Text)
    time.sleep(15)
