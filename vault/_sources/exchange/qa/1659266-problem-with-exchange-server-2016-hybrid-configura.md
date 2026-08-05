---
title: "Problem with Exchange Server 2016 Hybrid Configuration (Teams Rooms Mailbox)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1659266/problem-with-exchange-server-2016-hybrid-configura
question_id: 1659266
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Problem with Exchange Server 2016 Hybrid Configuration (Teams Rooms Mailbox)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1659266/problem-with-exchange-server-2016-hybrid-configura (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good day,

After setting up Exchange Hybrid (Classic Mode), the O365 mailboxes are not displayed in onPrem Exchange. Mails cannot be sent from onPrem to O365 either. In O365, the onPrem mailboxes are visible and mails can also be sent from O365 to onPrem.

The firewall uses its own public IP address exclusively for the Exchange server and has been configured to allow all ports from the documented Microsoft addresses to the Exchange.

A public wildcard certificate is used on the onPrem Exchange and is assigned to IIS, SMTP and all connectors.

EntraID Connect was also set up and Exchange Hybrid activated. All users are successfully synchronized without errors.

The goal of the configuration is to set up an O365 Teams Rooms mailbox that is available for onPrem users and can be booked.

Steps to reproduce:

-  Installed and configured Entra ID Connect.

-  Configured own public IP address for the local Exchange. Any port from Microsoft addresses are allowed, DNS name o365.XXXXXXXX.de points to this IP

-  Installed current public wildcard certificate on local Exchange and assigned to IIS and SMTP services as well as all connectors

-  Adjusted virtual directories in local Exchange to external DNS names

-  Installed and configured Exchange Hybrid Assistant

-  Created room mailbox in O365 and assigned Teams Rooms Pro license

-  Successfully sent mail from O365 to onPrem

-  Mail from onPrem to O365 cannot be sent

-  O365 objects are not visible in onPrem Exchange"

Thank you in advance for your help."

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-05-07*

Hi,

Great to know that the issue has already been resolved and thanks for sharing the solution so that others experiencing the same thing can easily reference this! Since the Microsoft Q&A community has a policy that "[The question author cannot accept their own answer. They can only accept answers by others, I'll repost your solution in case you'd like to "[Accept]" the answer : )     

--------------   

Issue Symptom: 

 Set up an O365 Teams Rooms mailbox that is available for onPrem users and can be booked.

 

Resolution: 

The way should now be to create a user in AD onPrem and then create a remote room mailbox:

Example: Enable-RemoteMailbox -Identity XXX_TeamsRoom -Room -RemoteRoutingAddress ******@CUSTOMER-DOMAIN.de

Afterwards, you can assign the license online and configure the Teams Rooms device.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-06*

Hi Noah,

through a similar problem with another customer, I have found a solution for the Teams Rooms issue:

Entra ID Sync synchronizes objects from OnPrem to Cloud. In the opposite direction, this works with some user attributes, but not with whole user objects. However, groups and devices work. So it is practically not possible to synchronize the room mailbox to onPrem.

The way should now be to create a user in AD onPrem and then create a remote room mailbox:

Example: Enable-RemoteMailbox -Identity XXX_TeamsRoom -Room -RemoteRoutingAddress “******@CUSTOMER-DOMAIN.de”

Afterwards, you can assign the license online and configure the Teams Rooms device.

Here is a site, that describes that a bit: https://www.msxfaq.de/cloud/identity/room_provisioning.htm

I hope this will help other people with the same problem. :-)

I thank you very much for the detailed help!

Thumbs up and best regards,

Alex

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-30*

Hi Noah, 

thanks for the reply. 

We have set up 2 mailboxes online, we get the same NDR when we write a test email. Everything is set to authoritative in the local Exchange and everything is set to internal relay in O365. I have attached corresponding screenshots.

Unfortunately, the problem still persists.

Greetz

Alex

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-04-24*

Hi @Alex GER_146  ,

According to your description, I know that there are two main issues in your environment:

-  O365 mailboxes cannot display in on-premise server. To help you better, may I ask whether the O365 mailboxes are directly created in Exchange Online or moved to Exchange online? If they are directly created in Exchange online, it's a normal behavior that they didn’t display in EAC of on-premise server.

-  Mail flow issue: the mails cannot be sent from on-premises to O365.  What error you get when sending the emails? Could you please provide the NDR information? Generally, when we run the HCW step by step, it would show two pages, one is Receive Connector Configuration which allow you to select the Exchange server to receive emails from Microsoft 365, and another one is the Send Connector page would allow you to select the Exchange server to send emails to Exchange Online. Please double check if you have changed these connectors. And if possible, you could also re-run the HCW to reload and see if the issue can be resolved.

If you have any questions, please feel free to contact me.
