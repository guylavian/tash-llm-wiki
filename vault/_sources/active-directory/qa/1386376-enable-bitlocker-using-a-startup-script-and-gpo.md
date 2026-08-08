---
title: "Enable bitlocker using a startup script and GPO."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1386376/enable-bitlocker-using-a-startup-script-and-gpo
question_id: 1386376
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-devices-deployment-config-app-groups", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
---
# Enable bitlocker using a startup script and GPO.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1386376/enable-bitlocker-using-a-startup-script-and-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm looking for some advice on enforcing BitLocker using a startup script, but I'm running into an issue.

The current setup is as follows:  

GPO to enforce certain BitLocker settings + startup script.  

Startup script:

```
Start-Transcript -Path "C:\IT\TestLog.txt"
$Date = Get-Date
$Tpm = Get-Tpm
$Bitlocker = Get-BitLockerVolume -MountPoint $env:SystemDrive

if($Tpm.TpmPresent -eq 'True' -and $Bitlocker.ProtectionStatus -eq 'off'){
manage-bde -protectors $env:SystemDrive -add -tpm
Enable-BitLocker -MountPoint $env:SystemDrive -UsedSpaceOnly -SkipHardwareTest -RecoveryPasswordProtector
}

Stop-Transcript
```

Output of the transcript:

```
Transcript started, output file is C:\IT\TestLog.txt
BitLocker Drive Encryption: Configuration Tool version 10.0.19041
Copyright (C) 2013 Microsoft Corporation. All rights reserved.

Key Protectors Added:

ERROR: An error occurred (code 0x80070522):
A required privilege is not held by the client.
Add-TpmProtectorInternal : A required privilege is not held by the client. (Exception from HRESULT: 0x80070522)
At C:\WINDOWS\system32\WindowsPowerShell\v1.0\Modules\BitLocker\BitLocker.psm1:2095 char:31
+ ...   $Result = Add-TpmProtectorInternal $BitLockerVolumeInternal.MountPo ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [Write-Error], COMException
    + FullyQualifiedErrorId : System.Runtime.InteropServices.COMException,Add-TpmProtectorInternal
Add-TpmProtectorInternal : A required privilege is not held by the client. (Exception from HRESULT: 0x80070522)
At C:\WINDOWS\system32\WindowsPowerShell\v1.0\Modules\BitLocker\BitLocker.psm1:2095 char:31
+ ...   $Result = Add-TpmProtectorInternal $BitLockerVolumeInternal.MountPo ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [Write-Error], COMException
    + FullyQualifiedErrorId : System.Runtime.InteropServices.COMException,Add-TpmProtectorInternal

**********************
Windows PowerShell transcript end
End time: 20231005154958
```

According to the transcript, there are insufficient permissions, but the script is being executed using the \SYSTEM user. 

I'm not really sure how to proceed here. Any advice is welcome.

## Answers

_No answers on this thread._
