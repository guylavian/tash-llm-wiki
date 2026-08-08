---
title: "Change exchange 2016 Hybrid"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1848279/change-exchange-2016-hybrid
question_id: 1848279
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Change exchange 2016 Hybrid

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1848279/change-exchange-2016-hybrid (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

If you are using Exchange 2016 hybrid but only for cloud mailbox management and outbound relay, is it "worth" switching in Exchange 2019 hybrid hosting?

More details: Recently, someone helped us set up Azure AD Connect and Exchange 2016 Hybrid for cloud mailbox setup and relay outbound from copiers and legacy applications. Except for SMTP authentication, no client or service has accessed the hybrid host (which is also an internal outbound to EXO). We do not have any public folders or anything else that may have been owned by others previously hosted on local Exchange. We do manage the distribution list internally, but synchronize it through AADConnect. That person has left, and I have been keeping track of cumulative updates and ensuring smooth operation of AADConnect and EX2016 hybrid.

The extended support for Exchange 2016 will end in October 2025. Now, Exchange 2019 CU12 comes with a free hybrid license and supports Windows 2022 Server, and I can't judge if it's worth the risk of switching it in for future proof protection.

Since I did not directly set up the initial environment, I'm concerned I'm over-simplifying what would be needed. My understanding of the process is as follows:

-  Leave EX2016 alone: On a separate host, install Windows 2022 and Exchange 2019 CU12 - this process obviously involves extending the AD schema for EX2019

-  Run the latest online Hybrid Configuration Wizard ("HCW") just long enough to get the free license

-  Configure 3rd party SSL cert, (re)create receive connectors, test relay out from internal apps

-  Re-run HCW, continue through to transfer the connection to this new EX2019 host versus EX2016 one

Things I don't know:

-  Whether we must export the certificate(s) from 2016 and import to 2019 manually, or does HCW handle using the current cert on the 2019 box

-  Whether HCW pulls in prior receive connector or any other useful settings from EX2016 to EX2019

-  Whether we need to re-run the separate AADConnect setup again after the hybrid host changes

-  Which MS entity handles support? Exchange Online support does not include Hybrid questions (even though we are only using a Hybrid box for EXO relay and cloud mailbox connectivity). Since we don't host on-prem Exchange, that team also does not handle support.Since I did not directly set up the initial environment, I'm concerned I'm over-simplifying what would be needed. My understanding of the process is as follows:

-  Leave EX2016 alone: On a separate host, install Windows 2022 and Exchange 2019 CU12 - this process obviously involves extending the AD schema for EX2019

-  Run the latest online Hybrid Configuration Wizard ("HCW") just long enough to get the free license

-  Configure 3rd party SSL cert, (re)create receive connectors, test relay out from internal apps

-  Re-run HCW, continue through to transfer the connection to this new EX2019 host versus EX2016 one

  Things I don't know:

-  Whether we must export the certificate(s) from 2016 and import to 2019 manually, or does HCW handle using the current cert on the 2019 box

-  Whether HCW pulls in prior receive connector or any other useful settings from EX2016 to EX2019

-  Whether we need to re-run the separate AADConnect setup again after the hybrid host changes

-  Which MS entity handles support? Exchange Online support does not include Hybrid questions (even though we are only using a Hybrid box for EXO relay and cloud mailbox connectivity). Since we don't host on-prem Exchange, that team also does not handle support.

  If someone has made a 'swap' from 2016 to 2019, please let me know how far away I am from the base.  I know I have time - another obvious plan is to reduce any need for internal relays in the next two years, while more and more traditional applications and devices are catching up with the changes in SMTP authentication (such as OAuth). thank you!

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-31*

Hi @Adele Vance,

Welcome to the Microsoft Q&A platform!

Based on your description, I understand there are some concerns about update Exchange 2016 to 2019 in hybrid.

For these concerns, I have the following to share with you. You may need to export your SSL certificates from the Exchange 2016 server and import them to the Exchange 2019 server. The HCW does not automatically handle SSL certificate transfer. 

Also, you will need to manually recreate the connectors on the Exchange 2019 server. The HCW does not import these settings from the Exchange 2016 server automatically either. And there is no need to reconfigure AADConnect when you change your hybrid server. 

Also, I found a detailed hybrid upgrade guide for your reference: How to Upgrade Exchange Hybrid Server 2016 to 2019? (linkedin.com). (Please note that the link is not an official Microsoft document and is for reference purposes only.)

Moving to Exchange 2019 is a good step to extend support and compatibility. If reducing the need for internal relays as you said is an option, it may eliminate the need for on-premises Exchange entirely, moving to a full cloud solution.

If the answer is helpful, please click "Accept Answer" and kindly upvote it.
