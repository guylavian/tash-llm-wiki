---
title: "Audience in access token issued by ADFS is not resource server URL"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1180929/audience-in-access-token-issued-by-adfs-is-not-res
question_id: 1180929
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Audience in access token issued by ADFS is not resource server URL

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1180929/audience-in-access-token-issued-by-adfs-is-not-res (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I am trying to use ADFS on Server 2019 for Oauth2. I have created a web application in ADFS with reference to this link and used the node.js application to request an access token. As per OpenID Connect Core 1.0 the audience in the access token should be the resource server URL, but it was 'urn:microsoft:userinfo'. I have also sent resource parameter while requesting the access token resulting in the following error:

```
OPError: invalid_token (MSIS9921: Received invalid UserInfo request. Audience 'https://resourceurl.com' in the access token is not same as the identifier of the UserInfo relying party trust 'urn:microsoft:userinfo'.)
```

Also, the access token's 'auth time' claim is in string format which should be a number.

auth_time
Time when the End-User authentication occurred. Its value is a JSON number representing the number of seconds from 1970-01-01T0:0:0Z as measured in UTC until the date/time. 

Any help will be highly appreciable.

Thanks,

Manoj.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-16*

Hi,

Thank you for posting your query.

Kindly follow the steps provided below to resolve your query.

Every OAuth client (native or web app) or resource (web api) configured with AD FS needs to be associated with an application group. The clients in an application group can be configured to access the resources in the same group. An application group can contain multiple clients and resources.

Go to this link for your reference and additional troubleshooting procedures https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/development/ad-fs-openid-connect-oauth-concepts

If the answer is helpful kindly click "ACCEPT AS ANSWER" and up vote it
