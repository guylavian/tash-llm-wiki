---
title: "HMA with ActiveSync won't work with Exchange Server 2019 CU14 HU April but work with CU14 SU March"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1792037/hma-with-activesync-wont-work-with-exchange-server
question_id: 1792037
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online", "office-exchange-other-l1"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# HMA with ActiveSync won't work with Exchange Server 2019 CU14 HU April but work with CU14 SU March

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1792037/hma-with-activesync-wont-work-with-exchange-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I have deployed two environments with similar configuration : Exchange 2019 CU14 Hybrid with Exchange Online / Intune.

HMA is implemented on-premises to allow Outlook mobile clients to access on-premises mailboxes using Modern Authentication : On the first environment it works well, but not on the second . Both on-premises platform are exactly the same.. 

Modern Auth with Outlook works well, the Test-OauthConnectivity works well however the online https://testconnectivity.microsoft.com and the script Test-HMAEAS.ps1 aren't working on the second platform. Below the error for both.

I already rotated the oAuth certificate, re-did the HMA configuration , re-ran the HCW again and again , checked the vdir and IIS configuration ,compared it with the working environment making sure that there is no differences but no luck - HMA with EAS doesn't work - Does anyone ever experienced the same type of  error ? Help! :) 

Below the output of the script Test-HMAEAS.ps1 :

Installing Microsoft.IdentityModel.Clients.ActiveDirectory package. Please accept if prompted.

Loading Microsoft.IdentityModel.Clients.ActiveDirectory package

We sent an AutoDiscover Request to On-Premises for the Exchange ActiveSync Virtual Directory and below is the response

The response should contain the Protocol ActiveSync with a valid URL

https://mail.dummy.uk/Microsoft-Server-ActiveSync

We sent an Empty Bearer Token Request to the On-Premises Exchange ActiveSync Virtual Directory and below is the response

The response should contain a valid WWW-Authenticate=Bearer. Make sure the authorization_uri is populated

request-id=d7782c63-6efc-4ab0-a672-0c70aa4a8616

x-ms-diagnostics=4000000;reason="Flighting is not enabled for domain 'mail.dummy.uk'.";error_category="oauth_not_available"

X-OWA-Version=15.2.1544.11

X-FEServer=DUMMY01

WWW-Authenticate=Bearer client_id="00000002-0000-0ff1-ce00-000000000000", trusted_issuers="00000001-0000-0000-c000-000000000000@1d3c9b43-0d0f-45d9-a207-99dc10fb7d4a", token_types="app_asserted_user_v1 service_asserted_app_v1", error="invalid_token",Basic realm="mail.dummy.uk"

Date=Wed, 03 Jul 2024 08:47:22 GMT

Content-Length=0

Set-Cookie=TS01a32329=014c63c9bbf67b987817fa56842b27340810fae5eeb381ade45aea24fb7e2db5593712423d44b0577512242e52380440c4472e2e7b; Path=/

TS01a32329=014c63c9bbf67b987817fa56842b27340810fae5eeb381ade45aea24fb7e2db5593712423d44b0577512242e52380440c4472e2e7b=

Autodetect has the following services listed for the user

This should have AAD pointing to Microsoft Online and On-Premises to the correct EAS URL

Service:

Protocol:    eas

Hostname:    mail.dummy.uk

Azure AD:

On-Premises:

Error:

Below the testconnectivity.microsoft.com to test Outlook Mobile with HMA :

Testing Outlook Mobile Hybrid Modern Authentication (HMA) for SMTP email address: ******@dummy.uk.

Testing Outlook Mobile Hybrid Modern Authentication (HMA) failed.



Test Steps

Sending an Autodiscover request to the on-premises Exchange Autodiscover service: https://autodiscover.dummy.uk/autodiscover/autodiscover.json?Email=******@dummy.uk&Protocol=activesync&RedirectCount=3.The on-premises Exchange Autodiscover service returned a valid response that passed analysis.Test Steps

Sending an empty Bearer token request to the on-premises Exchange ActiveSync (EAS) virtual directory: https://mail.dummy.uk/Microsoft-Server-ActiveSync.The on-premises Exchange ActiveSync virtual directory didn't return a valid response.Test StepsSending an empty Bearer token request to the on-premises Exchange ActiveSync (EAS) virtual directory: https://mail.dummy.uk/Microsoft-Server-ActiveSync.The on-premises Exchange ActiveSync (EAS) virtual directory returned a valid response.Additional DetailsA valid EAS Bearer token response was successfully received. HTTP Response Headers: request-id: 8f2514fe-ba3e-4105-9c35-0a276e75331b x-ms-diagnostics: 4000000;reason="Flighting is not enabled for domain 'mail.dummy.uk'.";error_category="oauth_not_available" X-OWA-Version: 15.2.1544.11 X-FEServer: DUMMY01 WWW-Authenticate: Bearer client_id="00000002-0000-0ff1-ce00-000000000000", trusted_issuers="00000001-0000-0000-c000-000000000000@1d3c9b43-0d0f-45d9-a207-99dc10fb7d4a", token_types="app_asserted_user_v1 service_asserted_app_v1", error="invalid_token" WWW-Authenticate: Basic realm="mail.dummy.uk" Date: Wed, 03 Jul 2024 07:44:30 GMT Content-Length: 0 Set-Cookie: TS01a32329=014c63c9bb8e44d8d23faf280300687b2f9a4f6aad2aa85b15a4fe95ab95203d10986335451a0e90fec960e730f2b5bb4ef9dfe28b; Path=/ Analyzing the Bearer token response from the on-premises Exchange ActiveSync (EAS) service.Analyzing the Bearer token response from the on-premises Exchange ActiveSync (EAS) service failed. Tell me more about this issue and how to resolve itAdditional DetailsThe Bearer response header did not contain the expected authorization URL value https://login.windows.net/common/oauth2/authorize. Please check that your on-premises environment meets the minimum requirements for Hybrid Modern Authentication and try running the latest version of the Hybrid Configuration Wizard again. You may also inspect the OAuth configuration yourself by using the Get-AuthServer cmdlet in the on-premises Exchange Management Shell.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-09-03*

Hi there, we’re facing a similar issue. Do you have any updates on this matter?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-09-03*

Hi, anyone found a solution to this issue ? Extended protection not enabled by the way

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-29*

Hello, we have same issue on same version

do you managed to solve it somehow? o with update?

tnx

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-07-03*

Extended Protection and HMA dont always play well together. 

Have you looked at this?

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/security-best-practices/exchange-extended-protection?view=exchserver-2019#extended-protection-cant-be-fully-configured-on-exchange-servers-that-are-published-using-hybrid-agent
