---
title: "Windows Server Active Directory is not work"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1283629/windows-server-active-directory-is-not-work
question_id: 1283629
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Windows Server Active Directory is not work

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1283629/windows-server-active-directory-is-not-work (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello family.

I hope all is well, I have something with Windows Server I would like to configure it to have access to the Server Role to Activate the options required for the IIS. I can't when I open Windows Server > add other server to manage > Active Directory: "The local computer is either no domain-join, or it cannot access a domain controller".

I tried to change the domain by accessing System > change settings > Computer name -> change then in Member of i Select Domain and i Enter the domain This is the error i get  when i submit "An Active Directory Domain Controller (AD DC) for the domain 'domain' couldn't be contacted".

I use the nltest /dsgetdc:domainname command to check the location of the domain controller, i get this in output: Getting DC name failed: Status = 1355 0x54b ERROR_NO_SUCH_DOMAIN

And ipconfig /registerdns to force host registration registration.

Its not working too.

## Answer (community) — community member

*upvotes: 2 · updated: 2023-05-14*

Thank you David.

I happen to be new to this system. If you don't mind, I would like you to develop a little about the PDC emulator, such as how to run the PDC emulator?

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2023-05-19*

Something here could help.  (same basic steps for Server 2019 or 2022)

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/install-a-new-windows-server-2012-active-directory-forest--level-200-      

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-05-13*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`	(run on PDC emulator)  

`repadmin /showrepl >C:\repl.txt`	(run on any domain controller)  

`ipconfig /all > C:\%computername%.txt`	(run on EVERY domain controller)  

`ipconfig /all > C:\problemwmember.txt`	(run on problem one)  

Also check the domain controller System and Replication (DFS or FRS) event logs for errors since last boot. Post the Event Source and Event IDs of any found. (no evtx files)  

then put `unzipped` text files up on OneDrive and share a link.
