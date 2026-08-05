---
title: "set smtp address for exchange online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/179099/set-smtp-address-for-exchange-online
question_id: 179099
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# set smtp address for exchange online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/179099/set-smtp-address-for-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello I have small non standard environment for microsoft. Old domain with exchange server 2013 and single domain name. All user are migrate to new domain "ad.domain.eu" and this domain is synchronized to m365 azure ad witch exchange online. Users have m365 office and use synchronized acc "******@ad.domain.eu". It possible change address to default smtp type "user@keyman  .eu" and alias "user@keyman  .(user localization state) etc com" and copy emails from pst or connect from their outlook profile to exchange server. Cutover migration is impossible because users are synchronized and exist on azure domain. Hybrid is migration is impossible because cant connect to old single name domain. What way its for my? Must migrate? Create new acc? Is possible changed smtp address or not? My dessing is bad? In best practise say good for you have domain like as ad.domain.com. I am in situation have old exchange 2013 and need move mailbox and public folders to exchange online. Its tiny environment only 20 users + pub. folders.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-30*

@Martin Dvorak       

For email address, you need to verify your domain name in Office 365 admin center first, then you will could apply email address on Exchange online mailbox:    

-  Add a domain to Microsoft 365    

-  Add or remove email addresses for a mailbox    

For import PST file to Exchange online mailbox, you could use network upload to import data to Exchange online mailbox: Use network upload to import your organization's PST files to Microsoft 365    

If your organization data file is large, you can save them into a hard disk drive, then send this disk to Microsoft, Microsoft will help you upload data(This item is chargeable)    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
