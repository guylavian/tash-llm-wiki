---
title: "how to repair secure channel for domain controllers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2186804/how-to-repair-secure-channel-for-domain-controller
question_id: 2186804
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 8
qa_tags: []
---
# how to repair secure channel for domain controllers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2186804/how-to-repair-secure-channel-for-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am getting wrong username or password while trying to repair the secure channel between Parent domain controller and child domain controller, I reset the password but the DC seems to forget it or not register it since I keep getting the error.

The trusts also went down due to this issue and now users can't login across domains. It was working fine up to about a month or so, then little by little it has been deteriorating to this point. Everything I have tried has failed up to now.

Thanks

## Answer (community) — community member

*upvotes: 3 · updated: 2024-02-01*

Hello Enrique Esqueda,

Thank you for posting on the Microsoft Community Forum.

To repair the secure channel between Parent domain controller and child domain controller, you can try the following steps:  

Method 1

-  On the child domain controller, open Command Prompt as an administrator.

-  Type the following command and press Enter: nltest /sc_verify:domain_name

Method 2

-  If the command returns an error message, try resetting the secure channel password by typing the following command and pressing Enter: nltest /sc_reset:domain_name

-  If the reset is successful, you should see a message that says "The secure channel reset on domain_name is successful".

For method 1 and 2, please refer to link below: Nltest | Microsoft Learn.

Method 3

You can run Reset-ComputerMachinePassword within a Powershell v4.0 console and have your secure channel fixed.

Method 4

Now you can reset the computer password using the command below on problematic (child domain controller):

netdom resetpwd /s:PDC Name /userd:Domain\User /password:Password  

Note: PDC: is the PDC in the root domain, domain is the root domain and user is the administrator in the root domain and its password.

As an example the command will look like this:  

netdom resetpwd /s:DC1 /userd:Contoso\administrator /password:P@ssw0rd

Reboot the machine and enable the KDC service and have your broken secure channel fixed.  

For method 3 and 4, please refer to link below:  

Detailed Concepts: Secure Channel Explained | Microsoft Learn

Method 5

If the reset fails, you may need to check the DNS settings on both the parent and child domain controllers to ensure they are pointing to the correct DNS servers.

Method 6

There may also be a network issue, elevated at the command prompt on a domain member computer, Nltest.exe /sc_change_pwd:[<DomainName>] Secure Channel Problems Detected - Windows Server | Microsoft Learn

I hope you the information above is helpful.

If you have any questions or concerns, please do not hesitate to let us know.

Best Regards,

Daisy Zhou
