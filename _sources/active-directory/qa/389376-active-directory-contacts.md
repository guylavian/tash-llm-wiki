---
title: "Active Directory Contacts"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/389376/active-directory-contacts
question_id: 389376
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory Contacts

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/389376/active-directory-contacts (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to import a few hundred users into an OU in our Active Directory as contacts. Not users, please do not tell me to import them as users, i want them as contacts.  

I have searched the internet and I have tried numerous scripts and they always fail.  

It seems to come down to the fact that I have unrecognised parameters.  

This is the code and the error I am getting:

Import-Module ActiveDirectory  

$Users = Import-CSV C:\Scripts\testimport.csv  

foreach($User in $Users){

$Params = @{  

'Name' = $User.DisplayName  

'mail' = $User.mail

```
Path = "OU=X,DC=Y,DC=com"
    }
New-ADObject  -Type Contact @Params
}
```

New-ADObject : A parameter cannot be found that matches parameter name 'mail'.  

At line:9 char:29  

-  New-ADObject -Type Contact @Params  

-  ~~~~~~~  

-  CategoryInfo : InvalidArgument: (:) [New-ADObject], ParameterBindingException  

-  FullyQualifiedErrorId : NamedParameterNotFound,Microsoft.ActiveDirectory.Management.Commands.NewADObject

It works fine without the email bit, but then it's a bit useless and there is no contact information there. I've tried looking at the attribute editor to get the right name of the parameter and it is correct.  

The only thing that seems to make sense is that if I do it through the AD and create a user it only asks basic name stuff, nothing about email addresses or phone numbers.  

Is it possible I have to create the contacts first and then get another script to populate the fields?

Any help would be appreciated.

Thank you  

DK

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 1 · updated: 2021-05-11*

Hi,    

As the error message said the New-ADObject cmdlet doesn't have the "-mail" parameter. To set the "mail" attribute you can use the "-OtherAttributes" parameter.    

```
$Params = @{  
    'Name' = $User.DisplayName  
    'OtherAttributes' = @{'mail'=$User.mail}  
    'Path' = "OU=X,DC=Y,DC=com"  
}  
New-ADObject -Type Contact @Params
```

Best Regards,    

Ian Xue    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
