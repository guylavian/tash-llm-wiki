---
title: "Active Directory Web Services was unable to determine if the computer is a global catalog server. Server 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1417559/active-directory-web-services-was-unable-to-determ
question_id: 1417559
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory Web Services was unable to determine if the computer is a global catalog server. Server 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1417559/active-directory-web-services-was-unable-to-determ (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

am facing some issues in my Secondary DC, when I open the active directory users and the computer gives the below error.

we thought its a normal issue because after a restart it worked fine without any issues. But what we noticed this issue keeps showing after a couple of days. then again we need to reboot. how we can fix it and what would be the reason?

Also in the DNS Events am getting the below.

"The DNS server was unable to open Active Directory.  This DNS server is configured to obtain and use information from the directory for this zone and is unable to load the zone without it.  Check that the Active Directory is functioning properly and reload the zone. The event data is the error code."

But DNS is working fine, also the nslook-up is working fine.

Looking forward support.

Thanks in Advance.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2023-11-08*

Hello Rashid Modevencheeri Panikkarakandi,  

Thank you for posting in Q&A forum.  

On secondary DC, then configure the server experiencing the issue to point to other active DNS server （PDC）in TCP/IP properties.  

1.Stop the KDC service on the DC experiencing the issue.

2.Run the following command with elevated rights:

netdom resetpwd /server:<PDC.domain.com> /userd:<Domain\domain_admin> /passwordd:*  

Change the domain name and admin account and password in the command above.

3.It will prompt for the password of the Domain Admin account that you used, enter that.

4.Once the command executes, reboot the server.

5.Check if DNS zones loads.  

https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/dns-zones-do-not-load-event-4000-4007

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-11-07*

What is the status of dcdiag?
