---
title: "Exchange 2016 on prem Autodiscover not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1690868/exchange-2016-on-prem-autodiscover-not-working
question_id: 1690868
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2016 on prem Autodiscover not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1690868/exchange-2016-on-prem-autodiscover-not-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Some time over the last month, an issue has arisen with our exchange 2016 server Autodiscovery.

Attempting to configure an outlook 2016 client I could not connect to the exchange 2016 server. The client is being configured on the internal LAN. I have attempted with another Outlook 2016 client and had the same issue.

This is Exchange 2016 with the latest CU, updates, and extended Protection Enabled, on prem, NOT a hybrid.

The Outlook client is 2016 with the latest patches on Win 10. Adobe is the only 3rd party app with hooks in Outlook. AV is Defender.

DNS is correct for both internal and external access. Pings from internal and external return the proper ip addresses.When I attempt to browse to the autodiscovery.xml via a browser,  it comes up with a http 500 error. It does not prompt me for a password. This happens on WIN 10 client and on the exchange server as well.

When I run the Microsoft Remote Connectivity Analyzer It fails at the autodiscover POST with an http 404 and 500 "The Microsoft Connectivity Analyzer failed to obtain an Autodiscover XML response". The certificate tests as a valid certificate.

Internally running the Test E-Mail AutoConfiguration from Outlook, I get that the Autodiscover is found through SCP then continuously fails with 500 and 404 errors. The failed erros are 0x800C820f, 0x80070057, and 0x8004010f (SRV Record Check). I have also run this externally with the same result.

I have reset the VDir on the exchange server but it has not resoloved the issue. I have checked the authentication for the VDir and it is set as recommended with permissions according to Ali Tajran's guides. 

Browsing the page from IIS gives the same 500 error in a browser. 

The exchange server has EP enabled as well as the URL Rewrite module. Server has been locked down to use TLS 1.2 and the best practices template from IISCrypto 3.3 applied. I have tried disabling EP temporarily, but this did not resolve the issue.

No errors showing up int he event logs or IIS logs for the site.

Everyone that is currently connected to exchange is not having an issue. Anyone attempting to connect to exchange cannot connect due to the autodiscover issue.

Then only things I have done in the past few months was install the March 2024 update, then enabled extended protection. The certificate was rekeyed after the march updates.  Then after the mess of the March patch I applied the hotfix. Since I have added one user that was from a fresh install of office 2016.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-06-09*

This issue was resolved.

Since I knew that DNS was resolving correctly, I pursued issues with IIS since it just felt like IIS was being contacted, but not serving up the page.

Checking the IIS logs, I found that the autodiscover.xml was throwing a 500 error.

I enabled Failed Requet Tracing Rules and configured a rule for error 500 on the autodiscover vdir.

This pointed directly to a URL Rewrite rule. The rule was a blocking rule for {HTTP_HOST}. Looking it up, this was for a autodiscover mitigation from 2022. Not sure if it was meant to be applied to the default website or the autodiscover vdir, but it was applied to the Default Website.

Now EEMS was applied to the server, and EEMS was attempting to apply the rule to the autodiscover vdir, which is why I could not open the URL Rewrite on that vdir.

Removing the rule on the Default Website allowed EEMS to apply the rule to the autodiscover vdir, and autrodiscover started accepting requests.

For me, the key to figuring this out was enabling the Failed Requet Tracing Rule, which pointed me to the exact issue as the IIS logs were not giving enough information to fully troubleshoot the issue.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-06-04*

Hi,

Thanks for posting your question in the Microsoft Q&A Community.

First I want to confirm whether OWA can work properly.

To better solve your problem, we need you to provide your screenshot of the Test E-Mail AutoConfiguration like this:

Then you can check the Autodiscover Service InternalUri  in SCP by running the following command:

Get-ClientAccessService | fl auto*

And you can run this command to get DNS records of Autodiscover:

nslookup autodiscover.yourdomain.com

Any updates please be free to contact me .
