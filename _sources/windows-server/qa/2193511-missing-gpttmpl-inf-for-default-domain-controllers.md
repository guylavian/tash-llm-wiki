---
title: "Missing GptTmpl.inf for Default Domain Controllers Policy"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2193511/missing-gpttmpl-inf-for-default-domain-controllers
question_id: 2193511
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
---
# Missing GptTmpl.inf for Default Domain Controllers Policy

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2193511/missing-gpttmpl-inf-for-default-domain-controllers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have been troubleshooting someone's domain for days now and trying to piece it all back together.  The domain has been around since 2005 and is currently at functional levels for 2016 on 2019 Server Standard.

My biggest issues have been with Group Policy completely broken and no backups available.  For both the Default Domain Policy and the Default Domain Controllers policy, the GptTmpl.inf files are just missing for some reason.

I was able to create a generic one for the Default Domain Policy since there were no SID references in it and now I can start pushing GPOs again (was showing that Account Policies security settings were unreadable for all GPOs because this was missing).  However, I can't do the same for the Default Domain Controllers Policy under \[domain]\SYSVOL[domain]\Policies{6AC1786C-016F-11D2-945F-00C04fB984F9}\MACHINE\Microsoft\Windows NT\SecEdit because it is just full of domain specific SIDs.

The utility dpogpfix does not do anything useful to create this.  Does anyone know how to regenerate or create a minimal new inf file?

## Answer (community) — community member

*upvotes: 1 · updated: 2024-09-20*

Hello Karl Pedersen1,

Thank you for posting in Microsoft Community forum.

Do you have only one Domain Controller in this domain?  

If so, I suggest you can try to do a lab:

1.Create only one Domain Controller with 2019 Server Standard and functional levels for 2016 in two test lab and check if the contents in GptTmpl.inf under \a.com\SYSVOL\a.com\Policies{6AC1786C-016F-11D2-945F-00C04fB984F9}\MACHINE\Microsoft\Windows NT\SecEdit are the same or not.  

If all the contents in GptTmpl.inf under \a.com\SYSVOL\a.com\Policies{6AC1786C-016F-11D2-945F-00C04fB984F9}\MACHINE\Microsoft\Windows NT\SecEdit are the same, you can copy one file from on DC in the lab to DC in your case.

Here are the contents within GptTmpl.inf on my 2016 DC.

[Unicode] 

Unicode=yes 

[Registry Values] 

MACHINE\System\CurrentControlSet\Services\NTDS\Parameters\LDAPServerIntegrity=4,1 

MACHINE\System\CurrentControlSet\Services\Netlogon\Parameters\RequireSignOrSeal=4,1 

MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters\RequireSecuritySignature=4,1 

MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters\EnableSecuritySignature=4,1 

[Version] 

signature="$CHICAGO$" 

Revision=1 

[Privilege Rights] 

SeAssignPrimaryTokenPrivilege = *S-1-5-82-3006700770-424185619-1745488364-794895919-4004696415,*S-1-5-20,*S-1-5-19 

SeAuditPrivilege = *S-1-5-82-3006700770-424185619-1745488364-794895919-4004696415,*S-1-5-20,*S-1-5-19 

SeBackupPrivilege = *S-1-5-32-549,*S-1-5-32-551,*S-1-5-32-544 

SeBatchLogonRight = *S-1-5-32-559,*S-1-5-32-551,*S-1-5-32-544,*S-1-5-32-568 

SeChangeNotifyPrivilege = *S-1-5-32-554,*S-1-5-11,*S-1-5-32-544,*S-1-5-20,*S-1-5-19,*S-1-1-0 

SeCreatePagefilePrivilege = *S-1-5-32-544 

SeDebugPrivilege = *S-1-5-32-544 

SeIncreaseBasePriorityPrivilege = *S-1-5-32-544 

SeIncreaseQuotaPrivilege = *S-1-5-82-3006700770-424185619-1745488364-794895919-4004696415,*S-1-5-32-544,*S-1-5-20,*S-1-5-19 

SeInteractiveLogonRight = *S-1-5-32-549,*S-1-5-32-550,*S-1-5-9,*S-1-5-32-551,*S-1-5-32-544,*S-1-5-32-548,*S-1-5-21-2051886910-1628492530-2711760023-5602,*S-1-5-21-2051886910-1628492530-2711760023-513 

SeLoadDriverPrivilege = *S-1-5-32-550,*S-1-5-32-544 

SeMachineAccountPrivilege = *S-1-5-11 

SeNetworkLogonRight = *S-1-5-32-554,*S-1-5-9,*S-1-5-11,*S-1-5-32-544,*S-1-1-0 

SeProfileSingleProcessPrivilege = *S-1-5-32-544 

SeRemoteShutdownPrivilege = *S-1-5-32-549,*S-1-5-32-544 

SeRestorePrivilege = *S-1-5-32-549,*S-1-5-32-551,*S-1-5-32-544 

SeSecurityPrivilege = *S-1-5-32-544 

SeShutdownPrivilege = *S-1-5-32-550,*S-1-5-32-549,*S-1-5-32-551,*S-1-5-32-544 

SeSystemEnvironmentPrivilege = *S-1-5-32-544 

SeSystemProfilePrivilege = *S-1-5-80-3139157870-2983391045-3678747466-658725712-1809340420,*S-1-5-32-544 

SeSystemTimePrivilege = *S-1-5-32-549,*S-1-5-32-544,*S-1-5-19 

SeTakeOwnershipPrivilege = *S-1-5-32-544 

SeUndockPrivilege = *S-1-5-32-544 

SeEnableDelegationPrivilege = *S-1-5-32-544 

SeRemoteInteractiveLogonRight = *S-1-5-32-544,*S-1-5-21-2051886910-1628492530-2711760023-5602,*S-1-5-21-2051886910-1628492530-2711760023-513,*S-1-5-21-2051886910-1628492530-2711760023-10601,*S-1-5-21-2051886910-1628492530-2711760023-500 

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-20*

Thank you, Daisy!  I did not have immediate access to a clean lab environment but I had thought of the same plan of action. My concern was seeing all of the SIDs that look like they are clearly or potentially domain specific, and what introducing those may do.  I assume creating a lab copy of the domain will not have the same sub-string domain component no matter what I do and was curious if it was able  to "re-generate" from the existing domain.

For instance, in your example you can see the line below in which S-1-5-32-xxx is used which is domain specific, and S-1-5-21, -80 or -82 which I can't find a referenced to here: https://learn.microsoft.com/en-us/windows/win32/secauthz/well-known-sids 

SeRemoteInteractiveLogonRight = *S-1-5-32-544,*S-1-5-21-2051886910-1628492530-2711760023-5602,*S-1-5-21-2051886910-1628492530-2711760023-513,*S-1-5-21-2051886910-1628492530-2711760023-10601,*S-1-5-21-2051886910-1628492530-2711760023-500

Would I just do a find and replace for the domain string and not include the last substring?

Regards,  

Karl
