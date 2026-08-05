---
title: "I need to use Exchange ActiveSync(A) service to configure and send and receive third-party email 📭, which can only be configured through the mail module in the control panel of the system. Currently, I cannot open this module, please help me solve it"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1425436/i-need-to-use-exchange-activesync-a-service-to-con
question_id: 1425436
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# I need to use Exchange ActiveSync(A) service to configure and send and receive third-party email 📭, which can only be configured through the mail module in the control panel of the system. Currently, I cannot open this module, please help me solve it

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1425436/i-need-to-use-exchange-activesync-a-service-to-con (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need to use Exchange ActiveSync(A) service to configure and send and receive third-party email 📭, which can only be configured through the mail module in the control panel of the system. Currently, I cannot open this module, please help me solve it

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-11-15*

Hi @Healer,

Welcome to our Q&A forum!

Regarding your problem, currently you cannot run the Exchange ActiveSync service, right? Any detailed explanation or screenshot is great appreciate.

There could be several reasons why the service is not opening. Here are some possible solutions:

-  Verify Autodiscover is working for Microsoft Exchange ActiveSync: You can do this by browsing to the Microsoft Remote Connectivity Analyzer site and selecting Exchange ActiveSync Autodiscover from the Microsoft Exchange ActiveSync Connectivity Tests. Enter all the required fields and select Perform Test. If the Connectivity Test fails, see Analyze Exchange Remote Connectivity Analyzer Results. If it passes, see User Principal Name Check.

-  Check User Principal Name: Most Exchange ActiveSync devices request the email address and password to set up the device. This combination only works when the userprincipal name value matches the email address for the user. Verify these two attributes have the same value. To do this, open the Exchange Management Shell and run the following cmdlet to retrieve the attribute values: `Get-Mailbox user | fl UserPrincipalName,PrimarySmtpAddress`. If the UserPrincipalName does not match the PrimarySmtpAddress for the user, see Domain suffix check.

-  Check Domain Suffix: Verify that the appropriate domain suffix is available for the UserPrincipalName attribute.

-  Disable/Quit all of your firewall and security software that may affect/stop the service running.

reference: https://learn.microsoft.com/en-us/exchange/troubleshoot/client-connectivity/troubleshoot-activesync-with-exchange-server

Hope it can help, please feel free to let us know if any updates.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
