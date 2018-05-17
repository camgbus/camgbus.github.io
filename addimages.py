import os
import shutil

image_folder = "/home/cam/git/camgbus.github.io/images/miscellaneous/"
page_to_change = "/home/cam/git/camgbus.github.io/miscellaneous.html"
spacing = "\t"*5
insertion_start = "<div class=\"gallery-bott\">"
insertion_end = spacing+"<div class=\"clearfix\"> </div>"

gallery = ""

for subdir, dirs, files in os.walk(image_folder):
    for file in files:
		gallery += ("\n"+spacing+"<div class=\"col-xs-4 col1 gallery-grid\">\n" +
						spacing+"\t<a href=\"images/miscellaneous/"+file+"\" class=\"b-link-stripe b-animate-go  thickbox\">\n" +
							spacing+"\t\t<figure class=\"effect-bubba\">\n" +
								spacing+"\t\t\t<img class=\"img-responsive\" src=\"images/miscellaneous/"+file+"\" alt=\"\">\n" +
							spacing+"\t\t</figure>\n" +
						spacing+"\t</a>\n" +
					spacing+"</div>\n")

f = open(page_to_change, "r")
contents = f.read()
f.close()

contents = contents[:contents.find(insertion_start)+len(insertion_start)] + gallery + contents[contents.find(insertion_end):]	

f = open(page_to_change, "w")
f.write(contents)
f.close()
