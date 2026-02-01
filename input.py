from textblob import TextBlob
#Takes input and returns blob object
def process_text():
    text = input("give new text: \n")
    #Makes a object out of the input
    blob = TextBlob(text)
    return blob
