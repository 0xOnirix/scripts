import re

def convert(titleToConvert):

    titleToConvert = str(titleToConvert.lower())

    titleToConvert = re.sub(r'(^#|[^#])# ', r'\1#', titleToConvert)

    if titleToConvert.find("&") != -1: 
        titleToConvert = titleToConvert.replace("&","")
    
    if titleToConvert.find("\"") != -1:
        titleToConvert = titleToConvert.replace("\"","")

    if titleToConvert.find("#") != -1: 
        titleToConvert = titleToConvert.replace("#","")

    if titleToConvert.find("'") != -1:
        titleToConvert = titleToConvert.replace("'","")

    if titleToConvert.find("{") != -1:
        titleToConvert = titleToConvert.replace("{","")

    if titleToConvert.find("}") != -1:
        titleToConvert = titleToConvert.replace("}","")

    if titleToConvert.find("(") != -1:    
        titleToConvert = titleToConvert.replace("(","")
    
    if titleToConvert.find(")") != -1: 
        titleToConvert = titleToConvert.replace(")","")

    if titleToConvert.find("[") != -1:    
        titleToConvert = titleToConvert.replace("[","")
    
    if titleToConvert.find("]") != -1: 
        titleToConvert = titleToConvert.replace("]","")

    if titleToConvert.find("-") != -1: 
        titleToConvert = titleToConvert.replace("-","")

    if titleToConvert.find("|") != -1: 
        titleToConvert = titleToConvert.replace("|","")
    
    if titleToConvert.find("`") != -1: 
        titleToConvert = titleToConvert.replace("`","")

    if titleToConvert.find("\\") != -1: 
        titleToConvert = titleToConvert.replace("\\","")

    if titleToConvert.find("^") != -1: 
        titleToConvert = titleToConvert.replace("^","")

    if titleToConvert.find("@") != -1: 
        titleToConvert = titleToConvert.replace("@","")

    if titleToConvert.find("°") != -1: 
        titleToConvert = titleToConvert.replace("°","")

    if titleToConvert.find("+") != -1: 
        titleToConvert = titleToConvert.replace("+","")

    if titleToConvert.find("=") != -1: 
        titleToConvert = titleToConvert.replace("=","")

    if titleToConvert.find("£") != -1: 
        titleToConvert = titleToConvert.replace("£","")

    if titleToConvert.find("$") != -1: 
        titleToConvert = titleToConvert.replace("$","")

    if titleToConvert.find("¤") != -1: 
        titleToConvert = titleToConvert.replace("¤","")

    if titleToConvert.find("*") != -1: 
        titleToConvert = titleToConvert.replace("*","")

    if titleToConvert.find("%") != -1: 
        titleToConvert = titleToConvert.replace("%","")

    if titleToConvert.find("§") != -1: 
        titleToConvert = titleToConvert.replace("%","")

    if titleToConvert.find("!") != -1: 
        titleToConvert = titleToConvert.replace("!","")
    
    if titleToConvert.find(":") != -1: 
        titleToConvert = titleToConvert.replace(":","")

    if titleToConvert.find(";") != -1: 
        titleToConvert = titleToConvert.replace(";","")

    if titleToConvert.find(".") != -1: 
        titleToConvert = titleToConvert.replace(".","")

    if titleToConvert.find(",") != -1: 
        titleToConvert = titleToConvert.replace(",","")

    if titleToConvert.find("?") != -1: 
        titleToConvert = titleToConvert.replace("?","")

    if titleToConvert.find("<") != -1: 
        titleToConvert = titleToConvert.replace("<","")

    if titleToConvert.find(">") != -1: 
        titleToConvert = titleToConvert.replace(">","")

    if titleToConvert.find(" ") != -1:
        titleToConvert = titleToConvert.replace(" ","-")

    if titleToConvert.find("²") != -1:
        titleToConvert = "Error, \"²\" is not supported in title"

    if titleToConvert.find("¨") != -1:
        titleToConvert = "Error, \"¨\" is not supported in title"

    if titleToConvert.find("µ") != -1: 
        titleToConvert = "Error, \"µ\" is not supported in title"

    titleToConvert = "#" + titleToConvert

    titleToConvert = re.sub(r'-+', '-', titleToConvert)

    return(titleToConvert)

print("\nThis script convert markedown title to markedown anchor\n\nFor exemple \"## Super Title 2\" become \"#super-title-2\"\n\n")

title = input("Title to convert: ")

title = convert(title)

print(title)