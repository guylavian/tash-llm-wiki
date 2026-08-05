---
title: "how to check if existing Exchange CAL is enterprise CAL or standard CAL"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/214095/how-to-check-if-existing-exchange-cal-is-enterpris
question_id: 214095
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# how to check if existing Exchange CAL is enterprise CAL or standard CAL

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/214095/how-to-check-if-existing-exchange-cal-is-enterpris (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi experts,   

we are planning for upgrade of existing Exchange server, so that we can implement Exchange in-place archiving with Retention policy.  

we are using Exchange server 2016, may I know how to find out the type of Exchange CAL we are using?  

secondly, what kind of Outlook license do we need? Existing Outlook licenses are either retail version or OEM version of Office Home and Business.  

Thank you  

pingatwork

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2020-12-31*

Hi @Pingatwork   ，    

In addition, Get-ExchangeServerAccessLicense gives you all types of the license you’re using, and you may use     

Get-ExchangeServerAccessLicenseUser -LicenseName “Exchange Server <Version> Standard/Enterprise CAL”  to check who is using these CALs.    

As for the outlook licenses, I agree with Michev, you’ll have to buy one for those additional features.    

    

And kindly suggest that you can Accept michev's answer so this thread could help others have the same issue.    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
