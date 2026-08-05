---
title: "Unable to update data from CSV to Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/461232/unable-to-update-data-from-csv-to-active-directory
question_id: 461232
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Unable to update data from CSV to Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/461232/unable-to-update-data-from-csv-to-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I have a list of users information in my csv, I want to update suppose the country of a user.     

Like here it is United States, I want to update it to France on Active Directory. How may I do so -     

Here is the powershell script -     

```
cls  
  
  
$ADUsers = Import-csv "C:\Updated1.csv"  
   
foreach ($User in $ADUsers)  
{  
      
    $Name1 = $User.username  
    $Name = $User.email  
    $country = $User.country  
  
  
    if ($country -eq "United States")  
    {  
  
    $test = Get-ADUser -filter {Name -eq $Name1}| Set-ADUser -Country -eq "France"  
  
       Write-Host ("Updated")   
    }  
  
    else  
    {  
       Write-Warning ("file not updated")   
      }
```

Here is the csv -     

     

csv as in file -     

```
firstname,middleInitial,lastname,username,email,streetaddress,city,zipcode,state,country,department,password,telephone,jobtitle,company,ou  
Dragon ,,Fruit,DragonAD,******@activedirectorypro.com,2749 Liberty Street,Dallas,75202,TX,United States,Marketing,ptwadgjmptw1.,214-800-4820,Marking Specialist,AD Pro,"OU=Developer,OU=Department,DC=test,DC=com"
```

Thanks

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-02*

Hi @Sourav Roy   ,    

The "-eq" operator should be removed from Line 17 and you have to use the country code "Fr" instead of "France" for the country property.    

```
Get-ADUser -filter {Name -eq $Name1}| Set-ADUser -Country -eq "France"
```

Best Regards,    

Ian Xue    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
