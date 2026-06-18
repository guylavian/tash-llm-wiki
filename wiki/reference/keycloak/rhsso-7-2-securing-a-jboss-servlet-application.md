---
title: "Chapter 4. Securing a JBoss Servlet Application - Red Hat Single Sign-On 7.2 Getting Started Guide"
type: reference
domain: keycloak
slug: rhsso-7-2-securing-a-jboss-servlet-application
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.2/html/getting_started_guide/securing_a_jboss_servlet_application
guide: getting_started_guide
version: 7.2
family: rhsso
documentKind: "Documentation"
---

# Chapter 4. Securing a JBoss Servlet Application - Red Hat Single Sign-On 7.2 Getting Started Guide

Chapter 4. Securing a JBoss Servlet Application
In this section you will learn how to secure a Java Servlet application on the JBoss EAP application server. You will learn how to install the Red Hat Single Sign-On Client Adapter onto a JBoss EAP application server distribution. You will create and register a client application in the Red Hat Single Sign-On Admin Console. Finally, you will configure the application to be secured by Red Hat Single Sign-On.
4.1. Before You Start
Before you can participate in this tutorial, you need to complete the installation of Red Hat Single Sign-On and create the initial admin user as shown in the Installing and Booting tutorial. There is one caveat to this. You have to run a separate JBoss EAP instance on the same machine as the Red Hat Single Sign-On server. This separate instance will run your Java Servlet application. Because of this you will have to run the Red Hat Single Sign-On under a different port so that there are no port conflicts when running on the same machine. Use the jboss.socket.binding.port-offset
system property on the command line. The value of this property is a number that will be added to the base value of every port opened by the Red Hat Single Sign-On server.
To boot the Red Hat Single Sign-On server:
Linux/Unix
$ .../bin/standalone.sh -Djboss.socket.binding.port-offset=100
Windows
> ...\bin\standalone.bat -Djboss.socket.binding.port-offset=100
After booting up Red Hat Single Sign-On, you can then access the admin console at http://localhost:8180/auth/admin/
4.2. Installing the Client Adapter
Download the JBoss EAP distribution and unzip it into a directory on your machine.
Next download the RH-SSO-7.2.7.GA-eap7-adapter.zip distribution.
Unzip this file into the root directory of your JBoss EAP distribution.
Next perform the following actions:
WildFly 10 and Linux/Unix
$ cd bin
$ ./jboss-cli.sh --file=adapter-install-offline.cli
WildFly 10 and Windows
> cd bin
> jboss-cli.bat --file=adapter-install-offline.cli
This script will make the appropriate edits to the …/standalone/configuration/standalone.xml file of your app server distribution. Finally, boot the application server.
Linux/Unix
$ .../bin/standalone.sh
Windows
> ...\bin\standalone.bat
4.3. Downloading, Building, and Deploying Application Code
The project and code for the application you are going to secure is available in Red Hat Single Sign-On Quickstarts Repository. You will need the following installed on your machine and available in your PATH before you can continue:
- Java JDK 8
- Apache Maven 3.1.1 or higher
- Git
You can obtain the code by cloning the repository at https://github.com/redhat-developer/redhat-sso-quickstarts. Use the branch matching the version of Red Hat Single Sign-On in use.
Follow these steps to download the code, build it, and deploy it. Make sure your JBoss EAP application server is started before you run these steps.
Clone Project
$ git clone https://github.com/redhat-developer/redhat-sso-quickstarts
$ cd redhat-sso-quickstarts/app-profile-jee-vanilla
$ mvn clean wildfly:deploy
You should see some text scroll down in the application server console window. After the application is successfully deployed go to:
Application Login Page
If you open up the application’s web.xml file you would see that the application is secured via BASIC
authentication. If you click on the login button on the login page, the browser will pop up a BASIC auth login dialog.
Application Login Dialog
The application is not secured by any identity provider, so anything you enter in the dialog box will result in a Forbidden
message being sent back by the server. The next section describes how you can take this deployed application and secure it.
4.4. Creating and Registering the Client
The next step you have to do is to define and register the client in the Red Hat Single Sign-On Admin Console.
- Log into the Admin Console with your admin account as you did in previous tutorials.
In the top left dropdown menu select and manage the
demo
realm. ClickClients
in the left side menu. The Clients page opens.Clients
- On the right click Create.
Complete the fields as shown below:
Add Client
After clicking the
Save
button your client application entry will be created. You now have to go back to the JBoss EAP instance that the application is deployed on and configure it so that this app is secured by Red Hat Single Sign-On. You can obtain a template for the configuration you need by going to theInstallation
tab in the client entry in the Red Hat Single Sign-On Admin Console.Installation Tab
Select Keycloak OIDC JBoss Subsystem XML. An XML template is generated that you’ll need to cut and paste.
Template XML
4.5. Configuring the Subsystem
Now that you have copied the XML template from the Installation page, you need to paste this into the standalone.xml file that resides in the standalone/configuration directory of the application server instance on which your application is deployed.
Open the standalone/configuration/standalone.xml file and search for the following text:
<subsystem xmlns="urn:jboss:domain:keycloak:1.1"/>
Modify this to prepare it for pasting in your template from the Installation page:
<subsystem xmlns="urn:jboss:domain:keycloak:1.1"> </subsystem>
Within the <subsystem> element, paste in the template. It will look something like this:
<subsystem xmlns="urn:jboss:domain:keycloak:1.1"> <secure-deployment name="WAR MODULE NAME.war"> <realm>demo</realm> <auth-server-url>http://localhost:8180/auth</auth-server-url> <public-client>true</public-client> <ssl-required>EXTERNAL</ssl-required> <resource>vanilla</resource> </secure-deployment> </subsystem>
Change the WAR MODULE NAME text to vanilla as follows:
<subsystem xmlns="urn:jboss:domain:keycloak:1.1"> <secure-deployment name="vanilla.war"> ... </subsystem>
- Reboot your application server.
- Go to http://localhost:8080/vanilla and click login. The Red Hat Single Sign-On login page opens. You can log in using the user you created in the Creating a New User chapter.
