---
title: "Active Directory - Delegation- FSMO role transfert"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/359154/active-directory-delegation-fsmo-role-transfert
question_id: 359154
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory - Delegation- FSMO role transfert

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/359154/active-directory-delegation-fsmo-role-transfert (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I was wondering if it was "supported" by Microsoft to delegate the permission to transfert FSMO roles using ADSI permission.  

By design, only Domain Admins (or other) are able to transfert FSMO roles between domain controllers. However, technical admins which have to operate on domain controller operating system might need to transfert roles before maintaining (patching, rebooting...).  

I've not a big fan of giving full admin privileges on an application just because a technical administrator need to make a service transfert (it's definitively against least privileges way of life).  

I've found in ADSI some permissions which allow role transfer (by e.g, on CN=RID Master$). If I had permission on these (using ad group), will I have to prepare myself for "unforeseen consequences"?  

Thank you for your feedback,  

Sincerely,  

Charles

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 1 · updated: 2021-04-20*

Hello @Charles Gerard - Le Metayer  ,

I am sorry for the late reply.

I have test in my lab. I give one domain user (a\lin)change PDC permission, then she can change PDC via UI.

1.I have two DCs 2019standard.a.com and additionalDC.a.com.  

2.I give A\lin change PDC permission as below.  

3.Before giving permission, lin can not change PDC via UI.  

4.After giving permission, lin can change PDC via UI.  

5.The FSMO role holders are all 2019standard before changing them.

Schema master 2019standard.a.com  

Domain naming master 2019standard.a.com  

PDC 2019standard.a.com  

RID pool manager 2019standard.a.com  

Infrastructure master 2019standard.a.com

6.The PDC role holder is additionalDC after changing PDC.  

Schema master 2019standard.a.com  

Domain naming master 2019standard.a.com  

PDC additionalDC.a.com  

RID pool manager 2019standard.a.com  

Infrastructure master 2019standard.a.com

Hope the information above is helpful.

Should you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-22*

Hello @Charles Gerard - Le Metayer  ,    

Thank you for your update.    

Based on my experience, Microsoft should not recommend this, but now the function of delegation can be implemented in the experiment. If you think it will not cause security problems, and you must do this, then you can do it.     

Tip: Once you do not need to delegate this function, it is recommended to cancel the delegation as soon as possible.     

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-21*

Hello,  

Indeed, I was aware about this this delegation. :)  

As explained, you can delegate all FSMO management from ADSI. But yes, you can delegate only PDC management from AD console.  

Again =D  

CN=Partitions,CN=Configuration --> Permission Change Domain Master (object only)  

CN=Schema,CN=Configuration --> Permission Change Schema Master (object only)  

Default Naming Context (domain) --> Permission Change PDC (object only)  

CN=Infrastructure --> Permission Change Infrastructure Master (object only)  

CN=RID Manager$,CN=System --> Change RID Master (object only)  

Does microsoft support these delegations?  

Thanks!  

Sincerely

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-16*

Hello @Charles Gerard - Le Metayer  ,    

Thank you for posting here.    

From the following official document, we can see:    

The signed-in user should be a member of the Enterprise Administrators group to transfer Schema master or Domain naming master roles, or a member of the Domain Administrators group of the domain where the PDC emulator, RID master and the Infrastructure master roles are being transferred.    

So member in the Enterprise Administrators group can transfer Schema master or Domain naming master roles, and member in the Domain Administrators group can transfer PDC emulator, RID master and the Infrastructure master roles.    

And as I understand you can not give the least privileges to one user to let him/her transfer the FSMO roles.    

For more infroamtion we can refer to link below.    

Transfer or seize FSMO roles in Active Directory Domain Services    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/transfer-or-seize-fsmo-roles-in-ad-ds    

Hope the information above is helpful.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou
