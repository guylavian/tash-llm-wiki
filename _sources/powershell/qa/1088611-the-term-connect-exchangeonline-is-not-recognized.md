---
title: "The Term Connect-ExchangeOnline is not recognized name of cmdlet, function, script file or operable program"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1088611/the-term-connect-exchangeonline-is-not-recognized
question_id: 1088611
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# The Term Connect-ExchangeOnline is not recognized name of cmdlet, function, script file or operable program

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1088611/the-term-connect-exchangeonline-is-not-recognized (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to connect with office365 PowerShell. I had also imported the module "ExchangeOnlineManagement". I'm getting the below exception:    

"The term Connect-ExchangeOnline is not recognized as cmdlet, function , script or operable problem".    

```
string script = @"  
               Set-ExecutionPolicy Unrestricted  
               $user = ''  
               $pwd = ''  
               $SecurePass = ConvertTo-SecureString -AsPlainText $pwd -Force  
               $Cred = New-Object System.Management.Automation.PSCredential -ArgumentList $user,$SecurePass  
               Import-Module -Name ExchangeOnlineManagement  
               Connect-ExchangeOnline -Credential $Cred  
               ";  
try  
{  
   using (Runspace runspace = RunspaceFactory.CreateRunspace())  
   {  
      runspace.Open();  
      Pipeline pipe = runspace.CreatePipeline();  
      pipe.Commands.AddScript(script);  
        
      try  
      {  
         var results = pipe.Invoke();  
      }   
      catch (Exception e)  
      {  
  
      }  
        
      var error = pipe.Error.ReadToEnd();  
      if (error.Count > 0)  
      {  
         foreach (PSObject err in error)  
         {  
            //more logging not sharing that code  
         }  
      }  
   }  
}  
catch (Exception ex)  
{ }
```

## Answer (community) — Q&A User

*upvotes: 2 · updated: 2022-11-16*

Hi!    

The question remaining is did the import of the module go well.    

(Like could the module be loaded in full)    

I would recommend to add the following line above the line where you import the module.     

Install-Module -Name ExchangeOnlineManagement -Force    

Alternatively you could do something with try-catch but I am not sure if that works in this scenario.    

Hope it helps!
