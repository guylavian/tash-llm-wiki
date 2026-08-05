---
title: "Exchange mailflow mystery"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/151739/exchange-mailflow-mystery
question_id: 151739
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange mailflow mystery

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/151739/exchange-mailflow-mystery (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have just added an Exchange 2016 machine to our setup, previously we had a single Exchange 2013 server. Our on prem Exchange is only used as a transport server, passing email from systems to Office 365 , all mailboxes are Exchange online, there is not a single mailbox on the on prem servers.   

The only other use of the on prem Exchange setup is for scan to email from our Konica MFDs. These are all able to scan to any address if they are set to send via the old server, the MFDs use IP address for SMTP. However, if I set them to use the new server I can only scan to internal email addresses, scanning to external fails, the only change required to point them to a different SMTP server is changing the IP address so it is not an issue on the actual devices.  

I created identical receive connectors on the the new server, the same config used on the old server, apart from FQDN presented by the connector and the IP address it is listening on the connectors are exactly the same.  

None of the MFDs have an Exchange mailbox, the receive connectors allow anonymous users and do not require TLS or any other authentication yet the MFDs fail with a logon error when trying to send to external addresses.  

Has anyone ever seen this, and if so what am I missing? We need to be able to scan to external email because we have a subsidiary company based at our corporate office who use a different email domain owned by them so their email addresses are seen as external

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2020-11-04*

Hey there. You probably need to allow anonymous relay on the application receive connector used for the MFDs.    

Important!    

Ensure there is a dedicated receive connector just for these MFDs - with the remote addresses scoped to just those IPs of those devices! Otherwise this connector can be used by anyone to relay    

https://learn.microsoft.com/en-us/exchange/mail-flow/connectors/allow-anonymous-relay?view=exchserver-2019#step-1-create-a-dedicated-receive-connector-for-anonymous-relay    

Also:     

https://practical365.com/exchange-server/exchange-2016-smtp-relay-connector/    

Start with the section:    

External SMTP Relay with Exchange Server 2016 Using Anonymous Connections    

Its very important that the rec connector is scoped to just those IPs allowed to relay anonymously!!!!!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-05*

Problem has been solved. the connector has been deleted and recreated, it now works

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-05*

Anonymous is already listed in the connector, as I said this is an exact copy  of the configuration of the previously existing connector on the old server which works and it only fails when sending to external addresses. If anonymous was not listed it would fail for any recipient address not just external  

To show this, here is the output I got from the Get-ADPermission command listed above  

User                         ExtendedRights  

NT AUTHORITY\ANONYMOUS LOGON {ms-Exch-SMTP-Accept-Authoritative-Domain-Sender}  

NT AUTHORITY\ANONYMOUS LOGON {ms-Exch-SMTP-Accept-Any-Sender}  

NT AUTHORITY\ANONYMOUS LOGON {ms-Exch-SMTP-Submit}  

NT AUTHORITY\ANONYMOUS LOGON {ms-Exch-SMTP-Accept-Any-Recipient}  

NT AUTHORITY\ANONYMOUS LOGON {ms-Exch-Accept-Headers-Routing}  

NT AUTHORITY\ANONYMOUS LOGON {ms-Exch-SMTP-Accept-Authoritative-Domain-Sender}  

NT AUTHORITY\ANONYMOUS LOGON {ms-Exch-SMTP-Accept-Any-Sender}  

NT AUTHORITY\ANONYMOUS LOGON {ms-Exch-SMTP-Submit}  

NT AUTHORITY\ANONYMOUS LOGON {ms-Exch-Accept-Headers-Routing}

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-05*

Hi @Gareth Davies  ,    

I created identical receive connectors on the the new server, the same config used on the old server, apart from FQDN presented by the connector and the IP address it is listening on the connectors are exactly the same.    

Have you configured the permissions for anonymous relay on the receive connector?     

To verify the permissions, you may running the command below:    

```
Get-ADPermission  -User "NT AUTHORITY\ANONYMOUS LOGON" | where {($_.Deny -eq $false) -and ($_.IsInherited -eq $false)} | Format-Table User,ExtendedRights
```

If "MS-Exch-SMTP-Accept-Any-Recipient" is not listed in the output, you can run the following command to add the permission:    

```
Get-ReceiveConnector  | Add-ADPermission -User "NT AUTHORITY\ANONYMOUS LOGON" -ExtendedRights "Ms-Exch-SMTP-Accept-Any-Recipient"
```

Andy has shared two great links about anonymous relay, hopefully you can find them useful.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2020-11-04*

https://answers.microsoft.com/en-us/msoffice/forum/msoffice_outlook/office-365-email-mystery/53314ed4-b527-436f-9b80-5a7bafd646fb  

I hope it will help
