---
title: "Windows Server 2012 R2, Folder Redirection GPO and Offline File Sync.  Sync failed.  Access Denied."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2684534/windows-server-2012-r2-folder-redirection-gpo-and
question_id: 2684534
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Windows Server 2012 R2, Folder Redirection GPO and Offline File Sync.  Sync failed.  Access Denied.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2684534/windows-server-2012-r2-folder-redirection-gpo-and (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need a solution for the below problem.  I have seen that other people have experienced the same issue but I have been unable to locate a fix.

I have set up a GPO that syncs user folders to a network location, e.g. My Documents folder.  The client machine in question is running W7 Pro x64.  Let's say the primary user of the machine is User1.

The sync center is displaying an error.  The error reads "Documents. (\\Server\Profiles$\User2).  Access is denied."

Obviously the problem here is that despite being logged in as User1 the folder redirection is trying to sync the user folders of other profiles on the machine, whether they are logged in or not.

Has anyone ever seen this before and if so has anyone ever managed to come up with a solution to this problem on a shared machine?

## Answers

_No answers on this thread._
