---
title: "Morden authentication oauth Exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2044891/morden-authentication-oauth-exchange-2019
question_id: 2044891
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Morden authentication oauth Exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2044891/morden-authentication-oauth-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Team,

I have completed all the necessary steps to configure modern authentication with an on-premises Exchange 2019(not online) server using ADFS 2019. While OWA and ECP are redirecting as expected, I'm encountering an issue with Outlook on Windows 11. When I try to sign in, it redirects me to the ADFS URL but does not accept my credentials. Instead, the login window continuously reloads, prompting me to sign in again on same page.

On my client machine i i am getting error event viewer.

Error

Error: 0xCAA20003 Authorization grant failed for this assertion.

Code: invalid_grant

Description: MSIS9615: The refresh token received in 'refresh_token' parameter has expired.

TokenEndpoint: https://adfs.mydomain.com/adfs/oauth2/token

Logged at OAuthTokenRequestBase.cpp, line: 452, method: OAuthTokenRequestBase::ProcessOAuthResponse.

Request: authority: https://adfs.mydomain.com/adfs, client: d3590ed6-52b3-4102-aeff-aad2292ab01c, redirect URI: ms-appx-web://Microsoft.AAD.BrokerPlugin/d3590ed6-52b3-4102-aeff-aad2292ab01c, resource: https://hcmail.mydomain.com/, correlation ID (request): 4c3316af-5fa2-4002-9b42-4418a2fe62f3

Warning

Error: 0xCAA90004 Getting token by refresh token failed.

Logged at RefreshTokenRequest.cpp, line: 150, method: RefreshTokenRequest::AcquireToken.

Request: authority: https://adfs.yourdomain.com/adfs, client: d3590ed6-52b3-4102-aeff-aad2292ab01c, redirect URI: ms-appx-web://Microsoft.AAD.BrokerPlugin/d3590ed6-52b3-4102-aeff-aad2292ab01c, resource: https://hcmail.yourdomain.com/, correlation ID (request): 4c3316af-5fa2-4002-9b42-4418a2fe62f3

I have done all registery setting as mention in micrsooft article even added expicit registery entry not to redirect to office365.

When i try to browse https://adfs.domain.com/adfs/oauth2/token  on browser i get error that

Error details: MSIS7065: There are no registered protocol handlers on path /adfs/oauth2/token to process the incoming request.

If any thing missing in adfs. please guide.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-09*

Hi @Zeeshan Butt  ,

Welcome to the Microsoft Q&A platform!

It sounds like you have encountered a complex issue involving ADFS and OAuth, which can be tricky to troubleshoot. Here are some steps you can follow to investigate and resolve the issue: 

1. ADFS Configuration for OAuth 

Ensure that ADFS is configured to support OAuth token requests. The error "MSIS7065: There are no registered protocol handlers on path /adfs/oauth2/token" implies that ADFS might not be configured correctly to handle OAuth token endpoints. 

-  Ensure that the OAuth2 endpoints are enabled in ADFS. You can do this by running the following PowerShell command on the ADFS server: 

```
Get-AdfsEndpoint -AddressPath "/adfs/oauth2/token"
```

The command should return details about the endpoint. If it does not, you may need to enable the endpoint. 

-  If the endpoint is not enabled, you can enable it using PowerShell: 

```
Set-AdfsEndpoint -TargetAddressPath "/adfs/oauth2/token" -Enabled $true
```

2. Client Configuration 

The client application (Outlook) should be correctly configured to use modern authentication. 

-  Ensure you've set the appropriate registry keys on the client machine to force the use of modern authentication. This includes the following: 

```
[HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\Common\Identity] "EnableADAL"=dword:00000001 

"Version"=dword:00000001
```

-  Make sure that Office has been activated properly and is recognizing the modern authentication settings. 

3. ADFS Relying Party Trust 

Ensure that the ADFS Relying Party Trust (RPT) for the Exchange server is configured correctly. 

-  Check the claims issuance rules for the RPT to ensure they are set correctly to issue the necessary claims for OAuth. 

-  Make sure the client ID and redirect URI configured in the RPT match those used by the Outlook client. 

4. Validate Certificates 

Modern authentication requires valid certificates for both ADFS and Exchange. Ensure that: 

-  Certificates are not expired. 

-  All certificates are trusted by the client machine. 

-  The ADFS and Exchange servers have valid SSL certificates. 

Troubleshooting Steps 

-  Review the ADFS logs for any errors or warnings that might provide more specific details about what is failing. 

-  Use tools like Fiddler or Wireshark to capture the network traffic between the client and the ADFS server to see if there are any obvious issues during the authentication process. 

-  Look for related events in the Event Viewer on both the client and the ADFS server. The specific error IDs and descriptions can often point you in the right direction.

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang
