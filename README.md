Norman Police Department,Daily Arrest Summary extraction 
===

The Norman, Oklahoma police department regularly reports of incidents arrests and other activity. This data is hosted on their website. This data is distributed to the public in the form of PDF files.

you can download these PDF files  here http://normanpd.normanok.gov/content/daily-activity

In this project you will see me  using the knowledge of Python and the Linux command line tools to extract information from a scraped file, such as one of the PDF files(we will be concentratig on Daily Arrests) , wrangle through the file ,download the data,
extract the fields from first page, create a SQLite database to store the data. and insert the data into the database finally returning one Random arrest.

----
Project Source can viewed from  https://oudalab.github.io/textanalytics/projects/project0
---

-------------
Author 
---
**Venkata Subbaraju Sagi**

All known Bugs and fixes can be sent to subbaraju.v@ou.edu
Packages required for the project : PyPF2, re, bs4, tempfile, sqllite3

------
File List
----
```
├── COLLABORATORS
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── README.md
├── docs
├── normanpd.db
├── project0
│   ├── main.py
│   ├── normanpd.db
│   └── project0.py
├── setup.cfg
├── setup.py
└── tests
    ├── test_database.py
    ├── test_download.py
    ├── test_fields.py
    └── test_status.py

```

-------
Platform used
---

I used Google cloud platform to run the file. I have created an instance in google cloud, which I used for cloning the git repository, then for running the file 

Your code should take a url from the command line and perform each operation. 

---
Once you have cloned the directory, follow these instructions
----------------
**The Pipfile and Pipfile.lock**
Create the Pipfile using the command `pipenv install --python 3.7`. Note for this project we will use Python 3.7 so be sure to install it using pyenv.

If you do not have python 3.7 on your system, revisit the start up script given in the document config file: https://oudalab.github.io/textanalytics/instance/startup.sh

You can create each initial file and folder using the touch and mkdir commands. The Python packaging how to page has more example of proper python packages https://python-packaging.readthedocs.io/en/latest/minimal.html

you will get more insights of running your project0.py file, but to make it clear 
After the code is installed, you should be able to run the code using the command below.
**pipenv run python project0/main.py --arrests `url` **

here url is the pdf link from which data needs to be extracted.

___

Description of Functions Used
---
I have two files to run the program, in `project0/project0.py'` I have written all function definitions and in `project0/main.py`, I have called these functions.

Functions

1 . **fetchincidents(url)**

The function fetchincidents() takes url as input parameters, it uses the python urllib.request library to grab one of the pdfs for the norman police report webpage.


 2 .  **extractincidents(url)**

The function extractincidents() takes  parameters retured froom fetchIncidents  and it reads data from the pdf files and extracts the incidents. The each incident includes a **date/time, case number, arrest location, offense, arrestee address, status, and officer**. A city, state, and zip code will typical be available if the arrested person(s) is not homeless or transient. 

To extract the data from the pdf files, use the PyPdf2.PdfFileReader class. It will allow you to extract pages and pdf file and search for the rows. Extract each row and add it to a list.

This function can return a list of rows so another function can easily insert the data into a database

while extracting the data from the PDF page, I faced some challenges.

firstly, i need to split every row as a seperate list, so that I can have more clarity on the values which are getting pushed. Every row in the page ends with ';',except the first row, so I have to insert it manually and only then could split it.

second challenge was of multi line values, ideally every column was seperated by a '\n', but if same column had multiple lines, then those all lines had '\n' seperating them. So if you seperate these values with '\n', we might end up pushing wrong text. we need to check this multi lines first.

More, the extracted data , had many unncessary text, which needs to be removed.

3 . **createdb()*
The createdb() function creates an SQLite database file named normanpd.db and inserts a table with the schema below.
```
CREATE TABLE arrests 
(
    arrest_time TEXT,  
    case_number TEXT,
    arrest_location TEXT,
    offense TEXT,
    arrestee_name TEXT,
    arrestee_birthday TEXT,
    arrestee_address TEXT,
    status TEXT,
    officer TEXT
)
````
Note, all the columns correspond directly to the columns in the arrest pdfs. The arrest address contains information from the arrestee address, city, state, and zip code. 


4 . **populatedb**
The function populatedb(db, incidents) function takes the rows created in the extractincidents() function and adds it to the normanpd.db database.


5 . **status(db)**

The status(db) function prints to standard out, a random row from the database

----
How To run this 
--
To run the file you  need to pass the command line as follows:

python main.py --arrests "url link"

`python main.py --arrests "http://normanpd.normanok.gov/filebrowser_download/657/2019-02-14%20Daily%20Arrest%20Summary.pdf"

expected output

1/22/2019 20:13þ2019-00005814þ811 E MAIN STþWARRANT-COUNTYþJIMMY GARRETT DYEþ6/12/2000þ811 E MAIN ST Norman  OK  73071 þFDBDC (Jail) þ1816 - Ross;

check the thorn character in between each fields
---

List of external links that I used for help
--

https://medium.com/@CharlesBordet/how-to-extract-and-clean-data-from-pdf-files-in-r-da11964e252e. gave me insights on how to extract the data from a pdf.

https://docs.python.org/3/howto/regex.html,  this explains in detail of regular expressions. This documentation came to my rescue while I am wrangling the data and while writing specific regular expressions to clean the data.

http://www.sqlitetutorial.net/sqlite-python/creating-database/ , I never used SQLlite before this link gave me moreinformation on creating the data base and the way to push the values to the database.

https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf, this helped in detailing my README.md structure.

https://www.geeksforgeeks.org/list-methods-in-python-set-2-del-remove-sort-insert-pop-extend/, helped with commands to remove specific values from my list.
--

**Assumptions/Bugs**
--

'''

I have assumed that the page have only 12 columns, out of which the data is missing only from columns 7,8,9. If there is a missing value in different column or number of columns are more than 12 the code might not give desired results.

To clean the data and to get desired formatting, you will see me using hard coding in some cases, like combing multi lined string values and removing space in between them, and adding some special characters and split the text using that character. So the code can handle only those cases.

The code requires manual input from the user, failing to give that might not give you any output, so I assume you know that condition.

------

Thankyou for your time, Happy Coding!!

--





