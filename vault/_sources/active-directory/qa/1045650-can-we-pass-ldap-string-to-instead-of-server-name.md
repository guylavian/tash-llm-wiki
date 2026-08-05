---
title: "Can we Pass LDAP string to instead of server-name, username & password"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1045650/can-we-pass-ldap-string-to-instead-of-server-name
question_id: 1045650
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["developer-technologies-aspnet-core-other-l1", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Can we Pass LDAP string to instead of server-name, username & password

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1045650/can-we-pass-ldap-string-to-instead-of-server-name (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

we have the following code to connect to Active Directory using PrincipleContext, where we pass the servername,username & password :-    

```
string ADServerName = System.Web.Configuration.WebConfigurationManager.AppSettings["ADServerName"];  
string ADusername = System.Web.Configuration.WebConfigurationManager.AppSettings["ADUserName"];  
string ADpassword = System.Web.Configuration.WebConfigurationManager.AppSettings["ADPassword"];  
using (var context = new PrincipalContext(ContextType.Domain, ADServerName, ADusername, ADpassword))
```

so my question is can we connect to this using LDAP string? Thanks

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-10-13*

Hi @john john  ,    

Yes,you can do that.    

You can pass the LDAP string via DirectoryEntry.    

https://learn.microsoft.com/en-us/dotnet/api/system.directoryservices.directoryentry.-ctor?view=windowsdesktop-7.0#system-directoryservices-directoryentry-ctor(system-string-system-string-system-string    

You can do this:    

```
var directoryEntry = new DirectoryEntry("LDAP://***");  
directoryEntry.Username = "***";  
directoryEntry.Password = "***";
```

Then you can query "AD" using the DirectorySearcher.    

```
var directorySearcher = new DirectorySearcher(directoryEntry);
```

Best regards,    

Lan Huang    

If the answer is the right solution, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
