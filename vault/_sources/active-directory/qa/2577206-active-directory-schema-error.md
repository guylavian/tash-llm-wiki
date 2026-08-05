---
title: "Active directory schema error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2577206/active-directory-schema-error
question_id: 2577206
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Active directory schema error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2577206/active-directory-schema-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear all,

We have an issue regarding active directory user registry. Our application wants to retrieve the user registry from active directory,

So after we type the domain name, username and password for the domain admin, the apps add a schema in the AD, usually we directly can get the respons from the active directory server.

Below is the log from the configuration                                   

< 3/17/2013 - 8:26:43 PM                                                  

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  

<<<<<<<<                                                                  

3/17/2013-8:27:03 PM: Configuring Access Manager Policy Server....        

C:\PROGRA~2\Tivoli\POLICY~1\sbin\ivmgrd_setup.exe -y no -m "********" -   

r 7135 -l 1460 -t 7200 -D no -f no                                        

OpenConfFile: "C:\PROGRA~2\Tivoli\POLICY~1\etc\pd.conf"                   

getentry: C:\PROGRA~2\Tivoli\POLICY~1\etc\pd.conf pdrte user-reg-type     

CloseConfFile: C:\PROGRA~2\Tivoli\POLICY~1\etc\pd.conf                    

OpenConfFile: "C:\PROGRA~2\Tivoli\POLICY~1\etc\activedir.conf"            

getentry: C:\PROGRA~2\Tivoli\POLICY~1\etc\activedir.conf uraf-registry    

hostname                                                                  

getentry: C:\PROGRA~2\Tivoli\POLICY~1\etc\activedir.conf uraf-registry    

useEncryption                                                             

getentry: C:\PROGRA~2\Tivoli\POLICY~1\etc\activedir.conf uraf-registry    

domain                                                                    

getentry: C:\PROGRA~2\Tivoli\POLICY~1\etc\activedir.conf uraf-registry    

dnforpd                                                                   

getentry: C:\PROGRA~2\Tivoli\POLICY~1\etc\activedir.conf uraf-registry    

Multi-domain                                                              

getentry: C:\PROGRA~2\Tivoli\POLICY~1\etc\activedir.conf uraf-registry    

bind-id                                                                   

getentry: C:\PROGRA~2\Tivoli\POLICY~1\etc\activedir.conf uraf-registry    

bind-pwd                                                                  

CloseConfFile: C:\PROGRA~2\Tivoli\POLICY~1\etc\activedir.conf             

OpenConfFile: "C:\PROGRA~2\Tivoli\POLICY~1\etc\pd.conf"                   

getentry: C:\PROGRA~2\Tivoli\POLICY~1\etc\pd.conf pdrte user-reg-type     

CloseConfFile: C:\PROGRA~2\Tivoli\POLICY~1\etc\pd.conf                    

OpenConfFile: "C:\PROGRA~2\Tivoli\POLICY~1\etc\pd.conf"                   

getentry: C:\PROGRA~2\Tivoli\POLICY~1\etc\pd.conf pdrte user-reg-type     

CloseConfFile: C:\PROGRA~2\Tivoli\POLICY~1\etc\pd.conf                    

C:\PROGRA~2\Tivoli\POLICY~1\sbin\mgrsslcfg.exe -config -f no -t 7200 -l   

1460 -D no                                                                

Creating the SSL certificate. This might take several minutes.            

The SSL configuration of the Tivoli Access Manager policy server          

has completed successfully.                                               

The policy server's signed SSL certificate is base-64 encoded and         

saved in text file "C:\PROGRA~2\Tivoli\POLICY~1\keytab\pdcacert.b64."     

This file is required by the configuration program on each machine        

in your secure domain.                                                    

C:\PROGRA~2\Tivoli\POLICY~1\sbin\bassslcfg.exe -config -f no -c "C:       

\PROGRA~2\Tivoli\POLICY~1\keytab\pdcacert.b64" -p 7135 -h TAMEB1          

The SSL configuration of Access Control Runtime has completed             

successfully.                                                             

Tivoli Access Manager policy server domain name: Default                  

Tivoli Access Manager policy server host name: TAMEB1                     

Tivoli Access Manager policy server listening port: 7135                  

2013-03-17-20:27:13.770-07:00I----- 0x16B48064 PID#2848 ERROR rgy ad E:   

\build\am611\src\uraf\ad\schema\adschema_update.cpp 550 0x00000ad0        

HPDRG0100E The operation in the Active Directory registry for             

adschema_update.exe: ADSCHEMA_CHECK_SCHEMA_RIGHTS failed with return      

error 8000500d.                                                           

adschema_update: result 1, retcode -2147463155                            

HPDBG0938E Configuration failed.                                          

3/17/2013-8:29:13 PM: HPDBG0938E Configuration failed.                    

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  

>>>>>>>>                                                                  

> 3/17/2013 - 8:29:15 PM                                                  

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  

>>>>>>>>

Please your advice,

Thanks,

Best Regards,

Achmad

## Answer (community) — community member

*upvotes: 0 · updated: 2013-03-20*

Hi Sandeep,

Thank you for your support, I will do as your advice,

Thanks & Regards,

Achmad

## Answer (community) — community member

*upvotes: 0 · updated: 2013-03-19*

Hi Achmad,

Welcome to Microsoft Community Forums.

As per the description, you are facing issues with Active directory user registry.

You have reached Microsoft end user support. The issue you are running into is best suited at the Forum below:

http://social.technet.microsoft.com/Forums/en-US/categories

Please feel free to post back if you face any issues with Windows. I’ll be glad to assist you.
