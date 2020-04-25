import json
import re

source_bug = '../../bugs/fixed-tool-chain-bugs.json'
source_commit = '../commits.json'
regex = re.compile(r' r(\d{3,6})\b|\brL(\d{3,6})\b|\brevision (\d{3,6})\b')

with open(source_bug,'r') as f:
    bugs = json.loads(f.read())

with open(source_commit,'r') as f:
    commits = json.loads(f.read())

commits = {commit['commit_id']:commit for commit in commits}

for bug in bugs:
    search = regex.findall(bug['comment'])
    if search:
        link_revisions = set() if not bug['link_svn_commit'] else set(bug['link_svn_commit'].split('|'))
        search = map(lambda x: next(filter(None, x)), search)
        for revision in search:
            link_revisions.add(revision)
        bug['link_svn_commit'] = '|'.join(link_revisions)

with open(source_bug, 'w') as f:
    f.write(json.dumps(bugs, indent=2))