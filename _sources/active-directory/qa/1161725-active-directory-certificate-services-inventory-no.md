---
title: "Active Directory Certificate Services - Inventory (Not Trusted Certificate)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1161725/active-directory-certificate-services-inventory-no
question_id: 1161725
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Active Directory Certificate Services - Inventory (Not Trusted Certificate)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1161725/active-directory-certificate-services-inventory-no (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi MSFT Team,

I am trying to clean up orphaned or not trusted certificate in our Active Directory Domain Server. Is there a way to check which services, device or machine that use that certificate? Is it possible to map the services and client devices that use that certificate before we can delete or clean it up?

Please advise.

Thanks,

GCE

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-02-09*

Hello Bourbita,

Do you have best practices and guides on how to enabled it?

Thanks,

GCE

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-01-31*

Hi @GCE

You can use a powershell script for cleaup expired  and untrsuted certificate , the script below works and you can adjust it to generate a log file to trace cleaup action.

This script can be used , if you have the list of member servers in csv file and run it through scheduled task on a admin server able to communicate with target member machines through WinRM:

```
$ServerList = Get-Content "c:\temp\serverlist.CSV"

Foreach($Server in $ServerList) {
    Invoke-Command -ComputerName $Server -ScriptBlock {
        # Get Certificate list 
        $Certs = Get-ChildItem "Cert:\LocalMachine\My" -Recurse
        # Get the list of root certificate

$root_cert_list = Get-ChildItem -Path "Cert:\LocalMachine\Root" | select -ExpandProperty Subject
# Loop through each object in $Certs
Foreach($Cert in $Certs) {
    # The property "NotAfter" indicate the expired time , if it's older than the current time, the certificate will be deleted 
    If($Cert.NotAfter -lt (Get-Date)) 
        {
        $Cert | Remove-Item
         }
# Delete untrust certificate : if the certificate issuer is not in the list of root certificate it will be deleted
elseif($root_cert_list -notcontains  $cert.Issuer) 
{
$Cert | Remove-Item
}
}
}
}
```

Please don't forget to mark helpful answer as accepted
