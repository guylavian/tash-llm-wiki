---
title: "sccm active directory forest publishing status failed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/786390/sccm-active-directory-forest-publishing-status-fai
question_id: 786390
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-other-l1"]
answer_author_roles: ["Q&A User"]
---
# sccm active directory forest publishing status failed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/786390/sccm-active-directory-forest-publishing-status-fai (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,   

Under \Administration\Overview\Hierarchy Configuration\Active Directory Forests  

All of the additional forest are show as failed.  

When I click on tab Publishing Statues it show failed for Site S01 but successful for site S02  

Can someone please let me know what logs I can check to see find out why Site S01 is failing but S02 is OK  

Our Setup  

CAS with 3 Primary Site

## Answer (community) — community member

*upvotes: 0 · updated: 2022-03-29*

Hi,    

Could not connect to the RootDSE container in Active Directory. HRESULT=0x8007052E    

HRESULT=0x8007052E It means that incorrect username or password.    

Could we know if we use a specific account instead of the computer account of the site server when the Active Directory Forest Publishing to untrusted forest?    

We could configure the user account and password and verify the LDAP. For example, LDAP://datacenter.domain.com/CN=System Management,CN=System,DC=datacenter,DC=domain,DC=com    

Tips: Type the complex password in a notepad and then copy and paste it to the password input :)    

If the answer is the right solution, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-03-26*

In the hman log i see these errors.  

Publishing site objects in AD Forest ABCXX.DOmain	SMS_HIERARCHY_MANAGER	3/24/2022 6:47:53 AM	7024 (0x1B70)  

   Publishing account user account ABCXX\UserAccount will be used	SMS_HIERARCHY_MANAGER	3/24/2022 6:47:53 AM	7024 (0x1B70)  

STATMSG: ID=4909 SEV=E LEV=M SOURCE="SMS Server" COMP="SMS_HIERARCHY_MANAGER" SYS=S01PRM.Domain.COM SITE=S01 PID=3908 TID=7024 GMTDATE=Thu Mar 24 06:47:55.813 2022 ISTR0="ABCXX.DOmain" ISTR1="" ISTR2="" ISTR3="" ISTR4="" ISTR5="" ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=0 LE=0X8007052e	SMS_HIERARCHY_MANAGER	3/24/2022 6:47:55 AM	7024 (0x1B70)  

   Could not connect to the RootDSE container in Active Directory. HRESULT=0x8007052E	SMS_HIERARCHY_MANAGER	3/24/2022 6:47:55 AM	7024 (0x1B70)  

Publishing site objects in AD Forest ABBXX.DOmain	SMS_HIERARCHY_MANAGER	3/24/2022 6:47:55 AM	7024 (0x1B70)  

   Publishing account user account ABBXX\UserAccount will be used	SMS_HIERARCHY_MANAGER	3/24/2022 6:47:56 AM	7024 (0x1B70)  

Waiting for Configuration Manager Client Upgrade changes for maximum 14400 seconds...	SMS_HIERARCHY_MANAGER	3/24/2022 6:47:58 AM	7108 (0x1BC4)  

STATMSG: ID=4909 SEV=E LEV=M SOURCE="SMS Server" COMP="SMS_HIERARCHY_MANAGER" SYS=S01PRM.Domain.COM SITE=S01 PID=3908 TID=7024 GMTDATE=Thu Mar 24 06:47:58.453 2022 ISTR0="ABBXX.DOmain" ISTR1="" ISTR2="" ISTR3="" ISTR4="" ISTR5="" ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=0 LE=0X8007052e	SMS_HIERARCHY_MANAGER	3/24/2022 6:47:58 AM	7024 (0x1B70)  

   Could not connect to the RootDSE container in Active Directory. HRESULT=0x8007052E	SMS_HIERARCHY_MANAGER	3/24/2022 6:47:58 AM	7024 (0x1B70)

## Answer (community) — community member

*upvotes: 0 · updated: 2022-03-25*

Hi,    

Sccm active directory forest is mainly about sccm active directory forest discovery, so we could check ADForestDisc.Log, it records Active Directory Forest Discovery actions.    

If the answer is the right solution, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
