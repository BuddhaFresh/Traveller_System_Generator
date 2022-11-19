import random

file = open('name.txt')
gopn = open('governments.txt')
coke = open('tech.txt')
with open('name.txt') as f: #these are to get rid of the hidden /n at the end of a txt file line.
  nomen = f.read().splitlines()
with open('governments.txt') as h:
  govnm = h.read().splitlines()
with open('tech.txt') as i:
  thlv = i.read().splitlines()

cultinfo = {
11: ["Sexist","One gender is considered subservient or inferior to the other."],
12: ["Religious","Culture is heavily influenced by a religion or belief systems, possibly one unique to this world"],
13: ["Artistic","Art and culture are highly prized. Aesthetic design is important in all artefacts produced on world."],
14: ["Ritualised","Social interaction and trade is highly formalised. Politeness and adherence to raditional forms is considered very important."],
15: ["Conservative","The culture resists change and outside influences."],
16: ["Xenophobic","The culture distrusts outsiders and alien influences. Offworlders will face considerable prejudice."],
21: ["Taboo","A particular topic is forbidden and cannot be discussed. Travellers who unwittingly mention this topic will be ostracised."],
22: ["Deceptive","Trickery and equivocation are considered acceptable. Honesty is a sign of weakness."],
23: ["Liberal","The culture welcomes change and offworld influence. Travellers who bring new and strange ideas will be welcomed."],
24: ["Honourable","One’s word is one’s bond in the culture. Lying is both rare and despised."],
25: ["Influenced","The culture is heavily influenced by another, neighbouring world. Roll again for a cultural quirk that has been inherited from the culture."],
26: ["Fusion","The culture is a merger of two distinct cultures. Roll again twice to determine the quirks inherited from these cultures. If the quirks are incompatible, then the culture is likely divided."],
31: ["Barbaric","Physical strength and combat prowess are highly valued in the culture. Travellers may be challenged to a fight, or dismissed if they seem incapable of defending themselves. Sports tend towards the bloody and violent."],
32: ["Remnant","The culture is a surviving remnant of a once-great and vibrant civilisation, clinging to its former glory. The world is filled with crumbling ruins, and every story revolves around the good old days."],
33: ["Degenerate","The culture is falling apart and is on the brink of war or economic collapse. Violent protests are common, and the social order is decaying."],
34: ["Progressive","The culture is expanding and vibrant. Fortunes are being made in trade; science is forging bravely ahead."],
35: ["Recovering","A recent trauma, such as a plague, war, disaster or despotic regime has left scars on the culture."],
36: ["Nexus","Members of many different cultures and species visit here."],
41: ["Tourist Attraction","Some aspect of the culture or the planet draws visitors from all over charted space."],
42: ["Violent","Physical conflict is common, taking the form of duels, brawls or other contests. Trial by combat is a part of their judicial system."],
43: ["Peaceful","Physical conflict is almost unheardof. The culture produces few soldiers, and diplomacy reigns supreme. Forceful Travellers will be ostracised."],
44: ["Obsessed","Everyone is obsessed with or addicted to a substance, personality, act or item. This monomania pervades every aspect of the culture."],
45: ["Fashion","Fine clothing and decoration are considered vitally important in the culture. Underdressed Travellers have no standing here."],
46: ["At war","The culture is at war, either with another planet or polity, or is troubled by terrorists or rebels."],
51: ["Unusual Custom: Offworlders","Space travellers hold a unique position in the culture’s mythology or beliefs, and travellers will be expected to live up to these myths."],
52: ["Unusual Custom: Starport","The planet’s starport is more than a commercial centre; it might be a religious temple, or be seen as highly controversial and surrounded by protestors."],
53: ["Unusual Custom: Media","News agencies and telecommunications channels are especially strange here. Getting accurate information may be difficult."],
54: ["Unusual Customs: Technology","The culture interacts with technology in an unusual way. Telecommunications might be banned, robots might have civil rights, or cyborgs might be property."],
55: ["Unusual Customs: Lifecycle","There might be a mandatory age of termination, or anagathics might be widely used. Family units might be different, with children being raised by the state or  banned in favour of cloning."],
56: ["Unusual Customs: Social Standings","The culture has a distinct caste system. Travellers of a low social standing who do not behave appropriately will face punishment."],
61: ["Unusual Customs: Trade","The culture has an odd attitude towards some aspect of commerce, which may interfere with trade at the spaceport. For example, merchants might expect a gift as part of a deal, or some goods may only be handled by certain families."],
62: ["Unusual Customs: Nobility","Those of high social standing have a strange custom associated with them; perhaps nobles are blinded, or must live in gilded cages, or only serve for a single year before being exiled."],
63: ["Unusual Customs: Sex","The culture has an unusual attitude towards intercourse and reproduction. Perhaps cloning is used instead, or sex is used to seal commercial deals."],
64: ["Unusual Customs: Eating","Food and drink occupies an unusual place in the culture. Perhaps eating is a private affair, or banquets and formal dinners are seen as the highest form of politeness."],
65: ["Unusual Customs: Travel","Travellers may be distrusted or feted, or perhaps the culture frowns on those who leave their homes."],
66: ["Unusual Custom: Conspiracy","Something strange is going on. The government is being subverted by another group or agency."]
}
tcodes = {
0 : ["Ag", "Agricultural"],
1 : ["As", "Asteroid"],
2 : ["Ba", "Barren"],
3 : ["De", "Desert"],
4 : ["Fl", "Fluid Oceans"],
5 : ["Ga", "Garden"],
6 : ["Hi", "High Population"],
7 : ["Ht", "High Tech"],
8 : ["Ie", "Ice-Capped"],
9 : ["In", "Industrial"],
10 : ["Lo", "Low Population"],
11 : ["Lt", "Low Tech"],
12 : ["Na", "Non-Agricultural"],
13 : ["NI", "Non-Industrial"],
14 : ["Po", "Poor"],
15 : ["Ri", "Rich"],
16 : ["Va", "Vacuum"],
17 : ["Wa", "Water World"]
}
sizeinfo = {
0: ["Less than 1000 km","(Like: Asteroid, orbital complex)","Negligible"],
1: ["1,600 km","(Like: Triton)","0.05"],
2: ["3,200 km","(Like: Luna, Europa)","0.15"],
3: ["4,800 km","(Like: Mercury, Ganymede)","0.25"],
4: ["6,400 km","","0.35"],
5: ["8,000 km","(Like: Mars)","0.45"],
6: ["9,600 km","","0.7"],
7: ["11,200 km","","0.9"],
8: ["12,800 km","(Like: Earth)","1.0"],
9: ["14,400 km","","1.25"],
10: ["16,000 km","","1.4"]
}
atmoinfo = {
0: ["None","(Like: Moon)","0.00","Just vacuum. Vacc Suit required. Cumulative 1D DAM every round without a suit. 2D x 10 Rads every round if in space unprotected.","Minimum Tech Level required: 8"],
1: ["Trace","(Like: Mars)","0.001 to 0.09","Trace amounts of gases in the atmosphere. Vacc Suit required. 1D DAM every round without a suit.","Minimum Tech Level required: 8"],
2: ["Very Thin, Tainted","","0.1 to 0.42","An atmosphere too thin the breath in containing harmful elements. Respirator and Filter required. 1D Dam every few minutes or hours if breathing tainted air. 1D DAM every minute without a Respirator.","Minimum Tech Level required: 5"],
3: ["Very Thin","","0.1 to 0.42","An atmosphere too thin the breath in. Respirator required. 1D DAM every minute without a Respirator.","Minimum Tech Level required: 5"],
4: ["Thin, Tainted","","0.43 to 0.7","A thin, but breathable, atmosphere containing harmful elements. Filter required. 1D DAM every few minutes or hours if breathing tainted air.","Minimum Tech Level required: 3"],
5: ["Thin","","0.43 to 0.7","A thin, but breathable, atmosphere.",""],
6: ["Standard","(Like: Earth)","0.71-1.49","A breathable atmosphere.",""],
7: ["Standard, Tainted","","0.71-1.49","A breathable atmosphere containing harmful elements. Filter required. 1D DAM every few minutes or hours if breathing tainted air.","Minimum Tech Level required: 3"],
8: ["Dense","","1.5 to 2.49","A thick N₂/O₂ atmosphere with a surface pressure too high to live in unprotected unless at higher altitudes.",""],
9: ["Dense, tainted","","1.5 to 2.49","A thick N₂/O₂ atmosphere, containing harmful elements, with a surface pressure too high to live in unprotected unless at higher altitudes. Filter required. 1D DAM every few minutes or hours if breathing tainted air.","Minimum Tech Level required: 3"],
10: ["Exotic","","Varies","An exotic atmosphere which is unbreathable but otherwise not hazardous. Air Supply required. 1D DAM every minute without an Air Supply.","Minimum Tech Level required: 8"],
11: ["Corrosive","(Like: Venus)","Varies","A highly dangerous corrosive atmosphere. Vacc Suit required. 1D DAM each round breathing corrosive air.","Minimum Tech Level required: 9"],
12: ["Insidious","","Varies","An atmosphere so corrosive it will distroy seals, filters, and gear after 2D hours on average. Vigilant maintenance or advanced protection gear can prolong survival time. Vacc Suit required. 1D DAM each round breathing corrosive air.","Minimum Tech Level required: 10(A)"],
13: ["Very Dense","","2.5+","A thick N₂/O₂ atmosphere with a surface pressure too high to live in unprotected unless at higher altitudes.","Minimum Tech Level required: 5"],
14: ["Low","","0.5 or less","A N₂/O₂ atmosphere so thin it is only present in lowland topographic and the highest points may be close to vacuum. Vacc Suit may be required. 1D DAM every round without a suit at high enough points.","Minimum Tech Level required: 5"],
15: ["Unusual","","Varies","A stange and unique atmosphere that may behave in unusual manners.","Minimum Tech Level required: 8"]
}
tempinfo = {
0: ["Frozen","-51° or less","A frozen world. No liquid water, very dry atmosphere."],
1: ["Cold","-51° to 0°","An icy world. Little liquid water, extensive ice caps, few clouds."],
2: ["Temperate","0°-30°","A temperate world. Earth-like. Liquid & vaporised water are common, moderate ice caps."],
3: ["Hot","31°-80°","A hot world. Small or no ice caps, little liquid water. Most water in the form of clouds."],
4: ["Boiling","81°+","A boiling world. No ice caps, little liquid water."]
}
hydroinfo = {
0: ["0%-5%","Desert world"],
1: ["6%-15%","Dry world"],
2: ["16%-25%","A few small seas."],
3: ["26%-35%","Small seas and oceans."],
4: ["36%-45%","Wet world"],
5: ["46%-55%","Large oceans"],
6: ["56%-65%",""],
7: ["66%-75%","Earth-like world"],
8: ["76%-85%","Water world"],
9: ["86%-95%","Only a few small islands and archipelagos."],
10: ["96-100%","Almost entirely water."]
}
lawinfo = {
0: ["No restrictions – heavy armour and","a handy weapon recommended…"],
1: ["Poison gas, explosives, undetectable weapons, WMD","Battle dress"],
2: ["Portable energy and laser weapons","Combat armour"],
3: ["Military weapons","Flak"],
4: ["Light assault weapons and submachine guns","Cloth"],
5: ["Personal concealable weapons","Mesh"],
6: ["All firearms except shotguns & stunners; carrying weapons discouraged",""],
7: ["Shotguns",""],
8: ["All bladed weapons, stunners","All visible armour"],
9: ["All weapons","All armour"]
}
baseinfo = {
  0: ["S","Scout"],
  1: ["R","Research"],
  2: ["N","Naval"],
  3: ["TAS","TAS"]
}



def twodsix():
  return(random.randint(2,12))

def onedsix():
  return(random.randint(1,6))

def threedsix():
  return(random.randint(3,18))

def dsixsix():
  x = onedsix()
  y = onedsix()
  z = str(x)+str(y)
  return int(z)

def systemloco():
  x = random.randint(1,8)
  y = random.randint(1,10)
  z = str(x).zfill(2)+str(y).zfill(2)
  return z

def worldname():
  count = len(open('name.txt').readlines())-1 #why do I need -1?
  return count






DCULT = dsixsix()
DSIZE = twodsix()
DATMO = twodsix()
DHYDRO = twodsix()
DTEMP = twodsix()
DPOP = twodsix()
DGOV = twodsix()
DLAW = twodsix()
DTECH = onedsix()
DPORT = twodsix()
tempdata = 99
seewlaw = 99
badair = [0,1,10,11,12]
tlowest = [2,3]
tlow = [4,5,14]
thigh = [8,9]
thigher = [10,13,15]
thighest = [11,12]
bases = ['S','R','N','TAS']
tch = ["Ag","As","Ba","De","Fl","Ga","Hi","Ht","Ie","In","Lo","Lt","Na","NI","Po","Ri","Va","Wa"]




def worldcreation(): #basicly main
  techDM = 0
  wsize = DSIZE-2
  #wsize = 0 #TESTING
  if wsize <= 1:
   techDM =+ 2
  elif wsize >= 2 and wsize <= 4:
   techDM =+ 1 
  
#World Atmosphere  +techDM
  
  hdroDM = 0
  watmo = DATMO-7+wsize
  #watmo = 0 #TESTING
  watmo = max(watmo,0)
  if watmo <= 3:
    techDM =+ 1
  elif watmo >= 10:
    techDM =+ 1
  if watmo in badair:
    hdroDM -= 4

#World Hydrographic  +techDM
  if wsize <= 1:
    whdro = 0
  else:
    whdro = DHYDRO-7+watmo+hdroDM 
    #whdro = 6 #TESTING
  whdro = max(whdro,0)
  whdro = min(whdro,10)
  if whdro == 0 or whdro == 9:
    techDM =+ 1
  elif whdro == 10:
    techDM =+ 2

#World Temperature +tempDM
  tempDM = 0
  if watmo in tlowest:
    tempDM -= 2
  if watmo in tlow:
    tempDM -= 1
  if watmo in thigh:
    tempDM += 1
  if watmo in thigher:
    tempDM += 2
  if watmo in thighest:
    tempDM += 6
  wtemp = DTEMP+tempDM
  #wtemp = 10 #TESTING
  wtemp = max(wtemp,0)
  if wtemp <= 2:
    tempdata = 0
  elif wtemp in range(3,4):
    tempdata = 1
  elif wtemp in range(5,9):
    tempdata = 2
  elif wtemp in range(10,11):
    tempdata = 3
  elif wtemp >= 12:
    tempdata = 4
    
#World Population  +techDM
  portDM = 0
  wpop = DPOP-2
  #wpop = 0 #TESTING
  if wpop >= 8 and wpop < 10:
    portDM =+ 1
  elif wpop >= 10:
    portDM =+ 2
  elif wpop <= 2:
    portDM =+ -2
  elif wpop <= 4 and wpop > 2:
    portDM =+ -1
  elif wpop >= 1 and wpop <= 5:
    techDM =+ 1
  elif wpop == 8:
    techDM =+ 1
  elif wpop == 10:
    techDM =+ 2
  elif wpop == 10:
    techDM =+ 4

#World Government +techDM 
  if wpop == 0:
    wgov = 0
  else:
    wgov = DGOV-7+wpop
    #wgov = 14 #TESTING
    wgov = max(wgov,0)
    if wgov == 0 or wgov == 5:
      techDM =+ 1
    if wgov == 7:
      techDM =+ 2
    if wgov == 13 or 14:
      techDM -= 2
  wgovd = wgov+16
  wgove = wgovd+16
  wgovc = wgove+16
      
#Factions
  factDM = 0
  if wpop == 0:
    wftotal = 0
  else:
    if wgov == 0 or wgov == 7:
     factDM += 1
    elif wgov >= 10:
     factDM -= 1
    wftotal = threedsix()+factDM
    
#World Law  
  if wpop == 0:
    wlaw = 0
  else:
    wlaw = DLAW-7+wgov
    #wlaw = 1 #TESTING
    wlaw = max(wlaw,0)
  seewlaw = min(wlaw,9)

#World Space Port +techDM 
  #wport = DPORT+portDM
  wport = 6 #TESTING
  if wport == 10:
    techDM =+ 6
  elif wport == 11:
    techDM =+ 4
  elif wport == 12:
    techDM =+ 2
  elif wport <= 2:
    techDM -= 4

#World Base
#  rollA = twodsix()
  rollA = 7 #TESTING
  rollB = twodsix()
  rollC = twodsix()
  hexB = ""
  if wport == 5 or wport == 6: #D Ports
    if rollA >= 7:
      hexB += " " + baseinfo[0][0]
  elif wport == 7 or wport == 8: #C Ports
    if rollA >= 8:
      hexB += " " + bases[0]
    if rollB >= 10:
      hexB += " " + bases[1]
    if rollC >= 10:
      hexB += " " + bases[3]
  elif wport == 9 or wport == 10: #B Ports
    if rollA >= 8:
      hexB += " " + bases[1]
    if rollB >= 8:
      hexB += " " + bases[0]
    if rollC >= 10:
      hexB += " " + bases[2]
    if wport == 9 or wport == 10:
      hexB += " " + bases[3]
  elif wport >= 11: #A Ports
    if rollA >= 8:
      hexB += " " + bases[2]
    if rollB >= 10:
      hexB += " " + bases[0]
    if rollC >= 8:
      hexB += " " + bases[1]  
    if wport >= 11:
      hexB += " " + bases[3]
    
#World Tech Level  
  if wpop == 0:
    wtech = 0
  else:
    wtech = DTECH+techDM
    wtech = max(wtech,0)
  #wtech = 0+techDM #TESTING
  wtechn = wtech+16

#UWP Hex Code
  if wport <= 2:
    SP = "X"
  elif wport == 3 or wport == 4:
    SP = "E"
  elif wport == 5 or wport == 6:
    SP = "D"
  elif wport == 7 or wport == 8:
    SP = "C"
  elif wport == 9 or wport == 10:
    SP = "B"
  elif wport >= 11:
    SP = "A"
  SZ = hex(wsize).upper().replace("0X","")
  AT = hex(watmo).upper().replace("0X","")
  HG = hex(whdro).upper().replace("0X","")
  PO = hex(wpop).upper().replace("0X","")
  GV = hex(wgov).upper().replace("0X","")
  LW = hex(wlaw).upper().replace("0X","")
  TH = hex(wtech).upper().replace("0X","")

#Trade Codes  #need to fix
  hexTC = ""
  AgATMO, AgHYDO, AgPOP = [4,5,6,7,8,9], [4,5,6,7,8], [5,6,7]
  GaSIZE, GaATMO, GaHYDO = [6,7,8], [5,6,8], [5,6,7]
  InATMO = [0,1,2,4,7,9]
  PoATMO = [2,3,4,5]
  RiATMO, RiPOP, RiGOV = [6,8], [6,7,8], [4,5,6,7,8,9]
  if watmo in AgATMO and whdro in AgHYDO and wpop in AgPOP:
    hexTC += " " + tch[0]
  if wsize == 0 and watmo == 0 and whdro == 0:
    hexTC += " " + tch[1]
  if wpop == 0 and wgov == 0 and wlaw == 0:
    hexTC += " " + tch[2]
  if watmo >= 2 and whdro == 0:
    hexTC += " " + tch[3]
  if watmo >= 10 and whdro >= 1:
    hexTC += " " + tch[4]
  if wsize in GaSIZE and watmo in GaATMO and whdro in GaHYDO:
    hexTC += " " + tch[5]
  if wpop >= 9:
    hexTC += " " + tch[6]
  if wtech >= 12:
    hexTC += " " + tch[7]
  if watmo <= 1 and whdro >= 1:
    hexTC += " " + tch[8]
  if watmo in InATMO and wpop >= 9:
    hexTC += " " + tch[9]
  if wpop <= 3:
    hexTC += " " + tch[10]
  if wtech <= 5:
    hexTC += " " + tch[11]
  if watmo <= 3 and whdro <= 3 and wpop >= 6:
    hexTC += " " + tch[12]
  if wpop <= 6:
    hexTC += " " + tch[13]
  if watmo in PoATMO and whdro <= 3:
    hexTC += " " + tch[14]
  if watmo in RiATMO and wpop in RiPOP and wgov in RiGOV:
    hexTC += " " + tch[15]
  if watmo == 0:
    hexTC += " " + tch[16]
  if whdro >= 10:
    hexTC += " " + tch[17]
  
  
  
  wname = str(nomen[random.randint(0,worldname())])
  
#Text Output  

  print(f'Size is {wsize} \n Roll was {DSIZE}-2 \n')
  print(f'Atmosphere is {watmo} \n Roll was {DATMO}-7+Size({wsize}) \n')
  print(f'Hydrographic is {whdro} \n Roll was {DHYDRO}-7+Atmosphere({watmo}) \n HydroDM of {hdroDM} \n')
  print(f'Temperature is {wtemp} \n Roll was {DTEMP} \n TempDM of {tempDM} \n')
  print(f'Population is {wpop} \n Roll was {DPOP}-2 \n')
  print(f'Government is {govnm[wgov]} ({wgov}) \n Roll of {DGOV}-7+Population({wpop}) \n FactDM is {factDM} \n Number of factions: {wftotal} \n')
  print(f'Law Level is {wlaw} \n Roll was {DLAW}-7+Government({wgov}) \n')
  print(f'Spaceport Level is {SP} ({wport}) \n Roll was {DPORT} \n PortDM of {portDM} \n')
  print(f'Tech Level is {wtech} \n Roll was {DTECH} \n TechDM of {techDM} \n {thlv[wtech]} \n')

  print(f'{tcodes[0][0]}') #holy shit this works!

 
  print(f"Cultural Difference roll is {DCULT}")
  print(f"""World's cultural difference is {cultinfo[DCULT][0]} - {cultinfo[DCULT][1]} \n\n""")

  print(f'This planet is known as {wname} \n\n')
  print(f'{wname} {systemloco()} {SP}{SZ}{AT}{HG}{PO}{GV}{LW}-{TH}{hexB}{hexTC} \n\n')
  print(f'=======================================')
  print(f"""---◄►Physical World Details◄►---
  ○ Diameter: {sizeinfo[wsize][0]} {sizeinfo[wsize][1]}
  ◙ Surface Gravity: {sizeinfo[wsize][2]} Gs
  ◌ Atmosphere: {atmoinfo[watmo][0]} {atmoinfo[watmo][1]}
      {atmoinfo[watmo][3]}
      {atmoinfo[watmo][4]}
  ◘ Pressure: {atmoinfo[watmo][2]}
  ≈ Hydrographic: {hydroinfo[whdro][0]}
      {hydroinfo[whdro][1]}
  ◊ Average Tempeature: {tempinfo[tempdata][1]}
      {tempinfo[tempdata][2]}

---◄►Civilization Details◄►---
  ☺ Population: 
  
  ♫ Cultural Differences: {cultinfo[DCULT][0]}
      {cultinfo[DCULT][1]}
  Ω Government: {govnm[wgov]} 
    (for example: {govnm[wgove]})
      {govnm[wgovd]}
  ■ Factions: 
  
  ♦ Common Contraband: {govnm[wgovc]}
  ♠ Banned Armament: {lawinfo[seewlaw][0]}
                     {lawinfo[seewlaw][1]}
  Starport Quality: 
  Facilities: 
  Berthing Cost: 
  Bases :
  Tech Level: {thlv[wtechn]}
    {thlv[wtech]}
  
  \n """)
  print(f'=======================================')

worldcreation()

file.close
gopn.close
coke.close