---
title: "Testing Active Directory with WinServer 2019 + Win10Pro"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1408166/testing-active-directory-with-winserver-2019-win10
question_id: 1408166
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Testing Active Directory with WinServer 2019 + Win10Pro

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1408166/testing-active-directory-with-winserver-2019-win10 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

```
Hi, I'm taking a course on active directory, following the instructions I created two virtual machines, one with Windows Server 2019 and one with windows 10 pro.

On the server, the admin is PhAdmin, I installed Active Directory and elevated the server to Domain Controller. I added a few users and groups for practice. The domain is called phoenix.local PHOENIX in NETBIOS. This is obviously also a DNS server, ip 192.168.1.40, the machines are in bridged mode
Then I switched to the Windows machine, left everything in dhcp and set 192.168.1.40 as DNS, then I changed the name of the PC and instead of workgroup I joined it to phoenix.local, it asked me for an administrator password and I put phoenix \PhAdmin and the related password, everything worked at first glance, it asked me to restart and so I did.
When logging in I saw that it recognizes all the users created in Active Directory and the mapped drives and home folders also work well (when logging in to My Computer two network drives appear which contain respectively the work folder and a reserved folder for each user .
However, from this moment on I am no longer able to make changes to the system, for example changing the date and time, changing the network card settings, much less changing the name of the PC... the previous screen always appears telling me to enter the credentials administrator to make the change but this time it doesn't work, whatever I enter it doesn't recognize the user, the mess is this:
"To continue, enter your administrator username and password (which one? local or domain?)"

after re-entering phoenix\PhAdmin and the related password that had previously worked, I get a red error message that says:
Running with elevated privileges is required to perform the requested operation

and from now on I can't do anything anymore..

Has anyone figured out where the problem is?
```

## Answers

_No answers on this thread._
