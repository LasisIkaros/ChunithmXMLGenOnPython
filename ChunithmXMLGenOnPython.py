import lxml
import os
from os import walk
import pathlib
from bs4 import BeautifulSoup
soup = BeautifulSoup

CD_Path = (pathlib.Path().absolute())
GameXMLFilesDirPath = [('L:/JMYsun/Arcadefile/Sega/Chunithm/SDBT_1.00-1.50/app/data/A000'),
                       ('L:\JMYsun\Arcadefile\Sega\Chunithm\SDBT_1.00-1.50\option\A001')]
SortFilesCD_Path = [(str(CD_Path)+'/SortFilesOutput/app/data/A000'),
                    (str(CD_Path)+'/SortFilesOutput/option/A001')]
XML_SortFileName = ['CharaSort', 'CourseDifSort', 'CourseSort', 'DDSFieldWallSort', 'DuelSort',
                    'EventSort', 'GenreSort', 'MapIconSort', 'MapSort', 'MusicSort',
                    'NamePlateSort', 'PresentSort', 'QuestSort', 'RightsInfoSort', 'ShopSort',
                    'SkillSort', 'SystemVoiceSort', 'TicketSort', 'TrophySort', 'WorksSort']
XML_FileName = ['Chara', 'Course', 'Course', 'DDSFieldWall', 'Duel',
                'Event', 'Music', 'MapIcon', 'Map', 'Music',
                'NamePlate', 'Present', 'Quest', 'RightsInfo', 'Shop',
                'Skill', 'SystemVoice', 'Ticket', 'Trophy', 'Chara']
XML_FileDirName = ['chara', 'course', 'course', 'ddsFieldWall', 'duel',
                   'event', 'music', 'mapIcon', 'map', 'music',
                   'namePlate', 'present', 'quest', 'rightsInfo', 'shop',
                   'skill', 'systemVoice', 'ticket', 'trophy', 'chara']
XML_TypeName = ['name', 'difficulty', 'name', 'name', 'name',
                'name', 'genreNames', 'name', 'name', 'name',
                'name', 'name', 'name', 'name', 'name',
                'name', 'name', 'name', 'name', 'works']

for i in range(2):
    for j in range(19):
        if not os.path.isdir(str(SortFilesCD_Path[i]+'/'+XML_FileDirName[j])):
            os.makedirs(str(SortFilesCD_Path[i]+'/'+XML_FileDirName[j]))
for i in range(2):
    for j in range(5):
        print('process '+XML_SortFileName[j])
        SortFiles_Path = (
            (str(SortFilesCD_Path[i]+'/'+XML_FileDirName[j]+'/'+XML_SortFileName[j]+'.xml')))
        SortFilesTXT_Path = (
            (str(SortFilesCD_Path[i]+'/'+XML_FileDirName[j]+'/'+XML_SortFileName[j]+'.xml')))
        file = open(SortFiles_Path, mode='w+', encoding="utf-8")
        file.write(
            '<?xml version="1.0" encoding="utf-8"?>\n' +
            '<SerializeSortData xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">\n' +
            '  <dataName>'+XML_FileDirName[j]+'</dataName>\n' +
            '  <formatVersion>10000</formatVersion>\n' +
            '  <resourceVersion>\n' +
            '    <id>0</id>\n' +
            '    <str>10000</str>\n' +
            '    <data />\n' +
            '  </resourceVersion>\n'
        )
        file.close
        file01 = open(SortFiles_Path, mode='a+', encoding="utf-8")
        file01.write("  <SortList>\n")
        for root, dirs, files in os.walk(GameXMLFilesDirPath[i]):
            for name in files:
                if name == (XML_FileName[j]+'.xml'):
                    GameXML = os.path.join(root, name)
                    file = open(GameXML, mode='r', encoding="utf-8")
                    contents = file.read()
                    file.close
                    soup = BeautifulSoup(contents, 'xml')
                    contents = (soup.find(XML_TypeName[j]).contents)
                    file01.write(str("    <StringID>"))
                    for PerLine in contents:
                        file01.write("      "+str(PerLine))
                    file01.write(str("    </StringID>"+"\n"))
        file01.write("  </SortList>"+"\n"+"</SerializeSortData>")
        file01.close
        print(XML_SortFileName[j]+' processed \n')
j = 6
for i in range(2):
    if (j == 6):
        print('process '+XML_SortFileName[j])
        SortFiles_Path = (
            (str(SortFilesCD_Path[i]+'/'+XML_FileDirName[j]+'/'+XML_SortFileName[j]+'.xml')))
        SortFilesTXT_Path = (
            (str(SortFilesCD_Path[i]+'/'+XML_FileDirName[j]+'/'+XML_SortFileName[j]+'.xml')))
        file = open(SortFiles_Path, mode='w+', encoding="utf-8")
        file.write(
            '<?xml version="1.0" encoding="utf-8"?>\n' +
            '<SerializeSortData xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">\n' +
            '  <dataName>'+XML_FileDirName[j]+'</dataName>\n' +
            '  <formatVersion>10000</formatVersion>\n' +
            '  <resourceVersion>\n' +
            '    <id>0</id>\n' +
            '    <str>10000</str>\n' +
            '    <data />\n' +
            '  </resourceVersion>\n'
        )
        file.close
        file01 = open(SortFiles_Path, mode='a+', encoding="utf-8")
        file01.write("  <SortList>\n")
        for root, dirs, files in os.walk(GameXMLFilesDirPath[i]):
            for name in files:
                if name == (XML_FileName[j]+'.xml'):
                    GameXML = os.path.join(root, name)
                    file = open(GameXML, mode='r', encoding="utf-8")
                    contents = file.read()
                    file.close
                    soup = BeautifulSoup(contents, 'xml')
                    contents = (soup.find('StringID').contents)
                    file01.write(str("    <StringID>"))
                    for PerLine in contents:
                        file01.write("      "+str(PerLine))
                    file01.write(str("    </StringID>"+"\n"))
        file01.write("  </SortList>"+"\n"+"</SerializeSortData>")
        file01.close
        print(XML_SortFileName[j]+' processed\n')
for i in range(2):
    for j in range(7, 19, 1):
        print('process '+XML_SortFileName[j]+'\n')
        SortFiles_Path = (
            (str(SortFilesCD_Path[i]+'/'+XML_FileDirName[j]+'/'+XML_SortFileName[j]+'.xml')))
        SortFilesTXT_Path = (
            (str(SortFilesCD_Path[i]+'/'+XML_FileDirName[j]+'/'+XML_SortFileName[j]+'.xml')))
        file = open(SortFiles_Path, mode='w+', encoding="utf-8")
        file.write(
            '<?xml version="1.0" encoding="utf-8"?>\n' +
            '<SerializeSortData xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">\n' +
            '  <dataName>'+XML_FileDirName[j]+'</dataName>\n' +
            '  <formatVersion>10000</formatVersion>\n' +
            '  <resourceVersion>\n' +
            '    <id>0</id>\n' +
            '    <str>10000</str>\n' +
            '    <data />\n' +
            '  </resourceVersion>\n'
        )
        file.close
        file01 = open(SortFiles_Path, mode='a+', encoding="utf-8")
        file01.write("  <SortList>\n")
        for root, dirs, files in os.walk(GameXMLFilesDirPath[i]):
            for name in files:
                if name == (XML_FileName[j]+'.xml'):
                    GameXML = os.path.join(root, name)
                    file = open(GameXML, mode='r', encoding="utf-8")
                    contents = file.read()
                    file.close
                    soup = BeautifulSoup(contents, 'xml')
                    contents = (soup.find(XML_TypeName[j]).contents)
                    file01.write(str("    <StringID>"))
                    for PerLine in contents:
                        file01.write("      "+str(PerLine))
                    file01.write(str("    </StringID>"+"\n"))
        file01.write("  </SortList>"+"\n"+"</SerializeSortData>")
        file01.close
        print(XML_SortFileName[j]+' processed\n')
