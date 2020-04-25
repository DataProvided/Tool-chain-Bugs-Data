import json
import re

source_bug = '../../bugs/tool-chain-bugs.json'
source_commit = '../commits.json'

regex = re.compile(r'\bPR(\d{1,5})\b|http://llvm.org/bugs/show_bug.cgi\?id=(\d{1,5})')

with open(source_bug, 'r') as f:
    bugs = json.loads(f.read())

bugs = {bug['bug_id']:bug for bug in bugs}

with open(source_commit, 'r') as f:
    commits = json.loads(f.read())

for c in commits:
    if c['msg']:
        search = regex.search(c.msg)
        if search:
            bug_id = search.groups()[0] if search.groups()[0] else search.groups()[1]
            if bug_id in bugs:
                bug = bugs[bug_id]
                link_revisions = set() if not bug.link_svn_commit else set(bug.link_svn_commit.split('|'))
                link_revisions.add(c.commit_id)
                bug.link_svn_commit = '|'.join(link_revisions)

with open(source_bug, 'w') as f:
    f.write(json.dumps(bugs, indent=2))