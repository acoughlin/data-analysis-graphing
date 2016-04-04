from collections import defaultdict
from collections import OrderedDict
import matplotlib.pyplot as plt
import csv, sys, datetime

reader = csv.DictReader(open(sys.argv[1], 'r'))
obamadonations = defaultdict(lambda: 0)
mccaindonations = defaultdict(lambda: 0)

for row in reader:
    name = row['cand_nm']
    datestr = row['contb_receipt_dt']
    amount = float(row['contb_receipt_amt'])
    date = datetime.datetime.strptime(datestr, '%d-%b-%y')
    if 'Obama' in name and "reattribution" in str(row['receipt_desc']).lower():
        obamadonations[date] += amount
    if 'McCain' in name and "reattribution" in str(row['receipt_desc']).lower():
        # print row
        mccaindonations[date] += amount
print "done with parsing rows"
obamadonations = OrderedDict(sorted(obamadonations.items(), key=lambda (key,val): key))
mccaindonations = OrderedDict(sorted(mccaindonations.items(), key=lambda (key,val): key))
# for n in range(len(obamadonations.values())):
#     if n > 0:
#         obamadonations[obamadonations.keys()[n]] += obamadonations[obamadonations.keys()[n-1]]
# for n in range(len(mccaindonations.values())):
#     if n > 0:
#         mccaindonations[mccaindonations.keys()[n]] += mccaindonations.values()[n-1]

# dictionaries
sorted_by_date_obama = sorted(obamadonations.items(), key=lambda (key, val): key)
xs, ys1 = zip(*sorted_by_date_obama)
plt.plot(xs, ys1, label='Obama Donations')
sorted_by_date_mccain = sorted(mccaindonations.items(), key=lambda (key, val): key)
xs, ys2 = zip(*sorted_by_date_mccain)
plt.plot(xs, ys2, label='McCain Donations')
plt.legend(loc='upper center', ncol=4)
plt.savefig('obamavsmccain.png', format='png')
