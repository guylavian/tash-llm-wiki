---
title: "OWA 2019 Autocomplete and suggestion list"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/272338/owa-2019-autocomplete-and-suggestion-list
question_id: 272338
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# OWA 2019 Autocomplete and suggestion list

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/272338/owa-2019-autocomplete-and-suggestion-list (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

i have exchange 2019 all users are using owa to check emails  

we decide to change the smtp address to emp id  and delete the old smtp   

how can i change or delete old smtp address for all users because it shows old address under suggestion and autocomplete ,  

all users now are facing sending error because the smtp address that in autocomplete list is no longer avaliable and they used to chose from autocomplet list   

appriciate any idea   

Regards  

S

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2021-02-15*

Hi @Salman Al Bedaiwi  ,

The autocomplete cache in OWA is stored in the item of message class IPM.Configuration.Autocomplete and a hidden folder named Recipient Cache also contains cached recipient information that could be used for OWA users. 

Based on my research and test, in order to empty these cache, a user would need to have an Outlook for Windows profile (Exchange Online mode) created and then delete the two objects using the MFCMAPI tool:

-  Download and extract the MFCMAPI tool, launch MFCMAPI.exe, click OK, on the Session Menu, click Logon, select the Outlook profile for the mailbox, click OK.

-  Double click the email address, right-click Root Container , and then click Open Associated Contents Table, arrange the columns header and scroll to the right until you can see the Message Class details for each entry, locate the object that has a Message Class ID of IPM.Configuration.Owa.AutocompleteCache to remove the OWA autocomplete.

-  Expand Root Container - Top of Information Store - Contacts - Recipient Cache, right click on it, choose Delete folder, click Hard delete, OK:

I fully understand that you need to delete the cache for all users, but to the best of my knowledge, I'm afraid it's not feasible to be realized using the built-in Exchange feature or regular powershell. Given this, I'd recommend having a go using the steps above on one of the users, if it works, you can then share the procedure with all users so that they can remove the cache by themselves.  

If an Answer is helpful, please click "Accept Answer" and upvote it.
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
