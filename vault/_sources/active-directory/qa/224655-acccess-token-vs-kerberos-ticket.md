---
title: "Acccess token vs kerberos ticket"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/224655/acccess-token-vs-kerberos-ticket
question_id: 224655
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_roles: ["Microsoft Moderator"]
---
# Acccess token vs kerberos ticket

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/224655/acccess-token-vs-kerberos-ticket (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

How access token is different from Kerberos ticket? Is there any difference between them? How are they related in terms of its usage and scope? Please explain both with examples. How, where and in which order they are used?  

Thanks in advance!

## Answer (community) — community member

*upvotes: 1 · updated: 2021-01-11*

Hello,    

Thank you so much for posting here.    

Kerberos Tickets    

The main component of Kerberos authentication is the ticket. The Kerberos messages are used to request and deliver tickets. There are two types of tickets used in Kerberos authentication, TGTs and service tickets.    

    

Below is Domain Logon Example:    

If the user is a member of a domain, then the account database is on a domain controller. If you are logging on to one of the domain controllers for the domain you belong to, then the process it the same as for local logon. If instead you are logging on to a member server or a domain controller of another domain, then Kerberos authentication will used if possible.    

Users never directly access the system. The system impersonates the user and accesses resources based on the resource permissions granted to the user. This is a standard security feature of all versions of Windows NT, Windows 2000, and Windows Server 2003. The user logging on to a workstation never directly accesses even local resources. The local system impersonates the user just as a remote system would.    

Because the local system relies on impersonation, the user who logs on to the domain must be authenticated as a valid local user. The only new component added to the domain logon process is Kerberos authentication prior to building an access token.    

The authentication process for a domain user to access their computer is very similar to the process used to authenticate access to network resources—that is, the user must obtain a valid ticket for the local workstation.    

The Kerberos client requests and then receives a TGT from the KDC.    

The Kerberos client uses the TGT to request and then receive a service ticket for the local workstation from the KDC.    

The service ticket for a network resource would be encrypted with the system or service key depending on whether the resource is a system or service. The workstation has a system key created when the computer joined the domain. The service ticket for the workstation is encrypted with this key.    

The local LSA builds an access token from the credentials contained in the service ticket and then grants or denies the user access.    

For more detailed information, we could refer to:    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc772815(v=ws.10)#w2k3tr_kerb_how_krud    

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-01-11*

Hi,    

you meant to say that Service ticket generate by KDC and access token refers to the same thing. If not, how they are both used?    

The Kerberos ticket has a extension named the Privileged Attribute Certificate (PAC)  that contains useful information about a user’s privileges.  including group membership data for authorization.    

This information is added to Kerberos tickets by a domain controller when a user authenticates within an Active Directory domain.  When users use their Kerberos tickets to authenticate to other systems, the PAC can be read and used to determine their level of privileges without reaching out to the domain controller to query for that information.    

So the access token is included in the PAC.    

You can refer to following link to get more details about the PAC :    

a00d0b83-97e3-44ad-ba2d-1221d4f51a35    

https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-apds/1d1f2b0c-8e8a-4d2a-8665-508d04976f84    

----------    

Please Don't forget to mark helpful reply as answer

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-01-10*

Hi,    

The kerberos is the default authentication protocol since Windows 2000  , it works on the basis of tickets.    

When a user try to access a service on a server, the user gives the TGT to the TGS part of the KDC which then authenticates the TGT and generates a session key and service ticket for both the user and server to use. The KDC copies all of the SIDs that are part of the contents of the TGT’s authorization data field to the service ticket’s authorization data field. This service ticket contains the user’s access token.    

The following links can help you to get more details:    

access-tokens    

kerberos-authentication-overview    

kerberos-authentication-explained    

----------    

Please don't forget to mark helpful reply as answer if it help you to fix your issue
