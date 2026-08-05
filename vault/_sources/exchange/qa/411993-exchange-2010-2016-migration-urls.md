---
title: "Exchange 2010 - 2016 migration - URLs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/411993/exchange-2010-2016-migration-urls
question_id: 411993
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2010 - 2016 migration - URLs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/411993/exchange-2010-2016-migration-urls (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

I am in the process of upgrading/migrating from Exchange 2010 to 2016  

I have already installed the 2016 server and am working through the Deployment Assistant.  

My question is regarding the changes to the internal/external web URLs.   All the mailboxes and internet access is currently via the Ex2010 server and I do not want to interrupt service to end users until or if it is definitely required.  

If I make the required changes to the URLs such as adding "mail.domain.com" to the Ex2016 server, will this affect user access to the 2010 server as this will also have "mail.domain.com" listed in its own settings ?   Is this going to cause issues with client access if both servers have the same URL ?  

There is no real mention of how or if this might affect the Ex2010 server in the deployment assistant, or if changes also need to be made to the 2010 server.  

I'd rather not change too many things if I don't need to in case I need to roll back.  

Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-28*

Hi    

Just to clarify.    

I understand I need to make the URL changes on the 2016 server.    

But do I need to actually remove the external entries (mail.domain.com) from the 2010 server or can I just leave these ?  Again I'd like to make the minimum changes necessary in case I need to roll back.    

@Lucas Liu-MSFT  's reply said "You can set Exchange 2010 and Exchange 2016 to be the same"    

So they can both contain the external URLs and it shouldn't cause any conflicts ?    

Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-27*

Hi  

Thanks for the response  

Regarding the second link.  We don't have a CAS array in the environment.  It's a simple setup with a single 2010 server migrating to a single 2016 server.  

Does this information still apply ?  

Thanks
