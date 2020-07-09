import requests
from lxml import html
import re
from win10toast import ToastNotifier
toaster = ToastNotifier()
import os

site = requests.get('https://status.zoom.us/')
ler= html.fromstring(site.content)

Meetings=ler.xpath('/html/body/div[1]/div[2]/div[3]/div[1]/div[1]/div/span[3]')
VideoWebinars=ler.xpath('/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/span[3]')
Phone=ler.xpath('/html/body/div[1]/div[2]/div[3]/div[1]/div[3]/div/span[2]')
Chat=ler.xpath('/html/body/div[1]/div[2]/div[3]/div[1]/div[4]/div/span[3]')
Website=ler.xpath('/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/div[1]/span[2]')
ConferenceRC=ler.xpath('/html/body/div[1]/div[2]/div[3]/div[1]/div[6]/div[1]/span[1]/span[2]')
CloudRec=ler.xpath('/html/body/div[1]/div[2]/div[3]/div[1]/div[7]/div/span[2]')
MTeleSer=ler.xpath('/html/body/div[1]/div[2]/div[3]/div[1]/div[8]/div/span[3]')
integrations=ler.xpath('/html/body/div[1]/div[2]/div[3]/div[1]/div[9]/div[1]/span[2]')
DevPLat=ler.xpath('/html/body/div[1]/div[2]/div[3]/div[1]/div[10]/div[1]/span[2]')

rMeetings=re.search('^Operational ',Meetings[0].text_content())
rVideoWebinars=re.search('^Operational ',VideoWebinars[0].text_content())
rPhone=re.search('^Operational ',Phone[0].text_content())
rChat=re.search('^Operational ',Chat[0].text_content())
rWebsite=re.search('^Operational',Website[0].text_content())
rConferenceRC=re.search('^Operational',ConferenceRC[0].text_content())
rCloudRec=re.search('^Operational',CloudRec[0].text_content())
rMTeleSer=re.search('^Operational',MTeleSer[0].text_content())
rintegrations=re.search('^Operational',integrations[0].text_content())
rDevPLat=re.search('^Operational',DevPLat[0].text_content())
erros=[]

if bool(rMeetings) == True:
    msg='Meetings'
    erros.append(msg)
if bool(rVideoWebinars) == True:
    msg='Video'
    erros.append(msg)
if bool(rPhone) == True:
    msg='Phone'
    erros.append(msg)
if bool(rChat) == True:
    msg='Chat'
    erros.append(msg)
if bool(rWebsite) == True:
    msg='Website'
    erros.append(msg)
if bool(rConferenceRC) == True:
    msg='Conference Room Connector'
    erros.append(msg)
if bool(rCloudRec) == True:
    msg='Cloud Recording'
    erros.append(msg)
if bool(rMTeleSer) == True:
    msg='Meeting'
    erros.append(msg)
if bool(rintegrations) == True:
    msg='Integrations'
    erros.append(msg)
if bool(rDevPLat) == True:
    msg='Developer'
    erros.append(msg)

arquivo=open('verificar.txt','r')
ultima=arquivo.readline()
print(ultima)
arquivo.close()

if erros != []:
    listToStr = ' / '.join(map(str, erros))
    if ultima != 'Zoom com problemas':
        arquivo=open('verificar.txt','w')
        arquivo.write('Zoom com problemas')
        arquivo.close()
        toaster.show_toast("Zoom Status - Problemas",
        'Os serviços abaixo estão com problema:\n'+listToStr,
        duration=None,
        threaded=False)
else:
    if ultima == 'Zoom com problemas':
        arquivo=open('verificar.txt','w')
        arquivo.write('Zoom sem problemas')
        arquivo.close()
        toaster.show_toast("Zoom Status - Problemas",
        'Todos os serviços foram normalizados.',
        duration=None,
        threaded=False)
