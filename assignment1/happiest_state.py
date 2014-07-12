import sys
import json
import operator

states = {'AK': 'Alaska',
		  'AL': 'Alabama',
		  'AR': 'Arkansas',
		  'AS': 'American Samoa',
		  'AZ': 'Arizona',
		  'CA': 'California',
		  'CO': 'Colorado',
		  'CT': 'Connecticut',
		  'DC': 'District of Columbia',
		  'DE': 'Delaware',
		  'FL': 'Florida',
		  'GA': 'Georgia',
		  'GU': 'Guam',
		  'HI': 'Hawaii',
		  'IA': 'Iowa',
		  'ID': 'Idaho',
		  'IL': 'Illinois',
		  'IN': 'Indiana',
		  'KS': 'Kansas',
		  'KY': 'Kentucky',
		  'LA': 'Louisiana',
		  'MA': 'Massachusetts',
		  'MD': 'Maryland',
		  'ME': 'Maine',
		  'MI': 'Michigan',
		  'MN': 'Minnesota',
		  'MO': 'Missouri',
		  'MP': 'Northern Mariana Islands',
		  'MS': 'Mississippi',
		  'MT': 'Montana',
		  'NA': 'National',
		  'NC': 'North Carolina',
		  'ND': 'North Dakota',
		  'NE': 'Nebraska',
		  'NH': 'New Hampshire',
		  'NJ': 'New Jersey',
		  'NM': 'New Mexico',
		  'NV': 'Nevada',
		  'NY': 'New York',
		  'OH': 'Ohio',
		  'OK': 'Oklahoma',
		  'OR': 'Oregon',
		  'PA': 'Pennsylvania',
		  'PR': 'Puerto Rico',
		  'RI': 'Rhode Island',
		  'SC': 'South Carolina',
		  'SD': 'South Dakota',
		  'TN': 'Tennessee',
		  'TX': 'Texas',
		  'UT': 'Utah',
		  'VA': 'Virginia',
		  'VI': 'Virgin Islands',
		  'VT': 'Vermont',
		  'WA': 'Washington',
		  'WI': 'Wisconsin',
		  'WV': 'West Virginia',
		  'WY': 'Wyoming'}


def clean_tweet(x):
	x = x.replace("!", "")
	x = x.replace("?", "")
	x = x.replace(",", "")
	x = x.replace(".", "")
	x = x.strip()
	return x


def rate_tweet(x, dicti):
	tweet_score = 0
	words = []  # list of words of a single tweet x

	msg = x[u'text'].encode("utf-8")  # get the message of the tweet
	msg = clean_tweet(msg)	#clean the tweet a little
	words = msg.split(" ")

	for word in words:
		if word in dicti:
			tweet_score += dicti[word]
	#print tweet_score

	return tweet_score


def main():
	sent_file = open(sys.argv[1])  # We open the sentiment file
	tweet_file = open(sys.argv[2])  # We open the file containing the tweets

	tweets = []  # We initialize a empty list that will contain the tweets
	happiest_state = {}  # Empty dictionary with the occurrence of each hashtag
	scores = {}

	# We fill up the dictionary with the terms and scores in the AFINN-111.txt
	for line in sent_file:
		term, score = line.split("\t")
		scores[term] = int(score)

	# Each line is a tweet, so for each line we parse it into a python dictionary
	for line in tweet_file:
		tweets.append(json.loads(line))  # Each tweet is parsed from JSON to a dictionary

	# print scores

	for tweet in tweets:
		if u'place' in tweet:
			if not (tweet[u'place'] is None):
				if tweet[u'place'][u'country'].encode("utf-8") == "United States":
					# print tweet[u'place'][u'name']
					lugar = tweet[u'place'][u'full_name'].split(",")
					lugar[0] = str(lugar[0]).strip()
					lugar[1] = str(lugar[1]).strip()
					if lugar[1] in states.keys():
						tweet_score = rate_tweet(tweet, scores)
						if lugar[1] in happiest_state:
							happiest_state[lugar[1]] += tweet_score
						else:
							happiest_state[lugar[1]] = tweet_score
					elif lugar[0] in states.values():
						tweet_score = rate_tweet(tweet, scores)
						if states.keys()[states.values().index(lugar[0])] in happiest_state:
							happiest_state[states.keys()[states.values().index(lugar[0])]] += tweet_score
						else:
							happiest_state[states.keys()[states.values().index(lugar[0])]] = tweet_score

	print "%s" % str(happiest_state.keys()[max(happiest_state.values())])

if __name__ == '__main__':
	main()