## Setup

### Download related chromedriver 
Version must be match your Chrome version, default chromedriver is version(113.0.5672.126)

Find your Chrome version
```
chrome://settings/help  <- parse to url at your Chrome

Click About Chrome -> see the version (eg, 113.0.5672.126)
```

Download Link, replace chromedriver to this folder
```
https://chromedriver.chromium.org/downloads
```

### Install Python
```
https://www.python.org/downloads/
```

### Install Selenium
``` 
pip install selenium
```

### Define the waitingRoomUrl and targetUrl
Open and edit ticket_busy_bot.py by using notepad or any IDE.

Everytime url includs words at waiting Room, will redirect to targetUrl.
```python
waitingRoom = ["busy.hkticketing.com","https://queue.hkticketing.com/hotshow.html"] 
targetUrl = "http://entry-hotshow.hkticketing.com/"
```

### Define multipage.command
Open and edit multipage.command by using notepad or any IDE.

Default is 5 browser at once. you can change any number you want.

## RUN Script

open single.command -> for open one browser

open multiPage.command -> for open multi browser, default is 5


