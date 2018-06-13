import sys
from os.path import isfile, abspath


file_name = str(sys.argv[1])
output_name = str(sys.argv[2])

template_file = open(file_name, "r")
template_data = template_file.read()
template_file.close()

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def getTags(file_in):
    global template_data
    tags=[]
    for line in template_data.splitlines():
        if '<' in line and '>' in line:
            found = find_between(line, '<', '>')
            if found != "":
                tags.append('<'+found+'>')
    return list(set(tags))

def getReplace(tags):
    tag_replace = []
    for tag in tags:
        replace_item = str(raw_input('Enter replacement for '+tag+': '))
        tag_replace.append(replace_item)
    return tag_replace

def replaceTags(tag,replace):
    global template_data
    tag_replace = zip(tag, replace)
    for tag in tag_replace:
        template_data = template_data.replace(tag[0], tag[1])

def writeFile():
    global output_name
    global template_data
    out_file=open(output_name, "w")
    out_file.write(template_data)
    out_file.close()

if file_name.find('template') > -1:
    if isfile(file_name):
        print "Template file detected."
        print "Template file located at \n"+abspath(file_name)
        tags = getTags(file_name)
        rep_tags = getReplace(tags)
        replaceTags(tags, rep_tags)
        try:
            writeFile()
        except:
            print "Error writing file"
    else:
        print "Template file " + file_name + " could not be found"
elif file_name != None:
    if isfile(file_name):
        print "File located at \n"+abspath(file_name)
        print "File does not appear to be a template"
    else:
        print "File " + file_name + " could not be found"
else:
    print "No file name given"