---
title: "Exchange Migration Timeout"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1573031/exchange-migration-timeout
question_id: 1573031
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 2
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Exchange Migration Timeout

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1573031/exchange-migration-timeout (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We ran the hybrid wizard and everything came back successful.  I created a new account, no emails in it, waited a few hours and then attempted to migrate it to Exchange Online.  

I got the following error message:  

Error: MrsHttpUnauthorizedException: The Mailbox Replication Service was unable to connect to the remote server using the credentials provided. Please check the credentials and try again. The call to 'https://7d7343aa-3169-41be-a38c-959d826c9248.resource.mailboxmigration.his.msappproxy.net/EWS/mrsproxy.svc' failed. Error details: The HTTP request is unauthorized with client authentication scheme 'Negotiate'. The authentication header received from the server was 'Negotiate,NTLM'. --> The remote server returned an error: (401) Unauthorized.. --> The HTTP request is unauthorized with client authentication scheme 'Negotiate'. The authentication header received from the server was 'Negotiate,NTLM'. --> The remote server returned an error: (401) Unauthorized. --> The call to 'https://7d7343aa-3169-41be-a38c-959d826c9248.resource.mailboxmigration.his.msappproxy.net/EWS/mrsproxy.svc' failed. Error details: The HTTP request is unauthorized with client authentication scheme 'Negotiate'. The authentication header received from the server was 'Negotiate,NTLM'. --> The remote server returned an error: (401) Unauthorized.. --> The HTTP request is unauthorized with client authentication scheme 'Negotiate'. The authentication header received from the server was 'Negotiate,NTLM'. --> The remote server returned an error: (401) Unauthorized.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-27*

After throwing the error above it changed it to an error about connectivity, about 15 minutes later. The connectivity analyzer identified our issue and after fixing that, the migration was successful.

Hi @Daniel Kaliel ,

Great to know that the migration was successful after fixing the connectivity issue and many thanks for your sharing so that others experiencing the same thing can easily reference this!   

Since the Microsoft Q&A community has a policy that "The question author cannot accept their own answer. They can only accept answers by others", I'll repost your solution in case you'd like to "Accept" the answer : )  

[Exchange Migration Timeout]  

Issue Symptom:  

"We ran the hybrid wizard and everything came back successful. I created a new account, no emails in it, waited a few hours and then attempted to migrate it to Exchange Online.
I got the following error message:
Error: MrsHttpUnauthorizedException: The Mailbox Replication Service was unable to connect to the remote server using the credentials provided. Please check the credentials and try again. The call to 'https://7d7343aa-3169-41be-a38c-959d826c9248.resource.mailboxmigration.his.msappproxy.net/EWS/mrsproxy.svc' failed. Error details: The HTTP request is unauthorized with client authentication scheme 'Negotiate'. The authentication header received from the server was 'Negotiate,NTLM'. --> The remote server returned an error: (401) Unauthorized.. "

Current Status:
"After throwing the error above it changed it to an error about connectivity, about 15 minutes later. The connectivity analyzer identified our issue and after fixing that, the migration was successful."

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-02-26*

After throwing the error above it changed it to an error about connectivity, about 15 minutes later.  The connectivity analyzer identified our issue and after fixing that, the migration was successful.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-26*

Hi @Daniel Kaliel  ,  

As indicated in the error message, it could be caused by the wrong credential of the associated administrator account of the migration endpoint.   

Please try updating the password of the associated administrator account in the migration endpoint settings page or create a new migration endpoint with the correct credentials of the on-premises administrator and then rerun the migration to check how it goes.   

Here's a relevant article for your reference:  Mailbox Replication Service was unable to connect to the remote server.  

(Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.)

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
