---
title: "Azure AD Connect - cannot configure and install"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5259632/azure-ad-connect-cannot-configure-and-install
question_id: 5259632
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 3
qa_tags: []
---
# Azure AD Connect - cannot configure and install

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5259632/azure-ad-connect-cannot-configure-and-install (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I had "successfully" running AD Connect (password hash sync) with my on-premise AD with version 2.0.3.0.

When I try install version 2.1 or above of AD Connect I received this error. Only I can install version 2.0.3.0 or below.

I check all thinks, like permissions of the global admin and enterprise admin and only received this error in specific ad connect version.

[ 27] [ERROR] ConfigSyncDirectoriesPage: Caught exception while creating the connector for directory: "localdomain"

Exception Data (Raw): System.Management.Automation.CmdletInvocationException: Failed to retrieve schema.<error><error><incident><connection-result>failed-authentication</connection-result><date>2023-09-05 15:25:04.318</date><server>localdomain389</server><cd-error><error-code>0x31</error-code> 

<error-literal>Invalid Credentials</error-literal> 

</cd-error></incident></error></error> ---> Microsoft.IdentityManagement.PowerShell.ObjectModel.SynchronizationConfigurationValidationException: Failed to retrieve schema.<error><error><incident><connection-result>failed-authentication</connection-result><date>2023-09-05 15:25:04.318</date><server>"localdomain":389</server><cd-error><error-code>0x31</error-code> 

<error-literal>Invalid Credentials</error-literal> 

</cd-error></incident></error></error>

than you for help

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-05*

Dear Fred VXI

Good day! Thank you for posting to Microsoft Community. We are happy to help you!

First of all, we apologize for the trouble and inconvenience caused to your work! Based on your description, since your problem is related to on-premise, and since we are focused on technical support for Microsoft 365 Business Exchange Online, which is not professional for local Exchange servers. For local Exchange server incident, to help you better and not waste more time, I recommend that you ask questions (based on) in **** Microsoft Q&A forum (using Exchange server tag). Technical engineers over there specialize in local Exchange-related issues, and experts will focus on queries to further assist you.

Thanks in advance for your understanding! Your patience and cooperation will be highly appreciated. Hope you all the best!

Sincerely,

Kerry Chen | Microsoft Community Moderator
