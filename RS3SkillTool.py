# RS3SKillTool
#

print("RS3SKILLTOOL\n")
print("********************")


# CALCULATION METHOD FOR MERCHANDISE
def calculate():
    print("********************************************************************************")
    name = input("What item are you buying and selling?: ")
    cost = int(input("How much gold per unit are you investing?: "))
    units = int(input("How many units will you be purchasing?: "))
    resale = int(input("How much gold are you selling the units for?: "))
    print("")
    investment = cost * units
    roi = units * resale
    profit = roi - investment

    margin = resale - cost

    print("Unit Purchase Price: " + "{:,}".format(cost) + "g\n" +
          "Units Purchased: " + "{:,}".format(units) + "\n" +
          "Unit Resale Value: " + "{:,}".format(resale) + "g\n" +
          "Profit Margin of: " + "{:,}".format(margin) + "g\n\n" +
          "You will spend " + "{:,}".format(investment) + "g and resell for "
          + "{:,}".format(roi) + "g " +
          name + " will profit you " + "{:,}".format(profit) + "g\n")
    print("********************************************************************************")
    main()


def xp():
    totalXp = float(input("How much XP until you level? "))
    bonusXp = float(input("How much Bonus XP do you have?"))
    item = input("What are you killing? ")
    earnedXp = float(input("How much XP are getting per kill? "))
    print("")
    # handle xp, if there is bonus XP present
    if (bonusXp > 0):
        bonusXpEarned = earnedXp
        bonusKills = bonusXp / bonusXpEarned
        totalXp = totalXp - bonusXp
        regKills = totalXp / (earnedXp / 2)
        totalKills = regKills + bonusKills
        print("You need to kill " + "%.2f" % totalKills + " more " + item + " to level.")
    else:
        totalKills = totalXp / earnedXp
        print("You need to kill " + "%.2f" % totalKills + " more " + item + " to level.")
    main()


# MAIN METHOD
def main():
    print("\nChoose an option: merch, combat, skill, help")
    version = input("Use: ")
    print("")
    if (version == "merch" or version == "Merch"):
        calculate()
    elif (version == "Combat" or version == "combat"):
        xp()
    elif (version == "help" or version == "Help" or version == "HELP"):
        helpMenu()
    elif (version == "skill" or version == "skills" or version == "Skill"):
        skillMenu()
    else:
        print("\nERROR:Please enter a valid option.\n")
        main()


# skillsMethod
def skillMenu():
    print("SKILL LIST")
    print("********************************************************************************")
    print("prayer, crafting, mining, smithing, fishing, cooking, firemaking, woodcutting")
    print("runecrafting, dungeoneering, agility, herblore, thieving, fletching")
    print("slayer, farming, construction, hunter, summoning, divination, invention\n")
    skill = input("What skill are you working on? ")

    if (skill == "prayer" or skill == "pray" or skill == "Pray" or skill == "PRAY"):
        prayer()
    elif (skill == "crafting" or skill == "craft" or skill == "Craft"
          or skill == "CRAFT" or skill == "CRAFTING"):
        crafting()
    elif (skill == "mining" or skill == "minin" or skill == "Mining" or skill == "MINING"):
        mining()
    elif (skill == "smithing" or skill == "smith" or skill == "Smithing" or skill == "Smith"
          or skill == "smelt" or skill == "smelting" or skill == "Smelt" or skill == "SMELT"):
        smithing()
    elif (skill == "fishing" or skill == "fish"):
        fishing()
    elif (skill == "cooking" or skill == "cook"):
        cooking()
    elif (skill == "firemaking" or skill == "fire" or skill == "fm"):
        firemaking()
    elif (skill == "woodcutting" or skill == "wc"):
        woodcutting()
    elif (skill == "runecrafting" or skill == "rune" or skill == "rc"):
        runecrafting()
    elif (skill == "dungeoneering" or skill == "dung" or skill == "dungeon" or skill == "dungeoning"):
        dungeoneering()
    elif (skill == "agility" or skill == "agile"):
        agility()
    elif (skill == "herblore" or skill == "herb" or skill == "herbs"):
        herblore()
    elif (skill == "thieving" or skill == "steal" or skill == "thief" or skill == "thieve"):
        thieving()
    elif (skill == "fletching" or skill == "fletch"):
        fletching()
    elif (skill == "slayer" or skill == "slay"):
        slayer()
    elif (skill == "farming" or skill == "farm"):
        farming()
    elif (skill == "construction" or skill == "construct" or skill == "constr" or skill == "con"):
        construction()
    elif (skill == "hunter" or skill == "hunt"):
        hunter()
    elif (skill == "summoning" or skill == "summon"):
        summoning()
    elif (skill == "divination" or skill == "div"):
        divination()
    elif (skill == "invention" or skill == "invent" or skill == "engineering" or skill == "engineer"):
        invention()
    else:
        print("\nERROR: You must enter a valid skill.\n")
        skillMenu()


# Skill specific functions

def prayer():
    xpLeft = float(input("How much XP until you level? "))
    item = input("What kind of bones are you burying? ")
    earnedXp = float(input("How much XP are getting per bone? "))
    bones = xpLeft / earnedXp
    print("You need to bury " + "%.2f" % bones + " more " + item + " to level.")
    main()


def crafting():
    xpLeft = float(input("How much XP until you level? "))
    item = input("What are you crafting? ")
    earnedXp = float(input("How much XP are getting per item? "))
    crafting = xpLeft / earnedXp
    print("You need to make " + "%.2f" % crafting + " more " + item + " to level.")
    main()


def mining():
    xpLeft = float(input("How much XP until you level? "))
    item = input("What are you mining? ")
    earnedXp = float(input("How much XP are getting per node? "))
    mining = xpLeft / earnedXp
    print("You need to mine " + "%.2f" % mining + " more " + item + " to level.")
    main()


def smithing():
    xpLeft = float(input("How much XP until you level? "))
    item = input("What are you smelting? ")
    earnedXp = float(input("How much XP are getting per bar? "))
    crafting = xpLeft / earnedXp
    print("You need to smelt " + "%.2f" % crafting + " more " + item + " bars to level.")
    main()


def fishing():
    xpLeft = float(input("How much XP until you level? "))
    item = input("What are you fishing? ")
    earnedXp = float(input("How much XP are getting per fish? "))
    crafting = xpLeft / earnedXp
    print("You need to catch " + "%.2f" % crafting + " more " + item + " to level.")
    main()


def cooking():
    xpLeft = float(input("How much XP until you level? "))
    item = input("What are you cooking? ")
    earnedXp = float(input("How much XP are getting per item? "))
    crafting = xpLeft / earnedXp
    print("You need to cook " + "%.2f" % crafting + " more " + item + " to level.")
    main()


def firemaking():
    xpLeft = float(input("How much XP until you level? "))
    item = input("What kind of logs are you burning? ")
    earnedXp = float(input("How much XP are getting per log? "))
    crafting = xpLeft / earnedXp
    print("You need to light " + "%.2f" % crafting + " more " + item + " logs to level.")
    main()


def woodcutting():
    xpLeft = float(input("How much XP until you level? "))
    item = input("What kind of tree are you cutting? ")
    earnedXp = float(input("How much XP are getting per log? "))
    crafting = xpLeft / earnedXp
    print("You need to cut " + "%.2f" % crafting + " more " + item + "logs to level.")
    main()


def runecrafting():
    xpLeft = float(input("How much XP until you level? "))
    item = input("What runes are you making? ")
    earnedXp = float(input("How much XP are getting per rune? "))
    crafting = xpLeft / earnedXp
    print("You need to make " + "%.2f" % crafting + " more " + item + " runes to level.")
    main()


def dungeoneering():
    xpLeft = float(input("How much XP until you level? "))
    earnedXp = float(input("How much XP are getting per dungeon? "))
    crafting = xpLeft / earnedXp
    print("You need to complete " + "%.2f" % crafting + " more dungeons to level.")
    main()


def agility():
    xpLeft = float(input("How much XP until you level? "))
    earnedXp = float(input("How much XP are getting per obstacle? "))
    crafting = xpLeft / earnedXp
    print("You need to make pass " + "%.2f" % crafting + " more obstacles to level.")
    main()


def herblore():
    xpLeft = float(input("How much XP until you level? "))
    item = input("What are you making or cleaning? ")
    earnedXp = float(input("How much XP are getting per item? "))
    crafting = xpLeft / earnedXp
    print("You need to make/clean " + "%.2f" % crafting + " more " + item + " to level.")
    main()


# TODO: FIX THE THIEVING OUTPUT LANGUAGE
def thieving():
    xpLeft = float(input("How much XP until you level? "))
    item = input("What are you stealing from? ")
    earnedXp = float(input("How much XP are getting per theft? "))
    crafting = xpLeft / earnedXp
    print("You need to steal " + "%.2f" % crafting + " more " + item + " to level.")  # CHANGE THIS
    main()


def fletching():
    xpLeft = float(input("How much XP until you level? "))
    item = input("What are you crafting? ")
    earnedXp = float(input("How much XP are getting per item? "))
    crafting = xpLeft / earnedXp
    print("You need to make " + "%.2f" % crafting + " more " + item + " to level.")
    main()


def slayer():
    xpLeft = float(input("How much XP until you level? "))
    item = input("What are you slaying? ")
    earnedXp = float(input("How much XP are getting per kill? "))
    crafting = xpLeft / earnedXp
    print("You need to slay " + "%.2f" % crafting + " more " + item + " to level.")
    main()


# TODO: finish method
def farming():
    print("FARMING IS GAY... THIS FUNCTION IS COMING SOON")
    main()


# TODO: finish method
def construction():
    print("FUNCTION COMING SOON")
    main()


def hunter():
    xpLeft = float(input("How much XP until you level? "))
    item = input("What are you hunting? ")
    earnedXp = float(input("How much XP are getting per catch? "))
    crafting = xpLeft / earnedXp
    print("You need to hunt " + "%.2f" % crafting + " more " + item + " to level.")
    main()


def summoning():
    xpLeft = float(input("How much XP until you level? "))
    item = input("What are you summoning? ")
    earnedXp = float(input("How much XP are getting per item? "))
    crafting = xpLeft / earnedXp
    print("You need to make " + "%.2f" % crafting + " more " + item + " to level.")
    main()


# TODO: finish method
def divination():
    print("IDK HOW THIS WORKS SO CANT MAKE IT YET")
    main()


# TODO: finish method
def invention():
    print("IDK HOW THIS WORKS SO CANT MAKE IT YET")
    main()


def craftingCost():
    item = input("What are you crafting?")
    counter = int(input("How many ingredients are there?"))


# help menu
def helpMenu():
    print("HELP MENU\n")
    print("Merch: How much can you profit from the Grand Exchange?")
    print("Combat: How many more monsters do I need to kill?")
    print("Skills: How many activities before leveling?\n")
    print("Keep in mind I can change or make updates at anytime.")
    print("Let me know of any suggestions you may have.\n")
    print("********************************************************************************")
    main()


main()