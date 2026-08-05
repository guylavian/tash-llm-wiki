---
title: "adfs relaystate not coming back properly on windows server 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/161546/adfs-relaystate-not-coming-back-properly-on-window
question_id: 161546
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# adfs relaystate not coming back properly on windows server 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/161546/adfs-relaystate-not-coming-back-properly-on-window (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

(1) Browser -> SP ( GET http://yahoo.com)  

(2) SP sends redirect to browser with URL

https://adfs.vxdemo.net/adfs/ls/idpinitiatedsignon.aspx?RelayState=RPID%3Dhttps%3A%2F%2Flogin.vxtest.com%2Findex.html%26RelayState%3Dhttp%3A%2F%2Fyahoo.com

(3) ADFS presents a login screen for the user to login with userid/password

(4) Browser posts SAML response

```
In the POST body was expecting two key, value pairs.

  (a) SAMLResponse
  (b) RelayState
```

I am only seeing SAMLResponse and no RelayState.

ADFS server was configured with RelayState enabled.

In windows\ADFS\Microsoft.IdentityServer.ServiceHost.exe.Config  

<microsoft.identityServer.web>  

<useRelayStateForIdpInitiatedSignOn enabled="true" />  

<acceptedFederationProtocols wsFederation="true" saml="true" />  

</microsoft.identityServer.web>

Please help.

## Answers

_No answers on this thread._
