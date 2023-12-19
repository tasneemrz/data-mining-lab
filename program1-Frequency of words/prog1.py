punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
file = open("data.txt", "r")
frequency = {}

for line in file:
    for word in line.split():
        # remove punctuaton from the end of the word
        word = word.lower()
        if word[-1] in punctuations:
            word = word[0:len(word)-1]

        if word in frequency:
            frequency[word] += 1
        else:
            frequency.update({word: 1}) 
        
frequency = sorted(frequency.items(), key=lambda x:x[1], reverse=True)
frequency = dict(frequency)

for key in frequency:
    print(key, " : ", frequency[key])
