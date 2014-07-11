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

	total_words = 0
	for tweet in tweets:
		if u'text' in tweet:
			aux = clean(tweet[u'text'].encode("utf-8"))
			#print aux
			words = aux.split()
			for word in words:
				#print word
				if word in word_freq:
					word_freq[word] =+ 1
					total_words += 1
				else:
					word_freq[word] = 1
					total_words += 1

	#print total_words

	for token in word_freq:
		if token.isalpha():
			s = "%s %s" % (token, (word_freq[token]/float(total_words)))
			#print len(s.split())
			print "%s %s" % (token, (word_freq[token]/float(total_words)))

if __name__ == '__main__':
	main()