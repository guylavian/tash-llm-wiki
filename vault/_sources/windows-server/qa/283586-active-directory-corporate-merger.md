---
title: "active directory & corporate merger"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/283586/active-directory-corporate-merger
question_id: 283586
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# active directory & corporate merger

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/283586/active-directory-corporate-merger (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Howdy All,  

I'm sure this and related aspects have been discussed quite a bit, but I wanted to post my own thread to aggregate answers for the many facets of this upcoming project.  

-  We have a single forest with a single domain.  

-  We are also Office365 using Okta for federation. Converted the email domain as UPN for the corporate domain.  

-  We are in the process of acquiring another company in our field who is still on-prem Exchange 2010. Planning to move them to O365.  

I've been told that we might simply fold them into our existing domain up front and then create a new forest/domain structure for the combined entity since we might also change names.  

Grey areas for me are, am I better off creating a new domain in same forest or totally new forest? Concerns are that we've had Exchange in our forest already and so have they. Would a new forest be advantageous or does O365 render some of that moot?  

'Preciate any input, examples, war stories of similar experiences, etc... :)

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-02-23*

Hello @MWave6  ,    

Thank you for posting here.    

Based on the description above, I understand you have a single forest with a single domain now, you are also using Office365.     

Meanwhile, you want to acquire/add/merge another company who is still on-prem Exchange 2010 (I may call it another forest with on-prem Exchange 2010) to your existing forest.    

I understand what your concern is you had better merge the two forests to your existing forest?    

Or you had better create a new forest and add all things in another company and your existing forest to this new forest?    

Based on my knowledge: The domain rename operation is not supported in Microsoft Exchange 2000 server,Microsoft Exchange Server 2007 or Exchange Server 2010,Microsoft Exchange Server 2013.    

According to my research and experience, I suggest we had create a new forest and add/migrate all the things you want to this new forest.    

Tips: I mainly focus on the issue or problem about local AD DS, if you have specific question related to Office365 or Exchange, you can post again by selecting Office365 or Exchange tag.    

Hope the information above is helpful.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou
