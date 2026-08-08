---
title: "The application 'my-app' asked for scope 'Exchange.ManageAsApp' that doesn't exist on the resource '00000003-0000-0000-c000-000000000000'."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1198913/the-application-my-app-asked-for-scope-exchange-ma
question_id: 1198913
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-ms-graph", "office-exchange-office-exchange-server-development"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# The application 'my-app' asked for scope 'Exchange.ManageAsApp' that doesn't exist on the resource '00000003-0000-0000-c000-000000000000'.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1198913/the-application-my-app-asked-for-scope-exchange-ma (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

My scenario is that, I want to request some scopes on my azure ad app from customer. Some of them are Graph API scope(e.g. Directory.AccessAsUserAll) and some of them are Exchange Online API scope(e.g. Exchange.ManageAsApp). I try this using node.js code but got the error "The application 'my-app' asked for scope 'Exchange.ManageAsApp' that doesn't exist on the resource '00000003-0000-0000-c000-000000000000'." . 

```
passport.use(new OIDCStrategy({
    identityMetadata: config.creds.identityMetadata,
    clientID: config.creds.clientID,
    responseType: 'code id_token',
    responseMode: 'form_post',
    redirectUrl: config.creds.redirectUrl,
    allowHttpForRedirectUrl: true,
    clientSecret: config.creds.clientSecret,
    scope: ["User.ReadWrite.All" , "Group.ReadWrite.All","offline_access", "Directory.AccessAsUser.All", "Exchange.ManageAsApp"],
    passReqToCallback: false
  },
  function (iss, sub, profile, accessToken, refreshToken, done) {
    // Authentication successful
    // accessToken contains the access token for the requested resource with the requested scope
    done(null, profile);
  }
));
```

Also tried to give scope like that:

```
scope: ["User.ReadWrite.All" , "Group.ReadWrite.All","offline_access", "Directory.AccessAsUser.All", "https://outlook.office365.com/Exchange.ManageAsApp"],
```

I think one problem is that the resource is different for Graph and Exchange Online
Graph Api resource id - 00000003-0000-0000-c000-000000000000
Exchange Online resource id - 00000002-0000-0ff1-ce00-000000000000
I give the necessary permission to my app and also customer have that permissions. The scopes that comes under Graph API does not through any error. I also gone through various references for that but got no solution on that. Please help me with that how can I add the scope(Exchange.ManageAsApp) using my code.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-12*

I got my answer after more research on that. I use scopes of two resources simultaneously that is not allowed because the audience claim for access token can only of one type either it is Microsoft graph resource or exchange resource that's why I got that error. Now, it is solved

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-04-06*

You would need to assign the app the Exchange role directly:
https://office365itpros.com/2022/10/13/exchange-online-powershell-app/
