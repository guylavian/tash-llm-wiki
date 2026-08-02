---
title: "software install with gpo with error 1376"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2188684/software-install-with-gpo-with-error-1376
question_id: 2188684
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
---
# software install with gpo with error 1376

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2188684/software-install-with-gpo-with-error-1376 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to run a batch file with GPO.

The GPO is 'Computer Configuration -> Policies -> Windows Settings -> Scripts -> Startup'

In the properties I have added a .cmd file. The .cmd file will install a .msi with additional parameters where one parameter is domain username and password.

The domain username and password is being used to run a service there is installed from the .msi file.

The .msi file is placed in \domain\netlogon

The GPO is linked to a test OU where I have placed a computer account for my test computer.

When I reboot the computer I can see the program is installed but when the service for the program needs to be started the installation rolls backup and leaves an almost empty folder under 'C:\Program Files'

In 'C:\Windows\Temp' there is a log file for the .msi and here I can see "A system error 1376 occurred. The specified local group does not exist."

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-24*

Hello 

Good day!  

You can try to export the group policy result and check if there is any error about this software installation gpo.

For checking Computer Configuration within gpresult, we can follow steps below.

Logon this machine using administrator account.

Open CMD (run as Administrator).

Type gpresult /h C:\gpo.html and click Enter.

Open gpo.html and check gpo setting under "Computer Details".  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-23*

Haven't be able to

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-23*

Hello   

In 'C:\Windows\Temp' there is a log file for the .msi and here I can see "A system error 1376 occurred. The specified local group does not exist."  

A: Did you try to find "what the specified local group" mean?  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-23*

The user do exist. It is a domain user.

The same .cmd file is working when I run the .cmd file manually.

I can also verify the user works by restarting the service on computer where I ran the .cmd manually.
