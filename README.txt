# simple_tag_replace
This is a python script for simply replacing tags in a template with use entered input

EXAMPLE TEMPLATE FILE template.txt:
The quick red <noun1>
jumped over the <noun2>.

EXAMPLE USAGE:
python template_filler.py template.txt fox.txt
Enter replacement for <noun2>: dog
Enter replacement for <noun1>: fox

EXAMPLE OUTPUT FILE fox.txt:
The quick red fox
jumped over the dog.

MAJOR LIMITATION:
If there are more than one tag per line it will not pick up any tags after the first
