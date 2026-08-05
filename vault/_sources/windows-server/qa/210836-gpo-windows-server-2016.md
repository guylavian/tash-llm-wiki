---
title: "GPO - windows server 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/210836/gpo-windows-server-2016
question_id: 210836
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# GPO - windows server 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/210836/gpo-windows-server-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hi all,  

I want to apply these group strategies (windows server 2016):  

-  When a computer is running, the windows logs in with a password automatically (Without user knowing the password).  

-  Startup and shutdown of all computers Automatic (linked with a server) from a server.  

Thanks all.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-28*

Although editing the registry is relatively simple and available to everyone (including domain accounts), it does pose a greater security risk than the other methods. The reason is the password for the account you want to automatically log on with is stored in the registry in plain text format.  

That means anybody can go to the registry key where the password is stored and find out what it is, even while the system is offline and not booted. For that reason, this method should be used only if the others have failed. With both of the other methods above the password is encrypted.  

-  Click on Start and type Regedit, administrator privileges are required to run the Registry Editor. Alternatively use the Win+R Run dialog.  

-  Navigate to the following registry key:  

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon  

Read More: https://www.raymond.cc/blog/auto-login-windows-xp-without-typing-password/  

Tip: This answer contains the content of a third-party website. Microsoft makes no representations about the content of these websites. We provide this content only for your convenience.  

Hope this information can help you  

Best wishes  

Vicky

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-12-25*

A couple of ways    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/user-profiles-and-logon/turn-on-automatic-logon    

https://learn.microsoft.com/en-us/sysinternals/downloads/autologon    

PSShutdown can accept wildcards.    

https://learn.microsoft.com/en-us/sysinternals/downloads/psshutdown    

--please don't forget to Accept as answer if the reply is helpful--
