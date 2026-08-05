---
title: "Microsoft Exchange self signed cert missing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/308306/microsoft-exchange-self-signed-cert-missing
question_id: 308306
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Microsoft Exchange self signed cert missing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/308306/microsoft-exchange-self-signed-cert-missing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I noticed in the event viewer that there was an error related to a certificate.   

Microsoft Exchange could not find a certificate that contains the domain name SERVERNAME.domainname.com in the personal store on the local computer. Therefore, it is unable to support the STARTTLS SMTP verb for the connector Default SERVERNAME with a FQDN parameter of SERVERNAME.domainname.com. If the connector's FQDN is not specified, the computer's FQDN is used. Verify the connector configuration and the installed certificates to make sure that there is a certificate with a domain name for that FQDN. If this certificate exists, run Enable-ExchangeCertificate -Services SMTP to make sure that the Microsoft Exchange Transport service has access to the certificate key.  

After checking the certificates, I noticed that the "Microsoft Exchange" Self Signed cert is missing from the list of certificates. I checked all the other servers and they all have that cert so the issue is only on the one server. Does anyone know how I can recreate that certificate so I can fix this error?  

Thanks,  

Gavin

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-10*

So I am trying to add it using Exchange powershell as I can't seem to get the correct names when using ECP, adds abunch of other names to the cert that I dont want. So when trying to open PS, I get this error;

New-PSSession : [servername.domainname.com] Connecting to remote server servername.domainname.com failed with the following error message :  

[ClientAccessServer=SERVERNAME,BackEndServer=servername.domainname.com,RequestId=802d0eac-210b-4738-9549-704ef08548d2,TimeStamp=3/10/2021 4:24:51 PM]  

[FailureCategory=Cafe-SendFailure] For more information, see the about_Remote_Troubleshooting Help topic.  

At line:1 char:1  

-  New-PSSession -ConnectionURI "$connectionUri" -ConfigurationName Microsoft.Excha ...  

-  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

-  CategoryInfo : OpenError: (System.Manageme....RemoteRunspace:RemoteRunspace) [New-PSSession], PSRemotingTransportException  

-  FullyQualifiedErrorId : -2144108477,PSSessionOpenFailed

Any ideas on what is causing this?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-10*

You can create it in EAC:    

https://learn.microsoft.com/en-us/exchange/architecture/client-access/create-self-signed-certificates?view=exchserver-2019    

For the domain, use the server's FQDN and its Netbios name    

so:    

ServerName    

and    

SERVERNAME.domainname.com    

Then ensure its bound to the backend website on the Exchange Server. you can do that from my blog: ( Or what cert is assigned to that now?)    

https://ehloergosum.com/2020/01/25/renewing-that-pesky-microsoft-exchange-certificate/
