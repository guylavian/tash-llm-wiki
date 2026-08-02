---
title: "Exchange PowerShell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/396337/exchange-powershell
question_id: 396337
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange PowerShell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/396337/exchange-powershell (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

First, I have not found a GAL report that would give me the below information, so, I think a powershell is what is needed.  I do have Exchange Powershell on my system, I can sign in to it and enter commands.  What I do need is help with creating a Powershell command  string that will show the following and download it in a CSV file.  

First Name,  Last Name, Mobile Phone, Home Phone, direct reports, Department, Email address, Manager, Title,  Office, Street Address, City, State, zip code, Country, Notes, and custom channels 1 through 16  

Thank you very much for any help with this.  

Regards,  

Gary Huber

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-22*

Eric, it worked great.  Thank you for the help.  

Best regards,  

Gary

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-17*

Hi,  

It's easy to retrieve AD properties by Get-Mailbox or Get-Recipient but it seems your requirement is most saved in GAL.  

However, we can't export information from GAL directly in Powershell.

I would suggest to use Outlook to do this, I'm using Office 365 as an example:

1) Log on to your Outlook desktop (or someone who can view all GALs), find "address book" and select the address book that you want to export, "GAL- username@keyman  .com" for example, "SHIFT+left-click" the first adress and "SHIFT+left-click" the last address, then right-click "add to Contacts". (My Outlook warns "too many items are selected" in this step by the way, you might have to handle whole GAL in several batches.)  

2) File- Open&Export- Import/Export- Export to a file- Comma Separated Values, find the "Contact" that contains your GAL, save it to a CSV file.  

3) Open the CSV file in excel and select the values you want, some excel skills are needed.

If an Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
