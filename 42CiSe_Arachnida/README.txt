
Install pip:
sudo apt-get install python-pip

sudo apt-get install python.pip

Install lxml:
pip install lxml


/*--------------------SPIDER----------------*/

Params:
-r: recursively visits and downloads images/gifs/etc... from links. (python3 spider.py -r ...)

-l: use it to especify the recursively depth level. (python3 spider.py -r -l 1 ...)

-p: especifies a new path to save the data of the urls visited. (python3 spider.py -r -l 1 -p data2 ...)

-h: help. (python3 spider.py -h)

-s [pdf,docx]: to search and save every file with pdf and docx extension. (python3 spider.py -r -l 1 -s pdf,docx ...)

How to use:
python3 spider.py -r -l 1 http://faecta.coop

/*----------------------SCORPION---------------------*/

How to use:
python3 scorpion.py data/folder_name/*.jpg

This way we tell the script to extract the metadata of every image contained
in the new folder created beforehand with the analyzed url´s name with spider.py.