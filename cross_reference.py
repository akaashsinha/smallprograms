# Takes item from you clipboard and then searches it through Google, Dictionary.com, and Wikipedia
import pyperclip
import webbrowser

term = pyperclip.paste()
webbrowser.open('https://www.google.com/webhp?hl=en#hl=en&q=' + term)
webbrowser.open('http://dictionary.reference.com/browse/' + term)
webbrowser.open('https://en.wikipedia.org/wiki/' + term)
