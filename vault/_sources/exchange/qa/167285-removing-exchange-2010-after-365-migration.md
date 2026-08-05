---
title: "Removing Exchange 2010 after 365 migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/167285/removing-exchange-2010-after-365-migration
question_id: 167285
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftEmployee", "Mvp"]
---
# Removing Exchange 2010 after 365 migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/167285/removing-exchange-2010-after-365-migration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Last year we migrated to 365 and has been running fine. I would like to decommission our in-house 2010 exchange server but before I do that, do I need to know any issues that may arise from this? Is there really a need to keep the exchange server? I've read pros and cons about it. For me, it's just another server that I have to manage.  

When I did the conversion, I used the Hybrid conversion.

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-11-19*

anonymous user     

Agree with AndyDavid. If you no longer need to manage from on-premises organization, you can just remove the hybrid configuration and uninstall your Exchange 2010.     

Additionally, if you decide to keep Exchange server in the end, it's also suggested to upgrade your Exchange 2010 to 2016 to remain secure and supported. For your reference: Exchange 2010 end of support roadmap.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-11-18*

You need to keep it around if you are using AADConnect and/or ADFS and want to be supported  :)     

That's really it. If you do not use sync from on-prem to Azure, then its not needed at all.    

If you decide to remove it and you are using AADConnect, then you would need to make any on-prem changes that sync to Azure using ADUC or ADSIEDIT or the scripting/tool of your choice.  You won't be technically supported, but that may not matter for you.    

Note that Microsoft is still working on fixing this requirement.     

I'm sure you have already seen:    

https://learn.microsoft.com/en-us/exchange/decommission-on-premises-exchange    

Otherwise, thats it for the most part.
