
def longest_common_substring(s, t):
	m = min(len(s), len(t))
	count = 0
	for i in range(m):
		if s[i] == t[i]:
			count += 1
	return count

def normalized_string(s):
	import re
	norm_s = s.decode('utf-8','ignore').encode("utf-8")
	norm_s = norm_s.lower()
	final = [re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in norm_s.split("\n")]
	if 'limited' in final:
		final = final.replace('limited','ltd')
	if 'incorporation' in final:
		final = final.replace('incorporation','inc')
	if 'incorporated' in final:
		final = final.replace('incorporated','inc')
	if 'incorporate' in final:
		final = final.replace('incorporate','inc')
	if 'corporation' in final:
		final = final.replace('corporation','corp')
	if 'corporated' in final:
		final = final.replace('corporated','corp')
	if 'corporate' in final:
		final = final.replace('corporate','corp')
	if 'holdings' in final:
		final = final.replace('holdings','hld')
	if 'holding' in final:
		final = final.replace('holding','hld')
	return final

def remove_bracket(string):
	import re
	regex = re.compile(".*?\((.*?)\)")
	result = re.findall(regex, string)
	result = ''.join(e for e in result)
	result = string.replace(result,'')
	return result

path = '/Users/anhdang/Desktop/dbmethods/fundholdings/'

from os import listdir
from os.path import isfile, join
import csv
import codecs
import pickle

onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
print onlyfiles

securities = {}
names = set()
for f in onlyfiles:
	#print(f)
	csv_file = open(path + f, 'rb')
	csv_reader = csv.reader(csv_file)
	if '\0' in open(path + f).read():
		csv_reader = csv.reader(x.replace('\0', '') for x in (path + f))
	for row in csv_reader:
		if len(row) == 7:
			key = row[3].decode('utf-8','ignore').encode("utf-8")
			if len(key) > 0:
				if key == 'CompanyName' or key == 'Cash' or key is None:
					continue
				elif key not in securities.keys():
					securities[key] = set(row[4])
				else:
					securities[key].add(row[4])
				names.add(key)
	csv_file.close()

output = open('securities.pkl', 'wb')
pickle.dump(securities, output)
output.close()

print('step 1')

#filtered_securities = {}
#for s in names:
#	for t in names:
#		m = min(len(s), len(t))
#		n = longest_common_substring(normalized_string(s)[0], normalized_string(t)[0])
#		if float(n)/float(m) > 0.8:
#			if s in filtered_securities.keys():
#				filtered_securities[s].add(t)
#			elif s not in filtered_securities.keys():
#				filtered_securities[s] = set(t)
#			names.remove(t)

print('done')