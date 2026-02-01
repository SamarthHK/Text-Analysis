#Text-Analysis 2/1/26
#Samarth Harish Kumar
#Matyas Ryhmes

#Importing other files
import input as inp
import output as out

print("This program takes a string input, and lists all the nouns it finds in it!")
#Runs input function, and inputs it into the output function
noun = out.noun(inp.process_text())

print("Nouns:\n")

#Lists out all nouns line by line with a comma at the end
for i in range(len(noun)):
    print(noun[i]+"" if i+1 == len(noun) else ",")
    