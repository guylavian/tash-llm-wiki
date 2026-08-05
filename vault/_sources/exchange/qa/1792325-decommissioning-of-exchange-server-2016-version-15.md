---
title: "Decommissioning of Exchange server 2016 version 15.1 from Coexistence environment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1792325/decommissioning-of-exchange-server-2016-version-15
question_id: 1792325
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Decommissioning of Exchange server 2016 version 15.1 from Coexistence environment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1792325/decommissioning-of-exchange-server-2016-version-15 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a exchange servers 2016 and 2019 in a coexistence environment. All our mailboxes are on O365. We use the On-prem Exchange as SMTP server. Now we are facing some issues with 2016. Hence we are planning to decommission the Exchange server 2016 version 15.1. 

Can some help me with the step by step document to smoothly decommission our old exchange server. 

Thank you

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 1 · updated: 2024-07-04*

Hi，@Nasir Mohammad

Thanks for posting your question in the Microsoft Q&A forum.

For information on how to retire some Exchange servers in your organization, you can refer to the following steps:

1.      Check that  the MX records and Autodiscover DNS records point to servers or Exchange Online that are still in use.

2.      Update the virtual directory.

3.      Move all mailboxes on the deactivated server, including the arbitration mailbox, to the server on hold.

4.      Delete all databases that are hosted in the server.

5.      Check to see if any Receive connectors are still in use.

6.      Check if there are Send connectors from this server.

Before you uninstall this Exchange server, you can shut down and observe for a while to see if there is a problem. If there are no problems, you can uninstall this Exchange server from Control Panel.

The Microsoft does not provide any documentation on how to delete Exchange 2016 in a coexistence environment, but it does provide documentation on how to delete Exchange 2010, which is worth referring to. Modify or Remove Exchange 2010: Exchange 2010 Help | Microsoft Learn

If my answer is helpful to you, please mark it as the answer so that other users can refer to it. Thank you for your support and understanding.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-05*

I am getting an error while uninstalling CU 22 from exchange server , My goal is to decommission the server. Any Help will be highly appreciated

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-11*

I have a question, while decommissioning exchange 2016, it is not going to impact my other server which is exchange 2019 which is in co-existence environment?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-11*

Thank you guys for your responses. I will try the above steps and update

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-07-04*

To decommission the Exchange Server 2016, you can go with the following steps-

1.       Before decommissioning, verify that all the roles had been transferred and do create a full backup of the Exchange Server 2016

2.       Now, open the Exchange Management Shell on 2016 server and run the following command- Remove-Server –Identity “Exchange2016ServerName”

3.       Go to Control Panel and then select Programs and Features

4.       Select Microsoft Exchange Server 2016 and click uninstall

5.       After uninstallation, check all services are functioning correctlyYou can also refer following links, Link 1 Link 2

Please Note: Since the web sites are not hosted by Microsoft, the links may change without notice. Microsoft does not guarantee the accuracy of this information.
