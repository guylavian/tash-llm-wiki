---
title: "Chapter 2. Getting Started - Red Hat Single Sign-On 7.2 Authorization Services Guide"
type: reference
domain: keycloak
slug: rhsso-7-2-getting-started-overview
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.2/html/authorization_services_guide/getting_started_overview
guide: authorization_services_guide
version: 7.2
family: rhsso
documentKind: "Documentation"
---

# Chapter 2. Getting Started - Red Hat Single Sign-On 7.2 Authorization Services Guide

Chapter 2. Getting Started
Before you can use this tutorial, you need to complete the installation of Red Hat Single Sign-On and create the initial admin user as shown in the Getting Started Guide tutorial. There is one caveat to this. You have to run a separate JBoss EAP instance on the same machine as Red Hat Single Sign-On Server. This separate instance will run your Java Servlet application. Because of this you will have to run the Red Hat Single Sign-On under a different port so that there are no port conflicts when running on the same machine. Use the jboss.socket.binding.port-offset
system property on the command line. The value of this property is a number that will be added to the base value of every port opened by Red Hat Single Sign-On Server.
To boot Red Hat Single Sign-On Server:
Linux/Unix
$ .../bin/standalone.sh -Djboss.socket.binding.port-offset=100
Windows
> ...\bin\standalone.bat -Djboss.socket.binding.port-offset=100
For more details about how to install and configure a JBoss EAP, please follow the steps on the Securing Applications and Services Guide tutorial.
After installing and booting both servers you should be able to access Red Hat Single Sign-On Admin Console at http://localhost:8180/auth/admin/ and also the JBoss EAP instance at http://localhost:8080.
2.1. Securing a Servlet Application
The purpose of this getting started guide is to get you up and running as quickly as possible so that you can experiment with and test various authorization features provided by Red Hat Single Sign-On. This quick tour relies heavily on the default database and server configurations and does not cover complex deployment options. For more information on features or configuration options, see the appropriate sections in this documentation.
This guide explains key concepts about Red Hat Single Sign-On Authorization Services:
- Enabling fine-grained authorization for a client application
- Configuring a client application to be a resource server, with protected resources
- Defining permissions and authorization policies to govern access to protected resources
- Enabling policy enforcement in your applications.
2.2. Creating a Realm and a User
The first step in this tutorial is to create a realm and a user in that realm. Then, within the realm we will create a single client application, which then becomes a resource server for which you need to enable authorization services.
To create a realm and a user complete the following steps:
Create a realm with a name hello-world-authz. Once created, a page similar to the following is displayed:
Realm hello-world-authz
- Create a user for your newly created realm. Click Users. The user list page opens.
- On the right side of the empty user list, click Add User.
To create a new user, complete the Username, Email, First Name, and Last Name fields. Click the User Enabled switch to On, and then click Save.
Add User
Set a password for the user by clicking the Credentials tab.
Set User Password
- Complete the New Password and Password Confirmation fields with a password and click the Temporary switch to OFF.
- Click Reset Password to set the user’s password.
2.3. Enabling Authorization Services
You can enable authorization services in an existing client application configured to use the OpenID Connect Protocol. You can also create a new client.
To create a new client, complete the following steps:
Click Clients to start creating a new client application and fill in the Client ID, Client Protocol, and Root URL fields.
Create Client Application
Click Save. The Client Details page is displayed.
Client Details
- On the Client Details page, click the Authorization Enabled switch to ON, and then click Save. A new Authorization tab is displayed for the client.
Click the Authorization tab and an Authorization Settings page similar to the following is displayed:
Authorization Settings
When you enable authorization services for a client application, Red Hat Single Sign-On automatically creates several default settings for your client authorization configuration.
For more information about authorization configuration, see Enabling Authorization Services.
2.4. Build, Deploy, and Test Your Application
Now that the app-authz-vanilla resource server (or client) is properly configured and authorization services are enabled, it can be deployed to the server.
The project and code for the application you are going to deploy is available in Red Hat Single Sign-On Quickstarts Repository. You will need the following installed on your machine and available in your PATH before you can continue:
- Java JDK 8
- Apache Maven 3.1.1 or higher
- Git
You can obtain the code by cloning the repository at https://github.com/redhat-developer/redhat-sso-quickstarts. Use the branch matching the version of Red Hat Single Sign-On in use.
Follow these steps to download the code.
Clone Project
$ git clone https://github.com/redhat-developer/redhat-sso-quickstarts
The application we are about to build and deploy is located at
$ cd redhat-sso-quickstarts/app-authz-jee-vanilla
2.4.1. Obtaining the Adapter Configuration
You must first obtain the adapter configuration before building and deploying the application.
To obtain the adapter configuration from the Red Hat Single Sign-On Administration Console, complete the following steps.
Click Clients. In the client listing, click the app-authz-vanilla client application. The Client Details page opens.
Client Details
Click the Installation tab. From the Format Option dropdown list, select Keycloak OIDC JSON. The adapter configuration is displayed in JSON format. Click Download.
Adapter Configuration
-
Move the file
keycloak.json
to theapp-authz-jee-vanilla/config
directory. (optional) By default, the policy enforcer responds with a
403
status code when the user lacks permission to access protected resources on the resource server. However, you can also specify a redirection URL for unauthorized users. To specify a redirection URL, edit the keycloak.json file you updated in step 3 and replace thepolicy-enforcer
configuration with the following:"policy-enforcer": { "on-deny-redirect-to" : "/app-authz-vanilla/error.jsp" }
This change specifies to the policy enforcer to redirect users to a
/app-authz-vanilla/error.jsp
page if a user does not have the necessary permissions to access a protected resource, rather than an unhelpful403 Unauthorized
message.
2.4.2. Building and Deploying the Application
To build and deploy the application execute the following command:
$ cd redhat-sso-quickstarts/app-authz-jee-vanilla
$ mvn clean package wildfly:deploy
2.4.3. Testing the Application
If your application was successfully deployed you can access it at http://localhost:8080/app-authz-vanilla. The Red Hat Single Sign-On Login page opens.
Login Page
Log in as alice using the password you specified for that user. After authenticating, the following page is displayed:
Hello World Authz Main Page
The default settings defined by Red Hat Single Sign-On when you enable authorization services for a client application provide a simple policy that always grants access to the resources protected by this policy.
You can start by changing the default permissions and policies and test how your application responds, or even create new policies using the different policy types provided by Red Hat Single Sign-On.
There are a plenty of things you can do now to test this application. For example, you can change the default policy by clicking the Authorization tab for the client, then Policies
tab, then click on Default Policy
in the list to allow you to change it as follows:
// The default value is $evaluation.grant(),
// let's see what happens when we change it to $evaluation.deny()
$evaluation.deny();
Now, log out of the demo application and log in again. You can no longer access the application.
Let’s fix that now, but instead of changing the Default Policy
code we are going to change the Logic
to Negative
using the dropdown list below the policy code text area. That re-enables access to the application as we are negating the result of that policy, which is by default denying all requests for access. Again, before testing this change, be sure to log out and log in again.
2.4.4. Next Steps
There are additional things you can do, such as:
- Create a scope, define a policy and permission for it, and test it on the application side. Can the user perform an action (or anything else represented by the scope you created)?
-
Create different types of policies such as rule-based, and associate these policies with the
Default Permission
. -
Apply multiple policies to the
Default Permission
and test the behavior. For example, combine multiple policies and change theDecision Strategy
accordingly. - For more information about how to view and test permissions inside your application see Obtaining the Authorization Context.
