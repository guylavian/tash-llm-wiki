---
title: "Unable to add 2022 or 2016 to 2012 r2 adfs farm"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1371653/unable-to-add-2022-or-2016-to-2012-r2-adfs-farm
question_id: 1371653
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Unable to add 2022 or 2016 to 2012 r2 adfs farm

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1371653/unable-to-add-2022-or-2016-to-2012-r2-adfs-farm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Production environment uses two 2012 r2 adfs farm with sql backend. 

ADFS rapid restore tool was used to backup the adfs and was restored in a new 2012 r2 server with WID option. 

Was able to add another 2012 r2 server into the farm as secondary of the newly restored 2012 r2 with WID. 

However, not able to add 2016 or 2022 to this new parallel farm. Pre-requisite tests fail with following. 

" Unable to determine the current Farm Behavior Level. SOAP security negotiation with 'http://server1.contoso.com/adfs/servcies/policystoretransfer' for target 'http://server1.contoso.com/adfs/services/policystoretransfer' failed "

Following has been verified:

-  spn is set up correctly on the service account (parallel 2012 r2 farm uses the same service account).

-  there are no duplicates spn

-  supported kerberos encryption types in the adfs servers, domain contollers (msds-SupportedEncryptionTypes) are set to use  RC4_HMAC_MD5, AES128_HMAC_SHA1, and AES256_HMAC_SHA1. 

-  no firewall in between and windows firewall turned off

-  This account supports Kerberos AES 256 bit encryption (and 128 bit) have been enabled for through the account tab of the service account in active directory

Not finding much info on "unable to determine the current Farm Behavior Level" error in MS site. 

Any help is greatly appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-20*

This was related to a duplicate spn assigned to the adfs server object in top level domain. 

The error received during the pre-requisites check was misleading. Running the diagnostics as outlined in the link below pointed to a possible SPN issue.

https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/troubleshooting/ad-fs-diagnostics-analyzer

There are three domains in the environment - contoso.com is the top level, domainA.contoso.com and domainB.contoso.com are the child domains. The adfs servers are located in the top level domain whereas the service account is located in the domainA.contoso.com. 

When duplicate SPNs were checked through the generic command "setspn -X" it was run from the domainA.contoso.com and didn't find any duplicates. That misled us to believe no duplicates existed. 

After the diagnostics pointed to a possible duplicate, ran the following command for every domain 

setspn -T * -T contoso.com -X

setspn -T * -T domainA.contoso.com -X

setspn -T * -T domainB.contoso.com -X

Sure enough, one of the adfs servers had host/sso.contoso.com SPN assigned to it. Once that was removed 2022 server was able to join the 2012 r2 farm.
