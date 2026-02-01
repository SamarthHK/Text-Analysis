from textblob import TextBlob
def noun(blob):
    #Tokenizes all the different words into POS (Parts Of Speech)
    tags = blob.tags #[('name', 'NN'), ('is', 'VB'), ('teamate', 'NN')]
    #returns first item (Word) in tags where the word is a noun
    return [tags[word][0] for word in range(len(tags)) if tags[word][1] == "NN"]