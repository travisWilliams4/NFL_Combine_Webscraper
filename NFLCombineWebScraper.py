from bs4 import BeautifulSoup
import lxml
import requests
import xlsxwriter
import os
#!/usr/bin/python


url = 'http://nflcombineresults.com/nflcombinedata.php'
spreadSheetName = 'NFLCombineRecords'


def parseTheWebsite(url):
    # FULL HTML WILL BE TAKEN FROM URL BELOW
    requestedURL = requests.get(url)
    # FULL HTML WILL BE CONVERTED FROM WHATEVER INTO TEXT THAT WE CAN USE
    wholeDamnWebsiteHTML = requestedURL.text
    # HTML WILL BE 'PARSED' WHATEVER THAT MEANS BELOW
    parsedHTML = BeautifulSoup(wholeDamnWebsiteHTML, 'lxml')
    return parsedHTML


def getHeaders(parsedHTML):
    # ALL ELEMENTS FROM HTML WITHIN <THEAD><TR></TR></THEAD> TAGS TURNED INTO OBJECT
    firstIterationHeaders = parsedHTML.thead.tr
    # ALL ELEMENTS WITH TAG <TD> FROM THE FIRST ITERATION TURNED INTO AN OBJECT
    secondInterationHeaders = firstIterationHeaders.find_all('td')
    # SETTING UP A VARIABLE BECAUSE IT FEELS RIGHT
    finalHeaders = []
    # TAKES EVERYTHING FROM ABOVE TAGS AND TURNS IT INTO A LIST TO USE AS THE HEADERS FOR THE TABLE
    for string in secondInterationHeaders:
        finalHeaders.append(string.text)
    return finalHeaders


def getTableData(parsedHTML):
    # STARTING AGAIN TO GET THE REST OF THE TABLE
    playerDataFirstIteration = parsedHTML.tbody
    # ESTABLISHING A VARIABLE TO STORE THE FINAL DATA IN
    officialPlayerData = []
    # HERES WHERE IT GETS TRICKY
    for listToBeIterated in playerDataFirstIteration.find_all('tr'):
        temporaryPlayerData = []

        for listWithinTheList in listToBeIterated.find_all('td'):
            try:
                getTextText = listWithinTheList.get_text()
                getTextText = float(getTextText)
                if getTextText == 9.99:
                    temporaryPlayerData.append("")
                else:
                    temporaryPlayerData.append(getTextText)

            except:
                getTextText = listWithinTheList.get_text()
                temporaryPlayerData.append(getTextText)

        officialPlayerData.append(temporaryPlayerData)
    return officialPlayerData


# officialPlayerData CONTAINS THE REST OF THE DATA FROM THE TABLE
        

# SETTING UP THE WORKBOOK AKA THE EXCEL FILE
def setUpWorkBook(workBookName):
    workbook = xlsxwriter.Workbook("" + workBookName + ".xlsx")
    # INSERTING A SHEET INTO THE EXCEL FILE
    return workbook

def setUpWorkSheet(workbook):
    worksheet = workbook.add_worksheet()
    # FORMATTING THE HEADER
    return worksheet


# ESTABLISHING THE HEADERS
def insertHeaders(worksheet, finalHeaders, headerFormat):
    rowHeader = 0
    columnHeader = 0
    for header in finalHeaders:
        worksheet.write(rowHeader, columnHeader, header, headerFormat)
        columnHeader += 1


# FILLING IN THE PLAYER DATA
def insertPlayerData(worksheet, officialPlayerData):
    playerRow = 0
    for players in officialPlayerData:
        playerRow += 1
        playerColumn = 0
        for playerStats in players:
            worksheet.write(playerRow, playerColumn, playerStats)
            playerColumn += 1

def formatHeaders(workbook):
    headerFormat = workbook.add_format({'bold': True, 'font_size': 12, 'bg_color': '#D3D3D3', 'bottom': 1})
    return headerFormat

# THE CLUSTER
parsedWebsite = parseTheWebsite(url)
finalHeaders = getHeaders(parsedWebsite)
theWorkbook = setUpWorkBook(spreadSheetName)
theHeaderFormat = formatHeaders(theWorkbook)
officialPlayerData = getTableData(parsedWebsite)
theWorkSheet = setUpWorkSheet(theWorkbook)
insertHeaders(theWorkSheet, finalHeaders, theHeaderFormat)
insertPlayerData(theWorkSheet, officialPlayerData)
theWorkbook.close()

os.startfile('nflcombinerecords.xlsx')

    
