---
title: "Error while login with Microsoft Active directory using Reactjs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1414533/error-while-login-with-microsoft-active-directory
question_id: 1414533
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-microsoft-authenticator", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Error while login with Microsoft Active directory using Reactjs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1414533/error-while-login-with-microsoft-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am attempting to log in with Microsoft using ReactJS with Client ID and Tenant ID. It is functioning correctly for one of my applications, but it is displaying an error for the other application.

Here is the code I am currently utilizing:

```
import {
  PublicClientApplication,
} from "@azure/msal-browser";

const msalConfig = {
  auth: {
    clientId: "bd0f7574-xxxx-xxxx-xxxx-xxxxxxx",
    authority:
      "https://login.microsoftonline.com/c6f6dd74-xxxxx-xxxx-xxxxx-xxxxxx",
    redirectUri: window.location.origin,
  },
};
const loginRequest = {
  scopes: ["openid", "profile", "User.Read"],
};

const msalInstance = new PublicClientApplication(msalConfig);
```

It's returning following error:

```
ServerError: invalid_request: 9002326 - [2023-11-03 07:35:52Z]: AADSTS9002326: Cross-origin token redemption is permitted only for the 'Single-Page Application' client-type. Request origin: 'https://www.yello-ai.com'. Trace ID: 0e3d94c4-e3f1-4cba-9eec-f46b80dd5100 Correlation ID: 13311371-6122-4e67-9ff4-54a2b5458fd8 Timestamp: 2023-11-03 07:35:52Z - Correlation ID: 13311371-6122-4e67-9ff4-54a2b5458fd8 - Trace ID: 0e3d94c4-e3f1-4cba-9eec-f46b80dd5100
```

Could you please let me know which settings need to be adjusted to resolve this issue?

## Answers

_No answers on this thread._
