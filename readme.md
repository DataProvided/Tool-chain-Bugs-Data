# LLVM Tool-chain Bugs Data

## Content

- `bugs`: LLVM tool-chain bugs source data
  - `tool-chain-bugs.json`: all tool-chain bugs collected
  - `fixed-toolchain-bugs.json`: all fixed tool-chain bugs which is used to find linkage between bugs and fixing commits
  - `linking-commits-toolchain-bugs.json`: all fixed tool-chain bugs with fixing commits
- `commits`: LLVM tool-chain commits
  - `scripts`: for linkage between bugs and fixing commits
  - `commits.json`: linked commits

- `statistics_1.csv`: statistics data for addressing tool-chain bugs' patterns
- `statistics_2.csv`: statistics data for addressing tool-chain bugs' debugging and fixing

## Data

Description of source data's partial fields

### Bug Report

- `bug_id`: bug report's id in Bugzilla system
- `creation_ts`: bug report's creating time
- `short_desc`: summary of a bug report
- `product`: what general tool the bug belongs to (here using "libraries" denoted tool "llvm core libraries")
- `component`: each product is divided into different components
- `op_sys`: operation systems where the bug occurs
- `resolution`: the handling situation of a bug
- `bug_severity`: the bug's severity
- `long_desc`: detailed description of the bug
- `comment`: discussion  from bug reporter and code reviewer about bugs (comments are separated by "\n\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~~\~\~\~\~\~\n")
- `link_svn_commit`: commit id which is linked with this bug
- `modified_component`: modified tools
- `modified_component_num`: the number of modified tools
- `associated_list`: involved tools
- `associated_num`: the number of involved tools
- `fixed_by_commits`: fixing commit id provided by Bugzilla

### Commit

- `commit_id`: commit id in SVN system
- `date`: commit date
- `msg`: description of the commit
- `modified`: what files the commit modified