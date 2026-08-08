---
title: "configuracion lenguage exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1491155/configuracion-lenguage-exchange
question_id: 1491155
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
---
# configuracion lenguage exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1491155/configuracion-lenguage-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Buenas necesito saber donde puedo configurar de manera fija de zona horaria al abrir un buzón por primera vez, si existe algún comando que permita configurarlo y en alguna extensión dentro de alguna carpeta de la estructura de exchange cuando se instala en el servidor, espero ser claro.
El problema ocurre cuando por primera vez abren el buzón se equivocan en la configuración de la zona horaria, debiendo solucionarlo por medio de comandos, leyendo los comandos no hemos encontrado nada para dejar fija la zona horaria.
Espero respuesta de ayuda saludos Atte.-

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-01-14*

Hola,
Puedes intentar el siguiente comando. Esto cambiara la zona horaria en todos los usuarios.

`Get-Mailbox -RecipientTypeDetails UserMailbox -ResultSize Unlimited | Set-MailboxRegionalConfiguration -TimeZone "<ZonaHoraria>"`

Para obtener una lista de zonas horarias validas, puedes usar el comando:

`$TimeZone = Get-ChildItem "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Time zones" | foreach {Get-ItemProperty $_.PSPath}; $TimeZone | sort Display | Format-Table -Auto PSChildname,Display`

Si la respuesta es útil, por favor haz clic en "Aceptar respuesta" o Sí y valórala positivamente. Si tienes más preguntas acerca de esta respuesta, por favor haz clic en "Comentar".
