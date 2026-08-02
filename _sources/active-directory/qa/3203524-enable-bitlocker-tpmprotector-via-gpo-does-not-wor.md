---
title: "Enable-Bitlocker -TpmProtector via GPO does not work (0x80070522)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3203524/enable-bitlocker-tpmprotector-via-gpo-does-not-wor
question_id: 3203524
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 63
qa_tags: []
---
# Enable-Bitlocker -TpmProtector via GPO does not work (0x80070522)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3203524/enable-bitlocker-tpmprotector-via-gpo-does-not-wor (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I am trying to automate the bitlocker in our corporate environment.  

I have written a script which enables the bitlocker and it works fine if I run it manually, but whenever I implement it via GPO (startup script) right after 

Enable-BitLocker -MountPoint C:\ -EncryptionMethod XtsAes256 -SkipHardwareTest -UsedSpaceOnly -TpmProtector  

I see in the transcription following error 

Add-TpmProtectorInternal : A required privilege is not held by the client. (Exception from HRESULT: 0x80070522)

At C:\WINDOWS\system32\WindowsPowerShell\v1.0\Modules\BitLocker\BitLocker.psm1:2095 char:31

-  ...   $Result = Add-TpmProtectorInternal $BitLockerVolumeInternal.MountPo ...

+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    + CategoryInfo          : NotSpecified: (:) [Write-Error], COMException

    + FullyQualifiedErrorId : System.Runtime.InteropServices.COMException,Add-TpmProtectorInternal

Add-TpmProtectorInternal : A required privilege is not held by the client. (Exception from HRESULT: 0x80070522)

At C:\WINDOWS\system32\WindowsPowerShell\v1.0\Modules\BitLocker\BitLocker.psm1:2095 char:31

-  ...   $Result = Add-TpmProtectorInternal $BitLockerVolumeInternal.MountPo ...

+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    + CategoryInfo          : NotSpecified: (:) [Write-Error], COMException

    + FullyQualifiedErrorId : System.Runtime.InteropServices.COMException,Add-TpmProtectorInternal

I have tried to wrap the PS script with bat file:

powershell.exe -ExecutionPolicy bypass -file "Enable-bitlocker_step2.ps1"  

Enable-bitlocker_step2.ps1 script body:

Start-Process Powershell.exe -ArgumentList '-ExecutionPolicy bypass -File "\**********\SYSVOL\***********\scripts\Enable Bitlocker.ps1"' -Verb RunAs -ErrorAction SilentlyContinue -WarningAction SilentlyContinue

The bitlocker script itself:

Start-Transcript -Path \Melandru\temp"$env:COMPUTERNAME.txt"

#get computer capability

$OS_edition = Get-WmiObject -Class win32_operatingSystem

$TPM_info = Get-Tpm

$bitlocker_status = Get-BitLockerVolume C: 

$gpo_path = "***********\SYSVOL\***********\Policies{*******-****-****-****-**********}"

###Pre-requisites###

#if bitlocker is on and encryption method is XtsAes256 - exit, since nothing to do

if (($bitlocker_status.protectionstatus -eq "On") -and ($bitlocker_status.EncryptionMethod -eq "XtsAes256")){

    if ((Get-Content "$($gpo_path)\bitlocker_list.txt") -like "*$($env:COMPUTERNAME)*") {Write-output "Bitlocker key already backed up";exit}

    else{

        $key_protector=(Get-BitLockerVolume C:).keyprotector | ?{$_.KeyProtectorType -eq "Recoverypassword"} | select -expandproperty KeyProtectorId

        Backup-BitLockerKeyProtector -KeyProtectorId $key_protector -MountPoint C:

        exit}

    }

#check if encryption/decryption in progress. If so - exit the script

elseif (($bitlocker_status.volumestatus -eq "EncryptionInProgress") -or ($bitlocker_status.volumestatus -eq "DecryptionInProgress")) {Write-output "Bitlocker encryption/decryption in progress";exit}

###define bitlocker functions###

function remove_old_key_protectors {

    foreach ($keyprotector in $bitlocker_status.keyprotector){

        Remove-BitLockerKeyProtector C: -KeyProtectorId $keyprotector.keyprotectorid

        Write-Output "Removed $($keyprotector.keyprotectorid)"

        }

    Write-Output "Old keys removed"

    }

function enable_bitlocker {

    #add a new key protector - recovery password

    Add-BitLockerKeyProtector -MountPoint C:\ -RecoveryPasswordProtector

    Write-Output "Added password key protector"

    #enable bitlocker

    Enable-BitLocker -MountPoint C:\ -EncryptionMethod XtsAes256 -SkipHardwareTest -UsedSpaceOnly -TpmProtector

    Write-Output "Bitlocker enabled"

    }

#check tpm chip and OS edition

if (($OS_edition.caption -notlike "*ent*") -or ($TPM_info.TPMPresent -ne $True)){write-output "Not compatible";exit}

#if all checks passed - do the script logic

else {

    #Check if bitlocker is enabled and enryption method is not XtsAes256. If so - disable bitlocker    

    If (($bitlocker_status.protectionstatus -eq "On") -and ($bitlocker_status.EncryptionMethod -ne "XtsAes256"))  {

        Write-Output "Disabling bitlocker"

        Disable-BitLocker C:

        }

    Elseif ($bitlocker_status.protectionstatus -eq "Off"){

        #check if there's an old protection key and remove it

        if ($bitlocker_status.keyprotector -ne $null) {

        Write-Output "Removing old keys"

        remove_old_key_protectors

        }

        Write-Output "Enabling Bitlocker XtsAes256"

        enable_bitlocker

    }

}

Stop-Transcript -ErrorAction SilentlyContinue

The thing is if i simply run bat file manually from a computer - I have bitlocker enabled, but if I add bat script to Computer Configuration->Policies->Windows Settings->Scripts(Startup/Shutdown)->Startup  

I see the error mentioned above. Any help appreciated

## Answers

_No answers on this thread._
