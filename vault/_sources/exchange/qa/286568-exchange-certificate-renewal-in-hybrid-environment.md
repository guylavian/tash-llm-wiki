---
title: "Exchange certificate renewal-in hybrid environment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/286568/exchange-certificate-renewal-in-hybrid-environment
question_id: 286568
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange certificate renewal-in hybrid environment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/286568/exchange-certificate-renewal-in-hybrid-environment (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

if I change on-premises Exchange 2013  3rd party  certificate  and than re-run HCW to attach this new certificate in hybrid enviroment does HCW only change this certificate information or does it change the whole configuration.    

Im asking this because I have on premises send connector to O 365 disabled.I dont know why,but does re-running HCW change this connector to enabled or does it change only new certificate information?

## Answer (community) — community member

*upvotes: 1 · updated: 2021-02-25*

Hi @Andy   ,    

For HCW, renew certificate does not need to re-run the HCW. If you planning to use the certificate for the SMTP service and select the new certificate, then I suggest you re-run the HCW.    

After you renew the certificate, you could run the commands provide by Andy to set the certificate bound to the sender connector. Then you could send test email to test the mail flow.    

According to check the sender connector in my Exchange hybrid environment. Then send connector to Office 365 is enabled by default. If you need to run HCW, it is recommended that you run the following command line to view the existing HCW settings.    

```
Get-HybridConfiguration
```

        

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-08-31*

If Cert Issuer and Subject is same then only import new certificate and remove old cerificate will work?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-02-24*

Note you could just replace the cert, assign SMTP to it and manually update the connectors. Its not required to run the Wizard.  

Thank you for advice.  

I thought to do only this without HCW.
