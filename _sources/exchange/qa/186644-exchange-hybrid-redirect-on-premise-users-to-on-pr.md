---
title: "Exchange Hybrid redirect On-Premise users to On-Premise owa"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/186644/exchange-hybrid-redirect-on-premise-users-to-on-pr
question_id: 186644
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Exchange Hybrid redirect On-Premise users to On-Premise owa

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/186644/exchange-hybrid-redirect-on-premise-users-to-on-pr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

All our mailboxes are created on our On-Premise Exchange 2019 and migrated to Exchange Online and back again to On-Premise. So they all exist on the On-Premise Exchange. They all have an Exchange Online license, and Office 365 have registred that the mailboxes exist On-Premise and did not create a Exchange Online mailbox for them. Which is all fine.  

But when our users press the Outlook icon in Office 365 they are forwarded to Outlook online where they get the following error:  

err: Microsoft.Exchange.Services.Core.Types.ErrornonExistenMailboxException  

estack: Error:500  

They are supposed to get a message that tells them that their mailboxes exist on the On-Premise server with a link to webmail. This works fine for all new users created.  

Do any have an idea why it doenst work with the old users?  

Our OrganizationRelationship looks fine with the correct TargetOwaURL and as said it works fine with new users.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-11-03*

@Joyce Shen - MSFT   I realize the conversation went silent so you didn't get to continue helping, but what you stated is exactly what the OP said wasn't working.  I've found the same to be true in multiple Exchange Hybrid environments (different customers/organizations altogether).    

Exchange Online's OWA doesn't seem to redirect people to the TargetOWAUrl that is set on the EXO-based Organization Relationship, the way that it is supposed to.  Instead it just tells the logging in user that no mailbox exists or user is missing the license.  Is this maybe something that was missed in the new Outlook on the Web that is exclusive to Exchange Online?    

It seems reasonably likely that it was a missed feature in the new OWA.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-07*

Hi @Mads Kahl      

According to your information above, OWA redirection not working for users migrated back to on-premise from online in your hybrid environment.    

Please make sure if you type on-premise OWA address work for migrated users properly. Also provide any screenshot about the error you meet above here.     

Exchange Online should show the redirect page for mailboxes still on or moved back on-premises.    

Please try removing O365 license After migration completed.     

And the official document here which introduces the steps about Move Exchange Online mailboxes to the on-premises organization in detail    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
