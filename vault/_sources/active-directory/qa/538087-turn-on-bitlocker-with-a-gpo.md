---
title: "Turn on BITLOCKER with a GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/538087/turn-on-bitlocker-with-a-gpo
question_id: 538087
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Turn on BITLOCKER with a GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/538087/turn-on-bitlocker-with-a-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,     

I would need to turn on Bitlocker with a GPO.     

I've created a policy where I've added the ps1 below to the startup:    

```
$CdriveStatus = Get-BitLockerVolume -MountPoint 'c:'  
  
if ($CdriveStatus.volumeStatus -eq 'FullyDecrypted') {  
    C:\Windows\System32\manage-bde.exe -on c: -recoverypassword -skiphardwaretest  
}
```

but it only works when I run it by opening powershell locally and "as administrator"     

this is the error that I receive when not running as administrator:     

    

any suggestions?     

Thank you very much

## Answer (community) — community member

*upvotes: 2 · updated: 2021-09-03*

Hello Marshall  

I do it in a different way, using purely group policy  

1.Go to Group Policy Editor in "gpedit.msc"   

2.Go to Computer Configuration > Administrative Templates > Windows Components > BitLocker Drive Encryption > Operating System Drives.  

3.n the right pane, double-click "Require additional authentication at startup"   

4.Make sure the "Enabled" option is chosen so that all other options below will be active.  

5.Uncheck the box for "Allow BitLocker without a compatible TPM."  

6.For the choice of "Configure TPM startup:", choose "Allow TPM."  

7.For the choice of "Configure TPM startup PIN:", choose "Require startup PIN with TPM."  

8.For the choice of "Configure TPM startup key:", choose "Allow startup key with TPM."  

9.For the choice of "Configure TPM startup key and PIN:", choose "Allow startup key and PIN with TPM."  

10. Click the "Apply" button and then the "OK" button to save the changes.  

Hope this helps in your case,  

Best regards,

## Answer (community) — community member

*upvotes: 0 · updated: 2022-05-31*

Hi   

i have BitLocker turned on but it keeps asking me for a password when i startup   

is there a way to turn it on without the need to enter a password with every startup?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-09-06*

GPOs alone cannot encrypt (unless you have MBAM).  

See my article. It uses a GPO to start it scripted: https://www.experts-exchange.com/articles/33771/We-have-bitlocker-so-we-need-MBAM-too.html?preview=hG26jVC1xow%3D

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-06*

Hi LimitLess,    

thanks for you reply!    

I created a policy with your instructions but unfortunately the bitlocker it's still not applied:    

    

any suggestions ?    

Thanks you very much    

Best regards
