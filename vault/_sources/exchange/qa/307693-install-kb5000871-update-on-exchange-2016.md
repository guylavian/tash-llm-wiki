---
title: "Install KB5000871 Update on Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/307693/install-kb5000871-update-on-exchange-2016
question_id: 307693
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Install KB5000871 Update on Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/307693/install-kb5000871-update-on-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have 3 Exchange servers 2016 CU17 in the environment. I am about to update one of the server to CU 19 and then install the KB5000871. My question is, before installing the CU 19, normally I will do a Windows Update to make my server up-to-date. So during the Windows Update, will it download the KB5000871 and install? If yes, do I still need to install it manually again after I install CU 19?  

Perhaps anyone could advise on this. Or can I just skip the Windows Update and straight to the CU 19 installation? Although I know this is not recommended by Microsoft but just wondering if it will cause any issues.  

Thank you.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-12*

Hi,  

One of the servers have been patched successfully and no issues were encountered. Thanks for the assistance.  

Thanks.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-11*

Hi @MarcusWong-9726,    

Although according to the update in KB5000871, an additional series of security updates are being produced by Microsoft for older CUs which include Exchange 2016 CU17, these update packages are only a temporary measure and are available only through the Microsoft Download Center (not on Microsoft Update). Therefore, KB5000871 won't be installed during the Windows Update.    

That being said, for your current scenario, it's suggested to follow the recommended path below, that is, installing the latest supported CU (CU19) and then apply the applicable SUs:    

    

Reference: March 2021 Exchange Server Security Updates for older Cumulative Updates of Exchange Server.    

Furthermore, the official blog below contains information and resources that can help you plan your updates, troubleshoot problems, and help you with mitigations, investigation, and remediation of the vulnerabilities, hopefully you can find it helpful:    

Released: March 2021 Exchange Server Security Updates    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
