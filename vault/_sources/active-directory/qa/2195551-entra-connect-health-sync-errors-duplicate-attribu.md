---
title: "Entra Connect Health Sync Errors Duplicate Attribute"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2195551/entra-connect-health-sync-errors-duplicate-attribu
question_id: 2195551
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Entra Connect Health Sync Errors Duplicate Attribute

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2195551/entra-connect-health-sync-errors-duplicate-attribu (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi

We have run into a little problem concerning our synced users.

Some users synced without errors and some apparently didnt sync at all.

We had a On-Prem ad with had only a local domain, This domain we added our registered domain upn suffix wich is a c****.se domain.

All users where "converted" to use the new domain upn suffix for login with name.lastname@c***.se

Now we received sync errors from Entra health.

"Unable to update this object because the ProxyAddresses value SMTP:R***.S***@c***.se associated with this object may already be associated with another object in your local directory services. To resolve this conflict, first determine which object should be using the conflicting value. Then, update or remove the conflicting value from the other object(s).!"

The only difference is the SMTP: is with a big letter on Name and Lastname.

Ive been trying to change this and cant get it done for the love of god.

How do i solve this?

Right now we have about 6 users with this problem.

Cheers 

Bjorn

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-14*

Hello Björn Jismark,  

Thank you for posting in Microsoft Community forum.  

Here are two similar threads with possible resolution for your reference.  

[SOLVED] ProxyAddresses Conflict... account won't sync between AD and AAD - Office 365 (spiceworks.com)  

AD Connect User Syncing Error - Microsoft Q&A

If it does not work, from the description above, I understand your question is related to Microsoft Entra.   

Since there are no engineers dedicated to Microsoft Entra in this forum. in order to be able to get a quick and effective handling of your issue, I recommend that you repost your question in the Q&A forum, where there will be a dedicated engineer to give you a professional and effective reply.

Here is the link for Q&A forum.  

Questions - Microsoft Q&A  

Click the "Ask a Question" button in the upper right corner to post your question and select "Microsoft Entra" tag and/or any other Entratag related to your products.  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
