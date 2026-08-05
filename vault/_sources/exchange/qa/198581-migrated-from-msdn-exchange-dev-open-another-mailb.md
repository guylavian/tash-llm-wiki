---
title: "[Migrated from MSDN Exchange Dev] Open another mailbox in OWA"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/198581/migrated-from-msdn-exchange-dev-open-another-mailb
question_id: 198581
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftEmployee", "Mvp"]
---
# [Migrated from MSDN Exchange Dev] Open another mailbox in OWA

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/198581/migrated-from-msdn-exchange-dev-open-another-mailb (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Note: This case is migrated from MSDN Exchange Server Development forum. Since Exchange Server Development forum mainly discuss issues about Exchange development, and non-developer Exchange has transitioned to Microsoft Q&A for support, we migrated this non-developer question manually to continue the discussion.  

Original Post: https://social.msdn.microsoft.com/Forums/office/en-US/d0e1e9c9-ca0b-471d-a702-1638338116fa/open-another-mailbox-in-owa?forum=exchangesvrdevelopment  

Hi all.  

How can I configure to open any mailbox in my Exchnage Online OWA with Impersonation role user?  

Now I get Error 500 (You don't have permission to perform this action).  

Or maybe is it possible to do by another way (please don't tell about "grant full access" - I'm trying to avoid that).

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-21*

I've found something similar to what i need - Evolution email client. It's support EWS and, unlike Thunderbird (via DavMail), I'm able to open another user's mailbox...  

But it works only for Linux.  

Is there something similar for Windows?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-12-15*

You may just have to spin something up if you want to test.     

https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/tools-and-resources-for-troubleshooting-ews-applications-for-exchange    

I usually recommend Glen's blog site for all things EWS. Hes got some great stuff up there:    

https://gsexdev.blogspot.com/    

You can also test with this:    

https://testconnectivity.microsoft.com/tests/EwsAccess/input

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-12-15*

Application Impersonation assumes EWS as the access protocol, so attempting to open  OWA or Outlook wont work with that service account.    

https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange    

If you want to test it against a mailbox, consider using:    

https://learn.microsoft.com/en-us/archive/blogs/chris_pollitt/testing-impersonation-permission-with-ews-editor

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-12-15*

Based on my knowledge, ApplicationImpersonation management role enables applications to impersonate users in an organization to perform tasks on behalf of the user. However, it cannot be used to open mailbox via MAPI or OWA. I'm afraid that we only can open other mailboxes from OWA with Full Access permission.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
