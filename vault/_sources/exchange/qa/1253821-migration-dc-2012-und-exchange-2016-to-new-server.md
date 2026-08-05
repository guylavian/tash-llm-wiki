---
title: "Migration DC 2012 und Exchange 2016 to new Server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1253821/migration-dc-2012-und-exchange-2016-to-new-server
question_id: 1253821
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "windows-business-windows-server-devices-deployment-set-up-install-upgrade", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Migration DC 2012 und Exchange 2016 to new Server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1253821/migration-dc-2012-und-exchange-2016-to-new-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

we have 2 Server:
DC on WS2012R2
Exchange2016 on WS2012R2

We would likt to update/upgrade the System.
We have installed 2 new Server:
WS2022 für DC
WS2016 für Exchange

1- How can we migrate the Domaincontroller and the Exchange Mailboxes? what is the best way for that?
2- After the Migration, should we deinstallieren the Roles on the DC & Exchange?
Thanks.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-25*

Hello, 
There is a quite explanative article in the MS Techcommunity that covers the DC migration:
https://techcommunity.microsoft.com/t5/itops-talk-blog/how-to-migrate-active-directory-from-windows-server-2012-r2-to/ba-p/329861
For Exchange, since all the infrastructure will remain on the same On-Premises, you can create a new Exchange Server on the new host, then migrate mailboxes:
https://learn.microsoft.com/en-us/exchange/architecture/mailbox-servers/manage-mailbox-moves?view=exchserver-2019
Then to decomission the old Exchange server, you can follow this article:
https://techcommunity.microsoft.com/t5/exchange-team-blog/decommissioning-exchange-server-2013/ba-p/3613793
--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-04-25*

You can perform a cross-forest move request to migrate your mailboxes from the legacy Exchange 2019 to the new server: Prepare mailboxes for cross-forest move requests. At the same time, back up configurations (except the default ones) of your legacy server(e.g. Connectors, Permission, Transport rule etc.) and apply them to the new server according to your requirements.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-04-25*

Hi @Yasrosa  ,

`1- How can we migrate the Domaincontroller and the Exchange Mailboxes? what is the best way for that?`

For DC migration, the recommended way to upgrade a domain is to promote new servers to DCs that run a newer version of Windows Server and demote the older DCs as needed. Prerequisites and steps you can refer to:Upgrade domain controllers to a newer version of Windows Server | Microsoft Learn

For Exchange migration, you can setup the exchange server on the new Windows Sever, migrate things over and then decommission the old one. More steps you can refer to: Performing a Like for Like Exchange Server Migration
Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.

`2- After the Migration, should we deinstallieren the Roles on the DC & Exchange?`

As far as I know, Roles will be transferred during the configuration phase of the new server. After the migration is complete you can remove the older server.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
