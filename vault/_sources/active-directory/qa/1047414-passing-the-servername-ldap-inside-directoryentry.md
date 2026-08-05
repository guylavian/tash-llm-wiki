---
title: "Passing the servername/Ldap inside  \"DirectoryEntry\" Vs \"PrincipalContext\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1047414/passing-the-servername-ldap-inside-directoryentry
question_id: 1047414
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["developer-technologies-aspnet-core-other-l1", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Passing the servername/Ldap inside  "DirectoryEntry" Vs "PrincipalContext"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1047414/passing-the-servername-ldap-inside-directoryentry (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have this action method inside my ASP.NET MVC-5 .net 4.6:-    

```
public ActionResult UsersInfo2()  
            {  
      
                List results = new List();  
                try  
                {  
                    // create LDAP connection object    
      
                    DirectoryEntry myLdapConnection = createDirectoryEntry();  
                    string ADServerName = System.Web.Configuration.WebConfigurationManager.AppSettings["ADServerName"];  
                    string ADusername = System.Web.Configuration.WebConfigurationManager.AppSettings["ADUserName"];  
                    string ADpassword = System.Web.Configuration.WebConfigurationManager.AppSettings["ADPassword"];  
                    using (var context = new DirectoryEntry("LDAP://mydomain.com:389/DC=mydomain,DC=com", ADusername, ADpassword))  
                    using (var search = new DirectorySearcher(context))  
                    {   
                                SearchResult r = search.FindOne();  
                             
                                ResultPropertyCollection fields = r.Properties;  
      
                                foreach (String ldapField in fields.PropertyNames)  
                                    string temp;  
                                    foreach (Object myCollection in fields[ldapField])  
                                        temp = String.Format("{0,-20} : {1}",  
                                                       ldapField, myCollection.ToString());  
                                }  
                    }  
                      
                   using (var context = new PrincipalContext(ContextType.Domain, "mydomain.com", ADusername, ADpassword))  
                    {  
      
                     bool isvalid  = context.ValidateCredentials("*******", "****************");  
      
                    }  
                              
                              
                              
                            }  
                              
                              
                  
      
                catch (Exception e)  
                {  
                    Console.WriteLine("Exception caught:\n\n" + e.ToString());  
                }  
                return View(results);  
      
            }
```

so after around one day of testing i realize that for the `DirectoryEntry` I need to pass the server/ldap as follow `("LDAP://mydomain.com:389/DC=mydomain,DC=com", ADusername, ADpassword))` , while for the `PrincipalContext` we need to pass it as follow:- `(ContextType.Domain, "mydomain.com", ADusername, ADpassword))`.. so i can not pass the ldap string inside the `PrincipalContext` nor the servrname only inside the  `DirectoryEntry` .. so is this the case? or i am doing things wrongly ?    

Thanks

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-10-14*

Hi @john john  ,    

The specific usage of DirectoryEntry and PrincipalContext can be found in the official documentation:    

PrincipalContext:    

```
public PrincipalContext (System.DirectoryServices.AccountManagement.ContextType contextType, string name, string container, string userName, string password);
```

string name:the domain name (e.g. "YOURDOMAIN" - or leave NULL for "default" domain)    

string container:optionally a container (as an LDAP path - a "distinguished" name, full path but without any LDAP:// prefix)    

https://learn.microsoft.com/en-us/dotnet/api/system.directoryservices.accountmanagement.principalcontext.-ctor?view=dotnet-plat-ext-6.0#system-directoryservices-accountmanagement-principalcontext-ctor(system-directoryservices-accountmanagement-contexttype-system-string-system-string-system-string-system-string)    

DirectoryEntry    

```
public DirectoryEntry (string? path, string? username, string? password);
```

https://learn.microsoft.com/en-us/dotnet/api/system.directoryservices.directoryentry.-ctor?view=windowsdesktop-7.0#system-directoryservices-directoryentry-ctor(system-string-system-string-system-string)    

Best regards,    

Lan Huang    

If the answer is the right solution, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
