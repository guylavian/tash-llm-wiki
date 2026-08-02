---
title: "TPM Check Readiness for Task Sequence New Operating System Installation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1009077/tpm-check-readiness-for-task-sequence-new-operatin
question_id: 1009077
fetched: 2026-07-25
answer_count: 8
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-deployment"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# TPM Check Readiness for Task Sequence New Operating System Installation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1009077/tpm-check-readiness-for-task-sequence-new-operatin (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,    

During OSD (New Computer or Reinstall Computer), can I notify the operator that the TPM is not enabled or configured ?    

This is because, during the Bitlocker Pre-Provisioning step, if the TPM is not active, the operator receives an error warning but does not understand that the problem is the TPM.    

No Task Sequence Upgrade, but Task Sequence Bare Metal from Network Boot, so even if the hdd disk is completely empty.    

Practically a Check Readiness for new operating system installation.    

I don't think this works for my scenario. I am not using a Task Sequence of Upgrade but a Task Sequence From Network Boot.    

https://www.prajwaldesai.com/enable-tpm-2-0-check-in-sccm-task-sequence/    

Thank you all for your support.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 1 · updated: 2022-10-05*

Same answer, it's not. You need to do something custom for this. You can build your own frontend to do this, you just won't be able to use PowerShell to do this to my knowledge per the shortcomings you called out although have you attempted to use WMI directly via PowerShell to check TPM Readiness? A quick web search will get some hits on how to do this with WMI. The key is to directly use the Win32_TPM class: https://learn.microsoft.com/en-us/windows/win32/secprov/win32-tpm    

As for implementing UI++, you can pick and choose exactly what you want, and it can be as simple as you want it to be. It's totally up to you what you want to do.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-06*

From WinPE, even with the Powershell component enabled in the boot image, the "Get-Tpm" command is not recognized.    

From WinPE, with the command "wmic /namespace:\root\CIMV2\Security\MicrosoftTpm path Win32_Tpm get /value", the "TpmReady" is not queried.    

From Windows Operating System installed, the command "Get-Tpm", shows the status of the "TpmReady".    

From Windows Operating System installed, the "wmic /namespace:\root\CIMV2\Security\MicrosoftTpm path Win32_Tpm get /value", the "TpmReady" is not queried.    

From the tests I carried out, the "Check Readiness" Step, both in a Windows PE environment and in an installed Operating System environment, is not 100% functional for the control of the TPM. Even if "TpmReady" is "FALSE", it still ends with "Check successfully". The TPM control of the "Check Readiness" Step does not check the "TpmReady" status, this causes the Task Sequence to stop with an error for the "Enable Bitlocker" step.    

From the tests I carried out, the step "Pre-Provisioning Bitlocker", is not 100% functional for the control to enable the Bitlocker. Even if "TpmReady" is "FALSE", it still ends with "Check successfully". The "Bitlocker Pre-Provisioning" step does not check the "TpmReady" status, this causes the Task Sequence to stop with an error for the "Enable Bitlocker" step.    

I need to find a method that shows a warning if "TpmReady" is "FALSE".

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-05*

The built-in Step "Check Readiness" for check TPM, does not perform the "TpmReady" status check. This information does not seem to be traceable through WMI queries, but only with Powershell. in the winpe environment the command "get-tpm" is not recognized, although in the boot image, in addition to the standard components, I have also added the following     

    

If "TpmReady" is False, "Pre-Provisioning Bitlocker" and "Enable Bitlocker" steps fail. How is it possible to make the Step "Check Readiness", also check the status of the "TpmReady"?    

Thank you all for your support.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-21*

Actually I did some tests, and the built-in Step "Check Readiness" in WinPE Boot PXE environment also works.    

What does not allow you to filter, however, is the version of the TPM. Control is only "TPM 2.0 or above is enabled" and "TPM 2.0 or above is activated".    

I would like to find a solution that fits version 1.2 or later of the TPM.    

For the time being, the suggestion https://uiplusplus.configmgrftw.com/ , seems to me too extensive for the small objective I would like to achieve.    

Thank you all for your support.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-09-15*

There's nothing built-in for this no, but that doesn't mean you can't do something custom using a simple script. There are community tools that can help with this depending on your requirements and desires. One such tool is UI++: https://uiplusplus.configmgrftw.com.
