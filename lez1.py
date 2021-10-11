if __name__=="__main__":
    #This is the main
    print ("Sentence to print")
    print("Another sentence")  ##no \n is needed
    
value = 4.356434
print("The average value is: %.2f" %value)  ##to print only 2 decimal numbers
pi=3.15169265
print(f"{pi:.4}")

##ESERCIZIO 2
name="Omar"
age= 25
birthday= "10/05/1996"

print('My name is ', name, ' and I\'m ', age, ' years old, I was born the ', birthday)

##ESERCIZIO 3
print("\n\nCompute an addition")
print(f"2+3={2+3}")

##ESERCIZIO 4
name=input("What's your name? ")
print(f"Hello {name}, how are you?")

##ESERCIZIO File

fw=open('myFile.txt','w')    ##open in write mode
fw.write('Line to write')
fw.close()

f=open('myFile.txt')        ##open in read mode
fileContent=f.readline()        ##read the content of the file
f.close()
print(fileContent)

fa=open('myFile.txt','a')    ##open in append mode
fa.write('\nAnother line')
fa.close()

##ESERCIZIO 5
f1=open("original.txt")
f2=open("copy.txt",'w')
f2.write('The content of the original file is:\n')
line=f1.readline()
print(line)
f2.write(line)
line=f1.readline()
print(line)
f2.write(line)

f1.close()
f2.close()



