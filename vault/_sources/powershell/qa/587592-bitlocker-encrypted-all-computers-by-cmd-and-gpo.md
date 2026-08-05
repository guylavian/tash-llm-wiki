---
title: "Bitlocker: Encrypted all computers by cmd and GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/587592/bitlocker-encrypted-all-computers-by-cmd-and-gpo
question_id: 587592
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
---
# Bitlocker: Encrypted all computers by cmd and GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/587592/bitlocker-encrypted-all-computers-by-cmd-and-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello guys,  

I have to join a lot of computers to a new domain and I would like to enable bitlocker in all computers domain.  

I want to create a GPO and, when I join a new computer to the domain, bitlocker was enable automatically.  

The solution that I found is to create a script to do it, and the create a GPO to deploy this script and see if the GPO works.  

I tested this script and works perfectly:

$CdriveStatus = Get-BitLockerVolume -MountPoint 'c:'  

if ($CdriveStatus.volumeStatus -eq 'FullyDecrypted') {  

C:\Windows\System32\manage-bde.exe -on c: -recoverypassword -skiphardwaretest  

}

But I want to add the password of the bitlocker and the recovery password, but I am not able to do it.  

I tried with these modifications, but it doesn’t work and i have a mistake when i launch it:

1) Try with password  

$pass = ConvertTo-SecureString "Password" -AsPlainText -Force  

$CdriveStatus = Get-BitLockerVolume -MountPoint 'c:'  

if ($CdriveStatus.volumeStatus -eq 'FullyDecrypted') {  

C:\Windows\System32\manage-bde.exe -on c: -password $pass -recoverypassword -skiphardwaretest  

}

2) Try with PIN  

$SecureString = ConvertTo-SecureString "1234" -AsPlainText -Force  

Enable-BitLocker -MountPoint c: -EncryptionMethod Aes256 -UsedSpaceOnly -Pin $SecureString -TPMandPinProtector

3) Try with password  

$pass = ConvertTo-SecureString Passw0rd -AsPlainText -Force  

Enable-BitLocker -MountPoint c:\ -EncryptionMethod Aes128 -Password $pass -PasswordProtector

Could you be so kind to help me, please?  

Thank so much.

## Answers

_No answers on this thread._
