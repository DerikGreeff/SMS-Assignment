'''
FC GREEFF
15107345
Assignment 9Feb
'''
import re

# input requested

print'\nBook list:\n\n(1) Adventures of Huckleberry Finn\n(2) The Adventures of Sherlock Holmes\n(3) The Project Gutenberg EBook of Ulysses\n(4) Pride And Prejudice'
choice = int(raw_input("\nPlease choose a book: "))

  
if choice == 1:
    book = 'pg76.txt'

elif choice == 2:
    book = 'pg1661.txt'
        
elif choice == 3:
    book = 'pg4300.txt'
    
else:
    book = 'pg1342.txt'
        

def sms():
    
    f = open(book, 'r')

    text = f.read()

    #text = raw_input("Please enter message: ")


    text = text.lower() # All text is in lowercase.


    place = re.split('\s', text)

    total = len(place)
    bcpsent = ''
    sentence = ''
    tel = 0
    while tel < total:
        
        num = list(place[tel])
        
        count = len(num)-1

        word = ''

        word = place[tel]
        
        backup = re.sub(r'a','0', word) # replace a with 0
        backup = re.sub(r'e','1', backup) # replace e with 1
        backup = re.sub(r'i','2', backup) # replace i with 2
        backup = re.sub(r'o','3', backup) # replace o with 3
        backup = re.sub(r'u','4', backup) # replace u with 4
        
        bcpsent = bcpsent + backup + ' '

      
        word = re.sub(r'\B[aeiou]\B','', word) # delete aeiou within word

        word = re.sub(r'[^a-z\s]','', word) # delete all 

        word = re.sub(r'(\s[a-z\s])\1+',r'\1', word)

        sentence = sentence + word + ' ' 
        tel+=1
        
    f = open("bcpsent.txt",'w')
    f.write(bcpsent)
    f.close()
    
    #print '\nConverted to sms text:\n\n' + sentence + '\n'

def newtext():
    
    f = open("bcpsent.txt", 'r')

    text = f.read()

    place = re.split('\s', text)
    
    total = len(place)
    
    bcptext = ''
    sentence = ''
    tel = 0
    while tel < total:
        
        num = list(place[tel])
        
        count = len(num)-1
        word = ''
        word = place[tel]
        #print word
        normal = re.sub(r'0','a', word) # replace 0 with a
        normal = re.sub(r'1','e', normal) # replace 1 with e
        normal = re.sub(r'2','i', normal) # replace 2 with i
        normal = re.sub(r'3','o', normal) # replace 3 with o
        normal = re.sub(r'4','u', normal) # replace 4 with u
        bcptext = bcptext + normal + ' '

        tel+=1
        
    f = open("bcptext.txt",'w')
    f.write(bcptext)
    f.close()
    
    print '\nConverted to normal text:\n\n' +bcptext + '\n'

def compare():
    f = open("bcptext.txt", 'r')
    revrtd = f.read()
    text_r = re.split('\s', revrtd)
    total_r = len(text_r)
    
    f = open(book, 'r')
    orgnl = f.read()
    orgnl = orgnl.lower()
    text_o = re.split('\s', orgnl)
    total_o = len(text_o)
    
    count = 0
    tel = 0
    sum = 0
    while tel < total_o:

        if list(text_r[tel]) == list(text_o[tel]):
            count+=1
            tel+=1
        else:
            tel+=1
    sum = (float(count)/float(total_o))*100
    
    #print '\nCompared : ', sum, '%'
'''
    #Timing execution

    from timeit import Timer

    # first argument is the code to be run, the second "setup" argument is only run once,
    # and it not included in the execution time.
    t = Timer("""x.index(456)""", setup="""x = range(1000)""")

    print t.timeit(1000) # prints float, for example 5.8254
'''
import os

menu = """
    (1) Convert to sms text
    (2) Convert to normal text
    (3) Compare sms with normal
    (4) Quit
    """
choice = 0
end = 0
print "Welcome to SMS/Text Converter"
while end != 1:
    str1 = ""

    print menu
    while choice < 1 or choice > 4:
        choice = int(raw_input("Pick an option? "))
        
    try:
        choice = int(choice)
    except ValueError: print "Please choose an option on the menu (number)."
    
    if choice == 1:
           import cProfile
           cProfile.run('sms()')

    if choice == 2:
           import cProfile
           cProfile.run('newtext()')
            
    if choice == 3:
            compare()

    if choice == 4:
            print "Thanks for using SMS/Text Converter."
            end = 1
    choice = 0
exit()


