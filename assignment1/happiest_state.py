import sys
import json
import operator


def rate_tweet(x):
	score = 0
	word = []  #list of words of a single tweet x

	if u'text in x':
		msg = x[u'text'].encode("utf-8")
		print msg
	return score


def main():
	sent_file = open(sys.argv[1])  # We open the sentiment file
	tweet_file = open(sys.argv[2])  # We open the file containing the tweets

	tweets = []  # We initialize a empty list that will contain the tweets
	happiest_state = {}  # Empty dictionary with the occurrence of each hashtag
	scores = {}

	#We fill up the dictionary with the terms and scores in the AFINN-111.txt
	for line in sent_file:
		term, score = line.split("\t")
		scores[term] = int(score)

	# Each line is a tweet, so for each line we parse it into a python dictionary
	for line in tweet_file:
		tweets.append(json.loads(line))  # Each tweet is parsed from JSON to a dictionary

	#print scores

	for tweet in tweets:
		if u'place' in tweet:
			if not (tweet[u'place'] is None):
				if tweet[u'place'][u'country'].encode("utf-8") == "United States":
					# print tweet[u'place'][u'name']
					lugar = tweet[u'place'][u'full_name'].split(",")
					lugar[0] = str(lugar[0]).strip()
					lugar[1] = str(lugar[1]).strip()
					if lugar[1] in states.keys():
						rate_tweet(tweet)


if __name__ == '__main__':
	main()