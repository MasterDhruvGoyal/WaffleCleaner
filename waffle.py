from pyodide import create_proxy
import random
price = 0
membfee = 0
buttoncount = 0
basicbutton=document.getElementById("basicsign")
probutton=document.getElementById("prosign")
premiumbutton=document.getElementById("premiumsign")
joinbutton=document.getElementById("joinmember")
areaSlider = document.getElementById("area")
ConSlide = document.getElementById("confirmSlide")
SqueegeeChoice = document.getElementById("squeegee")
ClothChoice = document.getElementById("cloth")
OneSideChoice = document.getElementById("window")
TwoSideChoice = document.getElementById("sidepane")
def BasicColor(event):
    global price
    basicbutton.setAttribute("style", "background-color:red")
    probutton.setAttribute("style", "background-color:#04AA6D")
    premiumbutton.setAttribute("style", "background-color:#04AA6D")
    price = 0
    price = price + .5
    console.log(price)
cc = create_proxy(BasicColor)
basicbutton.addEventListener("click",cc)
def ProColor(event):
    global price
    probutton.setAttribute("style", "background-color:red")
    basicbutton.setAttribute("style", "background-color:#04AA6D")
    premiumbutton.setAttribute("style", "background-color:#04AA6D")
    price = 0
    price = price + 1
    console.log(price)
cc = create_proxy(ProColor)
probutton.addEventListener("click",cc)
def PremiumColor(event):
    global price
    premiumbutton.setAttribute("style", "background-color:red")
    probutton.setAttribute("style", "background-color:#04AA6D")
    basicbutton.setAttribute("style", "background-color:#04AA6D")
    price = 0
    price = price + 2
    console.log(price)
cc = create_proxy(PremiumColor)
premiumbutton.addEventListener("click",cc)

code = [
    "waffles4ever",
    "everydayiswaffleday",
    "waffletime",
    "wafflesarethebest",
    "wafflesfordinner",
    "waffl",
    "Ilovewaffles",
    "pandanwaffle",
    "itiswaffletime",
    "15waffle8",
    "waffleeater"
]

def join(event):
    global membfee
    global buttoncount
    if (buttoncount % 2)==0:
        Element('code').element.innerText = random.choice(code)
        Element('instructions').element.innerText = "Enter the code above EXACTLY to join the Waffle Club! When using our services again, do not press on this to avoid paying again. Just type the same code and enjoy!"
        membfee = membfee + 8
        console.log(membfee)
        buttoncount = buttoncount + 1
        Element('joinmember').element.innerText = "Close"
    else:
        Element('code').element.innerText = ""
        Element('instructions').element.innerText = ""
        buttoncount = buttoncount + 1
        Element('joinmember').element.innerText = "Join the Waffle Club"
cc = create_proxy(join)
joinbutton.addEventListener("click",cc)

areapirce = 0

def getVal(event):
    global areapirce
    sliderval = int(areaSlider.value)
    Element('wafVal').element.innerText = sliderval
    areapirce = sliderval
    if areapirce == 1:
        areapirce = .5
        console.log(areapirce)
    elif areapirce == 2:
        areapirce = .8
        console.log(areapirce)
    elif areapirce == 3:
        areapirce = 1.3
        console.log(areapirce)
    elif areapirce == 4:
        areapirce = 2
        console.log(areapirce)
cc = create_proxy(getVal)
areaSlider.addEventListener("input",cc)



sCount = 0
cCount = 0
oCount = 0
tCount = 0
mPrice = 0
sPrice = 0

squeegee_selected = False
cloth_selected = False

def update_mPrice():
    global mPrice
    if squeegee_selected and cloth_selected:
        mPrice = 1.5
    elif squeegee_selected or cloth_selected:
        mPrice = 1
    else:
        mPrice = 0
    console.log(mPrice)

def sChoices(event):
    global sCount
    global squeegee_selected
    sCount += 1
    if (sCount % 2) == 0:
        SqueegeeChoice.setAttribute("style", "text-shadow: 0 0 0 0")
        squeegee_selected = False
    else:
        SqueegeeChoice.setAttribute("style", "text-shadow: 0 0 10px #00d2ff")
        squeegee_selected = True
    update_mPrice()

cc = create_proxy(sChoices)
SqueegeeChoice.addEventListener("click", cc)

def cChoices(event):
    global cCount
    global cloth_selected
    cCount += 1
    if (cCount % 2) == 0:
        ClothChoice.setAttribute("style", "text-shadow: 0 0 0 0")
        cloth_selected = False
    else:
        ClothChoice.setAttribute("style", "text-shadow: 0 0 10px #00d2ff")
        cloth_selected = True
    update_mPrice()

cc = create_proxy(cChoices)
ClothChoice.addEventListener("click", cc)

#SIDES
selected_choice = None

def oChoices(event):
    global selected_choice
    global sPrice
    if selected_choice != "OneSide":
        OneSideChoice.setAttribute("style", "text-shadow: 0 0 10px #ff0000")
        TwoSideChoice.setAttribute("style", "text-shadow: 0 0 0 0")
        sPrice = 1.5
        selected_choice = "OneSide"
    else:
        OneSideChoice.setAttribute("style", "text-shadow: 0 0 0 0")
        sPrice = 0
        selected_choice = None
    console.log(sPrice)

cc = create_proxy(oChoices)
OneSideChoice.addEventListener("click", cc)

def tChoices(event):
    global selected_choice
    global sPrice
    if selected_choice != "TwoSide":
        TwoSideChoice.setAttribute("style", "text-shadow: 0 0 10px #ff0000")
        OneSideChoice.setAttribute("style", "text-shadow: 0 0 0 0")
        sPrice = 2
        selected_choice = "TwoSide"
    else:
        TwoSideChoice.setAttribute("style", "text-shadow: 0 0 0 0")
        sPrice = 0
        selected_choice = None
    console.log(sPrice)

cc = create_proxy(tChoices)
TwoSideChoice.addEventListener("click", cc)

