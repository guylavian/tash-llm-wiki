---
title: "How to list multiple domains in an exchange mail flow exception rule?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2223455/how-to-list-multiple-domains-in-an-exchange-mail-f
question_id: 2223455
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to list multiple domains in an exchange mail flow exception rule?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2223455/how-to-list-multiple-domains-in-an-exchange-mail-f (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In Exchange I created a mail rule to prepend a disclaimer for mail outside our organization, however I want to add a list of domains as an exception.  The list of domains are our clients.  I want to do this so emails do not have the External mail banner if it's a client.  Is it possible to specify multiple sender domains?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-03-12*

Hi @Rose Ingrande,

Thanks for your input.

Using the Exchange Admin Center, we do need to add clients' domains one by one. For instance, input 'test01.domain.com' in the text box and click the '+' button. Then, proceed to input the next domain.

Additionally, I’ve identified an alternative approach to add clients’ domains in bulk by executing a command in the Exchange Management Shell.

Following is an example:

New-TransportRule -Name "AddDisclaimerToExternalDomains" -SentToScope NotInOrganization -ExceptIfRecipientDomainIs @("test01.domain.com", "test02.domain.com", "test03.domain.com") -ApplyHtmlDisclaimerText "test01" -ApplyHtmlDisclaimerLocation Prepend

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

 

Note: Please follow the steps in our documentation](https://aka.ms/msftqanotifications)"https://aka.ms/msftqanotifications)") to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-03-11*

The only way I was able to get the exception rule to accept multiple domains was to add each domain separately.  If you know a better way, I'm all ears, but this was the only way to avoid the error.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-03-11*

Yes, you can definitely set up a rule to exclude certain domains (like your clients' domains) from having the "External Mail" disclaimer. Follow this:  

-  When you edit the mail rule, there’s an option to add exceptions.

-  In the exception section, you can specify multiple sender domains. These would be your client domains.  

Let me know if you have any query.
