---
title: "delete LDAP address on outlook"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4655657/delete-ldap-address-on-outlook
question_id: 4655657
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 1
qa_tags: ["active-directory", "office-outlook-platform-windows-classic-outlook-windows-home", "windows-server", "windows-server-powershell"]
---
# delete LDAP address on outlook

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4655657/delete-ldap-address-on-outlook (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are going to perform Securemail active users cleanup, who were not using the functionality for many months. When we deleted the user, the LDAP autoenrollment settings which stored in user machine runs automatically and they can able to send and receive the encrypted email. So we need a script which will remove the LDAP configuration settings in those users machine

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-14*

Hello KV Kalpana .

Thank you for posting in Microsoft Community! We are happy to assist.

Based on your description you want to remove the LDAP configuration on certain machines in your domain. Kindly explain further if this is not the case.

This part of the Microsoft Q&A is dedicated to Outlook support. Hence, we do not have the appropriate resources to answer your question. Your inquire is better served via Microsoft Q&A Windows Server, Microsoft Q&A Active Directoryand Microsoft Q&A Windows Server PowerShell

Meanwhile, kindly check Set-CertificateAutoEnrollmentPolicy | Microsoft Learn and How to enable LDAP signing in Windows Server | Microsoft Learn  

Define mail flow rules to encrypt email messages | Microsoft Learn

You can also try using the credential manager cmdlet to remove the stored credentials forcing the user to re-sign in while will update their policies which you can update via the admin panel

I hope the above information will be helpful. Please feel free to let me know if you have any other concern or if I get you wrong. Glad to assist you. We sincerely appreciate your patience and cooperation. Thanks for your precious time!

Note: Please understand that our initial reply may not always immediately resolve the issue. However, with your help and more detailed information, we can work together to find a solution.

Best regards

Community Moderator

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-12*

Hello Eleni,

Thanks for your response.

We have created a script for de-enrollment. As a part of script, we need to know the ldapregpath. Could you please provide us the solution for how it can be found!

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-08*

yes, I need to remove ldap addresslist from outlook with script.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-08*

Hello KV Kalpana .

Thank you for posting in Microsoft Community! We are happy to assist.

Based on your description you want to remove the LDAP configuration on certain machines in your domain. Kindly explain further if this is not the case.

Let's work together to have this challenge resolved ASAP.

This part of the Microsoft Q&A is dedicated to Outlook support. Hence, we do not have the appropriate resources to answer your question. Your inquire is better served via Microsoft Q&A Windows Server, Microsoft Q&A Active Directoryand Microsoft Q&A Windows Server PowerShell

Meanwhile, kindly check Set-CertificateAutoEnrollmentPolicy | Microsoft Learn and How to enable LDAP signing in Windows Server | Microsoft Learn

I hope the above information will be helpful. Please feel free to let me know if you have any other concern or if I get you wrong. Glad to assist you. We sincerely appreciate your patience and cooperation. Thanks for your precious time!

Note: Please understand that our initial reply may not always immediately resolve the issue. However, with your help and more detailed information, we can work together to find a solution.

Best regards

Community Moderator

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-07*

Hello KV Kalpana .

Good day. Thank for posting in the community.

We've received your query and you can expect to receive response from one of our community moderator accordingly.

At this point, we appreciate your patience and cooperation. Thank you.

Sincerely,

Community moderator
