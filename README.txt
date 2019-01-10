# simple_tag_replace
This is a Python3 script for simply replacing tags in a template with user entered input
Here is an example of a template file using tags starting with < and closing with > name template.txt:
The quick red <noun1>
jumped over the <noun2>.

EXAMPLE USAGE:
python3 tagReplaceGUI.py
A window will open and from the file menue pick the template you want to use, everything between < and > will be give a lable and a text input box. If the file contains html cod this will cause it to recognize all tags, not just the ones you want to change.
Here is an example of what will appear in the tkinter window from opening the above template.txt
noun2 :     :
noun1 :     :

If will fill the box like this:
noun2 : fox :
noun1 : dog :

And then click save and use the file dialog name our file fox.txt the output will to the file will be:
The quick red fox
jumped over the dog.
