---
title: "Exchange Mailbox Report on Messageclass"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/397542/exchange-mailbox-report-on-messageclass
question_id: 397542
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange Mailbox Report on Messageclass

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/397542/exchange-mailbox-report-on-messageclass (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All,  

Is there a way to find out what type of messages are in a user mailbox and the count.   

Example: Find out the Items based on Message class. What we want to do is check how many archived Items are there in the mailbox and the number of items not archived.   

Thank you

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-05-18*

Hi @Niroshan Selvarajah  ,    

To the best of my knowledge, you might need to use EWS script in order to find items based on message class. Here are some relevant links for your reference:     

List number of messages by message class Exchange 2007    

[Exchange 2010 : Search and Delete Items by MessageClass  EWS method      

If you need further help on writing the EWS script, it's recommended to post with the tag "office-exchange-server-dev" which is dedicated for Exchange development issues.    

However, regarding to the example mentioned in your post, which is about counting the archived items in a mailbox, do you mean you would like to know the items in the archive mailbox of a user? If this is the case, you can take advantage of the Get-MailboxFolderStatistics cmdlet with the -archive parameter. For example, to view the statistics for User1's archive mailbox, the following command can be used:    

```
Get-MailboxFolderStatistics -Identity user1 -Archive | Format-Table Identity,ItemsInFolderAndSubfolders
```

    

If you want to view the statistics for User1's primary mailbox, you can use the above command without the -archive parameter.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
