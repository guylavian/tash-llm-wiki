---
title: "Run .bat from GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/113038/run-bat-from-gpo
question_id: 113038
fetched: 2026-07-25
answer_count: 9
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Run .bat from GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/113038/run-bat-from-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I'm trying to run a .bat from the machine gpo to save the bitlocker key in AD but it doesn't work.    

If I run it locally it works perfectly. All users are local administrators of their machines.    

What may be failing?? Other .bat files work without problems    

    

```
manage-bde -protectors -get c:  
for /f "skip=4 tokens=2 delims=:" %%g in ('"manage-bde -protectors -get c:"') do set MyKey=%%g  
manage-bde -protectors -adbackup c: -id%MyKey%
```

Thanks!!!

## Answer (community) — community member

*upvotes: 1 · updated: 2020-10-02*

Hello,    

You are welcome. Thank you so much for your kindly reply.    

We have searched for these articles. Hope they could be of some help to you.     

Enabling BitLocker with Group Policy and backing up Existing BitLocker recovery keys to Active Directory    

https://www.winsysadminblog.com/2019/08/enabling-bitlocker-with-group-policy-and-backing-up-existing-bitlocker-recovery-keys-to-active-directory/    

How to backup recovery information in AD after BitLocker is turned ON in Windows 7    

https://learn.microsoft.com/en-us/archive/blogs/askcore/how-to-backup-recovery-information-in-ad-after-bitlocker-is-turned-on-in-windows-7    

Please note: Information posted in the given link is hosted by a third party. Microsoft does not guarantee the accuracy and effectiveness of information.    

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2020-10-02*

1 was the script tested with the same account it would run under when run as startup script? I doubt that. That would be the system account and you would have to run it like that from an elevated command prompt: psexec -s -i \server\share\bit.bat  

Try that and see if it works.  

2 are you aware that startup scripts don't run by default on a normal shutdown and startup process? That's because of fast startup. Read my article about it: https://www.experts-exchange.com/articles/25279/Overcoming-software-deployment-pitfalls-on-modern-Windows.html?preview=iJYI%2BBCVtNk%3D  

Better would be to deploy an immediate scheduled task.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2020-09-30*

Capture stdout and stderr and see what error it encounters. Like this.  

```
md c:\temp
@echo Starting %date% %time% 1> c:\temp\Save-BL-Key.log
manage-bde -protectors -get c:  1>> c:\temp\Save-BL-Key.log  2>&1  
for /f "skip=4 tokens=2 delims=:" %%g in ('"manage-bde -protectors -get c:"') do set MyKey=%%g
manage-bde -protectors -adbackup c: -id%MyKey%   1>> c:\temp\Save-BL-Key.log  2>&1
@echo Ending %date% %time% 1>> c:\temp\Save-BL-Key.log
```

Just another thought... what event triggers it's execution? Are you sure it even running?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-01*

Hello,    

Thank you so much for posting here.    

According to our description, the script could run locally and it works perfectly. Since it is configured via GPO, we could have a check whether the configuration is correct and whether the GPO is applied successfully to the machines.     

Have we created an OU and add the machines to this OU? Besides, have we linked the GPO to this OU?    

We could check by running “gpresult /h” to get a detailed group policy result report, then check if the specific settings get applied or not.      

For computer configuration:      

Logon one machine and open CMD, run as administrator. Type gpresult /h C:\report.html and click Enter. Open report file to check the policies under Computer Details.      

For any question, please feel free to contact us.    

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
