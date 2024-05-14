import json

f = open('exportedLogRecords (1).JSON')
mf = open('data.txt', 'a')
count = 0
# Parse the JSON data
parsed_data = json.load(f)
# Iterate through each item in the parsed data
taxdict = {
    '1': [1012038216416260000, 7286675158197090000],
    '10': [4829620441415750, 34773267178193400],
    '56': [43957728750000000, 316495647000000000],
    '137': [543529666602951, 3913413599541250],
    '250': [339196275745222, 2442213185365600],
    '8453': [7953041482570470, 57261898674507400],
    '42161': [7910309950000000, 5695423164000000],
    '43114': [23263331250000000, 167495985000000000],
    '0': [0, 0]
}
for item in parsed_data:
    vali = True
    v = []
    c = []
    inds = []
    cur = ''
    ind = -1
    # Extract the message and decode the escaped JSON string
    message_json_str = item['message'].split('data=')[1].strip('"')
    message_json_str = message_json_str.encode().decode('unicode_escape')
    # Parse the inner JSON string
    message_data = json.loads(message_json_str)
    intention = message_data['IntentionInfo']
    mt = intention['BalanceUSD']
    for r in message_data['BalanceInfo']:
        if cur != r['ChainIndex']:
            cur = r['ChainIndex']
            ind += 1
            c.append(0)
            v.append([])
            inds.append(r['ChainIndex'])
        c[ind] += 1
        if r['BalanceUSD'].endswith('X'):
            v[ind].append('0')
        else:
            v[ind].append(r['BalanceUSD'])
    mf.write(str(mt) + " \n")
    mf.write(str(ind + 1) + "\n")
    for i in range(ind+1):
        mf.write(str(c[i]) + " " + str(taxdict[inds[i]][0]) + " " + str(taxdict[inds[i]][1]) + "\n")
        for j in range(c[i]):
            mf.write(str(v[i][j]) + " ")
        mf.write("\n")
    mf.write("\n")
    count += 1
print(str(count))
f.close()
mf.close()
