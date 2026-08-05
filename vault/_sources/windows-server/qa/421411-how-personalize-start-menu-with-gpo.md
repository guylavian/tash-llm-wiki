---
title: "How personalize Start Menu with GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/421411/how-personalize-start-menu-with-gpo
question_id: 421411
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How personalize Start Menu with GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/421411/how-personalize-start-menu-with-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I started personalised my start menu on my RDS Server 2019 (with 2019 DC too) with some GPO    

I find a way with the startLayout.xml file and with some paramèters on GPO    

So i have this result :    

    

How i can delete this last 3 elements :     

Paramèters, Search and Windows Security ?     

For the moment my GPO look like that :

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-07*

Hello,  

Thank's for your answer but on the link you give me ,i didn't found how desactivate the 3 items i mentionned earlier ?   

And the xml file is only for the tiles not the start menu with list of programs   

So i'm still looking for a solution  

Thank's

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-04*

Hi,  

Since you used the GPO to deploy the xml file, If you want to edit the start menu, i'm afraid you may need to update the startLayout.xml file through GPO.  

For how to remove the entries, you may refer to:  

https://www.howtogeek.com/197836/8-ways-to-customize-the-windows-10-start-menu/  

This response contains a third-party link. We provide this link for easy reference. Microsoft cannot guarantee the validity of any information and content in this link.  

Best Regards,
