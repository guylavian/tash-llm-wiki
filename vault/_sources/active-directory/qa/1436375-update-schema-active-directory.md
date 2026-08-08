---
title: "update Schema Active directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1436375/update-schema-active-directory
question_id: 1436375
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# update Schema Active directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1436375/update-schema-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Team,  

I need some help,  

I have a customer having 2 domain controllers with windows server 2016, but the AD schema version is in windows server 2003.  

In fact, the customer, had these old domain controllers on win server 2003, and started upgrading the OS but the not the schema version, now the customer need to do some tuning/hardening, integrate applications and is being restricted due to that old schema version.

I'm charged to update the schema with the less impact and with the best practises.  

I read in some forums, that starting from win server 2012, schema update is done automatically when we create/Promote a new domain controller to the existing domain having the old schma version, is my understanding correct?  

If so, i won't need to  update the schema manually using the adprep commands?

I want also to confirm when we say, starting from windows server 2012 schema update is done automatically, do we talk about the os version on the Domain controllers, or the OS version on the actual schema version?

Here is the blog that i read https://theitbros.com/upgrading-active-directory-schema/

Thank you a lot

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-11-24*

I'm a little bit confused, updating the active directory shema means concretly upgrading the domain/forest level ?     

Schema updates are now a built-in part of domain controller promotion. So when you add a new domain controller with a higher operating system to the domain then domain-wide schema is automatically updated.   

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/domain-wide-updates    

--please don't forget to close up the thread here by marking answer if the reply is helpful--

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2023-11-24*

Hello Mohamed jihad bayali,

Thank you for your reply.  

Is the AD schema you mentioned is objectVersion below?  

In my lab, I have 2 DCs in domain, one is 2016 and the other is 2022, the objectVersion on both DCs are 88.  

Please check what is the objectVersion on all DCs in your domain.

If you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2023-11-24*

Hello Mohamed jihad bayali,  

Thank you for posting in Q&A forum.  

Based on "but the AD schema version is in windows server 2003", I understand the AD schema you mentioned are Functional level （domain functional level and forest functional level）.  

And you can check it via PS command below:  

(Get-ADForest).ForestMode   

(Get-ADDomain).DomainMode  

You mentioned "In fact, the customer, had these old domain controllers on win server 2003", so domain functional level and forest functional level should be 2003.

Ensure that all domain functional levels are equal to or higher than the forest functional level;

Ensure that all domain controller operating systems are at or above the domain functional level;

The domain function level can only be upgraded on the PDC simulation simulator operating host;

Forest functional levels can only be upgraded on schema operations host.

I want also to confirm when we say, starting from windows server 2012 schema update is done automatically, do we talk about the os version on the Domain controllers, or the OS version on the actual schema version?  

A: I understand it is os version on the Domain controllers.

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou
