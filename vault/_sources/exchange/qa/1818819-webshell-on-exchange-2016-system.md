---
title: "webshell on exchange 2016 system"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1818819/webshell-on-exchange-2016-system
question_id: 1818819
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# webshell on exchange 2016 system

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1818819/webshell-on-exchange-2016-system (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Currently on our Exchange 2016 system there is an iisstart.aspx file. I don't know what it is. Does it affect the system? On the security side of our organization, we suspect it is a webshell attack on the system.

Thanks to everyone for help

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-18*

Hi @Yanhong Liu

I discovered some more of these files, please help me see what they are? Is it dangerous?

C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\ecp\auth\getidtoken.aspx

 

C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\ecp\auth\logon.aspx

 

C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\owa\auth\Current\themes\resources\owafont.aspx

 

C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\ecp\auth\Logout.aspx

 

C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\owa\auth\15.1.2242\themes\resources\aria-down.css.aspx

 

C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\owa\auth\15.1.2242\themes\resources\owafont_es.aspx

 

/aspnet_client/system_web.aspx

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-07-16*

The iisstart.aspx file is not harmful. It is a default file that is part of Internet Information Services (IIS), the web server software used by Exchange Server. You can remove this file, if you don’t want it.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-16*

Hello,

Thank you for posting in Q&A forum.

The "iisstart.aspx" file is usually a default placeholder page used by Internet Information Services (IIS) Microsoft. Its main purpose is to verify that IIS is installed and running correctly. In theory, it does not pose any threat to your system.

However, if you suspect that your system may have been attacked by a webshell, you should take the following steps to confirm and take action:

-  Check file integrity and content:

Verify the content of "iisstart.aspx". Compare it to a known good version from a clean installation of Exchange 2016 or IIS to ensure that it has not been tampered with.

-  Scan for viruses and malware:

Scan this file and the entire system with up-to-date antivirus software to detect any potential malware or webshells.

-  Check log files:

Review IIS logs, system event logs, and application logs for any unusual activity or logon attempts.

-  Check file properties:

Review file properties (e.g., creation date, modification date) to see if they are consistent with other system files or if they look suspicious.

-  Updates and Patches:

Make sure your Exchange 2016 and IIS installations are up to date with the latest security patches.

I hope the information above is helpful.

Best Regards,

Yanhong Liu

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
