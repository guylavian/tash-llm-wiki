---
title: "Kerberos change password faild after Windows update KB5008380 (CVE-2021-42287)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/660189/kerberos-change-password-faild-after-windows-updat
question_id: 660189
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups"]
---
# Kerberos change password faild after Windows update KB5008380 (CVE-2021-42287)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/660189/kerberos-change-password-faild-after-windows-updat (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

As the Windows updates KB5008380 described, Authentication updates (CVE-2021-42287) is involved in the update.    

After updating  KB5008380 on the  domain controller with setting the  registry key PacRequestorEnforcement to 2,  all the password changing operations on any computers within the Active Directory will failed with the  KDC_ERR_TGT_REVOKED(20)  error!But before updating KB5008380, the password of the computer can be changed successfully.    

    

In my application programe with C language, I always call the krb5_set_password API method in MIT krb5-1.19 opensource library as RFC 4120, this Kerberos password protocol is also specified in RFC 3244.    

My questions are:    

-  why does this happend after updating  KB5008380 on the domain controller?    

-  Is any fileds in the krb5_set_password caller  or other kerberos API caller MUST be specified after the KB5008380 update in my programe? Also means that they may not be necessory before KB5008380.    

-  Is any newly changes introduced to the [MS-PAC] or [MS-KILE] or other microsoft specification documents about this issue？    

Thanks.

## Answers

_No answers on this thread._
