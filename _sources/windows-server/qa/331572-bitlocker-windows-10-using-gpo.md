---
title: "Bitlocker Windows 10 using GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/331572/bitlocker-windows-10-using-gpo
question_id: 331572
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-devices-deployment-config-app-groups", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Bitlocker Windows 10 using GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/331572/bitlocker-windows-10-using-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,    

Inside company I would manage Bitlocker for Windows 10 Clients using Group Policy.    

I have already installed role to manage BitLocker on my domain controller.    

After that I create a new Group Policy (You can see it in the picture):    

    

In my case there are in this moment more than 50 laptops inside comany. Before IT Support encripted drive directly from Windows 10 PC and store all recovery keys in a shared folder. I would remove this practice to avoid mistakes.    

My goal is:    

-  automatically encrypt all Operating System Drive (all laptop has got just one partition due to users save all files on File Server)    

-  see all Bitlocker Recovery Key on Active Directory. Can I see actual recovery of all laptops in Active Directory?    

In this moment, any computer profile, is empty about Bitlocker Information:    

    

How can I do it?    

What happen if I enable GPO for all computers and all computers in this moment has got BitLocker enabled?    

Best regards    

Federico

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-29*

Thanks so much for your help!  

Best regards

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-26*

Hi @Jenny Feng       

Thanks for your reply!    

Sorry but I not undestand some steps:    

You set the options through GPO but to actually enable you need to run a script.    

Until yesterday, Bitlocker Windows 10 function was always manually enabled on PCs after joining them to the domain.    

Activation has always been done by:    

Start> Manage Bitlocker    

I admit that the bitlocker was often activated usung    

-  "Encrypt used disk space only"    

-  "New encryption mode"    

I usually save recovery key on a document file.    

Should I run the script to convert bitlocker mode (from Encrypt used disk space only to Encrypt entire drive)?    

Domain administrators can view the BitLocker recovery password by     

using the BitLocker Recovery Password Viewer.    

I already enabled it from Server Manager (I installed roles about bitlocker on Domain Controller).    

If a Group Policy setting was changed after the initial BitLocker deployment in     

your organization, and then the setting was applied to previously encrypted     

drives), no change can be made to the BitLocker configuration of that drive     

except a change that will bring it into compliance.    

Ok.    

In my case I have all laptop encrypted manually from Control Panel menu.    

From now I would avoid to it manually, but automatically.    

After that I would see actual recovery key of all laptop inside Active Directory.    

In this moment, all computer tab about Bitlocker is empty (I did not apply GPO yet).    

Is there a way that permit me to have inside Active Directory, all computer recovery key already encrypted by BitLocker?    

I hope to be clear.    

Federico

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-26*

@Federico Coppola       

Hi,    

automatically encrypt all Operating System Drive    

You set the options through GPO but to actually enable you need to run a script.    

You may refer to the following link for details:    

https://www.reddit.com/r/sysadmin/comments/aburax/how_to_enable_bitlocker_via_gpo/    

Please note: Information posted in the given link is hosted by a third party. Microsoft does not guarantee the accuracy and effectiveness of information.    

Can I see actual recovery of all laptops in Active Directory?    

Domain administrators can view the BitLocker recovery password by using the BitLocker Recovery Password Viewer.    

To complete the procedures in this scenario:    

https://learn.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-use-bitlocker-recovery-password-viewer    

If I enable GPO for all computers and all computers in this moment has got BitLocker enabled.    

If a Group Policy setting was changed after the initial BitLocker deployment in your organization, and then the setting was applied to previously encrypted drives), no change can be made to the BitLocker configuration of that drive except a change that will bring it into compliance.    

For your reference:    

https://learn.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-group-policy-settings    

Hope above information can help you.    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
