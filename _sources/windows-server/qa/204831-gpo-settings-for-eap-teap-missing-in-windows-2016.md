---
title: "GPO settings for EAP-TEAP missing in Windows 2016 and Windows 2012 R2"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/204831/gpo-settings-for-eap-teap-missing-in-windows-2016
question_id: 204831
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 2
qa_tags: ["windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee", "MicrosoftVendor"]
---
# GPO settings for EAP-TEAP missing in Windows 2016 and Windows 2012 R2

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/204831/gpo-settings-for-eap-teap-missing-in-windows-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Everyone,  

I have two Windows servers (2012 R2 and 2016) and even if I have downloaded and applied the latest Windows 10 2004 ADMX I cannot find any settings for the GP Manager for Wireless EAP-TEAP settings to distribute to the workstations.  

Ho can I make them available in a GPO without a workaround?  

Thanks!

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2020-12-22*

Hi，    

Thanks for posting in Q&A platform.    

I checked the GP in windows server 2016 and 2012 in my lab and found that there is also no related settings under Wireless Network. I'm afraid that your goal cannot be achieved in a GPO.    

    

    

As for ADMX, it’s applied for Administrative Templates and not related Windows Settings GP.    

    

Best Regards,    

Sunny    

----------    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-03-04*

Found these, same issue with one of my customers:    

https://learn.microsoft.com/en-us/answers/questions/120377/windows-10-alwayson-vpn-with-eap-teap.html    

Cisco published a workaround which I haven't tested    

https://community.cisco.com/t5/security-documents/teap-for-windows-10-using-group-policy-and-ise-teap/ta-p/4134289
