---
title: "Skype for Business 2019 and Exchange server 2016 Integration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/176614/skype-for-business-2019-and-exchange-server-2016-i
question_id: 176614
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-skype-business-platform-windows", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Skype for Business 2019 and Exchange server 2016 Integration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/176614/skype-for-business-2019-and-exchange-server-2016-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

In the Exchange management shell, entered the command ConfigureEnterprisePartnerApplication.ps1 to configure application partnership with another server ( skype for business) and received the following error message:    

Kindly help us to resolve the issue.    

Regards,    

Navinkumar S

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-27*

Hi @Navin Kumar      

Agree with AshokM, we also recommend you try to see these tips to check it .    

In my experience, this issue seems more related to Exchange server's certificates. Try to delete the old certificate and then restart IIS. For more details, please read Kismet’s reply in this link.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-11-26*

Hi,  

Error: The underlying connection was closed: could not establish trust relationship for the SSL/TLS secure channel  

For this error, please check below,  

-  Port 443 HTTPS is allowed between Exchange and skype for business  

-  Skype Metadata URL is accessible  

-  Proxy could cause this error - check if proxy is enabled on Exchange server  

-  Check if the SSL Self signed Certificate is trusted between Skype and Exchange   

-  Sometimes, SSL hardening could also be an issue on the windows server  

You can also try with running the same command with –Trustanyssl switch.  

If the above suggestion helps, please click on Accept Answer and upvote it.
