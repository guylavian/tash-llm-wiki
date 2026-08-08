---
title: "Exchange 2013 Hybrid with Split Roles"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/391253/exchange-2013-hybrid-with-split-roles
question_id: 391253
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2013 Hybrid with Split Roles

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/391253/exchange-2013-hybrid-with-split-roles (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am working on configuring Exchange 2013 Hybrid and I am running into issues sending mail from o365 to Exchange on Prem.  I am wondering if there is an issue with my setup or a possible firewall issue.   

We are running AZ AD Sync  

Our perimeter has 3 Cisco Ironport Servers which handle the incoming internet traffic.   

4 - Client Access Servers (DMZ - Front End is a Citrix ADC)  

4 - Mailbox Servers (LAN ONLY)  

I setup o365 to point to 1 of the Client Access Servers and to all 4 of mailbox servers.  The Wizard appears to setup properly and I can migrate accounts to o365 and open mailboxes.  I am also able to add accounts to clients.  However, when trying to send an internal e-mail from o365 to an on prem account, the message is queued for 24 hours then bounces saying deliverable.   

-  Is this most likely a firewall issue?  

-  Any issues with the split role and the mailboxes being LAN only?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-12*

Hi @Joe Computers   ,  

Is it normal for the mailbox in Exchange Online to send mail to external senders? Is it normal for send email from on-premises Exchange server to Exchange online?

1.According to the information, we need to consider the impact of firewalls. As Andy said, please check the ports, URLs and IPs required for Exchange online. And check whether there is a record of blocking these URLs and IPs communication on the firewall.

2I noted that "message in queued for 24 hours then bounces saying deliverable", is there an NDR generated? Please check the message trace in Exchange online admin center and see if there any error message in message trace report.  

In addition, for Client Access Server, Microsoft does not support placing the CAS server in the DMZ zone, and they must be deployed within your internal Active Directory environment.  

Please refer to: Client Access server

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-05-11*

Yea, that smells like a firewall issue.     

I'd ensure the servers can connect outbound on port 25 to Exchange Online IPs    

https://learn.microsoft.com/en-us/microsoft-365/enterprise/urls-and-ip-address-ranges?view=o365-worldwide#exchange-online
