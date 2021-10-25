# ArticleAutomation
Automating Articles through a CSV File, comparing sportsbooks and their features using Pandas and docx module

Careful with Data
dont ever write Yes as yes or No as no
dont enter delayed, or question marks to boolean values (yes or no)

The input and the data are CASE SENSITIVE If there is something wrong with the data given The Template WONT crash, but in the document it will tell you, in which part the problem is

There are 3 scripts

# Article Cmp
Where most variables are declared, compared, assigned this is done to make modifying the script easier in future

# Article Inp
takes input -> the FSNA and FSNB

# Article Wr
Is the file that adds content and saves the docx file

This script won't work without Pandas module and Docx module

Download Pandas
pip install pandas

Download Docx
pip install python-docx


End Note
One last thing, if you ever edit your Data/Spreadsheet. Make sure to use/download a CSV file and Make sure the RATINGS header is not there Put the docx file in the same directory as the programs If you don't want to, declare path with the OS_path ('import os' first)
