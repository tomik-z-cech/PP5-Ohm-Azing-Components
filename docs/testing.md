# **6.2. Testing**

## **6.2.1. Table of Content - Testing**

- [**6.2.1. Table of Content - Testing**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/docs/testing.md#521-table-of-content---testing)
- [**6.2.2. User stories testing**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/docs/testing.md#522-user-stories-testing)
- [**6.2.3. Test Cases**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/docs/testing.md#524-test-cases)
- [**6.2.4. Viewport Testing**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/docs/testing.md#524-viewport-testing)
- [**6.2.5. Compatibility Testing**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/docs/testing.md#525-compatibility-testing)

## **6.2.2. User stories testing**

| Epic 1                                                                     | Environment configuration                                       |                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                  |                                                               |                                                                                                                     |        |
| -------------------------------------------------------------------------- | --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------ |
| Issue                                                                      | Title                                                           | User Story                                                                                                                                                                          | Acceptance Criteria                                                                                                                                                                                                                                                              | Implementation                                                | Final Commit                                                                                                        | Result |
| [# 2](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/2)   | USER STORY : Set up GiHub repository                            | As a Developer, I need to set-up a repository on GitHub platform to be able to have control over versions of project.                                                               | Working GitHub repository.                                                                                                                                                                                                                                                       | Not Applicable                                                | [1861fb4](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/1861fb476f7bddef5536c8cea1f3afc96ba70731) | PASS   |
| [# 3](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/3)   | USER STORY : Set up dependencies                                | As a Developer, I need to register and obtain links for third party services.                                                                                                       | All links of third party services (DB, mail provider, AWS) are obtained and services set                                                                                                                                                                                         | Not Applicable                                                | [76e4e21](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/76e4e21c9676bfe20584fc6a3b10795d0e40dca9) | PASS   |
| [# 4](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/4)   | USER STORY : Create working Django app                          | As a Developer, I need to install all dependencies, correctly set settings.py and create working app in local environment.                                                          | All dependencies are installed, settings.py all set for local view and when project is ran locally, symbol of correctly set app is shown (rocket).                                                                                                                               | Not Applicable                                                | [c8d2a30](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/c8d2a30d6146cf84f0711ad5bdcd3c6ede959b02) | PASS   |
| [# 5](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/5)   | USER STORY : Deploy to Heroku                                   | As a Developer I need to create a working Heroku deployment.                                                                                                                       | Working Heroku Deployment, when first deployed site accessed, it gives hint of correctly installed Django App (DEBUG = True). Create if statement in settings.py for DEBUG = False when deployed.                                                                                 | Not Applicable                                                | [c8d2a30](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/c8d2a30d6146cf84f0711ad5bdcd3c6ede959b02) | PASS   |
|                                                                            |                                                                 |                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                  |                                                               |                                                                                                                     |        |
| Epic 2                                                                     | Database Models                                                 |                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                  |                                                               |                                                                                                                     |        |
| Issue                                                                      | Title                                                           | User Story                                                                                                                                                                          | Acceptance Criteria                                                                                                                                                                                                                                                              | Implementation                                                | Final Commit                                                                                                        | Result |
| [# 7](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/7)   | USER STORY : Define Database Schema                             | As a Developer, I need to create database schema that fits the purpose of the project and also create all the modular apps that will be used in the project.                         | All Django apps are created and database schema in place to adhere to.                                                                                                                                                                                                           | *( appendix 90 )*                                           | [1d2929d](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/1d2929d2a31e281b2890acd9827199d2101d7811) | PASS   |
| [# 8](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/8)   | USER STORY : Create database relationships                      | As a Developer, I need to define relationships between models and import the relationships into working apps models.                                                                 | All models are working with the relationships defined, all models that are related to other app models are linked via import statements.                                                                                                                                         | *( appendix 91 )*                                           | [1d2929d](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/1d2929d2a31e281b2890acd9827199d2101d7811) | PASS   |
| [# 9](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/9)   | USER STORY : Implement Data Validation in Models                | As a Developer, I need implement data validation rules within Ohm-Azing Components database models.                                                                                 | All values inserted into database are the correct values and types, all applicable fields are all set to be required or/and to be unique or/and nullable/not nullable.                                                                                                           | *( appendix 92 )*                                           | [1d2929d](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/1d2929d2a31e281b2890acd9827199d2101d7811) | PASS   |
|                                                                            |                                                                 |                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                  |                                                               |                                                                                                                     |        |
| Epic 3                                                                     | User Authentication and Authorization                           |                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                  |                                                               |                                                                                                                     |        |
| Issue                                                                      | Title                                                           | User Story                                                                                                                                                                          | Acceptance Criteria                                                                                                                                                                                                                                                              | Implementation                                                | Final Commit                                                                                                        | Result |
| [# 11](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/11) | USER STORY : Implement user registration                        | As a Site User I am able to register to create new account and to select username and password.                                                                                    | Not registered user : When I visit the site then I am able to register, select free username and create valid password.                                                                                                                                                          | *( appendix 93 )*                                           | [5a19fd0](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/5a19fd0b165c1ddda2e5cee6dc27f62fb5d4c213) | PASS   |
| [# 12](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/12) | USER STORY : Log In                                             | As a Site User I am able to Log In to see registered user section.                                                                                                                  | 1.Registered user : When I visit the site then I am able to login via login link. 2.Not registered user : When I visit the site and trying to log in then I am given error message that user does not exist.                                                                     | *( appendix 94 )*                                           | [5a19fd0](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/5a19fd0b165c1ddda2e5cee6dc27f62fb5d4c213) | PASS   |
| [# 13](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/13) | USER-STORY : Reset my password if forgotten                     | As a Site User I am able to Reset My Password to change my password if forgotten.                                                                                                   | When I visit login page then I have the option to reset my password via provided link and email with reset link is sent to me.                                                                                                                                                   | *( appendix 95 )*                                           | [5a19fd0](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/5a19fd0b165c1ddda2e5cee6dc27f62fb5d4c213) | PASS   |
| [# 14](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/14) | USER STORY : Log out                                            | As a Site User, I am able to log out to leave the site functions for registered users.                                                                                              | 1.Registered user : When I am logged in then I am able to logout. 2.Not registered user : Don't have that option.                                                                                                                                                                | *( appendix 96 )*                                           | [5a19fd0](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/5a19fd0b165c1ddda2e5cee6dc27f62fb5d4c213) | PASS   |
|                                                                            |                                                                 |                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                  |                                                               |                                                                                                                     |        |
| Epic 4                                                                     | Custom Admin Interface                                          |                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                  |                                                               |                                                                                                                     |        |
| Issue                                                                      | Title                                                           | User Story                                                                                                                                                                          | Acceptance Criteria                                                                                                                                                                                                                                                              | Implementation                                                | Final Commit                                                                                                        | Result |
| [# 16](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/16) | USER STORY : Categories section                                 | As a Business Owner, I have option to do full CRUD with item categories in order to manage my shop.                                                                                 | Staff/SuperUser : When I log in with my credentials then I am able to navigate to admin tools section to perform CRUD on shop categories. Users with no staff or Superuser rank : Not able to access that functionality.                                                          | *( appendix 97 )*                                           | [7750783](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/7750783f78551c3a812957ce6be6d23397cf471a) | PASS   |
| [# 17](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/17) | USER STORY : Items section                                      | As a Business Owner, I have option to do full CRUD with items in order to manage products sold in my shop.                                                                          | Staff/SuperUser : When I log in with my credentials then I am able to navigate to admin tools section to perform CRUD on shop items. Users with no staff or Superuser rank : Not able to access that functionality.                                                               | *( appendix 98 )*                                           | [bd40bbf](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/bd40bbfb7c2625bfb3903df6d746aaf481804568) | PASS   |
| [# 18](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/18) | USER STORY : Invoices section                                   | As a Business Owner, I have option to view or download any invoice that was created by shoppers.                                                                                    | Staff/SuperUser : When I log in with my credentials then I am able to navigate to admin tools section to view and download invoices. Users with no staff or Superuser rank : Not able to access that functionality.                                                               | *( appendix 99 )*                                           | [d041060](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/d0410601e36811992c9b0ff2b22db3646872a917) | PASS   |
| [# 19](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/19) | USER STORY : Vouchers section                                   | As a Business Owner, I have option to perform full CRUD on "Vouchers" that could be redeemed via checkout.                                                                          | Staff/SuperUser : When I log in with my credentials then I am able to navigate to admin tools section to create, read, edit and delete "vouchers" redeemable at the end of checkout process. Users with no staff or Superuser rank : Not able to access that functionality.       | *( appendix 100 )*                                          | [d5601e6](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/d5601e6a80130048d2d3533f3cde2a7172d47b62) | PASS   |
| [# 20](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/20) | USER STORY : Comments section                                   | As a Business Owner, I have option to approve/delete comments to ensure no inappropriate content on the project page.                                                               | Staff/SuperUser : When I log in with my credentials then I am able to navigate to admin tools section approve/delete comments. Users with no staff or Superuser rank : Not able to access that functionality.                                                                     | *( appendix 101 )*                                          | [797af69](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/797af69ea601041f30210b958552650628bdd9b7) | PASS   |
| [# 21](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/21) | USER STORY : Postage Settings section                           | As a Business Owner, I have option to adjust free postage threshold and postage fees for standard and express delivery options.                                                      | Staff/SuperUser : When I log in with my credentials then I am able to navigate to admin tools section to change postage settings. Users with no staff or Superuser rank : Not able to access that functionality.                                                                  | *( appendix 102 )*                                          | [1630d1f](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/1630d1f149919cf27264831bdeee4283c2e05902) | PASS   |
| [# 28](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/28) | USER STORY : Email interface for marketing purposes             | As a Site admin, I need to implement Mailing interface to be able to send emails to all users signed up for email communication.                                                    | Staff/SuperUser : When I log in with my credentials then I am able to navigate to admin tools section to to create drafts/send emails to all users that are signed up to receive email newsletter. Users with no staff or Superuser rank : Not able to access that functionality. | *( appendix 103 )*                                          | [c05fbef](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/c05fbefce9cd3214b232a4df6eefb26d31efd5e4) | PASS   |
| [# 97](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/97) | USER STORY : Postage label printing                             | As a Site Admin, I need implement postage label printing page to be able to Effortlessly print postage labels.                                                                      | When I log in as Superuser and navigate to Admin Tools then I can select order to view and print postage label based on order details.                                                                                                                                           | Won't be implemented - Marked as "Won't Have" on Kanban Board | N/A                                                                                                                 | N/A    |
| [# 98](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/98) | USER STORY : Order status emails                                | As a Site Admin, I can mark orders as accepted, pending, fulfilled to be able to keep customers informed of the status of their order.                                              | When I navigate to Admin Tools and Invoices then I can see status of the order and I can change the status, customer is then notified via email of the progress.                                                                                                                 | Won't be implemented - Marked as "Won't Have" on Kanban Board | N/A                                                                                                                 | N/A    |
|                                                                            |                                                                 |                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                  |                                                               |                                                                                                                     |        |
| Epic 5                                                                     | General Features                                                |                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                  |                                                               |                                                                                                                     |        |
| Issue                                                                      | Title                                                           | User Story                                                                                                                                                                          | Acceptance Criteria                                                                                                                                                                                                                                                              | Implementation                                                | Final Commit                                                                                                        | Result |
| [# 23](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/23) | USER STORY : FavIcon & Title                                    | As a Site User I would like to be able to differentiate this site from other sites opened in my browser, in order of easy navigation.                                                | When I navigate to the site, then I am clearly served with FavIcon and title of the site .                                                                                                                                                                                        | *( appendix 104 )*                                          | [8f235c7](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/8f235c7c3e6871b1f19ee4d28bcebeae9bc41171) | PASS   |
| [# 24](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/24) | USER STORY : Header                                             | As a Site User I want to be able to navigate easily through-out the site.                                                                                                           | When I navigate to the site, I am able to see header with logo and icons for menu, vault and wishlist (if logged in).                                                                                                                                                            | *( appendix 105 )*                                          | [5a19fd0](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/5a19fd0b165c1ddda2e5cee6dc27f62fb5d4c213) | PASS   |
| [# 25](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/25) | USER STORY : Footer                                             | As a Site User I want to be able to find useful info on the bottom of the site in order not to scroll and search too much around.                                                   | When I navigate to the site, I am able to see footer with basic contact details, link to socials and accepted payment options.                                                                                                                                                   | *( appendix 106 )*                                          | [5a19fd0](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/5a19fd0b165c1ddda2e5cee6dc27f62fb5d4c213) | PASS   |
| [# 26](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/26) | USER STORY : Loader                                             | As a Site User I want to be able to see if page is working in the form of loader that appears when complex task is performed.                                                       | When I navigate throughout the site when complex actions are being submitted (DB) then the loader appears to ensure me the site didn't freeze.                                                                                                                                   | *( appendix 107 )*                                          | [15a14bd](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/15a14bdcd9066bf13f0a9b1428debed0d879834a) | PASS   |
| [# 27](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/27) | USER STORY : Toasts                                             | As a Site User I want to be informed of results of requests performed in the form of toast that appears when complex task is done successfully / unsuccessfully.                     | When I navigate throughout the site when complex actions are being submitted (DB) then the toast appears to inform me of the result of action.                                                                                                                                   | *( appendix 108 )*                                          | [be40cc1](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/be40cc1431dc1394c6d53423c605bd844daa3fb7) | PASS   |
|                                                                            |                                                                 |                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                  |                                                               |                                                                                                                     |        |
| Epic 6                                                                     | User Profile Management                                         |                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                  |                                                               |                                                                                                                     |        |
| Issue                                                                      | Title                                                           | User Story                                                                                                                                                                          | Acceptance Criteria                                                                                                                                                                                                                                                              | Implementation                                                | Final Commit                                                                                                        | Result |
| [# 31](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/31) | USER STORY : Change Details (Phone Number, Email Address, etc.) | As a Site User I can Update My Details to be able to manage my account in case of changes.                                                                                          | Logged in user : When I login then I can clearly navigate to "My Details" section where I can change my details. Not logged in user : Don't have that option as not logged in.                                                                                                   | *( appendix 109 )*                                          | [608f056](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/608f0564333f5a55de3af447b3e0666e4ea4fe0a) | PASS   |
| [# 32](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/32) | USER STORY : Delete my account                                  | As a Site User I can Delete My Account to be able to opt out from all services.                                                                                                     | Logged in user : When I navigate to "my details" then I have the option of delete my account entirely. Not logged in user : Don't have that option as not logged in.                                                                                                             | *( appendix 110 )*                                          | [608f056](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/608f0564333f5a55de3af447b3e0666e4ea4fe0a) | PASS   |
| [# 33](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/33) | USER STORY : Profile Picture                                    | As a Site User I can Change my profile picture to add the finishing touch to my profile.                                                                                            | Logged in user : When I navigate to "My Details" section then I change my profile picture. Not logged in user : Don't have that option as not logged in.                                                                                                                         | *( appendix 111 )*                                          | [a7bd28a](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/a7bd28a7539cde8d158c8c3a8f95a51aeda3caec) | PASS   |
| [# 34](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/34) | USER STORY : Opt In/Out for Newsletter                          | As a Site User I can Opt In/Out for Newsletter or other marketing communication to be able to change my preferences.                                                                | Logged in user : When I navigate to "My Details" section then I can mark/un-mark to receive marketing emails, sms or phone calls. Not logged in user : Don't have that option as not logged in.                                                                                   | *( appendix 112 )*                                          | [a7bd28a](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/a7bd28a7539cde8d158c8c3a8f95a51aeda3caec) | PASS   |
|                                                                            |                                                                 |                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                  |                                                               |                                                                                                                     |        |
| Epic 7                                                                     | The Shop                                                        |                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                  |                                                               |                                                                                                                     |        |
| Issue                                                                      | Title                                                           | User Story                                                                                                                                                                          | Acceptance Criteria                                                                                                                                                                                                                                                              | Implementation                                                | Final Commit                                                                                                        | Result |
| [# 36](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/36) | USER STORY : Shop Highlights                                    | As a Site User, I would like to See Newest and Favorites on the landing page so I can see easily what products are after arriving and what are most popular.                       | When I navigate to the site then on landing page I can see featured products, free delivery threshold.                                                                                                                                                                            | *( appendix 113 )*                                          | [94932b4](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/94932b44ceee72c1dccff795eab32b6a73bdea0d) | PASS   |
| [# 37](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/37) | USER STORY : Shop by Category                                   | As a Site User, I would like to have the shop items sorted by category so I can browse the items faster.                                                                            | When I visit the shop with all items then I can see all the categories displayed and when category clicked, items belonging to the category will display.                                                                                                                        | *( appendix 114 )*                                          | [5081a8f](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/5081a8f7ec7c4d8886ccbaeb15f77cf5ddc5635a) | PASS   |
| [# 38](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/38) | USER STORY : Product Details                                    | As a Site User, I would like to see the details of each item in separate page so I won't get lost in too much info.                                                                 | When I visit the shop with all items and open details of certain item then I can see all the relevant info per item.                                                                                                                                                             | *( appendix 115 )*                                          | [765f8ad](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/765f8ad074062865599a148bbb882fddb095acd5) | PASS   |
| [# 39](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/39) | USER STORY : Add to Vault                                       | As a Site User, I need to be able to add items to vault in order to see the entire order before payment.                                                                            | When I click "Add to vault" button then the item adds to vault.                                                                                                                                                                                                                  | *( appendix 116 )*                                          | [06cf6d4](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/06cf6d49910a33306c951d4963dcee42c95d6ee5) | PASS   |
| [# 40](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/40) | USER STORY : Add to Wishlist                                    | As a Site User, I need to be able to add items to my Wishlist in order to see keep the items I am interested in separately.                                                         | Logged in User : When I click "Add to Wishlist" toggle then the item toggles in Wishlist. Not Logged in User : Doesn't have that option.                                                                                                                                         | *( appendix 117 )*                                          | [618624a](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/618624a73180d51eaeb62a656790f0b295726df1) | PASS   |
| [# 41](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/41) | USER STORY : Comment on Products                                | As a Site User I can Comment on Items to share my opinion.                                                                                                                          | Logged in user : When I navigate to item detail in shop then I am able to add comment on the relevant item. Not logged in user : Doesn't have that option.                                                                                                                       | *( appendix 118 )*                                          | [aaacdb9](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/aaacdb93817745397d28e8b3cd63dcafe8162939) | PASS   |
| [# 42](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/42) | USER STORY : See Comments of Others                             | As a Site User I can see other comments on Items to read other Users opinions.                                                                                                      | Logged in user : When I open item detail then I am able to see other people comments. Not logged in user : Doesn't have that option.                                                                                                                                             | *( appendix 119 )*                                          | [8c48498](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/8c484989ced1eb6a400534a8da2aadb6a89b4d98) | PASS   |
| [# 72](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/72) | USER STORY : Like / Dislike Items of Shop                       | As a Site User I can Like / Dislike particular Item in Shop in order to express my opinion.                                                                                          | Logged in user : When I navigate to shop and open detail of Item then I am able to like or dislike the Item. Not logged in user : Doesn't have that option.                                                                                                                      | *( appendix 117 )*                                          | [35a4884](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/35a48849bb86b7ace9b376d3d8e645dc4954d472) | PASS   |
| [# 99](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/99) | USER STORY : Frequently bought together                         | As a Site User, I can see what items are bought together to be able to what else can I buy for the same project.                                                                    | When I navigate to the shop and item detail, I can see what items are frequently bought with the item that I am viewing.                                                                                                                                                          | Won't be implemented - Marked as "Won't Have" on Kanban Board | N/A                                                                                                                 | N/A    |
|                                                                            |                                                                 |                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                  |                                                               |                                                                                                                     |        |
| Epic 8                                                                     | Wishlist                                                        |                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                  |                                                               |                                                                                                                     |        |
| Issue                                                                      | Title                                                           | User Story                                                                                                                                                                          | Acceptance Criteria                                                                                                                                                                                                                                                              | Implementation                                                | Final Commit                                                                                                        | Result |
| [# 44](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/44) | USER STORY : Display Wishlist Items                             | As a Site User, I can display items in My Wishlist in order to manage the items.                                                                                                    | Logged In User : When I log in and navigate to "My Wishlist" section then I can clearly see all items in the wishlist . Not Logged In User : Doesn't have that option.                                                                                                           | *( appendix 120 )*                                          | [b71e9f9](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/b71e9f93064e251ebca34ca52ecf6e4e2fa0e672) | PASS   |
| [# 45](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/45) | USER STORY : Remove Items from Wishlist                         | As a Site User, I can remove items from My Wishlist one by one in order to manage the items in the Wishlist.                                                                        | Logged In User : When I log in and navigate to "My Wishlist" section then I can clearly see an option to delete item from Wishlist . Not Logged In User : Doesn't have that option.                                                                                              | *( appendix 120 )*                                          | [15910d7](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/15910d7bb677671a70b3253290957915f93002ab) | PASS   |
| [# 46](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/46) | USER STORY : Clear Wishlist                                     | As a Site User, I can delete all items in My Wishlist in order to manage the items.                                                                                                 | Logged In User : When I log in and navigate to "My Wishlist" section then I can clearly see option to delete all items from the Wishlist . Not Logged In User : Doesn't have that option.                                                                                        | *( appendix 120 )*                                          | [84e5561](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/84e55610bf98f797529552d0dfd6f5df50ecdcd2) | PASS   |
|                                                                            |                                                                 |                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                  |                                                               |                                                                                                                     |        |
| Epic 9                                                                     | Vault                                                           |                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                  |                                                               |                                                                                                                     |        |
| Issue                                                                      | Title                                                           | User Story                                                                                                                                                                          | Acceptance Criteria                                                                                                                                                                                                                                                              | Implementation                                                | Final Commit                                                                                                        | Result |
| [# 48](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/48) | USER STORY : Display content of Vault                           | As a Site User, I can display items in Vault in order to manage the items.                                                                                                          | When I visit the site and navigate to "Vault" section then I can clearly see all items in the Vault .                                                                                                                                                                            | *( appendix 121 )*                                          | [d407252](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/d40725233ee4938ac42d36a9a8505bf096f3e737) | PASS   |
| [# 49](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/49) | USER STORY : Adjust amounts of items in Vault                   | As a Site User, I can adjust amount of each item in Vault in order to manage the items before proceeding to Checkout.                                                               | When I visit the site and navigate to "Vault" section then I can clearly see amount of each item and I have an option to adjust or remove the item from the Vault .                                                                                                              | *( appendix 121 )*                                          | [f90e353](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/f90e353901b79ed1e8083944ebcbf61716692e1d) | PASS   |
| [# 50](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/50) |  USER STORY : Clear the Vault                                   | As a Site User, I can display items in Vault in order to manage the items.                                                                                                          | When I visit the site and navigate to "Vault" section then I can clearly see all items in the Vault .                                                                                                                                                                            | *( appendix 121 )*                                          | [b0af0c3](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/b0af0c39015731013707ebca089e5854f4619573) | PASS   |
| [# 51](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/51) |  USER STORY : Proceed to Checkout                               | As a Site User, I can proceed to Checkout in order to pay for items in my Vault.                                                                                                    | When I visit the site and navigate to "Vault" and I am happy with the content then I can clearly proceed to Checkout .                                                                                                                                                           | *( appendix 121 )*                                          | [ea6f86e](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/ea6f86e2d27f280041f8d4c6b6deca2348392418) | PASS   |
| [# 52](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/52) | USER STORY : Vault management toasts                            | As a Site User, I can see message that indicates Vault action along all items that are in Vault in order to be informed and have an idea what's in Vault without opening the Vault. | When I submit any "Vault" section action (add, delete, adjust) then I can clearly see in form of toast all items in the Vault, the total and postage threshold .                                                                                                                  | *( appendix 108 )*                                          | [ea6f86e](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/ea6f86e2d27f280041f8d4c6b6deca2348392418) | PASS   |
|                                                                            |                                                                 |                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                  |                                                               |                                                                                                                     |        |
| Epic 10                                                                    | Checkout                                                        |                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                  |                                                               |                                                                                                                     |        |
| Issue                                                                      | Title                                                           | User Story                                                                                                                                                                          | Acceptance Criteria                                                                                                                                                                                                                                                              | Implementation                                                | Final Commit                                                                                                        | Result |
| [# 61](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/61) | USER STORY : Checkout Page                                      | As a Site User, I can see checkout page so I know exactly what am I being charged for.                                                                                              | When I add my desired products into Vault and click "secure Payment" then a payment page loads up.                                                                                                                                                                               | *( appendix 122 )*                                          | [8b3724a](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/8b3724a2ab7034874a20588ff9ca25fa3bd12cca) | PASS   |
| [# 54](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/54) | USER STORY : Shipping Details                                   | As a Site User, I can provide shipping details in order to inform the shop where to send my purchase.                                                                               | Logged In User : When I navigate to "Secure Checkout" then I can enter / change (if provided in "My Details") shippings details . Not Logged In User : When I navigate to "Secure Checkout" then I can enter shippings details .                                                   | *( appendix 123 )*                                          | [bbe7628](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/bbe7628cc0bcf618ba307c8b9084157e08c34c7c) | PASS   |
| [# 62](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/62) | USER STORY : Save info                                          | As a Site User, I can save provided shipping info in order the form being prefilled with next order.                                                                                | Logged In User : When I navigate to "Secure Checkout" and provide new / different shipping info then I have an option to save the details provided. Not Logged In User : Doesn't have that option.                                                                                 | *( appendix 124 )*                                          | [9c34d7d](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/9c34d7d35134ff1e957e435e64d248ee09e8fb6d) | PASS   |
| [# 63](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/63) | USER STORY : Delivery Options                                   | As a Site User, I can choose between standard and express delivery in order to control the speed of delivery.                                                                       | When I navigate to "Secure Checkout" then I can choose my preferred delivery option.                                                                                                                                                                                             | *( appendix 125 )*                                          | [0ab3c1e](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/0ab3c1e6966f2454189670aa4ba0ec9e135e9544) | PASS   |
| [# 57](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/57) | USER STORY : Payment                                            | As a Site User, I have an option providing payment details in order to pay for my goods.                                                                                            | When I navigate to "Secure Checkout" and fill in all the required info then I can pay by providing payment media number.                                                                                                                                                         | *( appendix 122 )*                                          | [0ab3c1e](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/0ab3c1e6966f2454189670aa4ba0ec9e135e9544) | PASS   |
| [# 55](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/55) | USER STORY : Vouchers                                           | As a Site User, I have an option to redeem discount codes in order to get discount on my purchase.                                                                                   | When I navigate to "Secure Checkout" then I have an option to redeem discount code in clear manner.                                                                                                                                                                               | *( appendix 126 )*                                          | [0fbac68](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/0fbac6828c0efd40a85cfc957e6787acdaf51aba) | PASS   |
| [# 58](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/58) | USER STORY : Invoice Generator                                  | As a Site Admin, I need to be able to generate invoice in *.pdf format in order the invoice being attached to the confirmation email.                                              | When User successfully proceeds through checkout the invoice in *.pdf needs to be generated based on order details adn saved to database.                                                                                                                                        | *( appendix 127 )*                                          | [7395bb8](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/7395bb80231ab9d561153d54931fdd3fa7de11fe) | PASS   |
| [# 59](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/59) | USER STORY : Confirmation Email                                 | As a Site User, I do get confirmation email in order to know the transaction was successful.                                                                                        | When I successfully proceed through payment, then I am notified via email about my purchase.                                                                                                                                                                                      | *( appendix 128 )*                                          | [2b5929a](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/2b5929accb57289a57dd7a6deb64f81ecc04a228) | PASS   |
| [# 60](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/60) | USER STORY : Stock Update                                       | As a Site Admin, I need to be able to update stock amounts after every purchase in order the manage the inventory.                                                                  | When User successfully proceeds through checkout then the amounts of stock levels are updated.                                                                                                                                                                                    | Not Applicable                                                | [f901a9c](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/f901a9cf9609396bd325d29f2319e886f5536043) | PASS   |
| [# 56](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/56) | USER STORY : Stripe and Webhooks Setup                          | As a Site Admin, I need to be able to process the order functions even in event of failure in order to ensure no paying customer is left without goods.                             | When User provides valid payment media number but connection is interrupted for some reason during the confirmation process then all other functions (saving order, email, invoice) needs to proceed as normal via webhooks.                                                     | Not Applicable                                                | [9d07b91](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/9d07b912e0be257efa606122f476a791748ac300) | PASS   |
| [# 64](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/64) | USER STORY : Success Page                                       | As a Site User, I can clearly see success page in order to know my order went through without checking my emails.                                                                     | When I successfully proceed with payment then I can see success page containing order details, order number and estimated delivery dates.                                                                                                                                         | *( appendix 129 )*                                          | [c7d638c](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/c7d638cc91c9e8cc931d036b574f4737b9b192e1) | PASS   |
|                                                                            |                                                                 |                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                  |                                                               |                                                                                                                     |        |
| Epic 11                                                                    | Order History                                                   |                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                  |                                                               |                                                                                                                     |        |
| Issue                                                                      | Title                                                           | User Story                                                                                                                                                                          | Acceptance Criteria                                                                                                                                                                                                                                                              | Implementation                                                | Final Commit                                                                                                        | Result |
| [# 66](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/66) | USER STORY : Accessing Order History                            | As a Site User, I can access my own past orders in case of needing them in future.                                                                                                  | Logged In User : When I navigate to "Order History" section then I clearly see all my past orders then . Not Logged in User : Doesn't have that option.                                                                                                                            | *( appendix 130 )*                                          | [3b301fc](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/3b301fc1521ad8851a4392ab00337a54ac8a402e) | PASS   |
| [# 67](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/67) | USER STORY : Viewing past invoices                              | As a Site User, I can view detail of any of my own past orders in case of needing them in future.                                                                                   | Logged In User : When I navigate to "Order History" and select particular invoice to view then then the the invoice opens in new browser tab . Not Logged in User : Doesn't have that option.                                                                                      | *( appendix 131 )*                                          | [3b301fc](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/3b301fc1521ad8851a4392ab00337a54ac8a402e) | PASS   |
| [# 68](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/68) | USER STORY : Downloading past invoices                           | As a Site User, I can download any of my own past order invoices in case of needing them in future.                                                                                 | Logged In User : When I navigate to "Order History" and select particular invoice to download then then the the invoice downloads in web browser . Not Logged in User : Doesn't have that option.                                                                                  | *( appendix 132 )*                                          | [3b301fc](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/3b301fc1521ad8851a4392ab00337a54ac8a402e) | PASS   |
|                                                                            |                                                                 |                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                  |                                                               |                                                                                                                     |        |
| Epic 12                                                                    | Search Bar                                                      |                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                  |                                                               |                                                                                                                     |        |
| Issue                                                                      | Title                                                           | User Story                                                                                                                                                                          | Acceptance Criteria                                                                                                                                                                                                                                                              | Implementation                                                | Final Commit                                                                                                        | Result |
| [# 70](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/70) | USER STORY : Search Bar in header of page                       | As a Site User I am able to use search function through Categories, Items and Item descriptions in order to quickly find what am I looking for.                                      | When I navigate to any page of the site then I can see the search bar located in the header.                                                                                                                                                                                     | *( appendix 133 )*                                          | [93a786e](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/93a786e4d8c00f1b8cdf8754843cd3f83bdf2549) | PASS   |
| [# 71](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/71) | USER STORY : Search results                                     | As a Site User I can see search result to easily navigate through them.                                                                                                             | When I submit search criteria and click the search button then I am able to see the results.                                                                                                                                                                                     | *( appendix 134 )*                                          | [76022d3](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/76022d3c766485f452f85bab87b7588ee384f46b) | PASS   |
|                                                                            |                                                                 |                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                  |                                                               |                                                                                                                     |        |
| Epic 13                                                                    | Styling and design of UI                                        |                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                  |                                                               |                                                                                                                     |        |
| Issue                                                                      | Title                                                           | User Story                                                                                                                                                                          | Acceptance Criteria                                                                                                                                                                                                                                                              | Implementation                                                | Final Commit                                                                                                        | Result |
| [# 74](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/74) | USER STORY : Intuitive Navigation                               | As a Site Developer, I need to insure easy navigation throughout the site                                                                                                           | When user does access the site then all links and actions are intuitive and don't need too much thinking, design is responsive on all device sizes.                                                                                                                              | Not Applicable                                                | [5707b7b](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/5707b7b967861552ed18de3f89c954560dd2f623) | PASS   |
| [# 75](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/75) | USER STORY : Color Scheme                                       | As a Site Developer, I need to insure easy navigation throughout the sit                                                                                                            | When user does access the site then all links and actions are intuitive and don't need too much thinking, design is responsive on all device sizes.                                                                                                                              | Not Applicable                                                | [5707b7b](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/5707b7b967861552ed18de3f89c954560dd2f623) | PASS   |
| [# 76](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/76) | USER STORY : W3C + WAVE Compatibility                           | As a Site Developer, I need to insure easy navigation throughout the site for users in need of ease of access                                                                       | When user in need of ease of access tools does access the site then all links and actions are labelled and intuitive and don't confuse the User.                                                                                                                                  | Not Applicable                                                | [2043e49](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/2043e497eef8b727f24fe90bf1f014b6756b9615) | PASS   |
|                                                                            |                                                                 |                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                  |                                                               |                                                                                                                     |        |
| Epic 14                                                                    | Testing and Validation                                          |                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                  |                                                               |                                                                                                                     |        |
| Issue                                                                      | Title                                                           | User Story                                                                                                                                                                          | Acceptance Criteria                                                                                                                                                                                                                                                              | Implementation                                                | Final Commit                                                                                                        | Result |
| [# 78](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/78) | W3C HTML validation                                             | As a Site Developer, I need to ensure *.html files do pass the W3C validation.                                                                                                     | When I access any site and inspect the source code then copy the source code to W3C validator it doesn't display any major errors.                                                                                                                                                | Not Applicable                                                | [3df6e14](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/3df6e14e18d1af001b0681e040c32bb0a0838817) | PASS   |
| [# 79](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/79) | W3C CSS validation                                              | As a Site Developer, I need to ensure style.css file do pass the W3C validation.                                                                                                    | When I copy and paste the content of style.css file then it doesn't throw any major errors.                                                                                                                                                                                      | Not Applicable                                                | [d2f8a5a](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/d2f8a5af34e5447385796a73a270ea102f2314d0) | PASS   |
| [# 80](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/80) | JS validation                                                   | As a Site Developer, I need to ensure *.js files do pass the JS Lint validation.                                                                                                   | When I copy and paste the content of *.js files then it doesn't throw any major errors.                                                                                                                                                                                         | Not Applicable                                                | [aa7b1ca](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/aa7b1ca0c5191d05575a69e381e3953c513a5526) | PASS   |
| [# 81](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/81) | PEP8 validation                                                 | As a Site Developer, I need to ensure *.py file do pass the PEP8 validation.                                                                                                       | When I copy and paste the content of *.py files then it doesn't throw any errors.                                                                                                                                                                                               | Not Applicable                                                | [d8cf9ba](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/commit/d8cf9babec03c031dc7dec4d960e453b9967d246) | PASS   |

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/docs/testing.md#521-table-of-content---testing)

[Back to README.md](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

*Appendix 90 - Testing*

![Appendix 90](/docs/testing/test-90.png)

*Appendix 91 - Testing*

![Appendix 91](/docs/testing/test-91.png)

*Appendix 92 - Testing*

![Appendix 92](/docs/testing/test-92.png)

*Appendix 93 - Testing*

![Appendix 93](/docs/testing/test-93.png)

*Appendix 94 - Testing*

![Appendix 94](/docs/testing/test-94.png)

*Appendix 95 - Testing*

![Appendix 95](/docs/testing/test-95.png)

*Appendix 96 - Testing*

![Appendix 96](/docs/testing/test-96.png)

*Appendix 97 - Testing*

![Appendix 97](/docs/testing/test-97.png)

*Appendix 98 - Testing*

![Appendix 98](/docs/testing/test-98.png)

*Appendix 99 - Testing*

![Appendix 99](/docs/testing/test-99.png)

*Appendix 100 - Testing*

![Appendix 100](/docs/testing/test-100.png)

*Appendix 101 - Testing*

![Appendix 101](/docs/testing/test-101.png)

*Appendix 102 - Testing*

![Appendix 102](/docs/testing/test-102.png)

*Appendix 103 - Testing*

![Appendix 103](/docs/testing/test-103.png)

*Appendix 104 - Testing*

![Appendix 104](/docs/testing/test-104.png)

*Appendix 105 - Testing*

![Appendix 105](/docs/testing/test-105.png)

*Appendix 106 - Testing*

![Appendix 106](/docs/testing/test-106.png)

*Appendix 107 - Testing*

![Appendix 107](/docs/testing/test-107.gif)

*Appendix 108 - Testing*

![Appendix 108](/docs/testing/test-108.png)

*Appendix 109 - Testing*

![Appendix 109](/docs/testing/test-109.png)

*Appendix 110 - Testing*

![Appendix 110](/docs/testing/test-110.png)

*Appendix 111 - Testing*

![Appendix 111](/docs/testing/test-111.png)

*Appendix 112 - Testing*

![Appendix 112](/docs/testing/test-112.png)

*Appendix 113 - Testing*

![Appendix 113](/docs/testing/test-113.png)

*Appendix 114 - Testing*

![Appendix 114](/docs/testing/test-114.png)

*Appendix 115 - Testing*

![Appendix 115](/docs/testing/test-115.png)

*Appendix 116 - Testing*

![Appendix 116](/docs/testing/test-116.png)

*Appendix 117 - Testing*

![Appendix 117](/docs/testing/test-117.png)

*Appendix 118 - Testing*

![Appendix 118](/docs/testing/test-118.png)

*Appendix 119 - Testing*

![Appendix 119](/docs/testing/test-119.png)

*Appendix 120 - Testing*

![Appendix 120](/docs/testing/test-120.png)

*Appendix 121 - Testing*

![Appendix 121](/docs/testing/test-121.png)

*Appendix 122 - Testing*

![Appendix 122](/docs/testing/test-122.png)

*Appendix 123 - Testing*

![Appendix 123](/docs/testing/test-123.png)

*Appendix 124 - Testing*

![Appendix 124](/docs/testing/test-124.png)

*Appendix 125 - Testing*

![Appendix 125](/docs/testing/test-125.png)

*Appendix 126 - Testing*

![Appendix 126](/docs/testing/test-126.png)

*Appendix 127 - Testing*

![Appendix 127](/docs/testing/test-127.png)

*Appendix 128 - Testing*

![Appendix 128](/docs/testing/test-128.png)

*Appendix 129 - Testing*

![Appendix 129](/docs/testing/test-129.png)

*Appendix 130 - Testing*

![Appendix 130](/docs/testing/test-130.png)

*Appendix 131 - Testing*

![Appendix 131](/docs/testing/test-131.png)

*Appendix 132 - Testing*

![Appendix 132](/docs/testing/test-132.png)

*Appendix 133 - Testing*

![Appendix 133](/docs/testing/test-133.png)

*Appendix 134 - Testing*

![Appendix 134](/docs/testing/test-134.png)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/docs/testing.md#521-table-of-content---testing)

[Back to README.md](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---


## **6.2.3. Test Cases**

Part ot this testing was to ensure user cannot access restricted content to registered users or user cannot change content that was created by another user. This was achieved by using `LoginRequiredMixin` for classes and `@login_required` for methods when user needs to be logged in for certain view.

For user not being able to change content that isn't created by user was used following Mixin and test function. 

`UserPassesTestMixin`
```
    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser
```
---

### **Test case 001 - General Site Navigation ( Appendix 135 )**

General site navigation tested.

*Appendix 135 - Test Case 001*

![Test Case 001](/docs/testing/case-001.png)

---

### **Test case 002 - Search Function ( Appendix 136 )**

Search functions tested.

*Appendix 136 - Test Case 002*

![Test Case 00](/docs/testing/case-002.png)

---

### **Test case 003 - Registering New User ( Appendix 137 )**

New User registration tested.

*Appendix 137 - Test Case 003*

![Test Case 003](/docs/testing/case-003.png)

---

### **Test Case 004 - Changing user's name, phone number, marketing preferences ( Appendix 138 )**

Details change of registered User tested.

*Appendix 138 - Test Case 004*

![Test Case 004](/docs/testing/case-004.png)

---

### **Test Case 005 - Changing user's email ( Appendix 139 )**

Email change of registered User tested.

*Appendix 139 - Test Case 005*

![Test Case 005](/docs/testing/case-005.png)

---

### **Test Case 006 - Changing user's password ( Appendix 140 )**

Password change of registered User tested.

*Appendix 140 - Test Case 006*

![Test Case 006](/docs/testing/case-006.png)

---

### **Test Case 007 - Commenting on Shop Item ( Appendix 141 )**

Comments on Shop Items tested.

*Appendix 141 - Test Case 007*

![Test Case 007](/docs/testing/case-007.png)

---

### **Test Case 008 - Liking/Disliking on Shop Item ( Appendix 142 )**

Likes/Dislikes on Shop Items tested.

*Appendix 142 - Test Case 008*

![Test Case 008](/docs/testing/case-008.png)

---

### **Test Case 009 - Add to Wishlist ( Appendix 143 )**

Wishlist toggle tested.

*Appendix 143 - Test Case 009*

![Test Case 009](/docs/testing/case-009.png)

---

### **Test Case 010 - Wishlist functions ( Appendix 144 )**

Internal Wishlist functions tested.

*Appendix 144 - Test Case 010*

![Test Case 010](/docs/testing/case-010.png)

---

### **Test Case 011 - Vault functions ( Appendix 145 )**

Internal Vault functions tested.

*Appendix 145 - Test Case 011*

![Test Case 011](/docs/testing/case-011.png)

---

### **Test Case 012 - Checkout functions ( Appendix 146 )**

Internal and external Checkout functions tested.

*Appendix 146 - Test Case 012*

![Test Case 012](/docs/testing/case-012.png)

---

### **Test Case 013 - Webhooks functions ( Appendix 147 )**

Internal and external Webhooks functions tested.

*Appendix 147 - Test Case 013*

![Test Case 013](/docs/testing/case-013.png)

---

### **Test Case 014 - Order History functions ( Appendix 148 )**

Internal functions of User's Order History tested.

*Appendix 148 - Test Case 014*

![Test Case 014](/docs/testing/case-014.png)

---

### **Test Case 015 - Deleting User account ( Appendix 149 )**

Deleting Users account tested.

*Appendix 149 - Test Case 015*

![Test Case 015](/docs/testing/case-015.png)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/docs/testing.md#521-table-of-content---testing)

[Back to README.md](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

## **6.2.4. Viewport Testing**

- **Task :** To physically test the final project responsiveness on different devices with different view-port.
- **Method :** All test cases listed above were tested on following devices : 
  - IPhone 8 - mobile phone with small view-port
  - Samsung Fold Z4 - mobile phone with large view-port
  - FireHD 8 - tablet with small view-port
  - Samsung Galaxy tab S6 - tablet with large view-port
  - PC with resolution 1366px * 768px (HD)
  - PC with resolution 1920px * 1080px (Full HD)  
- **Expected result :** Project does response without distortion on all devices.
- **Actual result :**  No content is distorted on any of the listed devices.
- **Overall result :** Pass *( Appendix 150 )*

*Appendix 150 - Responsiveness testing*

![Responsiveness Testing](/docs/testing/responsiveness.png)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/docs/testing.md#521-table-of-content---testing)

[Back to README.md](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

## **6.2.5. Compatibility Testing**

- **Task :** To physically test the final project functionality in different browsing applications.
- **Method :** All test cases listed above were tested in following applications : 
  - Google Chrome
  - Mozilla Firefox
  - Microsoft Edge
  - Opera
  - Safari
- **Expected result :** Project does function in all web browsers.
- **Actual result :**  No content is distorted in any of the listed browsers and project keeps functionality, all navigation links are working and form is responsive to empty fields.
- **Overall result :** Pass

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/docs/testing.md#521-table-of-content---testing)

[Back to README.md](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---