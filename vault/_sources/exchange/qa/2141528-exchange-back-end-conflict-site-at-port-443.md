---
title: "Exchange Back End conflict site at port 443"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2141528/exchange-back-end-conflict-site-at-port-443
question_id: 2141528
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Exchange Back End conflict site at port 443

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2141528/exchange-back-end-conflict-site-at-port-443 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All, We have a strange issue. In one of the exchange server 2019 the back end site in IIS is not getting started. It give error website cannot be started another website might be using same port. I observed there are three sites at port 81, 444, and 443 respectively. Not sure why port 443 is here. If we change the port of 443 to something different OWA stops.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-01-08*

Hi @ Vishal Verma ，

Thanks for posting your question in the Microsoft Q&A forum.

According to your description, The backend site in IIS of your Exchange Server 2019 cannot be started, and it prompts "Website cannot be started". Another website may be using the same port. I agree with Andy David - MVP that the self-signed certificate of Microsoft Exchange is generally bound to the Exchange backend website on port 444. You can try the following steps:

-  Get the thumbprint value through the command.

```
Get-ExchangeCertificate | Where-Object {$_.FriendlyName -like "Microsoft Exchange"} | Format-List FriendlyName,Subject,CertificateDomains,Thumbprint,RootCAType,*PrivateKey*,NotBefore,NotAfter
```

-  Create a new Microsoft Exchange certificate through the command.

```
Get-ExchangeCertificate -Thumbprint "thumbprint" | New-ExchangeCertificate -Force -PrivateKeyExportable $false
```

-  Copy the new Microsoft Exchange certificate from the personal store to the trusted root certificate authority store; assign the IIS service to the certificate.

-  Delete the old certificate and run the IISReset command to restart IIS.

-  Open IIS Manager, select the default site, and then click "Bindings" on the right.Check the site bound to port 443.

-  Press Win+R, type "services.msc" to check if the World Wide Web Publishing Service is running.

If you have any questions, please feel free to contact me. If the answer is helpful, please click "Accept Answer" because it can help other members of the Microsoft Q&A community who have encountered similar problems and are looking for solutions. Thank you.

Best,

Jeanne

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-01-08*

Someone added that 443 on the backend and they should not have.

444 is the back end port.

You can see how its supposed to look here:

https://www.alitajran.com/renew-microsoft-exchange-certificate/

Essentially, you need to set it to 444 and assign IIS and then bind the Microsoft Exchange Cert to the 444, not the 443.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-01-07*

There should be no 443 on the back end.

just 81 and 444.

Bind the Microsoft ExchangeCertificate to 444 on the backed and run IISRESET.

443 should be removed.

WHat is set for the front end?

Note: https://learn.microsoft.com/en-us/exchange/troubleshoot/client-connectivity/owa-ecp-ems-cannot-connect-after-self-signed-certificate-removed
