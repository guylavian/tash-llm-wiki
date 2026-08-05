---
title: "Exchange 2016 full NTLMv2"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2076625/exchange-2016-full-ntlmv2
question_id: 2076625
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2016 full NTLMv2

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2076625/exchange-2016-full-ntlmv2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I have a client who is switching to NTLM v1, and we would like to implement only NTLM v2. I started by changing the virtual directories (OWA, ECP, etc.).

I’m encountering an issue when trying to change OWA. I’m in basic authentication (checked but grayed out), and "enable forms-based authentication" was working well for our OWA users. However, when I switch to "integrated Windows authentication," I can’t get the authentication page in a login form format. Instead, I have a pop-up for Windows authentication, which confuses our users.

What are your methods for enabling NTLMv2 without using NTLMv1 and without "removing" the authentication pages on OWA?

Thank you in advance for your responses.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-24*

Hi,

Welcome to Microsoft Q&A community.

To enable NTLMv2 without using NTLMv1 and maintain the authentication pages on OWA, you can follow these steps:

Disable NTLMv1 and LM Protocols:

Ensure that NTLMv1 and LM protocols are disabled on both the client machines and the domain controllers. This can be done through Group Policy:

Navigate to Computer Configuration > Windows Settings > Security Settings > Local Policies > Security Options.

Set Network security: LAN Manager authentication level to Send NTLMv2 response only. Refuse LM & NTLM1.You can refer to:How to enable NTLM 2 authentication and,Stop using LAN Manager and NTLMv1!

Configure OWA for Integrated Windows Authentication:

In the Exchange Management Console, navigate to the OWA virtual directory.

Ensure that “Integrated Windows authentication” is enabled.

To avoid the pop-up and keep the forms-based authentication, you can use a combination of forms-based authentication and NTLMv2. This involves configuring the authentication settings in the web.config file of the OWA virtual directory.

Modify the web.config File:

Locate the web.config file for the OWA virtual directory (usually found in C:\Program Files\Microsoft\Exchange Server\V15\ClientAccess\owa).

Edit the web.config file to include the following settings under the <authentication> section:

```

  

  
    
  

```

This configuration allows you to use forms-based authentication while ensuring that NTLMv2 is used for authentication.

Test and Verify:

After making these changes, restart IIS using the command iisreset to apply the new settings.

Test the OWA login to ensure that users are presented with the forms-based authentication page and that NTLMv2 is being used for authentication.

By following these steps, you should be able to enable NTLMv2 without using NTLMv1 and maintain the authentication pages on OWA, providing a seamless experience for your users.
