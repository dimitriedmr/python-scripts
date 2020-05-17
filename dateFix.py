def convertesteLuna(dataSirIn):
    sirNou = dataSirIn.replace("mai","05")
    if sirNou != dataSirIn:
        return sirNou
    sirNou = dataSirIn.replace("May","05")
    if sirNou != dataSirIn:
        return sirNou
    sirNou = dataSirIn.replace("Mar","03")
    if sirNou != dataSirIn:
        return sirNou
    sirNou = dataSirIn.replace("martie","03")
    if sirNou != dataSirIn:
        return sirNou
    sirNou = dataSirIn.replace("Apr","04")
    if sirNou != dataSirIn:
        return sirNou
    sirNou = dataSirIn.replace("aprilie","04")
    if sirNou != dataSirIn:
        return sirNou
   
    return ""
        
        