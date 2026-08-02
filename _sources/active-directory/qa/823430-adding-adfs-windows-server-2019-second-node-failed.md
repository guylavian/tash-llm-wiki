---
title: "Adding ADFS Windows server 2019 second node failed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/823430/adding-adfs-windows-server-2019-second-node-failed
question_id: 823430
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Adding ADFS Windows server 2019 second node failed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/823430/adding-adfs-windows-server-2019-second-node-failed (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

we have already ADFS 2019 farm with two servers, suddenly ADFS service stopped on the second node. So, after troubleshooting, we decided to remove the role from the second node and delete the internal DB .  

So, when trying to add the ADFS role again on the same server we received errors:  

-  There was no SPNs set on the service account   

-  SOAP security negotiation for with http://servername/adfs/services/policystoretransfer   

-  value account be null  

-  unable to retrieve group managed service account information   

-  unable to determine the service SPN . there were no SPNs set on the following service account   

-  unbale to determine the current behavior level. SOAP security negotiation   

-  unable to retrieve configuration from the primary servers   

tried the following :  

-  verify MSA was registered SPN (host\fs.domain name)  

-  registred SPN again, the result was duplicated -Setspn - s host/FQDN service account and Setspn - s host/server name serviceaccount   

-  port 80 and 443 opened / no firewall between servers   

-  domain controller reached and DNS resolved successfully   

-  verify that the computer account listed under allowed to retrieve managed password by using Get-ADserviceaccount   

-  try to add new server to the ADFS farm but with the same error

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-27*

Hello  

Thank you for your question and reaching out.  

I can understand you are not able to add another Node in ADFS.  

You could try below steps to resolve the issue.  

-   Change Logon Domain controller do Different DC as below command.  

nltest /SC_RESET:mydomain.com\srv001  

-  Please try to create new ADFS server with New Name as it may happened due stale or Orphne records of Old ADFS server in the AD.  

-   Disable any Antivirus program or Windows firewall you may have for temporary purpose.  

-  Please verify AD health is Good and DATE and Time are synced your Domain controller.  

--If the reply is helpful, please Upvote and Accept as answer--
