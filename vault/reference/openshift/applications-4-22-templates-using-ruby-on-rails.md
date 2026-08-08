---
title: "Creating applications using Ruby on Rails"
type: reference
domain: openshift
slug: applications-4-22-templates-using-ruby-on-rails
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/applications/templates-using-ruby-on-rails
version: 4.22
family: applications
documentKind: "Documentation"
---

# Creating applications using Ruby on Rails

[id="templates-using-ruby-on-rails"]
= Creating applications using Ruby on Rails

Ruby on Rails is a web framework written in Ruby. This guide covers using Rails 4 on OpenShift Container Platform.

[WARNING]
====
Go through the whole tutorial to have an overview of all the steps necessary to run your application on the OpenShift Container Platform. If you experience a problem try reading through the entire tutorial and then going back to your issue. It can also be useful to review your previous steps to ensure that all the steps were run correctly.
====

== Prerequisites

* Basic Ruby and Rails knowledge.
* Locally installed version of Ruby 2.0.0+, Rubygems, Bundler.
* Basic Git knowledge.
* Running instance of OpenShift Container Platform 4.
* Provisioned account in OpenShift Online.
* Make sure that an instance of OpenShift Container Platform is running and is available. Also make sure that your `oc` CLI client is installed and the command is accessible from your command shell, so you can use it to log in using your email address and password.

// Module included in the following assemblies:
// * openshift_images/templates-ruby-on-rails.adoc

[id="templates-rails-setting-up-database_{context}"]
= Setting up the database

Rails applications are almost always used with a database. For local development use the PostgreSQL database.

.Procedure

. Install the database:
+
[source,terminal]
----
$ sudo yum install -y postgresql postgresql-server postgresql-devel
----

. Initialize the database:
+
[source,terminal]
----
$ sudo postgresql-setup initdb
----
+
This command creates the `/var/lib/pgsql/data` directory, in which the data is stored.

. Start the database:
+
[source,terminal]
----
$ sudo systemctl start postgresql.service
----

. When the database is running, create your `rails` user:
+
[source,terminal]
----
$ sudo -u postgres createuser -s rails
----
+
Note that the user created has no password.

// Module included in the following assemblies:
// * openshift_images/templates-ruby-on-rails.adoc

[id="templates-rails-writing-application_{context}"]
= Writing your application

If you are starting your Rails application from scratch, you must install the Rails gem first. Then you can proceed with writing your application.

.Procedure

. Install the Rails gem:
+
[source,terminal]
----
$ gem install rails
----
+
.Example output
[source,terminal]
----
Successfully installed rails-4.3.0
1 gem installed
----

. After you install the Rails gem, create a new application with PostgreSQL as your database:
+
[source,terminal]
----
$ rails new rails-app --database=postgresql
----

. Change into your new application directory:
+
[source,terminal]
----
$ cd rails-app
----

. If you already have an application, make sure the `pg` (postgresql) gem is present in your `Gemfile`. If not, edit your `Gemfile` by adding the gem:
+
[source,terminal]
----
gem 'pg'
----

. Generate a new `Gemfile.lock` with all your dependencies:
+
[source,terminal]
----
$ bundle install
----

. In addition to using the `postgresql` database with the `pg` gem, you also must ensure that the `config/database.yml` is using the `postgresql` adapter.
+
Make sure you updated `default` section in the `config/database.yml` file, so it looks like this:
+
[source,yaml]
----
default: &default
  adapter: postgresql
  encoding: unicode
  pool: 5
  host: localhost
  username: rails
  password: <password>
----

. Create your application's development and test databases:
+
[source,terminal]
----
$ rake db:create
----
+
This creates `development` and `test` database in your PostgreSQL server.

// Module included in the following assemblies:
//  * openshift_images/templates-ruby-on-rails.adoc

[id="templates-rails-creating-welcome-page_{context}"]
= Creating a welcome page

Since Rails 4 no longer serves a static `public/index.html` page in production, you must create a new root page.

To have a custom welcome page must do following steps:

* Create a controller with an index action.
* Create a view page for the welcome controller index action.
* Create a route that serves applications root page with the created controller and view.

Rails offers a generator that completes all necessary steps for you.

.Procedure

. Run Rails generator:
+
[source,terminal]
----
$ rails generate controller welcome index
----
+
All the necessary files are created.

. edit line 2 in `config/routes.rb` file as follows:
+
----
root 'welcome#index'
----

. Run the rails server to verify the page is available:
+
[source,terminal]
----
$ rails server
----
+
You should see your page by visiting http://localhost:3000 in your browser. If you do not see the page, check the logs that are output to your server to debug.

// Module included in the following assemblies:
// * openshift_images/templates-ruby-on-rails.adoc

[id="templates-rails-configuring-application_{context}"]
= Configuring application for OpenShift Container Platform

To have your application communicate with the PostgreSQL database service running in OpenShift Container Platform you must edit the `default` section in your `config/database.yml` to use environment variables, which you must define later, upon the database service creation.

.Procedure

* Edit the `default` section in your `config/database.yml` with pre-defined variables as follows:
+
.Sample `config/database` YAML file
[source,eruby]
----
<% user = ENV.key?("POSTGRESQL_ADMIN_PASSWORD") ? "root" : ENV["POSTGRESQL_USER"] %>
<% password = ENV.key?("POSTGRESQL_ADMIN_PASSWORD") ? ENV["POSTGRESQL_ADMIN_PASSWORD"] : ENV["POSTGRESQL_PASSWORD"] %>
<% db_service = ENV.fetch("DATABASE_SERVICE_NAME","").upcase %>

default: &default
  adapter: postgresql
  encoding: unicode
  # For details on connection pooling, see rails configuration guide
  # http://guides.rubyonrails.org/configuring.html#database-pooling
  pool: <%= ENV["POSTGRESQL_MAX_CONNECTIONS"] || 5 %>
  username: <%= user %>
  password: <%= password %>
  host: <%= ENV["#{db_service}_SERVICE_HOST"] %>
  port: <%= ENV["#{db_service}_SERVICE_PORT"] %>
  database: <%= ENV["POSTGRESQL_DATABASE"] %>
----

// Module included in the following assemblies:
// * openshift_images/templates-ruby-on-rails.adoc

[id="templates-rails-storing-application-in-git_{context}"]
= Storing your application in Git

Building an application in OpenShift Container Platform usually requires that the source code be stored in a git repository, so you must install `git` if you do not already have it.

.Prerequisites

* Install git.

.Procedure

. Make sure you are in your Rails application directory by running the `ls -1` command. The output of the command should look like:
+
[source,terminal]
----
$ ls -1
----
+
.Example output
[source,terminal]
----
app
bin
config
config.ru
db
Gemfile
Gemfile.lock
lib
log
public
Rakefile
README.rdoc
test
tmp
vendor
----

. Run the following commands in your Rails app directory to initialize and commit your code to git:
+
[source,terminal]
----
$ git init
----
+
[source,terminal]
----
$ git add .
----
+
[source,terminal]
----
$ git commit -m "initial commit"
----
+
After your application is committed you must push it to a remote repository. GitHub account, in which you create a new repository.

. Set the remote that points to your `git` repository:
+
[source,terminal]
----
$ git remote add origin git@github.com:<namespace/repository-name>.git
----

. Push your application to your remote git repository.
+
[source,terminal]
----
$ git push
----

// Module included in the following assemblies:
// * openshift_images/templates-ruby-on-rails.adoc

[id="templates-rails-deploying-application_{context}"]
= Deploying your application to OpenShift Container Platform

You can deploy you application to OpenShift Container Platform.

After creating the `rails-app` project, you are automatically switched to the new project namespace.

Deploying your application in OpenShift Container Platform involves three steps:

* Creating a database service from OpenShift Container Platform's PostgreSQL image.
* Creating a frontend service from OpenShift Container Platform's Ruby 2.0 builder image and
your Ruby on Rails source code, which are wired with the database service.
* Creating a route for your application.

.Procedure

* To deploy your Ruby on Rails application, create a new project for the application:
+
[source,terminal]
----
$ oc new-project rails-app --description="My Rails application" --display-name="Rails Application"
----

// Module included in the following assemblies:
//  * openshift_images/templates-ruby-on-rails.adoc

[id="templates-rails-creating-database-service_{context}"]
= Creating the database service

Your Rails application expects a running database service. For this service use PostgreSQL database image.

To create the database service, use the `oc new-app` command. To this command you must pass some necessary environment variables which are used inside the database container. These environment variables are required to set the username, password, and name of the database. You can change the values of these environment variables to anything you would like. The variables are as follows:

* POSTGRESQL_DATABASE
* POSTGRESQL_USER
* POSTGRESQL_PASSWORD

Setting these variables ensures:

* A database exists with the specified name.
* A user exists with the specified name.
* The user can access the specified database with the specified password.

.Procedure

. Create the database service:
+
[source,terminal]
----
$ oc new-app postgresql -e POSTGRESQL_DATABASE=db_name -e POSTGRESQL_USER=username -e POSTGRESQL_PASSWORD=password
----
+
To also set the password for the database administrator, append to the previous command with:
+
[source,terminal]
----
-e POSTGRESQL_ADMIN_PASSWORD=admin_pw
----

. Watch the progress:
+
[source,terminal]
----
$ oc get pods --watch
----

// Module included in the following assemblies:
// * openshift_images/templates-ruby-on-rails.adoc

[id="templates-rails-creating-frontend-service_{context}"]
= Creating the frontend service

To bring your application to OpenShift Container Platform, you must specify a repository in which your application lives.

.Procedure

. Create the frontend service and specify database related environment variables that were setup when creating the database service:
+
[source,terminal]
----
$ oc new-app path/to/source/code --name=rails-app -e POSTGRESQL_USER=username -e POSTGRESQL_PASSWORD=password -e POSTGRESQL_DATABASE=db_name -e DATABASE_SERVICE_NAME=postgresql
----
+
With this command, OpenShift Container Platform fetches the source code, sets up the builder, builds your application image, and deploys the newly created image together with the specified environment variables. The application is named `rails-app`.

. Verify the environment variables have been added by viewing the JSON document of the `rails-app` deployment config:
+
[source,terminal]
----
$ oc get dc rails-app -o json
----
+
You should see the following section:
+
.Example output
[source,json]
----
env": [
    {
        "name": "POSTGRESQL_USER",
        "value": "username"
    },
    {
        "name": "POSTGRESQL_PASSWORD",
        "value": "password"
    },
    {
        "name": "POSTGRESQL_DATABASE",
        "value": "db_name"
    },
    {
        "name": "DATABASE_SERVICE_NAME",
        "value": "postgresql"
    }

],
----

. Check the build process:
+
[source,terminal]
----
$ oc logs -f build/rails-app-1
----

. After the build is complete, look at the running pods in OpenShift Container Platform:
+
[source,terminal]
----
$ oc get pods
----
+
You should see a line starting with `myapp-<number>-<hash>`, and that is your application running in OpenShift Container Platform.

. Before your application is functional, you must initialize the database by running the database migration script. There are two ways you can do this:
+
* Manually from the running frontend container:
+
** Exec into frontend container with `rsh` command:
+
[source,terminal]
----
$ oc rsh <frontend_pod_id>
----
+
** Run the migration from inside the container:
+
[source,terminal]
----
$ RAILS_ENV=production bundle exec rake db:migrate
----
+
If you are running your Rails application in a `development` or `test` environment you do not have to specify the `RAILS_ENV` environment variable.
+
* By adding pre-deployment lifecycle hooks in your template.

// Module included in the following assemblies:
//  * openshift_images/templates-ruby-on-rails.adoc

[id="templates-rails-creating-route-for-application_{context}"]
= Creating a route for your application

You can expose a service to create a route for your application.

.Procedure

* To expose a service by giving it an externally-reachable hostname like `www.example.com` use OpenShift Container Platform route. In your case you need to expose the frontend service by typing:
+
[source,terminal]
----
$ oc expose service rails-app --hostname=www.example.com
----

.Procedure

* Expose the frontend service by typing:
+
[source,terminal]
----
$ oc expose service rails-app
----

[WARNING]
====
Ensure the hostname you specify resolves into the IP address of the router.
====
