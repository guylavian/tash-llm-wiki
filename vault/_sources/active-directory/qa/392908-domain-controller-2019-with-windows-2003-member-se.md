---
title: "Domain Controller 2019 with Windows 2003 member servers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/392908/domain-controller-2019-with-windows-2003-member-se
question_id: 392908
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Domain Controller 2019 with Windows 2003 member servers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/392908/domain-controller-2019-with-windows-2003-member-se (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We’re planning to promote our existing Domain controllers from Windows Server 2008 to Windows server 2019.   

As of now we don’t have any plans to raise the functional level.   

Current forest/domain level is at Windows Server 2008  

We have several Windows Server 2003 running as member servers. Will that be a problem for 2003 member servers if we upgrade Domain controllers to 2019 ? Upgrading 2003 servers is currently not an option.   

I read some comments about 2003 using smbv1.   

Now is there any specific thing that’ll stop working for all existing 2003 members once we upgrade DC’s to 2019?  

Do we need to enable smbv1 on all 2019 DC’s for 2003 member servers to work fine?  

If yes, is there any different process to enable it on DC’s? Or we need to enable it like its done on any other 2019 servers like mentioned in below URL?  

https://blog.baeke.info/2020/06/08/adding-smb1-protocol-support-to-windows-server-2019/amp/

## Answer (community) — community member

*upvotes: 0 · updated: 2022-01-19*

@Leon Laude    I reviewed and followed the article you pointed to @Yankee30   but I am still getting the error attached... Any ideas or suggestion,s please? I too have Windows 2003 that I MUST join to a Windows 2016 functional level domain.
