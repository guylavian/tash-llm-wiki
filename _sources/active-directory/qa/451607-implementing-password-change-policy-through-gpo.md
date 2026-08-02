---
title: "Implementing Password change policy through GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/451607/implementing-password-change-policy-through-gpo
question_id: 451607
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Implementing Password change policy through GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/451607/implementing-password-change-policy-through-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to implement the password policy through AD by GPO from my. windows servers 2016, but the user machines will only be able to talk with AD over VPN.   

So, just wanted to check that what will happen if policy is pushed to user machines when they connected to VPN but then if user didn't change the password even after several reminders, so what will happen in this case?. Suppose, if system is locked out with password expiration and user isn't able to connect via VPN.   

Thanks in advance for the support.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-30*

Hi，  

Thanks for your reply and waiting.  

Are you sure that the GPO has been applied? You can share the results of the successful application with us.  

We can first determine his application  

Hope this information can help you  

Best wishes  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-28*

By default, to set common requirements for user passwords in the AD domain the Group Policy (GPO) settings  are used. The password policy of the domain user accounts is configured in the Default Domain Policy. This policy is linked to the root of the domain and must be applied to a domain controller with the PDC emulator role.  

To configure the AD account password policy, open the Group Policy Management console (gpmc.msc);  

Expand your domain and find the GPO named Default Domain Policy. Right-click it and select Edit;  

Password policies are located in the following GPO section: Computer configuration-> Policies-> Windows Settings->Security Settings -> Account Policies -> Password Policy;  

Double-click a policy setting to edit it. To enable a specific policy setting, check the Define this policy settings and specify the necessary value (on the screenshot below, I have set the minimum password length to 8 characters). Save the changes;  

The new password policy settings will be applied to all domain computers in the background in some time (90 minutes), during computer boot, or you can apply the policy immediately by running the gpupdate /force command.  

You can change the password policy settings from the GPO Management console or by using the PowerShell cmdlet Set-ADDefaultDomainPasswordPolicy:  

Set-ADDefaultDomainPasswordPolicy -Identity woshub.com -MinPasswordLength 10 -LockoutThreshold 3  

reference：http://woshub.com/password-policy-active-directory/  

Hope this information can help you  

Best wishes  

Vicky

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-06-26*

Hi,  

In my opinion, the scenario you are referring has nothing to do with new password policy as it happens in normal situation as well. For example, in default domain policy password expiry is set for a period of xx days and notification also set to xx in advance reminding users to change their password. Now in working from home situation, user would use his/her (cached) password to logon to laptop as long as they are not connected vpn. However, as and when trying to connect to vpn, if the password is expired by the time, he/she won't be allowed to connect remotely as it would prompt again and again because password is expired already.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-06-25*

Hi,  

When the password is expired ,the user have to change it's password to be authenticated. To change password the user must use a machine able to communicate to domain controller with PDC role.  

So if the user is connected through VPN and the network flow is not opened between the VPN subnet and the domain controller with PDC role , the user will be unable to logon withe the password will be expired.  

Please don't forget to mark this reply as answer if it help you to resolve your issue
