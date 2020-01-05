import time
import re


class Parse_text:
	def __init__(self):
		print('\nPress Ctrl-c to exit at any time.\n')
		self.text = self.file_location()
		self.temp = []
		self.commander()
		
		
	def __str__(self):
		return str(self.text) 
		
	def print_text(self):
		print(self.text)
		
	def print_list(self):
		for i in self.text:
			print(i)
		
	# This will search each line for the key word then return those lines (parse_line_find)
	def p_l_f(self,key_word):
		for i in self.text:
			if key_word in i:
				self.temp.append(i)
		self.text = self.temp
		self.clear_temp()
		self.print_text()
		time.sleep(1)
		self.commander()
				
	
	# This will work similar to replace but it changes the string instead of creating a new string 
	def translate_text(self,key_word,word_replacement=''):
		for i in self.text:
			if key_word in i:
				i=i.replace(key_word,word_replacement)
			self.temp.append(i)
		self.text = self.temp
		self.clear_temp()
		self.print_text()
		time.sleep(1)	
		self.commander()
	
	#This code takes an keyword and a direction either left(l) or right(r) then looks for the key_word 
	# and deletes it and everything to left or right, word_replacement will replace with word of your choice 
	def strip_text(self,key_word,direction='l'):
		for i in self.text:
			if key_word in i:
				if direction=='l':
					i=re.sub(r'.*'+key_word, '', i)
			
				elif direction=='r':
					i=re.sub(r''+key_word+'.*', '', i)
				else:
					print('incorrect input for direction must be: l or r')
					self.commander()
			self.temp.append(i)
		self.text=self.temp
		self.clear_temp()
		self.print_text()
		time.sleep(1)
		self.commander()
	
	#uses sub and regex for more complex searches
	def regex_code_sub(self,r_code,sub):
		for i in self.text:
			try:
				sub(r''+r_code,sub,i)
			except: 
				print('error in the regex code')
				self.commander()
			self.temp.append(i)
		self.text=self.temp
		self.clear_temp()
		self.print_text()
		time.sleep(1)
		self.commander()
				
	def clear_temp(self):
		self.temp = []
	
	#This is what locates the file 
	def file_location(self):
		file=input('Enter file name/location ex. file.txt: \n')
		try:
			text=open(file).readlines()
		except:
			print('\nFile not found please try again\n')
			time.sleep(1)
			self.file_location()
		return text
		
	#This is what saves the file it asks for save location.
	def saver(self):
		save_location=input('Enter name/location to save file ex: save.txt \n')
		time.sleep(.2)
		yes_no=input('You have entered: "' + save_location + '" to save to is this correct? Type yes to confirm save, no to cancel:\n')
		if yes_no == 'yes':
			open(save_location,'w').writelines(self.text)
		elif yes_no == 'no':
			options=input('Would you like to try again? Type yes to retry, no to return to menu\n')
			time.sleep(.5)
			if options == 'yes':
				self.saver()
			else: 
				self.commander()
		else:
			print('\nIncorrect input. Try again\n')
			time.sleep(1)
			self.saver()
		self.commander()
		
			
	def commander(self):
		
		time.sleep(1)
		menu_option=input('\n------\nEnter a menu number to begin:\n 1. Print text \n 2. Line keyword search \n 3. Translate text \n 4. Strip text \n 5. Regex code sub \n 6. Save \n')
		
		if menu_option=='1':
			self.print_text()
			self.commander()
		
		elif menu_option=='2':
			print('This will search each line for the key word then return those lines')
			keyword=input('Enter Keyword:\n')
			self.p_l_f(keyword)
		
		elif menu_option=='3':
			print('This will work similar to replace but it changes the string instead of creating a new string ')
			keyword=input('Enter Keyword:\n')
			replacement_word=input('Enter replacement word:\n')
			self.translate_text(keyword,replacement_word)
		
		elif menu_option=='4':
			print('This will take keyword search every line and removes everything either to the left or right based on input')
			keyword=input('Enter Keyword:\n')
			direction=input('Enter direction r or l:\n')
			self.strip_text(keyword,direction)
		
		elif menu_option=='5':
			print('This will use a regex code to search for an more advance pattern then replace that word')
			regex=input('Enter regex code:\n')
			replacement_word=input('Enter replacement word:\n')
			self.regex_code_sub(regex,replacement_word)
		
		elif menu_option=='6':
			self.saver()
		
		else: 
			print('Incorrect input try again\n')
			time.sleep(.3)
			self.commander()

Parse_text()
