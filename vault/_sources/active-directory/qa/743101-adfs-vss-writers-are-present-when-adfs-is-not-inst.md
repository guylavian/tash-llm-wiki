---
title: "ADFS VSS Writers are present when ADFS is not installed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/743101/adfs-vss-writers-are-present-when-adfs-is-not-inst
question_id: 743101
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-server-user-experience-user-experience-other"]
---
# ADFS VSS Writers are present when ADFS is not installed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/743101/adfs-vss-writers-are-present-when-adfs-is-not-inst (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I have a windows 2012 R2 server. Backup tool is TSM. When trying system state backup the creation of snapshot is getting failed with error stating that some ADFS files are missing. But the server does not have the ADFS role installed.  

Also when checking the VSS writers status I could see 'ADFS VSS writer'. Why this server is having ADFS VSS writer when there is no ADFS is installed?  

Possibly that is causing the snapshot operation to search for ADFS related files?  

How to get this resolved and get the backup successful?  

Thanks in advance!  

Bala N

## Answer (community) — community member

*upvotes: 0 · updated: 2022-02-23*

Hello @Balasubramanian N       

The ADFS vss writer is an In-Box writer by default, as specified here: https://learn.microsoft.com/en-us/windows/win32/vss/in-box-vss-writers#active-directory-federation-services-writer    

On the other hand TSM is a 3rd Party tool to Microsoft Windows platform, and thus it would be recommended to check with their community or support what are the requirements, or why is driving this error. Be aware that some backup tools will require machines to be in a Active Directory hirierchy in order to provide security and authentication.    

Hope this helps with your query,    

--    

--If the reply is helpful, please Upvote and Accept as answer--
