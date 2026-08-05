---
title: "User Mailbox on Exchange Online but Sfb on prem"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/127487/user-mailbox-on-exchange-online-but-sfb-on-prem
question_id: 127487
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-skype-business-platform-windows", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# User Mailbox on Exchange Online but Sfb on prem

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/127487/user-mailbox-on-exchange-online-but-sfb-on-prem (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Support,  

User A mailbox is on Exchange Online but Skype account is hosted on prem.  

If User A is on external network,EWS Internal URL and EWS External URL are blank and EWS Information will show "EWS not deployed". With this, calendar tab in Skype client will not sync correctly.  

If User A on external network and connected to company VPN, EWS Internal URL and EWS External URL will have value  and EWS Information will show "EWS Status OK". With this, calendar tab in Skype client will sync correctly.  

Any idea how to fix the issue? Appreciate and thank you in advanced.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2020-10-16*

@ktying  ,    

Does anyone else have the same issue?    

It recommends your IT admin to check if the Autodiscover is pointing to the Office 365 server.    

Besides, if there is related error message in Skype for Business server, please give us a screenshot for further investigation.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
