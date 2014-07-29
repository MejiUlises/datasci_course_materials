import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
	# key: document identifier
	# value: document contents

	value = []

	key = record[1]  # The first element of the line we are reading is the order_id
	value = record[0:len(record)]

	#print (key,value)

	mr.emit_intermediate(key, value)


def reducer(key, list_of_values):
	# key: word
	# value: list of occurrence counts
	# total = 0
	#print type(key)
	for v in list_of_values[1:len(list_of_values)]:
		lista = []
		#lista.append(list_of_values[0])
		#print list_of_values[0] + v
		mr.emit((list_of_values[0] + v))


# Do not modify below this line
# =============================
if __name__ == '__main__':
	inputdata = open(sys.argv[1])
	mr.execute(inputdata, mapper, reducer)