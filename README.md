<H1>EasySharePoint</H1>
<p>v.0.1</p>


<h3>About</h3>
EasySharePoint is a Python 3 module to perform HTTP requests to Microsoft Sharepoint easily.
It relays on well known and loved requests library <url>http://docs.python-requests.org/en/master/</url>.
<br>
<br>
<h3>Features</h3>
EasySharepoint utilizes whole Microsoft Sharepoint REST architecture to work with lists, views, folders and files.
<br>
<br>
<h3>Installation</h3>
``` shell

pip install easy_sharepoint

```
<br>
<br>
<h3>Usage</h3>

```python

import easy_sharepoint

connector = easy_sharepoint.SharePointConnector("login", "password", "sharepointURL")
connector.create_new_list(list_name="myNewList")

myList = connector.get_list_items(list_name="myNewList")


```

Above Example establishes session with SharePoint Site, then creates new list and assigns all its items to variable myList.
Feel free to check other methods of SharePointConnector Object.




