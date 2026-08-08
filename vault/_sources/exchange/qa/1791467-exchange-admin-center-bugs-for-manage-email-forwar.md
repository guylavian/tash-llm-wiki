---
title: "Exchange admin center bugs for manage email forwarding"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1791467/exchange-admin-center-bugs-for-manage-email-forwar
question_id: 1791467
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Exchange admin center bugs for manage email forwarding

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1791467/exchange-admin-center-bugs-for-manage-email-forwar (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have set up the email forwarding in the Exchange Admin Center, where it is mentioned that "The mailbox owner will not be able to view and change this forwarding address."  

But I found that user logging into their mailbox can see which destination email it is being forwarded to, and they are able to turn it off. 

then i tried the PowerShell command advised by community but it is still did not work,

Set-Mailbox -Identity <User ID> -DeliveryToMailboxAndForward $False -ForwardingAddress $Null

What should I do so that users cannot view or make any changes to the email forwarding set by the admin?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-02*

Hi, STKM2024

Based on your description, I understand that the mailbox owner should not have been able to view and modify the forwarding address after setting up the forwarding feature, but this is not the case.

After my tests, when the forwarding function is turned on in the EAC, it is shown in the following figure. The mailbox owner will not receive messages that need to be forwarded, and there will be no errors. This is probably the best outcome you want.

But in OWA, if the mailbox owner turns on the forwarding feature as shown in the image below, then something strange happens.

At this point, the mailbox owner will be able to receive the message that needs to be forwarded and will be able to view and modify the forwarding function, which is consistent with the situation in the thread you gave it.

When I turned off forwarding for the mailbox owner in OWA, everything was back to normal again. Therefore, it is recommended that you check and try disabling the forwarding feature in OWA. After the EAC setup is complete, this operation does not affect the mail forwarding functionality.

In addition, for you to give the cmdlet, I need to clarify the following.

If the value of -ForwardingAddress is $null, the forwarding email address is not configured, that is, the message cannot be forwarded to the specified mailbox, and this cmdlet may not work. For more information about this cmdlet, please refer to Vasil Michev.

If my answer is helpful to you, please mark it as the answer so that other users can refer to it. Thank you for your support and understanding.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-07-02*

It's the other way around. The user can see/manage forwarding set via the ForwardingSMTPAddress parameter, so that's the one you need to null. Here's (a bit old) article where I've explained the difference between the two: https://www.enowsoftware.com/solutions-engine/m365-exchange-online-center/simplified-forwarding-settings-in-office-365
