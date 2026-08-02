---
title: "Domain Controller Replication Issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/816087/domain-controller-replication-issue
question_id: 816087
fetched: 2026-07-25
answer_count: 11
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Domain Controller Replication Issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/816087/domain-controller-replication-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

i have two Domain Controllers one DC - Win2019 and Second is BDC - Windows 2012 R2    

DC - win2019 is Primary and BDC - win 2012 R2 is the Backup Domain Conroller    

my Problem is that I got this error :- DCdiag.exe  - on DC win2019    

```
From BDC to DC   

        Naming Context: DC=DomainDnsZones,DC=domainnamehere,DC=com   

        The replication generated an error (8606):   

        Insufficient attributes were given to create an object. This object may not exist because it may have been deleted and already garbage collected.  

  The failure occurred at 2022-04-18 11:22:54.   

        The last success occurred at 2022-03-20 17:55:39.   

        2712 failures have occurred since the last success.   

     ......................... DC failed test Replications
```

,check the snapshot below    

and how to fix it?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-19*

@Anonymous       

no it's working all the time ,but I don't know what is the issue and how to fix it?    

i want the replication works ,or do I have to drop this Domain Controller BDC and recreate new one,or what do u think?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-04-18*

What's the history here? Has the domain controller been disconnected for some time?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-18*

i have seen this article of microsoft before but I didn't understand what to delete,I'll read it again and see what I can do

here is the result when run command :

C:\Windows\system32>repadmin /showattr dc dc=domainnamehere,dc=com  

DN: DC=domainnamehere,DC=com  

3> objectClass: top; domain; domainDNS  

1> distinguishedName: DC=domainnamehere,DC=com  

1> instanceType: 0x5 = ( IS_NC_HEAD | WRITE )  

1> whenCreated: 24/01/2014 10:00:19 PM Egypt Standard Time  

1> whenChanged: 22/03/2022 8:54:32 PM Egypt Standard Time  

3> subRefs: DC=ForestDnsZones,DC=domainnamehere,DC=com; DC=DomainDnsZones,DC=domainnamehere,DC=com; CN=Configuration,DC=domainnamehere,DC=com  

1> uSNCreated: 13080  

1> dSASignature: { V1: Flags = 0x0; LatencySecs = 0; DsaGuid = 6d8b2a09-41ef-4455-9bca-22806d3fec0c }  

1> repsTo: dwVersion: 2 v1.cb: 484 v1.cConsecutive Failures: 0 v1.timeLastSuccess: 13294759937 v1.timeLastAttempt: 13294759937 v1.ulResultLastAttempt: 0 v1.cbOtherDraOffset: 216v1.cbOtherDra: 268v1.ulReplicaFlags: 16 v1.rtSchedule: <skipped> v1.usnvec.usnHighObjUpdate: 0 v1.usnvec.usnHighPropUpdate: 0 v1.pszUuidDsaObj: bf9cd30e-487b-403e-a1aa-a6af280106d9 v1.pszUuidInvocId: 00000000-0000-0000-0000-000000000000 v1.pszUuidTransportObj: 00000000-0000-0000-0000-000000000000 v1.cbPASDataOffset: 0 v1~PasData: (none) v2~pdsa_rpc_inst v2.pszDSIServer bf9cd30e-487b-403e-a1aa-a6af280106d9._msdcs.domainnamehere.com v2.pszDSIAnnotation (null) v2.pszDSIInstance bf9cd30e-487b-403e-a1aa-a6af280106d9._msdcs.domainnamehere.com v2.pguidDSIInstance (null)  

1> repsFrom: dwVersion: 2 v1.cb: 484 v1.cConsecutive Failures: 0 v1.timeLastSuccess: 13294762062 v1.timeLastAttempt: 13294762062 v1.ulResultLastAttempt: 0 v1.cbOtherDraOffset: 216v1.cbOtherDra: 268v1.ulReplicaFlags: 112 v1.rtSchedule: <skipped> v1.usnvec.usnHighObjUpdate: 5118581 v1.usnvec.usnHighPropUpdate: 5118581 v1.pszUuidDsaObj: bf9cd30e-487b-403e-a1aa-a6af280106d9 v1.pszUuidInvocId: 62d5fbdd-43f1-422d-a33b-c0667a4b3720 v1.pszUuidTransportObj: 00000000-0000-0000-0000-000000000000 v1.cbPASDataOffset: 0 v1~PasData: (none) v2~pdsa_rpc_inst v2.pszDSIServer bf9cd30e-487b-403e-a1aa-a6af280106d9._msdcs.domainnamehere.com v2.pszDSIAnnotation (null) v2.pszDSIInstance bf9cd30e-487b-403e-a1aa-a6af280106d9._msdcs.domainnamehere.com v2.pguidDSIInstance (null)  

1> uSNChanged: 11862167  

1> name: domainnamehere  

1> objectGUID: ff4b77b2-1c31-4e41-a838-5a00aa851692  

1> replUpToDateVector: <176 byte blob>  

1> creationTime: 22/03/2022 8:54:32 PM Egypt Standard Time  

1> forceLogoff: (never)  

1> lockoutDuration: 0:00:30:00  

1> lockOutObservationWindow: 0:00:30:00  

1> lockoutThreshold: 0  

1> maxPwdAge: (never)  

1> minPwdAge: (never)  

1> minPwdLength: 0  

1> modifiedCountAtLastProm: 0  

1> nextRid: 1000  

1> pwdProperties: 0x0 = ( )  

1> pwdHistoryLength: 0  

1> objectSid: S-1-5-21-353254996-3754926767-3490704302  

1> serverState: 1  

1> uASCompat: 1  

1> modifiedCount: 1  

1> auditingPolicy: <2 byte blob>  

1> nTMixedDomain: 0  

1> rIDManagerReference: CN=RID Manager$,CN=System,DC=domainnamehere,DC=com  

1> fSMORoleOwner: CN=NTDS Settings,CN=DC,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=domainnamehere,DC=com  

1> systemFlags: 0x8C000000 = ( DISALLOW_DELETE | DOMAIN_DISALLOW_RENAME | DOMAIN_DISALLOW_MOVE )  

11> wellKnownObjects: B:32:6227F0AF1FC2410D8E3BB10615BB5B0F:CN=NTDS Quotas,DC=domainnamehere,DC=com; B:32:F4BE92A4C777485E878E9421D53087DB:CN=Microsoft,CN=Program Data,DC=domainnamehere,DC=com; B:32:09460C08AE1E4A4EA0F64AEE7DAA1E5A:CN=Program Data,DC=domainnamehere,DC=com; B:32:22B70C67D56E4EFB91E9300FCA3DC1AA:CN=ForeignSecurityPrincipals,DC=domainnamehere,DC=com; B:32:18E2EA80684F11D2B9AA00C04F79F805:CN=Deleted Objects,DC=domainnamehere,DC=com; B:32:2FBAC1870ADE11D297C400C04FD8D5CD:CN=Infrastructure,DC=domainnamehere,DC=com; B:32:AB8153B7768811D1ADED00C04FD8D5CD:CN=LostAndFound,DC=domainnamehere,DC=com; B:32:AB1D30F3768811D1ADED00C04FD8D5CD:CN=System,DC=domainnamehere,DC=com; B:32:A361B2FFFFD211D1AA4B00C04FD7D83A:OU=Domain Controllers,DC=domainnamehere,DC=com; B:32:AA312825768811D1ADED00C04FD8D5CD:CN=Computers,DC=domainnamehere,DC=com; B:32:A9D1CA15768811D1ADED00C04FD8D5CD:CN=Users,DC=domainnamehere,DC=com  

1> objectCategory: CN=Domain-DNS,CN=Schema,CN=Configuration,DC=domainnamehere,DC=com  

1> isCriticalSystemObject: TRUE  

1> gPLink: [LDAP://cn={F259A3EC-1B68-46DB-8754-41747EA64737},cn=policies,cn=system,DC=domainnamehere,DC=com;2][LDAP://cn={7C9BE0F8-0D21-46DF-A361-BC57210961C4},cn=policies,cn=system,DC=domainnamehere,DC=com;0][LDAP://CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=Policies,CN=System,DC=domainnamehere,DC=com;2]  

1> dSCorePropagationData: 0x0 = ( )  

2> otherWellKnownObjects: B:32:683A24E2E8164BD3AF86AC3C2CF3F981:CN=Keys,DC=domainnamehere,DC=com; B:32:1EB93889E40C45DF9F0C64D23BBB6237:CN=Managed Service Accounts,DC=domainnamehere,DC=com  

2> masteredBy: CN=NTDS Settings,CN=BDC,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=domainnamehere,DC=com; CN=NTDS Settings,CN=DC,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=domainnamehere,DC=com  

1> ms-DS-MachineAccountQuota: 10  

1> msDS-Behavior-Version: 3 = ( WIN2008 )  

1> msDS-PerUserTrustQuota: 1  

1> msDS-AllUsersTrustQuota: 1000  

1> msDS-PerUserTrustTombstonesQuota: 10  

2> msDs-masteredBy: CN=NTDS Settings,CN=BDC,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=domainnamehere,DC=com; CN=NTDS Settings,CN=DC,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=domainnamehere,DC=com  

2> msDS-IsDomainFor: CN=NTDS Settings,CN=BDC,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=domainnamehere,DC=com; CN=NTDS Settings,CN=DC,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=domainnamehere,DC=com  

1> msDS-NcType: 0  

1> msDS-ExpirePasswordsOnSmartCardOnlyAccounts: FALSE  

1> dc: domainnamehere

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-04-18*

I'd work through this one.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/replication-error-8606    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
