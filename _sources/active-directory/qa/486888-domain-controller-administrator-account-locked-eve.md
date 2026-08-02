---
title: "Domain Controller Administrator Account Locked Event ID"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/486888/domain-controller-administrator-account-locked-eve
question_id: 486888
fetched: 2026-07-25
answer_count: 8
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Domain Controller Administrator Account Locked Event ID

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/486888/domain-controller-administrator-account-locked-eve (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

We have Domain Controller & Additional Domain controller in our environment. From last few days false event ID 4740 getting generated continuously for every second for Domain controller Administrator ID. Administrator account is not getting locked but event ID 4740 getting generates in Security event. We have not used administrator account for any service.    

    

Thanks & Regards,    

Sachin Shinde

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-28*

Hi Sachin,    

Thank you so much for your kindly reply.    

Yeah, as mentioned in the first response, the built-in administrator account will not be locked out. So in our case, the account is not getting locked out but there will be event 4740 recorded for the account.     

We are trying to figure out why there is event 4740 for this account. Normally there should be no false event IDs. If there is event recorded for the account, it should be triggered by some operations.     

Normally, the reason the user is locked is that a certain process (caller process) on a certain machine (caller computer) stores the user's wrong credential, and this process uses the wrong credential to initiate authentication requests to domain controllers. After reaching a certain number of times(Account lockout Threshold), our account will be locked. (It will not be locked out for the built-in admin account.)    

Now we have found out the caller computer. Then we logon to the caller computer and if we have configured audit policy as Audit Logon Events – Failure, we can filter 4625 event in security. From 4625, generally we could trace the process name. And check following possible cause.    

a. Stored user names and passwords in credential manager    

b. Persistent drive mappings.     

c. Scheduled tasks.     

d. Third-party application stored the wrong password.    

e. Clear logon session by running the following command:    

Get-WmiObject Win32_LogonSession | Where-Object {$.AuthenticationPackage -ne 'NTLM'} | ForEach-Object {klist.exe purge -li ([Convert]::ToString($.LogonId, 16))}    

f. Use PStool to check if there’s any cache password in system:    

	i. Download PsExec.exe from http://technet.microsoft.com/en-us/sysinternals/bb897553.aspx and copy it to C:\Windows\System32.    

	ii. From a command prompt run:    psexec -i -s -d cmd.exe    

	iii. From the new DOS window run:  rundll32 keymgr.dll,KRShowKeyMgr    

	iv. Clear the cache in it.  

    

For any question, please feel free to contact us.    

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-28*

Hi,  

Yes failure code is 0x18, but actually account is not getting locked. Parrot (Admin ID) is not at all getting locked but only it generates event ID 4740 for this account. My concern is only that why it is generating false event IDs for this account.  

Thanks,  

Sachin Shinde

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-27*

Hi,  

Yes event ID 4771 is around to event ID 4740. No event ID for 4776. Caller computer name is Domain controller.  

Thanks,  

Sachin Shinde

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-27*

Hi,    

Still getting events for 4740 without locking admin account.    

    

We have renamed Administrator account to Parrot while implementation 2-3 years before. No password changed recently or password policy applied for User container (OU).    

Thanks,    

Sachin Shinde

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-23*

Hello @Sachin Shinde  ,    

Thank you so much for posting here.    

The built-in domain administrator account will not be locked out actually. It still could be successfully logged in as soon as the correct password is used.    

I did the test in my lab. Configured the account lockout policy as shown below. Logged on to the BDC with the domain admin account and typed the wrong password many times. There were events logged on the BDC as shown below.    

    

    

Then on the PDC, I could see the event ID 4740 and 4771. Even though there is event 4740, the admin account could still be logged in as soon as the correct password is used.    

    

Please note that only the built-in administrator account will not be locked out.     

Have we made any changes from last few days, such as changing the password of this account?    

Next to event 4740, could we find the event ID 4771 or 4776? If we could find the event 4771, then we could find out the failure code.     

For more information about event 4771, please refer to:     

https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4771    

For any question, please feel free to contact us.    

Best regards,    

Hannah Xiong
