---
title: "ADFS retrieving claims using native client application"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1791440/adfs-retrieving-claims-using-native-client-applica
question_id: 1791440
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["developer-technologies-csharp", "developer-technologies-dotnet-other-l1", "microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# ADFS retrieving claims using native client application

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1791440/adfs-retrieving-claims-using-native-client-applica (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We are currently attempting to write a test application in C#, which needs to retrieve certain claims upon authorization. No matter what we have tried, it seems we only receive the same 10 claims from the ADFS server (see image for the received claims) . We are using .NET Framework 4.8, is this a forum to ask code related questions? If so I could post what code we have.

Thank you.

G Niles

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-07-15*

Hi @G_Niles  ,   

There are default claims that are sent to the app if there are no additional claims configured via "Edit Claim Issuance Policy" in ADFS console.

If you need to configure any additional attribute to be provided for successful authentication/authorization, please feel free to configure it through "Edit Claim Issuance Policy" in ADFS console.

Also, when you're configuring additional claims, these claims needs to follow some "logic" in process, so please let me know which attributes you need to receive from AD, so I can help you with.  

Best regards,  

JJ

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-02*

Hi @G_Niles  , Welcome to Microsoft Q&A,

Make sure that the correct claim rules are configured in ADFS to publish the claims you need. You can check and configure by following the steps below:

-  Open the ADFS Management Console.

-  Navigate to Relying Party Trusts.

-  Select your application and click Edit Claim Rules.

-  In the Sending Rules tab, check the existing claim rules. If you need to add new claim rules, you can click the Add Rule button and follow the wizard.

Check your application's `web.config` or `app.config` file to make sure it is configured correctly. Pay special attention to the following points:

-  `wsFederation` configuration section

-  `identityConfiguration` configuration section

Make sure the claim type (URI) is correct. For example:

```

  
    
    
  

  
    
    
  

```

Best Regards,

Jiale

If the answer is the right solution, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
