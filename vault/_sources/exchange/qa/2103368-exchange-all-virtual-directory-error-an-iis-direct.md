---
title: "exchange all virtual directory error: An IIS directory entry couldn't be created. The error message is Access is denied."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2103368/exchange-all-virtual-directory-error-an-iis-direct
question_id: 2103368
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-development-iis"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# exchange all virtual directory error: An IIS directory entry couldn't be created. The error message is Access is denied.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2103368/exchange-all-virtual-directory-error-an-iis-direct (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Здравствуйте,

при попытке изменить свойство "проверка подлинности" в ECP возникает ошибка:

Не удалось создать запись каталога служб IIS. Сообщение об ошибке - Access is denied. . HResult = -2147024891

при попытке сбросить виртуальный каталог в ECP ошибка: Exception has been thrown by the target of an invocation.

при этом в PowerShell виртуальные директории пересоздаются и никаких ошибок не возникает

## Answer (community) — community member

*upvotes: 0 · updated: 2024-11-15*

Привет Jake Zhang-MSFT

-  Запускал обе команды, ошибок не выявлено

-  После переустановки IIS - перестал работать, пришлось восстанавливать из бекапа

-  Информационная безопасность не позволяет обновляться до последних актуальных обновлений

-  пересоздавал ВСЕ виртуальные директории таким способом в том числе и ECP - ошибки остались

-  Проверил все "MSExchangeECPAppPooL" работает под ECP

какие еще могут быть решения данной проблемы, может нужны какие логи ?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-10-15*

Hi @Andry Haretonuyk，

Welcome to the Microsoft Q&A platform!

Based on your description, you are experiencing a permissions issue when trying to change the "Authentication" properties in the Exchange Control Panel (ECP). The error message "Access is denied. HResult = -2147024891" usually means that the required permissions for the action you are trying to perform are not in place. 

Here are several things you can check and try: 

-  Make sure the Exchange Trusted Subsystem group has the appropriate permissions. This group should have Full Control permissions to the Default Web Site in IIS: 

-  Open IIS Manager. 

-  Navigate to Sites > Default Web Site. 

-  Right-click the Default Web Site and select Permissions. 

-  Add the Exchange Trusted Subsystem and grant Full Control permissions. 

-  Restart IIS and the Exchange server. 

-  Check the identity of the application pool used by the Exchange virtual directory. It should run under "MSExchangeECPAppPooL". 

-  Make sure the directory permissions are set correctly: 

-  Navigate to C:\Program Files\Microsoft\Exchange Server\V15\ClientAccess. 

-  Right-click "ecp" and select "Properties". 

-  Go to the Security tab and make sure the Exchange Trusted Subsystems group has full control over this directory. 

-  Since you mentioned that recreating the virtual directory in PowerShell fixes the issue without errors, you might consider this as a workaround if the above steps don't resolve the issue. 

-  Check Event Viewer for any related events that might provide more insight into the issue. 

-  Make sure there are no DNS misconfigurations that could be causing the issue. 

These steps should help you diagnose and potentially resolve the permissions issue you're facing. If the issue persists, it might be worth considering a deeper investigation into the migration path and the state of the Active Directory schema, especially if this is a new Exchange server coexisting with an older version.

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang
