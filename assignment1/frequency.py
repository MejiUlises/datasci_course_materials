import sys
import json


def clean(pal):
	pal = pal.replace("!", "")
	pal = pal.replace("?", "")
	pal = pal.replace(",", "")
	pal = pal.replace(".", "")
	pal = pal.replace(":", "")
	return pal


def main():
	tweet_file = open(sys.argv[1])  # We open the file containing the tweets

	tweets = []  # We initialize a empty list that will contain the tweets
	words = {}  # Words of each tweet
	word_freq = {}  # Empty dictionary with the occurrence of each word

	for line in tweet_file:
		tweets.append(json.loads(line))  # Each tweet is parsed from JSON to a dictionary

	total_words = 0  #Total count of words
	for tweet in tweets:
		if u'text' in tweet:
			aux = clean(tweet[u'text'].encode("utf-8"))
			words = aux.split()
			for word in words:	#for each word in the tweet, we check if it already exists within the dictionary of words
				if word in word_freq:	#if it exists, we add 1 to the value
					word_freq[word] =+ 1
					total_words += 1
				else:	#if not, we add it to the dictionary with a value of 1
					word_freq[word] = 1
					total_words += 1


	for token in word_freq:
		if token.isalpha():
			#s = "%s %s" % (token, (word_freq[token]/float(total_words)))   debugging purposes
			#print len(s.split())
			print "%s %s" % (token, (word_freq[token]/float(total_words)))

if __name__ == '__main__':
	main()