---
title: "SharePoint 2016 to o365 Exchange: Configuration and testing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/113087/sharepoint-2016-to-o365-exchange-configuration-and
question_id: 113087
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-sp-server-business", "office-exchange-hybrid-management"]
---
# SharePoint 2016 to o365 Exchange: Configuration and testing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/113087/sharepoint-2016-to-o365-exchange-configuration-and (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all, currently using onprem SP with incoming and outgoing email configured to use an onprem addresses. In DEV:   

-  Incoming: mylist@@devspemail.contoso.local  

I've been asked to begin testing switching to Exchange Online, using  

-  Incoming: mylist@@devspemail.contoso.com  

Other than existing lists possibly needing a refresh, seems straightforward. I generated a list of Document Libraries currently set to receive emails, there's 250, so creating emails, checking the DROP folder, and verifying that the emails reach their destination also seems straightforward.  

However, I do not have Outbound emails configured in my DEV or STAGE environments, only PROD. I don't want users receiving emails from the non PROD environment as it would create confusion.  

Any recommendations on how I'd test the Outbound functionality? Either trap it on the server, or when it reaches Exchange?   

Thanks!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-01*

Hi, @sco gordo   ,    

For testing the outbound functionality, you will need to configure it in your current farm. If you do not want to bother common users, you can either configure and test it in your Dev environment, or create test users in your Prod environment, use features like alerts or workflow emails to test sending emails.    

If the answer is helpful, please click Accept Answer and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
