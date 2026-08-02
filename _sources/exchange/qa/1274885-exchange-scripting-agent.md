---
title: "Exchange Scripting Agent"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1274885/exchange-scripting-agent
question_id: 1274885
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange Scripting Agent

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1274885/exchange-scripting-agent (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

Help my in xml file for Scripting Agent

We have not been able to solve the problem for several days now.

where is the error here?

```

 
if($succeeded) {
    # Waiting for synchronization after mailbox has been created.
    Set-ADServerSettings -ViewEntireForest $true
    Start-Sleep -s 10
    # New-Mailbox triggered. Taking SamAccountName parameter.
        if ($provisioningHandler.UserSpecifiedParameters.Contains("SamAccountName") -eq $true) {
        $UsrSamAccountName = $provisioningHandler.UserSpecifiedParameters["SamAccountName"]
        $UsrAlias = (Get-Mailbox -Filter {SamAccountName -eq $UsrSamAccountName}).Alias.ToString()
        }
    # Enable-Mailbox triggered. Taking Identity parameter, this is the only one avalaible in this case.
    if ($provisioningHandler.UserSpecifiedParameters.Contains("Identity") -eq $true) {
    $UsrIdentity = $provisioningHandler.UserSpecifiedParameters["Identity"].ToString()
    $UsrAlias = (Get-Mailbox -Identity $UsrIdentity).Alias.ToString()
    }
  
    chcp 65001
$smtpServer = "srvEXCH.contoso.com"
$from = "******@contoso.com"
$searchOU = "OU=etest,OU=Contoso org structure,OU=Contoso Organization,DC=contoso,DC=com"
$hourAgo = (Get-Date).AddHours(-1)
$employees = Get-ADUser -SearchBase $searchOU -Filter "whenCreated -ge '$hourAgo'" -Properties EmailAddress
$existingEmployees = Get-Content -Path "C:\employees.txt"
$subject = "Добро пожаловать в нашу компанию!"
$body = "Уважаемый коллега!

Добро пожаловать в АО  «Contoso»!

Надеемся, что работа в нашей компании принесет Вам полезный опыт, новые впечатления и удовольствие от общения с коллективом!

Для более быстрой адаптации рекомендуем пройти по нижеследующей ссылке и ознакомиться с Адаптационным курсом, разработанным специально для новых работников https://adaptaciya.contoso.com/

В случае возникновения вопросов по содержанию курса, просим обращаться к представителю ДУЧР, Имя Фамилия (******@contoso.com, 78-78-78)

В случае возникновения вопросов технического характера (ссылка не открывается и др.), просим обращаться в Единый контакт-центр по номеру 9999 или на email ******@contoso.com.

Удачи Вам!

тел. 8787"
Send-MailMessage -SmtpServer $smtpServer -From $from -To $to -Subject $subject -BodyAsHtml $body -Encoding utf8

foreach ($employee in $employees) {
    if ($existingEmployees -notcontains $employee.EmailAddress) {
        $to = $employee.EmailAddress
        Send-MailMessage -SmtpServer $smtpServer -From $from -To $to -Subject $subject -BodyAsHtml $body -Encoding utf8
        Add-Content -Path "C:\employees.txt" -Value $to
    }
}
 }
 # Clearing variables. Each one in its own line in order to prevent error messages from being shown on EMC.
 if ($UsrAlias) { Remove-Variable UsrAlias }
 if ($UsrAddr) { Remove-Variable UsrAddr }
 if ($UsrOU) { Remove-Variable UsrOU }
 if ($UsrMsg) { Remove-Variable UsrMsg }
 if ($UsrIdentity) { Remove-Variable UsrIdentity }
 if ($UsrSamAccountName) { Remove-Variable UsrSamAccountName }
}

```

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2023-05-03*

Hi @Evgen Kotov  ,  

From the xml file, seems like you are trying to send welcome Email to new users using Exchange Scripting Agent, right? If this is the case, instead of writing the scripts from scratch all by yourself, it's recommended to follow the steps in the blog below and make necessary changes into the sample scripts provided to fit your needs:  

Send Welcome Email to New Mailbox / New Users.  

Should it still doesn't work, could you clarify what exact problem you meet so that we can understand better about your situation? Is there any error message or it just doesn't work as expected?  

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
