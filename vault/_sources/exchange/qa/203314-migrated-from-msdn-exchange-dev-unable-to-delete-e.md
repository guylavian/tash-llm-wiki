---
title: "[Migrated from MSDN Exchange Dev] Unable to delete Exchange contacts via Powershell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/203314/migrated-from-msdn-exchange-dev-unable-to-delete-e
question_id: 203314
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# [Migrated from MSDN Exchange Dev] Unable to delete Exchange contacts via Powershell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/203314/migrated-from-msdn-exchange-dev-unable-to-delete-e (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have some contacts in Microsoft 365 online that I cannot remove. They do not appear in the Contacts area of the admin console, nor the exchange admin center, but are causing problems because I cannot update the contacts with new data.  

I don't know how they got in this state, or how to solve the problem.  

If I use:  

Get-Contact  

The names are listed. If I use:  

Get-MailContact  

They are not. What this means is that  

Remove-MailContact -Identity <blah>  

Throws an error:  

The operation couldn't be performed because object '<blah>' couldn't be found on <exchange server>  

If I inspect the problem contacts using:  

Get-Contact -Identity <blah> | fl  

I find that these values are the different ones  

RecipientType            : Contact  

RecipientTypeDetails     : Contact  

Correct MailContacts have the value "MailContact" in these fields.  

How can I delete these contacts?  There does not appear to be a "Remove-Contact" method.  Is there a way to remove a general exchange object by Guid (for example)?  

Source Link: https://social.msdn.microsoft.com/Forums/office/en-US/29ecfeba-16ad-41de-bfc9-c3da3a63b625/unable-to-delete-exchange-contacts-via-powershell?forum=exchangesvrdevelopment

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-18*

The Get-Contact command returns contacts and mail contacts.     

The Get-MailContact command only return the mail enabled contacts.    

So, this user was a non-mail enabled contact.    

Based on my searching, the enable/disable Mail Contact command only suitable for Exchange on-premises. Do you use a hybrid environment and this contact is synced from local AD? If so, you can enable from Exchange on-premises, then delete it with Remove-MailContact command.    

If you aren't using a hybrid environment, you could contact the Office support team to help you check from the backend.
