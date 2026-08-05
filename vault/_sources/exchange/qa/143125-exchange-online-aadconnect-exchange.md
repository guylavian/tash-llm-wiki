---
title: "Exchange online - AADconnect - Exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/143125/exchange-online-aadconnect-exchange
question_id: 143125
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Exchange online - AADconnect - Exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/143125/exchange-online-aadconnect-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi ,   

yet another challenge.  

A customer is in the cloud with full cloud identity.  

This was done by a cutover migration from an exchange2013.  

Now , the customer has decided that they want AADConnect.  

No problem there, i can softmatch the users.  

Exchange server is not uninstalled.  

The thing is , this Exchange server is not in hybrid - so the user's mailboxes are still on the databases.  

In a hybrid server, these users are mail enabled users (after migration) and you can just delete the databases and downsize the server.  

In this case ,I just want to keep this server as a "management" server and downsize it.  

Do i need to run the hybrid wizard on this machine ?   

kind regards,   

Filip

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-10-29*

@Filip Soogen       

If you just want to manage users from on-premises, and no hybrid features are needed (such as mailbox migration, mail routing...), you don't have to run HCW.     

Here is a similar thread, this user's organization is in a hybrid deployment. He wants to upgrade from Exchange 2010 to 2016, and use Exchange 2016 for user management. The hybrid configuration is not needed and will be removed. For your reference:    

Decommision last Exchange 2010,    

Scenario two.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
