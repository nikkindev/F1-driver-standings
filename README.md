#F1-driver-standings
_! This repo is archived since the Formula1 website changed the templates and structure of their sites and data_
===================
Python scripts to get driver standings data from the Formula 1 website.  
If you don't know what to do to get the driver standings file, click [here](https://github.com/nikkindev/F1-driver-standings/wiki)  

**Package contains two files:**  
* F1driverstandings.py - To create .txt file with driver standings data for any desired year
* F1driverstandings_complete.py - To create .txt files for all the years automatically when the script is run

**Requirements:**  
* Python
* [BeautifulSoup module](http://www.crummy.com/software/BeautifulSoup/bs4/download/4.0/)  

**Tip:**  
The .txt file can be saved as .csv file since the data in .txt files are already comma separated.  
**Caution:**  
Open the .txt file and save as .csv file with ANSI Encoding option to correctly display names like 'Räikkönen'
