import tkinter as tk
import os
os.system("color")

#To make text bold and underlined, you can enclose the text in the escape sequence '\033[1;4m' and '\033[0m'.

underline = "\x1B[4m"
bold = "\x1B[1m"
end = '\033[0m'
boldANDunderline = bold + underline
divider = "|"

vowels = ["a", "e", "i", "o", "u"]
consonants = ["b" , "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
dip = ["ai", "au", "ei", "eu", "oi", "ou", "ui", "uu", "ia", "ie", "io", "iu", "ua", "ue", "uo"]
singleConsonants = ["ch", "ll", "rr"]

root=tk.Tk()
root.geometry("400x200")
name_var=tk.StringVar()


def submit():
	global name
	name = name_var.get()
	
	print("Calculating " + "'" + name + "'" + " for you...")
	name_var.set("")


# creating a label for
# name using widget Label
name_label = tk.Label(root, text = 'Enter Spanish Word:', font=('calibre',10, 'bold'))
answer = tk.Label(root, text = 'Answer', font=('calibre',10, 'bold'))

# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))

# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(root,text = 'Submit', command = submit)

# placing the label and entry in
# the required position using grid
# method

name_label.grid(row=0,column=0)
answer.grid(row=4,column=0)
name_entry.grid(row=0,column=1)
sub_btn.grid(row=2,column=1)

# performing an infinite loop
# for the window to display
root.mainloop()

##### calculate word #####

# calculate how many vowels are in the word and how many syllables will be in the word
def countVowels(word):
	print("counting Vowels...")
	vowel_count = 0
	for letter in word:
		if letter in vowels:
			vowel_count += 1
	print("There will be " + str(vowel_count) + " vowels in " + "'" + word + "'!")
	vowel_count = int(vowel_count) - 1
	print("There will be " + str(vowel_count) + " syllables in " + "'" + word + "'!")
	line_count = int(vowel_count) - 1
	print("There will be ", str(line_count) + " lines in " + "'" + word + "'!")
	return vowel_count

def findConsonant(word):
	print("locating Consonants...")
	global new_word
	new_word = []
	for letter in word:
		if letter in consonants:
			letter = underline + letter + end
			new_word.append(letter)
		else:
			new_word.append(letter)
	global name
	name = print("".join(new_word))
	print("located Consonants!")

def createSyllable(word):
	print("creating Syllables...")
	for letter in word:
		#check if a consonant is surrounded by vowels and add a divider between the first vowel and consonant
		if letter in consonants:
			if word[word.index(letter) - 1] in vowels and word[word.index(letter) + 1] in vowels:
				word = word[:word.index(letter)] + divider + word[word.index(letter):]
			# if a vowel is surrounded by consonants, add a divider between the second consonants and vowel
			elif word[word.index(letter) - 1] in consonants and word[word.index(letter) + 1] in consonants:
				word = word[:word.index(letter)] + divider + word[word.index(letter):]
			
	print(word)
	print("created Syllable!")

def doubleTripleConsonant(word):
	#if two consonats are follwing one another, add a divider between them unless they second letter starts with a l or r
	for letter in word:
		if letter in consonants:
			if word[word.index(letter) + 1] in consonants and word.startsWith("l") or word.startsWith("r"):
				break
			else:
				#add a divider between the consonants
				word = word[:word.index(letter)] + divider + word[word.index(letter):]
		else:
			print(word)



countVowels(name)
findConsonant(name)
createSyllable(name)
doubleTripleConsonant(name)


