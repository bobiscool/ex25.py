def break_words(stuff):
	"""this functionj will break up words for us."""
	words = stuff.split(' ')  # split fenggehanshu
	return words

def sort_words(words):
	"""sortd the words """

	return sorted(words) # paixuhanshu


def print_first_word(words):
	"""Prints the first word after poping it off."""

	word = words.pop(0)  # yichuliebiaohanshu deweizhi
	print word

def print_last_word(words):
	"""Prints the last word after popping it off."""

	word = words.pop(-1)
	print word


def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""

	word = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	global words
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
