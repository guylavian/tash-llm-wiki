---
title: "Bitlocker -  Protector basado en Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/633958/bitlocker-protector-basado-en-active-directory
question_id: 633958
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-devices-deployment-config-app-groups", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Bitlocker -  Protector basado en Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/633958/bitlocker-protector-basado-en-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

En mi organizacion estamos barajando la posiblidad de cifrar los discos extraibles USB con Bitlocker utilizando la proteccion basada en pertenencia a grupos de Directorio activo, consiste en generar un clave que permita a un usuario o grupo de directorio activo desbloquear automaticamente el dispositivo si el usuario o el equipo en el que se inserta el USB coincide con la pertencia al grupo de la clave. Este es el comando que estoy usando para tal fin:  

Add-BitLockerKeyProtector -MountPoint D: -ADAccountOrGroup "Dominio/Nombre del grupo" –ADAccountOrGroupProtector  

Funciona ya que si creo un grupo en directorio activo y un usuario no esta en ese grupo, al introducir el USB en su ordenador no se desbloquea el dispositivo automaticamente hasta que el usuario no sea añadido al grupo.  

El problema ocurre cuando elimino al usuario del grupo con el que esta cifrado el USB y este sigue pudiendo acceder al dispositivo, aun actualizando su pertenencia a grupos d directorio activo.  

¿Hay alguna forma de que esto se pueda solucionar?  

Un cordial saludo.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-15*

You can try the article below on how to Protect Cluster Shared Volumes and Storage Area Networks with BitLocker":    

https://learn.microsoft.com/en-us/windows/security/information-protection/bitlocker/protecting-cluster-shared-volumes-and-storage-area-networks-with-bitlocker    

-----    

--If the answer is helpful, please vote positively and accept the answer--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-11-22*

After removing the user from that group, did that user logoff and logon again? He needs to do that, else, group membership tokens stay alive for a while.
