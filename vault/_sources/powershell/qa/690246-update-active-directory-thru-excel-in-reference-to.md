---
title: "update active directory thru excel in reference to employee ID"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/690246/update-active-directory-thru-excel-in-reference-to
question_id: 690246
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# update active directory thru excel in reference to employee ID

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/690246/update-active-directory-thru-excel-in-reference-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,   

I am not good at powershell. I have to update the  telephone no. in active directory from the excel sheet in correspondence to the employee ID mentioned in the sheet.  

Can anyone help me with a script please.  

The sheet contains below details.  

Emp ID     Employee Name  Telephone No.  

576           John                      5738  

789           Genelia                  2793  

 and so on .  

Thanks.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-01-11*

Hello,  

Below an example of the script :  

```
$CSVFile = Import-Csv -Delimiter "," -Path example_csv.csv
foreach($line in $CSVFile) {
    try {
        $ADUser = Get-ADUser -Identity $line.'Employee Name' -errorAction Stop
    }
    catch {
        Write-Output "Cannot find user : $($line.'Employee Name')"
        $ADUser = $null
    }

    if($ADUser -ne $null) {
        try {
            Set-ADUser -Identity $ADUser -OfficePhone $line.'Telephone No.' -ErrorAction Stop
        }
        catch {
            Write-Output "Cannot change Office phone"
        }
    }
}
```

My CSV look like that :  

EmpID,Employee Name, Telephone No.  

576,John,5738560100  

789,Genelia,2793  

890,Shyvana,8901  

Regards,
