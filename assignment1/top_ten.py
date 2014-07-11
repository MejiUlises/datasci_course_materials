import sys
import json
import operator


#With this function we get the hashtags. The parameter is a list of the form [{index:xxx},{u'text:"HashtagValue"}]
#Once we extract these hashtags, we store them in a dictionary and count if they have already been added
def gethashtag(lis, hash_freq):
	for dicc in lis:
		hash = str(dicc[u'text'].encode("utf-8"))
		if hash in hash_freq:
			hash_freq[hash] += 1
		else:
			hash_freq[hash] = 1

#This is not used
def sort(d,reverse=False):
    return sorted(d.iteritems(), key=itemgetter(1), reverse=True)


def main():
	tweet_file = open(sys.argv[1])  # We open the file containing the tweets

	tweets = []  # We initialize a empty list that will contain the tweets
	hash_freq = {}  # Empty dictionary with the occurrence of each hashtag

	#Each line is a tweet, so for each line we parse it into a python dictionary
	for line in tweet_file:
		tweets.append(json.loads(line))  # Each tweet is parsed from JSON to a dictionary

	#For each tweet, we extract the entities dictionary, where all the hashtags are stored
	for tweet in tweets:
		if u'entities' in tweet:
			lista = tweet[u'entities'][u'hashtags']  #list of dictionary containing the hashtags
			if len(lista) > 0:	#We ommit the ones that are empty
				gethashtag(lista, hash_freq)  #see gethashtag method above

	z=0
	for w in sorted(hash_freq, key=hash_freq.get, reverse=True):  #We sort by ocurrences and print only the top ten
  		if z <=9:
  			print w, hash_freq[w]
			z +=1


if __name__ == '__main__':
	main()