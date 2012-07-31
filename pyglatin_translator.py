#This translates words into pig latin using python
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
	print original
	word = original.lower()
	first = word[0]
"""Cshecks first letter of word to determine whether or not it's a vowel
if it's a vowel, append 'ay' to the end.  If it's a consonant, move the
letter to the end and append 'ay' """"
	if first == ( 'a' or 'e' or 'i' or 'o' or 'u'):
		print 'vowel'
		new_word = word + pyg
		print new_word
	else:
		print 'consonant'
		new_word = word[1:] + word[0] + pyg
		print new_word
else:
	print 'empty'
