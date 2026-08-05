---
title: "Exchange/Outlook 2016: Allow dist list owner to add external recipients"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/162449/exchange-outlook-2016-allow-dist-list-owner-to-add
question_id: 162449
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange/Outlook 2016: Allow dist list owner to add external recipients

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/162449/exchange-outlook-2016-allow-dist-list-owner-to-add (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello-  

We would like to delegate the task of distribution list management to one of our employees.  Furthermore, we would like her to have the ability to add new external recipients to an existing distribution list from Outlook, without the need for accessing the Exchange Admin Center.  Is this possible?  Am I missing something obvious?  

She is able to remove existing members, but it seems she cannot add new external recipients that do not exist in the Exchange GAL.  

Apologies in advance if this is the incorrect forum.  Closest I could find :)

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-16*

Hi @Bryce I       

She is able to remove existing members, but it seems she cannot add new external recipients that do not exist in the Exchange GAL.    

This is the expected behavior. As mentioned by Andy, the external recipients need to be added to the Exchange GAL first in order to be added into a distribution list.     

Here are two relevant links for your reference:    

Add External Email Address to a Distribution List    

Adding external email address to internal exchange distribution group.    

Please Note: Since the web sites are not hosted by Microsoft, the links above may change without notice. Microsoft does not guarantee the accuracy of this information.    

Therefore, you would need to help create a mail contact for the external recipient via EAC or using Exchange powershell, so that the distribution list owner can add the external recipient to a distribution list from Outlook. Or you can assign the Recipient Management role group permission to the distribution list owner so that she can create the mail contacts on her own:    

```
Add-RoleGroupMember -Identity "Recipient Management" -Member 
```

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-11-13*

If the List exists in the Exchange GAL, then the external contacts will have to exist there as well.   

An admin or someone delegated with Recipient Management rights will have to create the contacts in EAC or with Exchange powershell and then they can be added by this user to the group via Outlook.
