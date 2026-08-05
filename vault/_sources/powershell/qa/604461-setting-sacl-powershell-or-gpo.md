---
title: "Setting SACL powershell or GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/604461/setting-sacl-powershell-or-gpo
question_id: 604461
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
---
# Setting SACL powershell or GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/604461/setting-sacl-powershell-or-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Im trying to set SACL on a set of folders (server 2016) and the HKLM reg key. Overwtirtting what is currently there(which is currently nothing set).     

I first tried with GPO but the the DACL pemissions got overwritten. I've seen articles on modifying the inf file but the missing pemissions from the deault GPO permissions are not easy to set up in the infi file. Setting to inherit then had multiple DACL persmissions applied - those DACLs set in the GPO plus those pulled from parent. The SACLs though were set as I wanted (although liek my issue with powersell didnt get applied to sub folders and files).    

The folders we want to set SACL on are system32 and syswow64 (plus some others) with change permission for success and full control for failure.    

I've tried powershell with samples I've found. This worked well    

$folder1 = "folder path"    

$SuccessAudit = New-Object System.Security.AccessControl.FileSystemAuditRule(     

    "Everyone",   

    "ChangePermissions",   

    "ContainerInherit, ObjectInherit",   ##as want applied to this folder, folders and files  

    "None",  #using settings here made no differenace to the SACL being applied to sub folders or files  

    "Success"  

)    

$FailureAudit = New-Object System.Security.AccessControl.FileSystemAuditRule(    

    "Everyone",  

    "FullControl",  

   "ContainerInherit, ObjectInherit",       

    "None",   

    "Failure"  

)    

if (Test-Path -path $folder1) {    

    $Acl = Get-Acl $folder1  

    $Acl.AddAuditRule($SuccessAudit)  

    $Acl.AddAuditRule($FailureAudit)  

    $Acl | Set-Acl   

}    

However, this only sets on folder1 and doesnt propagrate the SACLs down to the sub folders and files.    

How can this be achieved? - I can't see to find examples of this.    

I've seen articles pointing to https://learn.microsoft.com/en-gb/samples/browse/?redirectedfrom=TechNet-Gallery    

for code examples but when I go there I'm unsure of where I'm looking. Serach powershell doesn't seem to give the exampels I was hoping for.    

Also futher issues might be to rollback. How to unset the SACLs on folder1 and then the subfodlers and files    

And I've also seen articles where the above code may not work if the folder owner is TrustedInstaller (which it will be for some of the folders).    

So any ways to solves these as well    

Is Powershell the best way for me to go or is there an alteratiove to this and to GPO ?    

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-10-29*

Hello @Freeman, Mark  ,    

Thank you for your question and for getting in touch. My name is Samuel and I would be more than happy to help you with your query.    

Sometimes, during setup, we missed some things that we didn't notice, so I recommend you check the link below to get a sense of how to do this, using a topic for a problem similar to yours:    

https://social.technet.microsoft.com/Forums/lync/en-US/0e44bca0-b251-4d52-b853-a6c514ba080e/using-a-gpo-to-set-the-sacl-for-mapped-drives- and-shares-on-servers?forum=winserverGP    

------    

--If the answer is helpful, please vote positively and accept as an answer--
