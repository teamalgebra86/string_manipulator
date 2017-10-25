def longest_common_substring(s, t):
	m = min(len(s), len(t))
	count = 0
	for i in range(m):
		if s[i] == t[i]:
			count += 1
		else:
			break
	return count

def normalized_string(s):
	import re
	norm_s = s.decode('utf-8', 'ignore').encode("utf-8")
	norm_s = norm_s.lower()
	shortened_name = [re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in norm_s.split("\n")]
	shortened_name = shortened_name[0]
	if 'limited' in shortened_name:
		shortened_name = shortened_name.replace('limited','ltd')
	if 'incorporation' in shortened_name:
		shortened_name = shortened_name.replace('incorporation','inc')
	if 'incorporated' in shortened_name:
		shortened_name = shortened_name.replace('incorporated','inc')
	if 'incorporate' in shortened_name:
		shortened_name = shortened_name.replace('incorporate','inc')
	if 'corporation' in shortened_name:
		shortened_name = shortened_name.replace('corporation','corp')
	if 'corporated' in shortened_name:
		shortened_name = shortened_name.replace('corporated','corp')
	if 'corporate' in shortened_name:
		shortened_name = shortened_name.replace('corporate','corp')
	if 'holdings' in shortened_name:
		shortened_name = shortened_name.replace('holdings','hld')
	if 'holding' in shortened_name:
		shortened_name = shortened_name.replace('holding','hld')
	if 'company' in shortened_name:
		shortened_name = shortened_name.replace('company','co')
	return shortened_name

def remove_bracket(string):
	import re
	regex = re.compile(".*?\((.*?)\)")
	result = re.findall(regex, string)
	result = ''.join(e for e in result)
	result = string.replace(result,'')
	return result


import pickle
import copy
pickle_in = open('securities.pkl','rb')
securities= pickle.load(pickle_in)
pickle_in.close()
print len(securities.keys())


# print securities.keys()
thefile = open('output.txt', 'w')
names = copy.deepcopy(securities.keys())
originlen =  len(names)
filtered_securities = {}
for s in names:
	ns = normalized_string(s)
	if not names:
		break
	else:
		print str(originlen) + ' , ' + str(len(names))
		for t in names:
			nt = normalized_string(t)
			m = max(len(ns), len(nt))
			n = longest_common_substring(ns, nt)
			if float(n)/float(m) > 0.7:
				thefile.write("%s , %s , %d , %d \n" %(ns, nt, m, n))
				if s in filtered_securities.keys():
					filtered_securities[s].add(t)
				else:
					filtered_securities[s] = {t}
				if t in names:
					names.remove(t)
	if s in names:
		names.remove(s)
thefile.close()
output = open('filtered_securities_07.pkl', 'wb')
pickle.dump(filtered_securities, output)
output.close()
#print filtered_securities
