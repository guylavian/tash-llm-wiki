---
title: "Exchange account gets locked out several times a day"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2042934/exchange-account-gets-locked-out-several-times-a-d
question_id: 2042934
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange account gets locked out several times a day

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2042934/exchange-account-gets-locked-out-several-times-a-d (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Community,

I have a 2019 Exchange Server (on premise) with roughly a 100 users.  

For no reason that I know of, 1 users keeps getting locked out in AD.  But she can still log on if her computer goes offline, reboots, goes to sleep.  But her Microsoft Outlook 2021 software will ask for password and refuse to get her connected to exchange server.   

If shes working, she will get locked out of her outlook software, her outlook will disconnect from exchange and ask for password which will never work until I unlock in AD Users and Computers.

Once unlocked, it works for 10-20-60 minutes...until next time.

I have some knowledge of servers, tried to google it, did some test.  

Also, she has outlook on her Iphone, which wont disconnect when outlook on her computer locks out.  That will be her only way of getting her emails.  They will still be available, and connected.

Hope i can find an answer or help to find a solution to my problem.

Thanks

Ian

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-09-06*

There can be a few possible causes-

You can check the saved credentials if it is old or incorrect.

If you have hybrid setup, make sure the password is synced correctly between AD and office 365.

You can also check the Active Directory logs: Event Viewer > Security Logs to identify the cause.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-06*

Hi @ian bougie  ,

Welcome to the Microsoft Q&A platform!

 

Based on your issue description, you're experiencing an issue with a user account lockout. Here are some steps you can take to troubleshoot and hopefully resolve the problem:

1.Identify the Source of Lockouts:

-  Use the Event Viewer on your domain controllers to look for Event ID 4740, which logs account lockout events. This can help you identify which device or service is causing the lockouts.

-  You can also use tools like LockoutStatus.exe or Netwrix Account Lockout Examiner to track down the source of the lockouts.

2.Check for Cached Credentials:

-  Ensure that there are no old or incorrect credentials cached on her devices. This includes her computer, any mapped network drives, and any other devices that might be trying to authenticate with her old credentials.

3.Examine ActiveSync Devices:

-  Since her iPhone remains connected, it might be worth checking if there are any other devices trying to connect using outdated credentials. You can use the Get-ActiveSyncDeviceStatistics cmdlet in Exchange PowerShell to list all devices associated with her account.

4.Update Passwords:

-  Make sure that her password is updated on all devices and services she uses. Sometimes, a device with an old password can repeatedly attempt to authenticate, causing the account to lock.

5.Audit Logon Events:

-  Set up an audit policy to track logon events. This can help you identify any suspicious activity or failed logon attempts that might be causing the lockouts.

6.Check for Malware:

-  Run a malware scan on her computer to ensure that there is no malicious software attempting to use her credentials.

7.Review Group Policies:

-  Ensure that your Group Policies are correctly configured and not causing unintended lockouts.

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang
