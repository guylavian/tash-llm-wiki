---
title: "Bitlocker on Active directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5830025/bitlocker-on-active-directory
question_id: 5830025
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-devices-deployment-recovery-key"]
answer_author_roles: ["Independent Advisor"]
---
# Bitlocker on Active directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5830025/bitlocker-on-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Team,

We are trying to enable Bitlocker for domain controllers C drive, D drive and E drive. we referred ms blogs but little confusing. Could you please give some insight and share the steps to enable that.

We also want to store the keys in AD. Please do the needful

## Answer (community) — Independent Advisor

*upvotes: 1 · updated: 2026-03-20*

Hello SAGA,

Think of BitLocker as a lock for your server’s hard drives. To make it simple: first, you turn on the BitLocker feature in Windows Server. Next, you set a rule in Group Policy that tells the server to automatically save the “spare keys” (called recovery keys) into Active Directory, so if you ever lose access you can get them back safely. Once that rule is in place, you restart the server so it picks up the setting, and then you switch on BitLocker for each drive (C, D, and E). The system will encrypt the data and keep the recovery keys stored in AD automatically.

So, just in short, enable BitLocker, set the policy to save keys in AD, apply the policy, then encrypt each drive. That way your domain controllers are protected, and you’ll always have the recovery keys available in Active Directory if needed.

I hope you found something helpful here. If it does help to explain your question, please accept the answer, or give it a thump up to encourage my contribution. Thank you.

Harry.

## Answer (community) — community member

*upvotes: 0 · updated: 2026-03-20*

Below are concise steps to enable BitLocker on domain controllers’ C:, D:, and E: drives and escrow recovery keys in Active Directory.

-  Plan key storage in AD DS

-  Extend the AD schema and enable BitLocker key storage in AD DS if not already done.

-  Configure Group Policy to back up recovery information before allowing BitLocker:

-  For OS drives: Computer Configuration → Administrative Templates → Windows Components → BitLocker Drive Encryption → Operating System Drives → Choose how BitLocker-protected operating system drives can be recovered.

-  For fixed data drives (D:, E:): … → BitLocker Drive Encryption → Fixed Data Drives → Choose how BitLocker-protected fixed drives can be recovered.

-  In each policy:

-  Enable the policy.

-  Select Save BitLocker recovery information to Active Directory Domain Services.

-  Choose to store at least the BitLocker recovery password (and optionally the key package).

-  Enable Do not enable BitLocker until recovery information is stored in AD DS to ensure escrow succeeds before encryption starts.

-  Understand what is stored in AD DS

-  For each BitLocker-protected volume, AD DS stores:

-  BitLocker recovery password (48-digit password used to unlock the drive in recovery).

-  BitLocker key package (used with the recovery password and `Repair-bde` to repair severely damaged disks).

-  Recovery entries are not overwritten; multiple passwords can exist for a drive, distinguished by date.

-  Enable BitLocker on the OS drive (C:)

-  Ensure the domain controller is already joined to the domain so that recovery info can be escrowed automatically.

-  Recommended approach (PowerShell) with TPM + PIN or TPM-only, depending on security policy.

-  Example (TPM + PIN, used-space-only encryption):

-  Create a secure PIN:

```
$SecurePin = ConvertTo-SecureString "1234" -AsPlainText -Force
```

-  Enable BitLocker on C: with TPM and PIN:

```
Enable-BitLocker -MountPoint "C:" -EncryptionMethod Aes256 -UsedSpaceOnly -Pin $SecurePin -TPMandPinProtector
```

-  Alternatively, use TPM + startup key or startup key only (for example, if TPM policy requires it):

```
Enable-BitLocker C: -StartupKeyProtector -StartupKeyPath E: -SkipHardwareTest
```

  or via `manage-bde`:

```
manage-bde.exe -protectors -add C: -TPMAndStartupKey E:
  manage-bde.exe -on C:
```

-  After enabling, add a recovery password protector (if not already added by policy) and back it up to AD DS using `Backup-BitLockerKeyProtector` if needed.

-  Enable BitLocker on data drives (D:, E:)

-  Use similar PowerShell commands, typically with a recovery password and/or AD DS account protector, and used-space-only encryption for speed:

```
Get-BitLockerVolume -MountPoint "D:" | Enable-BitLocker -EncryptionMethod Aes256 -UsedSpaceOnly -RecoveryPasswordProtector
  Get-BitLockerVolume -MountPoint "E:" | Enable-BitLocker -EncryptionMethod Aes256 -UsedSpaceOnly -RecoveryPasswordProtector
```

-  Ensure the Group Policy for fixed data drives is configured to save recovery information to AD DS and to block enablement until escrow succeeds.

-  Verify recovery key backup

-  On the domain controller, check the event log for BitLocker backup success/failure entries.

-  Use the BitLocker Recovery Password Viewer tool in AD DS (with domain admin rights) to confirm that:

-  Recovery passwords and key packages are present for the domain controller computer object.

-  Remember that even if an event log shows “Success,” only querying AD DS confirms that a usable backup exists.

-  Additional considerations

-  For new domain-joined computers, join to the domain first, then enable BitLocker so that recovery keys are automatically stored in AD DS.

-  If BitLocker was enabled before domain join or before policies were in place, recovery info is not automatically backfilled; use the BitLocker operations guide to reset and back up recovery passwords after the fact.

-  For FIPS environments, FIPS-compliant recovery password protectors can be created and stored in AD DS; BitLocker recovery policies behave the same in FIPS and non-FIPS modes.

References:

-  BitLocker FAQ

-  BitLocker planning guide

-  BitLocker recovery overview

-  BitLocker operations guide

-  Task sequence steps

-  Enable-BitLocker
