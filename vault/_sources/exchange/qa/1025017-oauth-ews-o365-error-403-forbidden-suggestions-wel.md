---
title: "oAuth ews o365 - error 403 forbidden - suggestions welcome"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1025017/oauth-ews-o365-error-403-forbidden-suggestions-wel
question_id: 1025017
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# oAuth ews o365 - error 403 forbidden - suggestions welcome

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1025017/oauth-ews-o365-error-403-forbidden-suggestions-wel (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Code works correct with another o365 tennant but not this tennant.    

 Code flow is exactly as stated here https://learn.microsoft.com/nl-nl/exchange/client-developer/exchange-web-services/how-to-authenticate-an-ews-application-by-using-oauth    

Debugging it I see the token verification works fine but my ews call to bind to a user inbox errors out with 403.    

the email address is correct, mailbox has a license in o365, ews policy is enabled for all mailboxes.    

i guess it must be a setting in o365 but what?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-30*

Hi @john in t veld   ,    

Glad to know that your issue is resolved now! Since our forum has the policy that The question author cannot accept their own answer, I would make a brief summary of this post so that other forum members could easily find useful information here:     

Issue Symptom:     

oAuth ews o365 - error 403 forbidden    

the application ID being incorrect in AAD    

Solution:    

Change to the correct application ID    

You could "Accept Answer" for this summary to close this thread, and your action would be helpful to other users who encounter the same issue and read this thread. Thanks for your understanding!    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-29*

it was simply an issue with the application ID being incorrect in AAD !    

thanks for your help guys.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-29*

It sounds like they have either disabled EWS on the Mailbox that you're trying to access, or they have limited the clients that are allowed to connect e.g., https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/how-to-control-access-to-ews-in-exchange . You can try testing EWS itself using a user account via the EWSeditor https://github.com/dseph/EwsEditor

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-09-27*

403 can be a result of an Application access policy blocking access to certain mailboxes. Read here for more details: https://practical365.com/new-application-access-policies-extend-support-for-more-scenarios/
