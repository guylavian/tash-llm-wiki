---
title: "SuccessFactors to Active Directory user provisioning service, CN is not updated"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/916316/successfactors-to-active-directory-user-provisioni
question_id: 916316
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# SuccessFactors to Active Directory user provisioning service, CN is not updated

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/916316/successfactors-to-active-directory-user-provisioni (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,     

When using SAP SuccessFactors to Active Directory User Provisioning model, the default attribute maps the "Full name" from SuccessFactors to a "cn" attribute in Active Directory. We changed that and mapped the "formalName" from SF to "cn" in AD.     

As I am testing, this doesn't work in all cases. Some users have "cn" property updated with Full names and some do not.     

I made a test and changed "cn" (renamed it, because you cannot change the CN directly as an attribute in AD) for one user (myself) and provisioned the user on demand. I got the following status:    

-  Attribute name -> Attribute value     

-  PropertyName -> cn     

-  SkipReason -> NotSupported     

-  Michał Ziemba -> cn Add    

If the "CN" update is not supported, why this has been changed before for some users?    

Can you explain the mechanism and help to get it solved and have it updated, please?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-07-07*

Hi there,    

The provisioning service does not have a default logic for null value processing. When the provisioning service gets an empty string from the source app, it tries to flow the value "as-is" to the target app. In this case, on-premises Active Directory does not support setting empty string values and hence you see the above error.    

To rename the CN of the object which also changes the DistinguishedName below will do the trick which I found online.    

Import-Module activedirectory    

$varCSV = "C:\VBT\AD Users Update\Student Users17v1.csv"     

$userlist = Import-Csv -Path $varCSV  -Delimiter ","    

foreach ($user in $userlist)    

{    

    $SamAccountName = $user.SamAccountName  

    $FirstName = $user.GivenName  

    $LastName = $user.Surname  

    $DisplayName = $user.GivenName + " " + $user.Surname  

    $UserPrincipalName = $user.UserPrincipalName + "@students.stdeclanscollege.ie"   

    $JobTitle = $user.JobTitle  

    $EmailAddress = $user.UserPrincipalName  

    $Department = $user.Department  

    $dn = (Get-ADUser -Identity $SamAccountName).DistinguishedName  

           Get-ADUser -Identity $user.SamAccountName |   

           Set-ADUser  -DisplayName $DisplayName -GivenName $FirstName -Surname $LastName -Title $JobTitle `                         -UserPrincipalName $UserPrincipalName`  

                       -EmailAddress $UserPrincipalName `                         -Department $Department`  

   Try {    

        Rename-ADObject $dn -NewName $DisplayName  

```
}  

catch {  
    Write-Output "Error Check Acc: " ($user.samaccountname) | Out-File C:\errors.txt -Append  
      
}
```

}    

-----------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer–
