---
title: "Audience in access token issues by ADFS is not resource server URL"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1180928/audience-in-access-token-issues-by-adfs-is-not-res
question_id: 1180928
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Audience in access token issues by ADFS is not resource server URL

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1180928/audience-in-access-token-issues-by-adfs-is-not-res (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I am trying to use ADFS on Server 2019 for Oauth2. I have created a web application in ADFS with reference to this link and used the node.js application to request an access token. As per OpenID Connect Core 1.0 the audience in the access token should be the resource server URL. I have also sent resource parameter while requesting the access token resulting in the following error:

```
OPError: invalid_token (MSIS9921: Received invalid UserInfo request. Audience 'https://resourceurl.com' in the access token is not same as the identifier of the UserInfo relying party trust 'urn:microsoft:userinfo'.)
```

Also, the access token's 'auth time' claim is in string format which should be a number.

auth_time
Time when the End-User authentication occurred. Its value is a JSON number representing the number of seconds from 1970-01-01T0:0:0Z as measured in UTC until the date/time. 

Any help will be highly appreciable.

Thanks,

Manoj.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-02-17*

Hello @Manojkumar Kulkarni  

Thank you for posting this concern on this community space.

I would like to gather the following URL's down below that might fit into your case scenario and get it to the right track.

https://stackoverflow.com/questions/40201682/cors-is-not-working-on-oauth2-userinfo-endpoint-in-wso2-api-manager

https://learn.microsoft.com/en-us/answers/questions/33997/oauth-openid-cant-call-the-openid-userinfo-cors-po

https://github.com/IdentityModel/oidc-client-js/issues/1077

Looking forward to your feedback,

Cheers,

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.
