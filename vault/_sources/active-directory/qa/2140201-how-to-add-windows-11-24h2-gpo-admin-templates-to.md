---
title: "How to add Windows 11 24H2 GPO Admin Templates to Central Store"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2140201/how-to-add-windows-11-24h2-gpo-admin-templates-to
question_id: 2140201
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# How to add Windows 11 24H2 GPO Admin Templates to Central Store

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2140201/how-to-add-windows-11-24h2-gpo-admin-templates-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi and HNY to you all....! 

I need to start using the Admin Templates form Win11 22/24/24 versions and I already have an AD Central Store for GP Admin Templates set and in Production for years.

 Now this article says that we should add new folder describing the current version such as:

`\\contoso.com\SYSVOL\contoso.com\policies\PolicyDefinitions-24H2 `

Now how is this going to work on the GPO setup side (from GP Management) if I have 2 x folders out of of policies: 

`\\contoso.com\SYSVOL\contoso.com\policies\PolicyDefinitions`  ->Containing Windows 10 and Windows Server 2016/19/22 ADMX/L 

`\\contoso.com\SYSVOL\contoso.com\policies\PolicyDefinitions-24H2`->Containing Windows 11 and Windows Server 20125 ADMX/L 

Will we be able to search and create GP Objects settings for Win10 and W11 separately?

Quite confusing and not really understanding the point of a new folder! 

Question 2 - can I dump the Win11 ADMX/L files and overwrite the Win10 files in the standard location:  \contoso.com\SYSVOL\contoso.com\policies\PolicyDefinitions  ?

Thanks M

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2025-01-07*

In my experience, the new ADMX files are backwards compatible with the old.  They say that because there are rare circumstances where a unexpected behaviors can occur.  They explain this later on in the same article:  

...When this is finished, rename the current PolicyDefinitions folder to reflect that it's the previous version, such as PolicyDefinitions-23H2. Then, rename the new folder (such as PolicyDefinitions-24H2) to the production name.

*We suggest this approach as you can revert to the old folder in case you experience a severe problem with the new set of files. When you don't experience any problems with the new set of files, you can move the older PolicyDefinitions folder to an archive location outside sysvol folder.  

*  

So, the answer to Question 2 is "generally speaking", yes. That is what I have always done, just keep a backup of the old definitions. Hope this helps.
