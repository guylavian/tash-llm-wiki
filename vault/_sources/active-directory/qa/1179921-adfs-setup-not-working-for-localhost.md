---
title: "ADFS setup not working for localhost"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1179921/adfs-setup-not-working-for-localhost
question_id: 1179921
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS setup not working for localhost

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1179921/adfs-setup-not-working-for-localhost (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

```
Dear i have followed steps given in this 

when I debug the application, I am getting Error

This site can’t be reached

What I have tried:

ASP.NET

   
  

C#
public partial class Startup
   {
       public void Configuration(IAppBuilder app)
       {
           ConfigureAuth(app);
       }
   }

C#
public partial class Startup
   {
       private static string realm = ConfigurationManager.AppSettings["ida:Wtrealm"];
       private static string adfsMetadata = ConfigurationManager.AppSettings["ida:ADFSMetadata"];

       public void ConfigureAuth(IAppBuilder app)
       {
         app.SetDefaultSignInAsAuthenticationType(CookieAuthenticationDefaults.AuthenticationType);

           app.UseCookieAuthentication(new CookieAuthenticationOptions());

           app.UseWsFederationAuthentication(
               new WsFederationAuthenticationOptions
               {
                   Wtrealm = realm,
                   MetadataAddress = adfsMetadata
               });
       app.UseStageMarker(PipelineStage.Authenticate);
       }
   }
```

## Answers

_No answers on this thread._
