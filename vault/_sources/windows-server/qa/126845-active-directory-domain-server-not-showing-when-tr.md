---
title: "Active Directory Domain Server not showing when trying to install server roles on Server Manager GUI."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/126845/active-directory-domain-server-not-showing-when-tr
question_id: 126845
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Active Directory Domain Server not showing when trying to install server roles on Server Manager GUI.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/126845/active-directory-domain-server-not-showing-when-tr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone, i have a little issue here.    

It turns out i have a Server Dell PowerEdge R640 with Windows Server 2016 License.    

I want to install the server roles ADDS to add a domain name so i can later start with Remote Desktop Services.    

The problem is I do not see the Active Directory Domain Services Server Role when Server Roles window appear to check the ones i want to install.    

This is what i see when i try to install, but i got stuck here.    

How can i make the ADDS server role appear here?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-15*

Hi, thanks for your replies, i just found a way to do it with static ip address and with remote desktop connection.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-10-15*

Hi,    

Please try running below commands as administrator in CMD and then see if the server manager issue could be resolved.    

cd C:\Windows\System32\wbem\AutoRecover    

for /f %s in ('dir /b *.mof *.mfl') do mofcomp %s    

    

Thanks,    

Eleven    

----------    

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-10-15*

Looks like something may be broken. Some things to try;  

-  sfc /scannow  

-  dism /online /cleanup-image /restorehealth  

-  patch fully https://support.microsoft.com/en-us/help/4000825  

-  repair install by running setup.exe from the root of the install media  

More than likely the quicker thing to do is standup a new one, patch it fully, and move on.  

--please don't forget to Accept as answer if the reply is helpful--
