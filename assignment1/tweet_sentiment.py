##Made by MejiUlises
##10/07/2014

import sys
import json


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {}       # initialize an empty dictionary to store the words and values associated with each word
    tweets = []       # initialize an empty list for the tweets
    texts = []        # list of text of each tweet
    words = []        # list of words of each text in each tweet
    sent_scores = []  # list of the scores for each text

    #We fill the score dictionary wih the data in the FINN-111 file and store it in a dictionary
    for line in sent_file:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    #We do the same to the tweets
    for line in tweet_file:
        tweets.append(json.loads(line))     #Each tweet is parsed from JSON to a dictionary

    #To see the fields of the tweet we can print them out with keys()
    #print tweets[0].keys()

    #Fore each tweet, we store the message in a list called texts
    for tweet in tweets:
        if u'text' in tweet:                    #We have to make sure the tweet we are looking at has a text field
            msg = tweet['text'].encode("utf-8") #We also have to decode the data into a readable form
            texts.append(msg.lower())           #We lower case it so we can match correctly with the term dictionary

    #for each text stored, we erase special characters so we can match wih the sent_dictonary properly
    for token in texts:
        token.replace("!", " ")
        token.replace("?", " ")

    #Evaluation of the sentiment of each tweet based on the score of each term within the tweet
    for token in texts:
        sent_score=0
        words = token.split(" ")                #We slpit the text in words
        for palabra in words:
            if palabra in scores:
                sent_score += scores[palabra]
        print sent_score
        sent_scores.append(sent_score)          #We append it to a list of scores

if __name__ == '__main__':
    main()
