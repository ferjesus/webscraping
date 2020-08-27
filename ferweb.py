from selenium import webdriver
Path = '/home/fer/ferproyects/webscrapt/chromedriver'
driver = webdriver.Chrome(Path)
driver.get("https://www.wwethunderdome.com/")
print (driver.title)
print (driver.current_url)
event = driver.current_url
listOfWords = event.split('eventID=')
for item in listOfWords:
    print item
ID = listOfWords[1]
if ID != 'raw08242020':
    print 'Alerta registro nuevo'
else:
    print 'Evento pasado'
