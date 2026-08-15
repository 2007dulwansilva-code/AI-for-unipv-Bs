#Writing data to a text file
#We first download the text file

def special_line (line):
    return line.startswith("*** ") and line.endswith(" ***")
reader = open("pg345.txt") #opens the file to read
writer = open("pg345_cleaned.txt", "w") #opens a copy for writing

for line in reader :
    if special_line(line):
        break               #terminates immediately

for line in reader :
    if special_line(line):
        break     
    writer.write(line)      #Writes that line

#When the file object is no longer needed, it should be closed:
reader.close()
writer.close()

line.find("jonathan") #returns the lowest index where jonathan is in line
line.count("jonathan") #returns the number of jonathans in line
line.replace ("jonathan","thomas") #replace all jonathans with thomas
#this returns a copy of line with all occurences or jonathan replaced with thomas

