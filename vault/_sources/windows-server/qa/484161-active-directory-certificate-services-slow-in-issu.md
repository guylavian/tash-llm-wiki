---
title: "Active Directory Certificate Services - Slow in issue Certificate via powershell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/484161/active-directory-certificate-services-slow-in-issu
question_id: 484161
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory Certificate Services - Slow in issue Certificate via powershell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/484161/active-directory-certificate-services-slow-in-issu (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

We are using certreq command to generate certificate signing requests on a Windows Server 2016 server programmatically.  

The observation is that every 35mins, the certreq command holds for 8-16 seconds before returning the response. Subsequently, the request and response resumes normally at about 3-5 seconds per certificate.  

We have increased the CPU and RAM on the server and disabled most of the background applications like antivirus etc, but to no avail.  

What could be the cause of this issue?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-22*

Hello @NOC  ,

Thank you for posting here.

Please try to troubleshoot as below.

1.Please check if you request certificate via GUI, whether the same situation occurs.

2.Whether this Windows Server 2016 server is a CA server or a domain member server?  

If it is a member server, please check whether the same situation occurs when you are using certreq command to generate certificate signing requests on other domain Windows machines programmatically.

3.You can try to perform a clean boot on this machine, then check whether the same situation occurs when you are using certreq command to generate certificate signing requests on other domain Windows machines programmatically.

How to perform a clean boot in Windows  

https://support.microsoft.com/en-us/topic/how-to-perform-a-clean-boot-in-windows-da2f9573-6eec-00ad-2f8a-a97a1807f3dd

Hope the information above is helpful to you.

Should you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
