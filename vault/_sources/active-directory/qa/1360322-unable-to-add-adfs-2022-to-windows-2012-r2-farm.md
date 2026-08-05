---
title: "Unable to add adfs 2022 to windows 2012 R2 farm"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1360322/unable-to-add-adfs-2022-to-windows-2012-r2-farm
question_id: 1360322
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# Unable to add adfs 2022 to windows 2012 R2 farm

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1360322/unable-to-add-adfs-2022-to-windows-2012-r2-farm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Domain Structure --> root contoso, child domains : domain1.contoso.com & domain2.contoso.com

Current 2012 r2 adfs servers located in contoso.com but use service account from domain1.contoso.com. 

Current production deployment uses SQL backend. 

The service account has spn https://sso.contoso.com and http://sso.contoso.com

ADFS rapid restore tool was used to back up the current ADFS farm on windows 2012 R2. Then on a new 2012 R2 server (server3) created in contoso.com top domain, it was restored using WID option. Verified that the ADFS SSO worked in the new server by pointing the local host file  for sso.contoso.com to the new server after the restore.  

However, when joining 2022 server to this new 2012 server it fails the pre-requisite checks. Error cited are

SOAP security negotiation with 'http://server3.contoso.com/adfs/services/policystoretransfer' for target 'http://server3.contoso.com/adfs/services/policystoretransfer' failed. 

Unable to determine the current Farm Behavior Level. SOAP security negotiation with 'http://server3.contoso.com/adfs/services/policystoretransfer'  for target 'http://server3.contoso.com/adfs/services/policystoretransfer'  failed. 

Server3 (new restored 2012 r2) has the same  msDS-SupportedEncryptionTypes as the 2012 r2 server in production and also the 2022 server that is unable to join to it. Adding RC4_HMAC_MD5 and other AES related options through security settings --> security options --> Network security: Configure encryption types allowed for kerberos, both in newly restored 2012 r2 and windows 2022 server didn't work .

Windows firewall is turned off on all the machines. 

Any help is appreciated.

@Pierre Audonnet - MSFT

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-20*

@Pierre Audonnet - MSFT  

Pierre, 

It was a case of SPN as hinted by you. But the errors from the pre-requisite checks didn't have any information pertaining to that. MS and other articles mentioned that the kerberos error that was seen in the logs could be ignored. 

The issue was due to a duplicate spn assigned to the adfs server object in top level domain. 

The error received during the pre-requisites check was misleading. Running the diagnostics as outlined in the link below pointed to a possible SPN issue.

https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/troubleshooting/ad-fs-diagnostics-analyzer

There are three domains in the environment - contoso.com is the top level, domainA.contoso.com and domainB.contoso.com are the child domains. The adfs servers are located in the top level domain whereas the service account is located in the domainA.contoso.com. 

When duplicate SPNs were checked through the generic command "setspn -X" it was run from the domainA.contoso.com and didn't find any duplicates. That misled us to believe no duplicates existed. 

After the diagnostics pointed to a possible duplicate, ran the following command for every domain 

setspn -T * -T contoso.com -X

setspn -T * -T domainA.contoso.com -X

setspn -T * -T domainB.contoso.com -X

Sure enough, one of the adfs servers had host/sso.contoso.com SPN assigned to it. Once that was removed 2022 server was able to join the 2012 r2 farm.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-20*

..........

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-09-08*

Did you try to enable the two Kerberos options on the account tab of the account being used for our ADFS service?
