---
title: "Active Directory backup, restore, or disaster recovery"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2188803/active-directory-backup-restore-or-disaster-recove
question_id: 2188803
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Active Directory backup, restore, or disaster recovery

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2188803/active-directory-backup-restore-or-disaster-recove (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Customer have 1 number of Root Domain Controller & 1 number of Additional Domain Controller.

In case, if RDC fails, how to auto failover ADC as a Root Domain Controller.

Windows Operating System in both Domain Controller have Windows Server 2022 Standard Edition.

Please CC to another email ID: ******** (Technical)

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-23*

Hi Soumabratab,

Certainly, I can provide you with some resources to help you automate the failover process in case of a disaster.  

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/transfer-or-seize-operation-master-roles-in-ad-ds 

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/fsmo-transfer-seizure-process

https://learn.microsoft.com/en-us/powershell/scripting/learn/remoting/running-remote-commands?view=powershell-7.4

Please note that these resources are provided as-is and Microsoft does not provide any warranty or support for any scripts or tools that are not developed by Microsoft.  

I hope this helps! Let me know if you have any further questions.

Best regards

Qiuyang

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-23*

Hi Soumabratab,

Yes, there are ways to automate the transfer of FSMO roles in case of a failure of the RDC without manual intervention. One way to achieve this is by using PowerShell scripts that can be scheduled to run periodically to check the health of the RDC and transfer the FSMO roles to the ADC if the RDC is found to be unavailable.

There are also third-party tools available that can automate the process of transferring FSMO roles in case of a failure of the RDC. However, as a Microsoft customer support agent, I can only provide support for Microsoft products and cannot recommend or provide support for third-party tools.

I would recommend referring to the Microsoft documentation on FSMO role transfer and PowerShell scripting for more information on how to automate the transfer of FSMO roles in case of a failure of the RDC.

Please note: This is a public forum. To prevent your personal information from being leaked, I will delete your email address and phone number.

Best regards

Qiuyang

Hello Qiuyang,

Please share the PowerShell Script or documents to automate the fail-over in case any disaster happen.

Thanks & Regards,

Soumabrata Bhaumik

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-23*

Hi Soumabratab,

Yes, there are ways to automate the transfer of FSMO roles in case of a failure of the RDC without manual intervention. One way to achieve this is by using PowerShell scripts that can be scheduled to run periodically to check the health of the RDC and transfer the FSMO roles to the ADC if the RDC is found to be unavailable.

There are also third-party tools available that can automate the process of transferring FSMO roles in case of a failure of the RDC. However, as a Microsoft customer support agent, I can only provide support for Microsoft products and cannot recommend or provide support for third-party tools.

I would recommend referring to the Microsoft documentation on FSMO role transfer and PowerShell scripting for more information on how to automate the transfer of FSMO roles in case of a failure of the RDC.

Please note: This is a public forum. To prevent your personal information from being leaked, I will delete your email address and phone number.

Best regards

Qiuyang

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-23*

Hi Soumabratab,

To enable automatic failover of the Additional Domain Controller (ADC) as the new Root Domain Controller (RDC) in case of a failure, you can use the Active Directory Domain Services (AD DS) feature called "Flexible Single Master Operation (FSMO) role seizure".

Here are the steps to follow:

-  Determine which FSMO roles are held by the failed RDC. You can use the "netdom query fsmo" command on any domain controller to determine this.

-  Transfer the FSMO roles from the failed RDC to the ADC using the "ntdsutil" command.

-  If the failed RDC cannot be brought back online, you can seize the FSMO roles on the ADC using the same "ntdsutil" command.

-  Once the ADC has taken over the FSMO roles, it will become the new RDC and will handle all domain controller functions.

It is important to note that seizing FSMO roles should only be done as a last resort, as it can cause issues if the failed RDC is brought back online later. It is recommended to try to bring the failed RDC back online first, and transfer the FSMO roles back to it if possible.

I hope this helps! Let me know if you have any further questions.

Best regards

Qiuyang

Hello Qiuyang,

Thanks for your support.

I have another query regarding the automatic failover between RDC & ADC.

Customer wants automatic failover between RDC & ADC in case of failure of RDC without manual transfer of FSMO roles using "ntdsutil" command.

Are there any process with third party tools or, without third party tools that involves triggering the command for transferring FSMO roles automatically in case of any failure of RDC? .... Please advise.

Thanks & Regards,

Soumabrata Bhaumik

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-23*

Hi Soumabratab,

To enable automatic failover of the Additional Domain Controller (ADC) as the new Root Domain Controller (RDC) in case of a failure, you can use the Active Directory Domain Services (AD DS) feature called "Flexible Single Master Operation (FSMO) role seizure". 

Here are the steps to follow:

-  Determine which FSMO roles are held by the failed RDC. You can use the "netdom query fsmo" command on any domain controller to determine this.

-  Transfer the FSMO roles from the failed RDC to the ADC using the "ntdsutil" command. 

-  If the failed RDC cannot be brought back online, you can seize the FSMO roles on the ADC using the same "ntdsutil" command. 

-  Once the ADC has taken over the FSMO roles, it will become the new RDC and will handle all domain controller functions.

It is important to note that seizing FSMO roles should only be done as a last resort, as it can cause issues if the failed RDC is brought back online later. It is recommended to try to bring the failed RDC back online first, and transfer the FSMO roles back to it if possible. 

I hope this helps! Let me know if you have any further questions.

Best regards

Qiuyang
