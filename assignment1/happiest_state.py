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


states = { 'AK': 'Alaska', 'AL': 'Alabama', 'AR': 'Arkansas', 'AS': 'American Samoa', 'AZ': 'Arizona', 'CA': 'California', 'CO': 'Colorado',
        'CT': 'Connecticut','DC': 'District of Columbia', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia', 'GU': 'Guam',
        'HI': 'Hawaii', 'IA': 'Iowa', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'KS': 'Kansas', 'KY': 'Kentucky',
        'LA': 'Louisiana', 'MA': 'Massachusetts', 'MD': 'Maryland', 'ME': 'Maine', 'MI': 'Michigan', 'MN': 'Minnesota',
        'MO': 'Missouri', 'MP': 'Northern Mariana Islands', 'MS': 'Mississippi', 'MT': 'Montana', 'NA': 'National', 'NC': 'North Carolina',
        'ND': 'North Dakota', 'NE': 'Nebraska', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'NV': 'Nevada', 'NY': 'New York',
        'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'PR': 'Puerto Rico', 'RI': 'Rhode Island', 'SC': 'South Carolina',
        'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VA': 'Virginia', 'VI': 'Virgin Islands', 'VT': 'Vermont',
        'WA': 'Washington', 'WI': 'Wisconsin', 'WV': 'West Virginia', 'WY': 'Wyoming'}




def main():
	tweet_file = open(sys.argv[1])  # We open the file containing the tweets

	tweets = []  # We initialize a empty list that will contain the tweets
	hash_freq = {}  # Empty dictionary with the occurrence of each hashtag

	#Each line is a tweet, so for each line we parse it into a python dictionary
	for line in tweet_file:
		tweets.append(json.loads(line))  # Each tweet is parsed from JSON to a dictionary

	for tweet in tweets:
		if u'place' in tweet:
			if not(tweet[u'place']is None):
				if tweet[u'place'][u'country'].encode("utf-8") == "United States":
					#print tweet[u'place'][u'name']
					print tweet[u'place'][u'full_name'].split(",")[1]
					#print " "

			#location = tweet[u'user'][u'location'].encode("utf-8")
			#print location
			#if location != "":
			#	print location


	#For each tweet, we extract the entities dictionary, where all the hashtags are stored
	#for tweet in tweets:
	#	if u'entities' in tweet:
	#		lista = tweet[u'entities'][u'hashtags']  #list of dictionary containing the hashtags
	#		if len(lista) > 0:	#We ommit the ones that are empty
	#			gethashtag(lista, hash_freq)  #see gethashtag method above

	#z=0
	#for w in sorted(hash_freq, key=hash_freq.get, reverse=True):  #We sort by ocurrences and print only the top ten
  	#	if z <=9:
  	#		print w, hash_freq[w]
	#		z +=1


if __name__ == '__main__':
	main()
