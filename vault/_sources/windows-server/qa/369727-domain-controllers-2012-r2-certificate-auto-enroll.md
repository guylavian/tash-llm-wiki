---
title: "Domain Controllers 2012 R2 certificate auto enrolled"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/369727/domain-controllers-2012-r2-certificate-auto-enroll
question_id: 369727
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Domain Controllers 2012 R2 certificate auto enrolled

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/369727/domain-controllers-2012-r2-certificate-auto-enroll (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I have some trouble understanding how DC is renewing its machine certificate.  

In my environment:  

-  DCs 2021 R2  

-  2 root CA servers (not on DCs): 1 that we are going to decommission and 1 new  

-  No GPO for DC certificate auto enrollement  

The DCs had their certificates issued by the old CA (not expired yet). I want to renew them on the new CA.  

I added the Domain Controller template on the new CA. After restarting one of the DC following windows updates, I noticed the the DC took automatically a new certificate from the new CA.  

I restarted the 2nd DC, it did not.  

Note: both CA have the Domain Controller template.  

My questions:  

-  how come DC2 renewed its certificate from the new CA?  

-  If i remove the Domain Controller template from the old CA, and reboot DC1, will it auto renew its certificate issued by the new CA?  

Thank you!  

Chris

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-27*

Hi,    

If you want to decommission a Windows enterprise certification authority you can refer to the following link:    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/decommission-enterprise-certification-authority-and-remove-objects    

Then use the new CA to issue certs for the domain members.    

Best Regards,

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-26*

The plan is only to decommission the old CA, so I had to change the issuer CA for the DCs certificates, as they were the last the be issued by the old CA.  

I manually changed the other DC certificate (simply did a request new certificate, Domain Controller templates, from mmc.exe)  

I have now a lot of SChannel errors :(. "A fatal alert was received from the remote endpoint. The TLS protocol defined fatal alert code is 46." which is when the certificate is unknown, from user "SYSTEM".  

I definitly miss something, but I don't know what...  

Actually, I was hired recently in this company, and the CA changes was started by the previous person.

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2021-04-26*

I only have the DC certificates still issued by the old Root CA.

what is the purpose of your PKI? Do you ever need it? If there is nothing you use from PKI, you may consider to decommission all PKI services.

Is it hard-coded on the DC to request a certificate if missing?

yes, it is hardcoded in DC code.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-26*

Hello,  

Thank you for your quick response FanFan :).  

Actually, I'm switching from a domain-joined Enterprise Root CA (the old Root CA), to, issuing the DC certificate on a Enterprise Intermediate CA (New CA). Sorry, I thought the new CA was a root also.  

I only have the DC certificates still issued by the old Root CA.  

There is no GPO configured to auto-enrolled DC certificate. Is it hard-coded on the DC to request a certificate if missing? if so I just need to delete the existing certificate on the DC, have the DC template only on the new intermediate CA, and restart the DC?  

Thank you.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-26*

Hi,  

Before going further, would you please tell the Root CA is domain joined server or standalone server?  

The 2 servers are different CA, not a migration, right?  

If it is the Enterprise Root CA, the Root CA certificate will be published on the DCs and clients automatically. So, your DC2 gets the new CA certificate automatically.  

Your DC1 and clients will get the new CA certificate too.  

Make sure the DCs are health and replication between DCs works well.  

But other certificates issued by the New Root CA will not enroll automatically unless you configure the policy manually.  

The certificates issued by the old CA will not be renewed if the old CA was removed.  

Best Regards,
