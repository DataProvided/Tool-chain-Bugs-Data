import re
import json

sql_connection = 'mysql+mysqlconnector://root:123456@localhost:3306/bugs2'
regex = re.compile(r'\br(\d{6})\b|\brL(\d{6})\b|\b(\d{6})\b')
source = '../../bugs/tool-chain-bugs.json'

with open(source,'r') as f:
    bugs = json.loads(f.read())

for bug in bugs:
    search = regex.findall(bug['fixed_by_commits'])
    if not search: continue
    link_revisions = set()
    search = map(lambda x: next(filter(None, x)), search)
    for commit in search:
        print('%s: %s' % (bug['bug_id'], commit))
        link_revisions.add(commit)
    bug['link_svn_commit'] = '|'.join(sorted(link_revisions))

with open(source,'w') as f:
    f.write(json.dumps(bugs,indent=2))

