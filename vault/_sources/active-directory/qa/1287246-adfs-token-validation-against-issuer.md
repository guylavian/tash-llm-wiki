---
title: "ADFS token validation against issuer"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1287246/adfs-token-validation-against-issuer
question_id: 1287246
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# ADFS token validation against issuer

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1287246/adfs-token-validation-against-issuer (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I developed an api which will receives request from client app and process the request.  The client app implemented ADFS token and send this token to api in each and every the request (as bearer token).  Now in api end, I have to validate the token against the issuer and process the request if token is valid.

Please let me know if any code sample available for this implementation.

Thank you

Selvakumar R

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-18*

Hi,

Here's an example of how you can validate the ADFS token in your API using the JwtBearerAuthentication middleware:

```
using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.IdentityModel.Tokens;

// ...

public void ConfigureServices(IServiceCollection services)
{
    // ...

    services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
        .AddJwtBearer(options =>
        {
            options.Authority = "https://your-adfs-server/adfs";
            options.TokenValidationParameters = new TokenValidationParameters
            {
                ValidateIssuer = true,
                ValidIssuer = "your-issuer", // The issuer of the ADFS token
                ValidateAudience = true,
                ValidAudience = "your-audience", // The audience (client app) of the ADFS token
                ValidateLifetime = true,
                ValidateIssuerSigningKey = true,
                IssuerSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes("your-signing-key")) // The signing key used by ADFS
            };
        });

    // ...
}
```
