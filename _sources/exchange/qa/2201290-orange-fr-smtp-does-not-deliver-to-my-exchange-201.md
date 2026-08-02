---
title: "Orange.fr SMTP does not deliver to my Exchange 2013 server anymore"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2201290/orange-fr-smtp-does-not-deliver-to-my-exchange-201
question_id: 2201290
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Orange.fr SMTP does not deliver to my Exchange 2013 server anymore

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2201290/orange-fr-smtp-does-not-deliver-to-my-exchange-201 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,

We use an on premise Exchange 2013 Server for our mail base.

Since a few weeks, only mails from @orange.fr can't contact our organization.

Any othe domain can. I update SPF, DKIM and dmarc policy on our domain but nothing has changed. Every people frome orange.fr domain can't get us by mail and get after 4 days a message saying domain xxxxx.xx timed out

## Answer (community) — community member

*upvotes: 0 · updated: 2025-03-06*

Hello @Anonymous  

Thanks for trying to help me.

I forgot to say, we can send messages to orange.fr domain without any problem.

our domain -> orange.fr no problem

orange.fr -> our domain can't get it.  

Even when the person respond to a message we sent, it doesn't work..

I tried from another domain (Google mail) and there is no problem, from and to orange.fr and from and to our domain.

I don't have any result on our Exchange Server log, there is not any track from incoming mails from this domain.  

The logs I got from orange.fr users resolve properly our DNS, but end with a time out anyway...

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-03-06*

Hi @Mickael Vosgien，

Thank you for posting your question in the Microsoft Q&A forum.

According to your description, your problem is undeliverable emails from the domain orange.fr. Is it possible for your organization to send emails to orange.fr and is it possible for orange.fr to send emails to other organizations? If sending to @orange.fr also fails, may indicate that there is a problem with two-way communication or that the other party's server has global restrictions. Here are some suggestions for this issue, hopefully they can help you.

-  Review the sender's message tracking log and the non-delivery report (NDR) as well as the Exchange server's message tracking log. Any errors or issues in the log related to undelivered messages may provide clues as to what the problem is, and the code in the NDR may also indicate why the message was not delivered. The meaning of the enhanced status codes returned for common mail delivery failures can be found in the documentation: DSNs and NDRs in Exchange 2013: Exchange 2013 Help | Microsoft Learn.

-  Ensure that DNS settings are configured correctly. Incorrectly configured DNS settings can cause email delivery issues. Ensure that Orange.fr's mail servers are properly resolving MX records for the user's domain name. Check that the MX records are correct and verify that the TTL has not expired causing the cache not to be updated.

-  Check that the @orange.fr domain or its IP address is not blacklisted on the server and that there are no firewall rules or network configurations blocking email from the @orange.fr domain.

If the answer is helpful, please click on “Accept answer” as it could help other members of the Microsoft Q&A community who have similar questions and are looking for solutions.

Thank you for your support and understanding.
