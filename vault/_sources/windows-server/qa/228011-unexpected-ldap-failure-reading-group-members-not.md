---
title: "Unexpected LDAP failure reading group members - Not enough space"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/228011/unexpected-ldap-failure-reading-group-members-not
question_id: 228011
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Unexpected LDAP failure reading group members - Not enough space

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/228011/unexpected-ldap-failure-reading-group-members-not (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are trying to run Adobe's "User Sync Tool" to sync Adobe's licensing server with select AD Groups in our environment. It shows it connects to LDAP without issue but throws this error:    

CRITICAL main - Unexpected LDAP failure reading group members: {'desc': 'Other (e.g., implementation specific) error', 'info': '00000008: SysErr: DSID-0205199E, problem 12 (Not enough space), data 0\n     

There was an older TechNet forum post regarding this issue. Ryan Ries [MSFT] talked about a Hot Fix - KB4516077, but this was for older versions of Win 2019. In an effort to try to resolve this, I did run this hotfix but it didn't resolve the issue.    

To make this even more interesting....    

We have 4 Windows 2019 Domain Controllers and all have been built in the last 60 days using the lastest ISO from VLSC    

Three (3) servers are Virtual (VMWare) and one (1) is physical    

Two (2) servers are 2019 Standard, and two (2) are 2019 Datacenter    

The sync tool runs fine on the 2 Datacenter machines, but fails on the Standard OS version; not sure if this has any bearing.    

I have increased CPUs, Memory Size, and Cache memory to no avail.    

Can anyone suggest the next step in troubleshooting?    

UPDATE: I am able to successfully sync 5 out-of 10 times intermittently.    

@Ryan Ries [MSFT]

## Answers

_No answers on this thread._
