# ***Ohm-Azing Components - Portfolio Project 5***
---
# **1. Key project information**

- **Description :** This Portfolio Project 5 website called **Ohm-Azing Components** is a site of imaginary online shop that sells electronic components, electronic kits, tools, books, etc. User can easily browse through the shop items, **add/delete** items from their **Wishlist**, express their opinion by **commenting** and **liking/disliking** shop items and most importantly order their selected items for home delivery including online payment.
- **Key project goal :** To offer all visitors of **Ohm-Azing Components** site the option to buy their chosen products, select delivery option and finish payment online without the need of leaving the house.
- **Audience :** There's no age or any other limit to audience of this page. Target audience are individuals at any level of experience that have interest in electronic components and electronic kits.
- **Live version :** Live version of **Ohm-Azing Components** e-shop page can be viewed at [https://ohmazing-components-1a5a0fcb9e95.herokuapp.com/](https://ohmazing-components-1a5a0fcb9e95.herokuapp.com/).
- **Dummy Card :** 4242 4242 4242 4242, expiry 04/24, cvc 242, zip 42424 
- **Developer :** [Tomas Kubancik](https://github.com/tomik-z-cech/)

![Mockup](/docs/mockup.png)

---

# **2. Table of Contents**

- [**1. Key project information**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#1-key-project-information)
- [**2. Table of Contents**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#2-table-of-contents)
- [**3. User Experience (UX)**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#3-user-experience-ux)
  * [**3.1. The Strategy Plane**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#31-the-strategy-plane)
    + [**3.1.1 The Idea**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#311-the-idea)
    + [**3.1.2 The Ideal User**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#312-the-ideal-user)
    + [**3.1.3 Site Goals**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#313-site-goals)
    + [**3.1.4 Epics**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#314-epics)
    + [**3.1.5 User stories**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#315-user-stories)
  * [**3.2. The Scope Plane**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#32-the-scope-plane)
    + [**3.2.1. Features to be implemented**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#321-features-to-be-implemented)
  * [**3.3. The Structure Plane**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#33-the-structure-plane)
    + [**3.3.1. Site Maps**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#331-site-maps)
    + [**3.3.2. Database Schemas**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#332-database-schemas)
  * [**3.4. Wire-frames**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#34-wire-frames)
  * [**3.5. The Surface Plane**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#35-the-surface-plane)
    + [**3.5.1. Logo**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#351-logo)
    + [**3.5.2. Color pallette**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#352-color-pallette)
    + [**3.5.3. Fonts**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#353-fonts)
    + [**3.5.4. Icons and pictures**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#354-icons-and-pictures)
- [**4. Features**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#4-features)
  * [**4.1. Features used in every HTML template**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#41-features-used-in-every-html-template)
    + [**4.1.1 Header**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#411-header)
    + [**4.1.2. Footer**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#412-footer)
    + [**4.1.3. Favicon**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#413-favicon)
    + [**4.1.4. Error Pages**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#414-error-pages)
    + [**4.1.5. Scroll bar**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#415-scroll-bar)
    + [**4.1.6. Loader**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#416-loader)
    + [**4.1.7. Sorting criterion**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#417-sorting-criterion)
    + [**4.1.8. Pagination**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#418-pagination)
    + [**4.1.9. Toasts**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#419-toasts)
    + [**4.1.10. Easter Egg**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#4110-easter-egg)
  * [**4.2. Main Content**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#42-main-content)
    + [**4.2.1. Landing Page**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#421-landing-page)
    + [**4.2.2. Shop Page**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#422-shop-page)
    + [**4.2.3. Item Detail Page**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#423-item-detail-page)
    + [**4.2.4. Wishlist Page**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#424-wishlist-page)
    + [**4.2.5. Vault Page**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#425-vault-page)
    + [**4.2.6. Checkout Page**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#426-checkout-page)
    + [**4.2.7. Checkout Success Page**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#427-checkout-success-page)
    + [**4.2.8. Order History Page**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#428-order-history-page)
    + [**4.2.9. My Profile Page**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#429-my-profile-page)
    + [**4.2.10. Search Results Page**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#4210-search-results-page)
    + [**4.2.11. Forms**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#4211-forms)
    + [**4.2.12. Admin Tools**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#4212-admin-tools)
    + [**4.2.13. User Emails**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#4213-user-emails)
  * [**4.3. Future Features**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#43-future-features)
- [**5. Marketing**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#5-marketing)
  * [**5.1. Social Media Presence**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#51-social-media-presence)
  * [**5.2. Search Engine Optimization (SEO)**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#52-search-engine-optimization-seo)
- [**6. Validation, Testing & Bugs**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#6-validation-testing--bugs)
  * [**6.1. Validation**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#61-validation)
  * [**6.2. Testing**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#62-testing)
  * [**6.3. Bugs**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#63-bugs)
- [**7. Deployment**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#7-deployment)
  * [**7.1. Transfer of progress from IDE**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#71-transfer-of-progress-from-ide)
  * [**7.2. Offline cloning**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#72-offline-cloning)
  * [**7.3. Deployment Prerequisites**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#73-deployment-prerequisites)
    + [**7.3.1. Gmail**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#731-gmail)
    + [**7.3.2. Neon Tech DB**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#732-neon-tech-db)
    + [**7.3.3. AWS Cloud Service**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#733-aws-cloud-service)
    + [**7.3.4. Django AWS Connection**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#734-django-aws-connection)
    + [**7.3.5. Stripe Configuration & Connection**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#735-stripe-configuration--connection)
    + [**7.3.6. Settings.py & file-tree**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#--736-settingspy---file-tree--)
  * [**7.4. Deployment to Heroku**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#74-deployment-to-heroku)
- [**8. Technologies & Credits**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#8-technologies---credits)
  * [**8.1. Technologies used to develop and deploy this project**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#81-technologies-used-to-develop-and-deploy-this-project)
  * [**8.2. Requirements.txt**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#82-requirementstxt)
  * [**8.3. Credits**](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#83-credits)

---

# **3. User Experience (UX)**

## **3.1. The Strategy Plane**

### **3.1.1 The Idea**
- The intention of **Ohm-Azing Components** site is to be friendly online shop where users can browse variate of products sorted between categories. Besides that, user can read details of each product, see product comments and also see opinion of other users in form of **likes/dislikes**.

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---
### **3.1.2 The Ideal User**

The target audience are individuals or groups such as rookies that are seeking inspiration in electronic components to build their own circuit or electronic kits that are programmable and versatile or electronic veterans that need tools or to top up their components stash. 

- Ideal user likes electronics
- Ideal user creates electronic projects
- Ideal user likes to shop online
- Ideal user likes to explore new trends and ideas in the electronics field
- Ideal user likes to share their opinion in form if **likes/dislikes** and **comments**

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---
### **3.1.3 Site Goals**

- Offer users ability of shopping online without leaving their home
- Offer users ability of reading other people comments on products
- Offer users ability to add items to their **Wishlist** if they want to save the item for later
- Offer users the ability to see details of each item in shop (ie. stock, price, description, etc. ) 
- Offer users inspiration in electronics field

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---
### **3.1.4 Epics**

As a thought process of the strategy plane, 14 epics were created and utilized. Please see below the detail list of epics with links, or a link to the project's [Kanban Board](https://github.com/users/tomik-z-cech/projects/4/views/1) *(Appendix 1)*. Those Epics were further sliced into 69 USER STORIES.

*Appendix 1 - Kanban Board*

![Kanban Board](/docs/kanban.png)

- EPIC 1 : Environment configuration - [issue #1](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/1)
- EPIC 2 : Database models - [issue #6](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/6)
- EPIC 3 : User Authentication and Authorization - [issue #10](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/10)
- EPIC 4 : Custom Admin Interface - [issue #15](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/15)
- EPIC 5 : General Features - [issue #22](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/22)
- EPIC 6 : User Profile Management - [issue #30](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/30)
- EPIC 7 : The Shop - [issue #35](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/35)
- EPIC 8 : Wishlist - [issue #43](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/43)
- EPIC 9 : Vault - [issue #47](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/47)
- EPIC 10 : Checkout - [issue #53](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/53)
- EPIC 11 : Order History - [issue #65](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/65)
- EPIC 12 : Search Bar - [issue #69](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/69)
- EPIC 13 : Styling and design of UI - [issue #73](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/73)
- EPIC 14 : Testing and Validation - [issue #77](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/77)


[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

### **3.1.5 User stories**
69 User stories were created based on the Epics. Each user story uses the MoSCoW prioritization technique. Each user story was also estimated for relative effort required to implement satisfactory result of acceptance criteria. My Story points are using a sequence inspired by the Fibonacci numbers (1, 2, 3, 5, 8, 13, etc.). This reflects the uncertainty and variability in estimating larger tasks. The idea was to easy distinguish the initial size of user story using this non-linear sequence. Each user story on the Kanban Board was given 2 labels (MoSCoW and Story Points).

MoSCoW prioritization technique stands for:

Must-Have: Critical requirements that must be implemented for the project to be considered successful.

Should-Have: Important requirements that are not critical but add significant value.

Could-Haves: Desirable features that would be nice to have but are not crucial.

Won't-Have: Features that are explicitly excluded from the project scope.

The **TOTAL** of Story Points for all User Stories in the project is 207.
- **Must-Have** : 125 story points ( 60 % )
- **Should-Have** : 46 story points ( 23 % )
- **Could-Have** : 27 story points ( 13 % )
- **Wont-Have** : 9 story points ( 4 % )

<details>
<summary>
View User Stories for EPIC 1 : Environment configuration
</summary>

| Issue                                                                    | Title                                  | User Story                                                                                                                 |
| ------------------------------------------------------------------------ | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [# 2](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/2) | USER STORY : Set up GiHub repository   | As a Developer, I need to set-up a repository on GitHub platform to be able to have control over versions of project.      |
| [# 3](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/3) | USER STORY : Set up dependencies       | As a Developer, I need to register and obtain links for third party services.                                              |
| [# 4](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/4) | USER STORY : Create working Django app | As a Developer, I need to install all dependencies, correctly set settings.py and create working app in local environment. |
| [# 5](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/5) | USER STORY : Deploy to Heroku          | As a Developer I need to create a working Heroku deployment.                                                          |
</details>


<details>
<summary>
View User Stories for EPIC 2 : Database Models
</summary>

| Issue                                                                    | Title                                            | User Story                                                                                                                                                  |
| ------------------------------------------------------------------------ | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [# 7](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/7) | USER STORY : Define Database Schema              | As a Developer, I need to create database schema that fits the purpose of the project and also create all the modular apps that will be used in the project. |
| [# 8](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/8) | USER STORY : Create database relationships       | As a Developer, I need to define relationships between models and import the relationships into working apps models.                                         |
| [# 9](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/9) | USER STORY : Implement Data Validation in Models | As a Developer, I need implement data validation rules within Ohm-Azing Components database models.                                                         |
</details>


<details>
<summary>
View User Stories for EPIC 3 : User Authentication and Authorization
</summary>

| Issue                                                                      | Title                                       | User Story                                                                                       |
| -------------------------------------------------------------------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| [# 11](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/11) | USER STORY : Implement user registration    | As a Site User I am able to register to create new account and to select username and password. |
| [# 12](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/12) | USER STORY : Log In                         | As a Site User I am able to Log In to see registered user section.                               |
| [# 13](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/13) | USER-STORY : Reset my password if forgotten | As a Site User I am able to Reset My Password to change my password if forgotten.                |
| [# 14](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/14) | USER STORY : Log out                        | As a Site User, I am able to log out to leave the site functions for registered users.           |
</details>


<details>
<summary>
View User Stories for EPIC 4 : Custom Admin Interface
</summary>

| Issue                                                                      | Title                                               | User Story                                                                                                                             |
| -------------------------------------------------------------------------- | --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| [# 16](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/16) | USER STORY : Categories section                     | As a Business Owner, I have option to do full CRUD with item categories in order to manage my shop.                                    |
| [# 17](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/17) | USER STORY : Items section                          | As a Business Owner, I have option to do full CRUD with items in order to manage products sold in my shop.                             |
| [# 18](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/18) | USER STORY : Invoices section                       | As a Business Owner, I have option to view or download any invoice that was created by shoppers.                                       |
| [# 19](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/19) | USER STORY : Vouchers section                       | As a Business Owner, I have option to perform full CRUD on "Vouchers" that could be redeemed via checkout.                             |
| [# 20](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/20) | USER STORY : Comments section                       | As a Business Owner, I have option to approve/delete comments to ensure no inappropriate content on the project page.                  |
| [# 21](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/21) | USER STORY : Postage Settings section               | As a Business Owner, I have option to adjust free postage threshold and postage fees for standard and express delivery options.         |
| [# 28](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/28) | USER STORY : Email interface for marketing purposes | As a Site admin, I need to implement Mailing interface to be able to send emails to all users signed up for email communication.       |
| [# 97](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/97) | USER STORY : Postage label printing                 | As a Site Admin, I need implement postage label printing page to be able to Effortlessly print postage labels.                         |
| [# 98](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/98) | USER STORY : Order status emails                    | As a Site Admin, I can mark orders as accepted, pending, fulfilled to be able to keep customers informed of the status of their order. |
</details>


<details>
<summary>
View User Stories for EPIC 5 : General Features
</summary>

| Issue                                                                      | Title                        | User Story                                                                                                                                                      |
| -------------------------------------------------------------------------- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [# 23](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/23) | USER STORY : FavIcon & Title | As a Site User I would like to be able to differentiate this site from other sites opened in my browser, in order of easy navigation.                            |
| [# 24](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/24) | USER STORY : Header          | As a Site User I want to be able to navigate easily through-out the site.                                                                                       |
| [# 25](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/25) | USER STORY : Footer          | As a Site User I want to be able to find useful info on the bottom of the site in order not to scroll and search too much around.                               |
| [# 26](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/26) | USER STORY : Loader          | As a Site User I want to be able to see if page is working in the form of loader that appears when complex task is performed.                                   |
| [# 27](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/27) | USER STORY : Toasts          | As a Site User I want to be informed of results of requests performed in the form of toast that appears when complex task is done successfully / unsuccessfully. |
</details>


<details>
<summary>
View User Stories for EPIC 6 : User Profile Management
</summary>

| Issue                                                                      | Title                                                           | User Story                                                                                                           |
| -------------------------------------------------------------------------- | --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| [# 31](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/31) | USER STORY : Change Details (Phone Number, Email Address, etc.) | As a Site User I can Update My Details to be able to manage my account in case of changes.                           |
| [# 32](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/32) | USER STORY : Delete my account                                  | As a Site User I can Delete My Account to be able to opt out from all services.                                      |
| [# 33](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/33) | USER STORY : Profile Picture                                    | As a Site User I can Change my profile picture to add the finishing touch to my profile.                             |
| [# 34](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/34) | USER STORY : Opt In/Out for Newsletter                          | As a Site User I can Opt In/Out for Newsletter or other marketing communication to be able to change my preferences. |
</details>


<details>
<summary>
View User Stories for EPIC 7 : The Shop
</summary>

| Issue                                                                      | Title                                     | User Story                                                                                                                                                    |
| -------------------------------------------------------------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [# 36](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/36) | USER STORY : Shop Highlights              | As a Site User, I would like to See Newest and Favorites on the landing page so I can see easily what products are after arriving and what are most popular. |
| [# 37](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/37) | USER STORY : Shop by Category             | As a Site User, I would like to have the shop items sorted by category so I can browse the items faster.                                                      |
| [# 38](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/38) | USER STORY : Product Details              | As a Site User, I would like to see the details of each item in separate page so I won't get lost in too much info.                                           |
| [# 39](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/39) | USER STORY : Add to Vault                 | As a Site User, I need to be able to add items to vault in order to see the entire order before payment.                                                      |
| [# 40](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/40) | USER STORY : Add to Wishlist              | As a Site User, I need to be able to add items to my Wishlist in order to see keep the items I am interested in separately.                                   |
| [# 41](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/41) | USER STORY : Comment on Products          | As a Site User I can Comment on Items to share my opinion.                                                                                                    |
| [# 42](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/42) | USER STORY : See Comments of Others       | As a Site User I can see other comments on Items to read other Users opinions.                                                                                |
| [# 72](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/72) | USER STORY : Like / Dislike Items of Shop | As a Site User I can Like / Dislike particular Item in Shop in order to express my opinion.                                                                    |
| [# 99](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/99) | USER STORY : Frequently bought together   | As a Site User, I can see what items are bought together to be able to what else can I buy for the same project.                                              |
</details>


<details>
<summary>
View User Stories for EPIC 8 : Wishlist
</summary>

| Issue                                                                      | Title                                   | User Story                                                                                                   |
| -------------------------------------------------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| [# 44](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/44) | USER STORY : Display Wishlist Items     | As a Site User, I can display items in My Wishlist in order to manage the items.                             |
| [# 45](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/45) | USER STORY : Remove Items from Wishlist | As a Site User, I can remove items from My Wishlist one by one in order to manage the items in the Wishlist. |
| [# 46](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/46) | USER STORY : Clear Wishlist             | As a Site User, I can delete all items in My Wishlist in order to manage the items.                          |
</details>


<details>
<summary>
View User Stories for EPIC 9 : Vault
</summary>

| Issue                                                                      | Title                                         | User Story                                                                                                                                                                          |
| -------------------------------------------------------------------------- | --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [# 48](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/48) | USER STORY : Display content of Vault         | As a Site User, I can display items in Vault in order to manage the items.                                                                                                          |
| [# 49](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/49) | USER STORY : Adjust amounts of items in Vault | As a Site User, I can adjust amount of each item in Vault in order to manage the items before proceeding to Checkout.                                                               |
| [# 50](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/50) |  USER STORY : Clear the Vault                 | As a Site User, I can display items in Vault in order to manage the items.                                                                                                          |
| [# 51](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/51) |  USER STORY : Proceed to Checkout             | As a Site User, I can proceed to Checkout in order to pay for items in my Vault.                                                                                                    |
| [# 52](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/52) | USER STORY : Vault management toasts          | As a Site User, I can see message that indicates Vault action along all items that are in Vault in order to be informed and have an idea what's in Vault without opening the Vault. |
</details>


<details>
<summary>
View User Stories for EPIC 10 : Checkout
</summary>

| Issue                                                                      | Title                                  | User Story                                                                                                                                              |
| -------------------------------------------------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [# 61](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/61) | USER STORY : Checkout Page             | As a Site User, I can see checkout page so I know exactly what am I being charged for.                                                                  |
| [# 54](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/54) | USER STORY : Shipping Details          | As a Site User, I can provide shipping details in order to inform the shop where to send my purchase.                                                   |
| [# 62](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/62) | USER STORY : Save info                 | As a Site User, I can save provided shipping info in order the form being prefilled with next order.                                                    |
| [# 63](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/63) | USER STORY : Delivery Options          | As a Site User, I can choose between standard and express delivery in order to control the speed of delivery.                                           |
| [# 57](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/57) | USER STORY : Payment                   | As a Site User, I have an option providing payment details in order to pay for my goods.                                                                |
| [# 55](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/55) | USER STORY : Vouchers                  | As a Site User, I have an option to redeem discount codes in order to get discount on my purchase.                                                       |
| [# 58](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/58) | USER STORY : Invoice Generator         | As a Site Admin, I need to be able to generate invoice in \*.pdf format in order the invoice being attached to the confirmation email.                  |
| [# 59](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/59) | USER STORY : Confirmation Email        | As a Site User, I do get confirmation email in order to know the transaction was successful.                                                            |
| [# 60](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/60) | USER STORY : Stock Update              | As a Site Admin, I need to be able to update stock amounts after every purchase in order the manage the inventory.                                      |
| [# 56](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/56) | USER STORY : Stripe and Webhooks Setup | As a Site Admin, I need to be able to process the order functions even in event of failure in order to ensure no paying customer is left without goods. |
| [# 64](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/64) | USER STORY : Success Page              | As a Site User, I can clearly see success page in order to know my order went through without checking my emails.                                         |
</details>


<details>
<summary>
View User Stories for EPIC 11 : Order History
</summary>

| Issue                                                                      | Title                                 | User Story                                                                                          |
| -------------------------------------------------------------------------- | ------------------------------------- | --------------------------------------------------------------------------------------------------- |
| [# 66](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/66) | USER STORY : Accessing Order History  | As a Site User, I can access my own past orders in case of needing them in future.                  |
| [# 67](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/67) | USER STORY : Viewing past invoices    | As a Site User, I can view detail of any of my own past orders in case of needing them in future.   |
| [# 68](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/68) | USER STORY : Downloading past invoices | As a Site User, I can download any of my own past order invoices in case of needing them in future. |
</details>


<details>
<summary>
View User Stories for EPIC 12 : Search Bar
</summary>

| Issue                                                                      | Title                                     | User Story                                                                                                                                     |
| -------------------------------------------------------------------------- | ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| [# 70](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/70) | USER STORY : Search Bar in header of page | As a Site User I am able to use search function through Categories, Items and Item descriptions in order to quickly find what am I looking for. |
| [# 71](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/71) | USER STORY : Search results               | As a Site User I can see search result to easily navigate through them.                                                                        |
</details>


<details>
<summary>
View User Stories for EPIC 13 : Styling and design of UI
</summary>

| Issue                                                                      | Title                                 | User Story                                                                                                    |
| -------------------------------------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| [# 74](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/74) | USER STORY : Intuitive Navigation     | As a Site Developer, I need to insure easy navigation throughout the site                                     |
| [# 75](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/75) | USER STORY : Color Scheme             | As a Site Developer, I need to insure easy navigation throughout the sit                                      |
| [# 76](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/76) | USER STORY : W3C + WAVE Compatibility | As a Site Developer, I need to insure easy navigation throughout the site for users in need of ease of access |
</details>


<details>
<summary>
View User Stories for EPIC 14 : Testing and Validation
</summary>

| Issue                                                                      | Title               | User Story                                                                        |
| -------------------------------------------------------------------------- | ------------------- | --------------------------------------------------------------------------------- |
| [# 78](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/78) | W3C HTML validation | As a Site Developer, I need to ensure \*.html files do pass the W3C validation.   |
| [# 79](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/79) | W3C CSS validation  | As a Site Developer, I need to ensure style.css file do pass the W3C validation.  |
| [# 80](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/80) | JS validation       | As a Site Developer, I need to ensure \*.js files do pass the JS Lint validation. |
| [# 81](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/81) | PEP8 validation     | As a Site Developer, I need to ensure \*.py file do pass the PEP8 validation.     |
</details>


[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

## **3.2. The Scope Plane**

After decided on the strategy, the scope plane was carefully created.

### **3.2.1. Features to be implemented**

- **User Authentication** : Users can Register, access **My Profile** page where users can manage their information and preferences and delete their account (CRUD)

- **Shop** : Users can browse through the items that are offered, divided by categories. The items can be sorted via multiple criterion (Name, Price, Rating) and paginated to users preference.

- **Item Detail** : Users can easily see all details that are attached to the item of their selection (Price, Rating, Amount of comments) and can add the item to the **Vault** from here.

- **Liking and Commenting** : Users can **Like** or **Dislike** shop items so they can express their interest. Users can also comment on shop items in order to allow them to engage in discussions.

- **Wishlist** : Users can save items that want to view or buy in later time.

- **Vault** : Users can review all items that want to buy before the final purchase is made.

- **Checkout** : Offers users safe way of paying for their goods.

- **Vouchers** : Users can redeem vouchers that can be created via **Admin Tools** that offer discount on users purchase.

- **Delivery Option** : User can opt for standard or express delivery that deffer by length of delivery time and price.

- **My Details** : Page where users can manage all aspects of their account after successful registration process.

- **Search** : Search bar for users is provided in the header so users can access the search function at any stage of browsing. 

- **Notifications** : Notifications for new orders bookings need to be provided to the user both on screen and via email.


[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

## **3.3. The Structure Plane**

### **3.3.1. Site Maps**

The following site-maps show how the site is structured to **Logged in user** *( Appendix 2 )* ,**Not logged in user** *( Appendix 3 )* and **Site Admin** *( Appendix 3 )*.

*Appendix 2 - Site Map - Logged In*

![Site Map - Logged In](/docs/sitemap-logedin.png)

*Appendix 3 - Site Map - Not Logged In*

![Site Map - Not Logged In](/docs/sitemap-logedout.png)

*Appendix 4 - Site Map - Site Admin*

![Site Map - Not Logged In](/docs/sitemap-admin.png)


[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

### **3.3.2. Database Schemas**

Following schemas show intended database structure *( Appendix 5 )* and the actual database structure generated by DBeaver *( Appendix 6 )*.

*Appendix 5 - Initial DB schema*

![Initial DB Schema](/docs/db-dchema.png)

*Appendix 6 - DBeaver DB schema and relationships*

![DBeaver DB Schema](/docs/dbeaver-schema.png)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

## **3.4. Wire-frames**

- **Header and Footer** : Header and footer is established on every single page. **Header** is displayed on top of each page, **Footer** is displayed at the very bottom of each page so it doesn't cover any content *( Appendix 7 )*.

*Appendix 7 - Header and Footer Wire-frame*

![Header and Footer Wire-frame](/docs/wireframes/header-footer-wireframe.png)

- **Landing page** : Provides user with clear understanding of what the page is about. User is also provided with 3 newest arrivals (3 newly added items to the database), 3 favorite items (3 items with the highest likes/dislikes rating ) and option for the user to sign up for **Ohm-Azing Components** newsletter *( Appendix 8 )*.

*Appendix 8 - Landing Page Wire-frame*

![Landing Page Wire-frame](/docs/wireframes/landing-wireframe.png)

- **Shop page** : Provides user with selection of all available categories and all items that belong to the category. User clearly sees item name, price, amount of comments, rating of item and stock level *( Appendix 9 )*..

*Appendix 9 - Shop Page Wire-frame*

![Shop Page Wire-frame](/docs/wireframes/shop-wireframe.png)

- **Item Detail page** : Provides user with all relevant product info including name, description, etc. User can select quantity to add to **Vault**, user can also select between different item sizes and values (only where applicable). User can add item to **Wishlist** - *( Appendix 10 )*.

*Appendix 10 - Item Detail Page Wire-frame*

![Item Detail Page Wire-frame](/docs/wireframes/item-detail.png)

- **Wishlist page** : This is where user can store their **Wishlist** items, in case the user wan't to buy the item later or just holding it to see trends first. This function is only available to logged in users. *( Appendix 11 )*.

*Appendix 11 - Wishlist Page Wire-frame*

![Wishlist Page Wire-frame](/docs/wireframes/wishlist-wireframe.png)

- **Vault Page** : This page serves as last check before **Checkout**. Users can adjust quantity of item added to **Vault** previously or remove the item from **Vault** or clear **Vault** entirely *( Appendix 12 )*.

*Appendix 12 - Vault Page Wire-frame*

![Vault Page Wire-frame](/docs/wireframes/vault-wireframe.png)

- **Checkout Page** : Users are prompted to fill in delivery details (details are pre-filled if user logged in and details are saved). Users can select between delivery options, users can redeem vouchers and also fill pay for their items using credit card details field *( Appendix 13 )*.

*Appendix 13 - Checkout Page Wire-frame*

![Checkout Page Wire-frame](/docs/wireframes/checkout-wireframe.png)

- **Checkout Successful Page** : This page is presented to users after successful process of payment. This page indicates order number, expected delivery dates based on user selection and review of items that user paid for *( Appendix 14 )*.

*Appendix 14 - Checkout Successful Page Wire-frame*

![Checkout Successful Page Wire-frame](/docs/wireframes/checkout-ok.png)

- **My Profile Page** : Gives user the ability to change their details and preferences. The form is pre-populated with existing details. It also gives the user ability to delete their account entirely. *( Appendix 15 )*.

*Appendix 15 - My Profile Page*

![My Profile Page Wire-frame](/docs/wireframes/profile-wireframe.png)

- **Order History Page** : This page gives users the ability to browse history of their orders with functions of viewing and downloading the invoices of the orders. *( Appendix 16 )*.

*Appendix 16 - Order History Page*

![Order History Page Wire-frame](/docs/wireframes/history-wireframe.png)

- **Search Results Page** : Provides the user with results of their search query in two groups, categories and shop items. Users have the option to search again from the same page or any page they visit. *( Appendix 17 )*.

*Appendix 17 - Search Results Page*

![Search Results Page Wire-frame](/docs/wireframes/search-results-wireframe.png)

- **Forms** : Forms do interact with user. They are designed to be clear and to the point, always in center of the screen. *( Appendix 18 )*.

*Appendix 18 - Forms*

![Forms Wire-frame](/docs/wireframes/forms-wireframe.png)

- **Admin Tools Page** : Admin tools page is designed only for SuperUsers. This page allows the admin to manage functionality of the whole site with various settings and options. Admin Tools are accessible from devices with width of screen greater than 1200px.  *( Appendix 19 )*.

*Appendix 19 - Admin Tools Page*

![Admin Tools Page Wire-frame](/docs/wireframes/admin-wireframe.png)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

## **3.5. The Surface Plane**

Once the Strategy, Scope, Structure and Skeleton Planes were in place, it was time to work on the Surface Plane (Design).

### **3.5.1. Logo**

To create the logo, site called [Looka](https://looka.com/) was used. Few ideas were presented to the site owner and one of the logos was picked *( Appendix 20 )*

*Appendix 20 - Logo*

![Logo](/docs/email_logo.png)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

### **3.5.2. Color pallette**

Based on the colors of the logo, rest of the colors were picked using the [Adobe Color Wheel](https://color.adobe.com/create/color-wheel), following colors were picked into the color pallette *( Appendix 21 )*. As some of the colors needed to be opaque, following CSS variables were established *( Appendix 22 )*.

*Appendix 21 - Color pallette*

![Color pallette](/docs/color-pallette.png)

*Appendix 22 - Color variables*

![Color variables](/docs/color-vars.png)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

### **3.5.3. Fonts**

[Google Fonts](https://fonts.google.com/) site was used to pick the best typography style. The most importance was given to balance between style and readability. As a developer I needed to ensure that all text is displayed clear.

One font was picked and saved in CSS vars *( Appendix 24)* :
 - Electrolize (Sans Serif fallback) -  *( Appendix 23 )*

*Appendix 23 - Electrolize Font*

![Electrloze Font](/docs/electrolize-font.png)

*Appendix 24 - Font Variable*

![Font Variable](/docs/font-vars.png)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

### **3.5.4. Icons and pictures**

Icons used throughout the projects are [Bootstrap Icons](https://icons.getbootstrap.com/). All of the icons are free to use under their T&C license. Icons were user for various parts of the project such as the Menu, Footer and Buttons as they do enhance user experience.

Site called [Freepik](https://www.freepik.com/) was used to download images used in this project. The site offers massive amounts of imagery that is free to download and use under their T&C license. Images from [Freepik](https://www.freepik.com/) were used as product images and background image.

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

# **4. Features**

## **4.1. Features used in every HTML template**

### **4.1.1 Header**
- Header contains a Logo section *( Appendix 27 )*, which is also used as a link to Home page `{% url 'home' %}`. Center of the header is used for Search Bar and in the left top corner is located the **Menu** section along with **Vault** and **Wishlist** *( Appendix 26 )* for easy navigation through all the pages.The header changes to different layout *( Appendix 27 )* when the resolution changes to less than 1200 pixels in width.
- Header is designed to cover full width `width: 100%` of the browsing window.
- This will allow user to navigate through the pages and to navigate back to home page when click on logo.
- Header extends `base.html` in block `{% include 'header.html' %}`

*Appendix 25 - Logo*

![Logo](/docs/features/logo.png)

*Appendix 26 - Header on HD devices*

![Header on HD devices](/docs/features/big-header.png)

*Appendix 27 - Header on devices less 1200px in width*

![Header on devices less 1200px](/docs/features/small-header.png)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

### **4.1.2. Footer**

- Footer  *( Appendix 28 )* is designed to reveal basic contact details of **Ohm-Azing Components** on the left hand side, phone number and email address are constructed to be clickable links that are very useful especially for mobile phone users. Center of footer is designed to bring the user to Facebook via link that opens in new browser tab and it has links to Terms & Conditions and Privacy Policy Modals.
Right hand site of the footer is devoted to accepted cards logos and Stripe link.
- Footer is designed to cover full width `width: 100%` of the browsing window.
- This will allow user to open phone app (dial the number directly), send e-mail (open e-mail application on phone/tablet) and open Facebook link in new window.
- Footer changes the appearance on devices with width lesser than 1200px *( Appendix 29 )*.
- Footer extends `base.html` in block `{% include 'footer.html' %}`

*Appendix 28 - Footer on HD devices*

![Footer on HD devices](/docs/features/big-footer.png)

*Appendix 29 - Footer on devices less 1200px in width*

![Footer on devices less 1200px in width](/docs/features/small-footer.png)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

### **4.1.3. Favicon**

- Every template in this project is equipped with Favicon. This is to ease navigation for user in case of more tabs opened. The logo was selected as Favicon *( Appendix 30)*. 

*Appendix 30 - Favicon*

![Favicon](/docs/features/favicon.png)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

### **4.1.4. Error Pages**

- This project is designed to have custom error pages. In case of user clicks on broken link, submits action that isn't supported or tries to reach certain view without permission, then user isn't completely "cut off" from browsing, instead an error page with header and footer appears and user is informed of the situation.

- The following custom error pages were created :
- - 403 - Received when user attempts to access a web resource for which they lack the necessary permissions. *( Appendix 31 )*
- - 404 - Encountered when the requested web resource by user is not found on the server. *( Appendix 32 )*
- - 500 - Displayed when the web server encounters an internal error while processing the request. *( Appendix 33 )*

*Appendix 31 - 403.html*

![403.html](/docs/features/403html.png)

*Appendix 32 - 404.html*

![404.html](/docs/features/404html.png)

*Appendix 33 - 500.html*

![500.html](/docs/features/500html.png)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

### **4.1.5. Scroll bar**
- Custom scroll bar was used to fit within the color theme within the project *( Appendix 34 )*.

*Appendix 34 - Scroll bar*

![Scrollbar](/docs/features/scrollbar.png)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

### **4.1.6. Loader**
- Custom loader was used to fit within the color theme within the project to indicate to users that the page is working even if it might take a bit of time *( Appendix 35 )*.

*Appendix 35 - Loader*

![Loader](/docs/features/loader.gif)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

### **4.1.7. Sorting criterion**
- Multiple pages are equipped by sorting criterion that allows user to sort display items by their choice. This is used in **Shop Page** and **Admin Tools**  *( Appendix 36 )*.

*Appendix 36 - Sorting criterion*

![Sorting criterion](/docs/features/sorting.png)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

### **4.1.8. Pagination**
- Multiple pages are equipped by pagination that allows user to display amount of items by their choice. This is used in **Shop Page** and **Admin Tools** *( Appendix 37 )*. When pagination in use (All Items is not the selected option), pagination Navigation Bar will be displayed *( Appendix 38 )*. 

*Appendix 37 - Pagination option*

![Pagination option](/docs/features/pagination.png)

*Appendix 38 - Pagination Navbar*

![Pagination Navbar](/docs/features/pagination-nav.png)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

### **4.1.9. Toasts**
- Toasts are used to communicate with the user. Four levels of toasts are in use (success, error, info and vault). Toasts do appear on the right bottom corner of the page with useful message for the user. Templates for toasts are nesting in `templates/toasts`. Two designs were created, simple message toast *( Appendix 39 )* that communicates simple message to the user and Vault toasts that let's user know how much more to spend for free delivery and recapitulates the whole content of Vault *( Appendix 40 )*. 

*Appendix 39 - Simple toast*

![Simple toast](/docs/features/simple-toast.png)

*Appendix 40 - Vault toast*

![Vault toast](/docs/features/vault-toast.png)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

### **4.1.10. Easter Egg**
- "Easter Egg" surprise is hidden within the project. When user types "ilovetocode" at any stage of browsing, they will be revealed with hidden voucher discount code.  *( Appendix 41 )*. 

*Appendix 41 - Easter Egg*

![Easter Egg](/docs/features/easteregg.png)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

## **4.2. Main Content**

### **4.2.1. Landing Page**

- **App :** `landing`
- **Template File :** `index.html` - extends `base.html`
- **User :** Provides user with clear understanding of what the page is about. User is also provided with 3 newest shop items along with 3 favorite items. User can sign up to newsletter  *( Appendix 42 )*.

*Appendix 42 - Landing Page*

![Landing Page](/docs/features/landing.png)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

### **4.2.2. Shop Page**

- **App :** `items`
- **Template File :** `shop.html` - extends `base.html`
- **User :** Provides users with selection of all available categories on the left hand site and all items that are in the category on the right hand site. Users can sort the items by various criterion and paginate the page as they wish. Users can find details of price, stock level, rating and amount of comments. *( Appendix 43 )*.

*Appendix 43 - Shop Page*

![Shop Page](/docs/features/shop.png)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

### **4.2.3. Item Detail Page**

- **App :** `items`
- **Template File :** `item_detail.html` - extends `base.html`
- **User :** Provides users with exhaustive details of selected product, including price, description, etc. Logged in users can add/remove item to/from their Wishlist, like/dislike item and add comments. Not logged in users have the ability to read comments of others. *( Appendix 44 )*. Protection against adding greater quantity than in stock in place.

*Appendix 44 - Item Detail Page*

![Item Detail Page](/docs/features/item-detail.png)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

### **4.2.4. Wishlist Page**

- **App :** `wishlist`
- **Template File :** `wishlist.html` - extends `base.html`
- **User :** Wishlist is only available to logged in users. Users can review all items that users ever added to their Wishlist. Users have the ability to remove item from Wishlist or completely clear the Wishlist *( Appendix 45 )*. Modal is used as confirmation when user likes to clear their Wishlist.

*Appendix 45 - Wishlist Page*

![Wishlist Page](/docs/features/wishlist.png)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

### **4.2.5. Vault Page**

- **App :** `vault`
- **Template File :** `vault.html` - extends `base.html`
- **User :** Vault gives users the ability to check their order once again before they navigate to checkout page. Users can adjust the quantity of item in their Vault, remove the item or clear the Vault entirely. All those functions are available to both logged in or not logged in users. Once they are happy with the Vault content, they can proceed to checkout *( Appendix 46 )*. Modal is used as confirmation when user likes to clear their Vault. Protection against adding greater quantity than in stock in place.

*Appendix 46 - Vault Page*

![Vault Page](/docs/features/vault.png)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

### **4.2.6. Checkout Page**

- **App :** `checkout`
- **Template File :** `checkout.html` - extends `base.html`
- **User :** In checkout page *( Appendix 47 )* , users have to fill in their contact and shipping details. If user is logged in and has those details saved in their profile, those details are pre-populated in checkout *( Appendix 48 )*. If users are logged and but don't have those details saved, they have option to save it now for later *( Appendix 49 )*. Users can select between two delivery options *( Appendix 50 )*. Users can use discount codes *( Appendix 51 )* and *( Appendix 52 )*. Users do pay for their order on this page *( Appendix 53 )*. Page is protected for incorrect form submission *( Appendix 54 )*. The checkout app also updates the amount of stock of item after successful purchase.

*Appendix 47 - Checkout Page*

![Checkout Page](/docs/features/checkout.png)

*Appendix 48 - Shipping details*

![Shipping details](/docs/features/shipping-details.png)

*Appendix 49 - Save checkbox*

![Save checkbox](/docs/features/save-shipping.png)

*Appendix 50 - Delivery options*

![Delivery options](/docs/features/delivery-options.png)

*Appendix 51 - Unused voucher*

![Unused voucher](/docs/features/voucher-unused.png)

*Appendix 52 - Used voucher*

![Used voucher](/docs/features/vocuher-used.png)

*Appendix 53 - Payment*

![Payment](/docs/features/payment.png)

*Appendix 54 - Incorrect field protection*

![Incorrect field protection](/docs/features/checkout-protection.gif)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

### **4.2.7. Checkout Success Page**

- **App :** `checkout`
- **Template File :** `checkout_ok.html` - extends `base.html`
- **User :** This page confirms to the user that the payment processed correctly adn also lets them know the order number and estimated delivery dates *( Appendix 55 )*.

*Appendix 55 - Checkout Success Page*

![Checkout Success Page](/docs/features/checkout-ok.png)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

### **4.2.8. Order History Page**

- **App :** `history`
- **Template File :** `history.html` - extends `base.html`
- **User :** This page lists all previous orders to the users and lets them view and download the invoices *( Appendix 56 )*. 

*Appendix 56 - Order History Page*

![Order History Page](/docs/features/history.png)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

### **4.2.9. My Profile Page**

- **App :** `profilemanager`
- **Template File :** `my_details.html` - extends `base.html`
- **User :** Gives user the ability to change their details and preferences. The form is pre-populated with existing details. It also gives the user ability to delete their account entirely. *( Appendix 57 )*.

*Appendix 57 - My Details Page*

![My Details Page](/docs/features/my-details.png)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

### **4.2.10. Search Results Page**

- **App :** `landing`
- **Template File :** `search_results.html` - extends `base.html`
- **User :** Provides the user with results of their search query in two groups. Categories and Items *( Appendix 58 )*.

*Appendix 58 - Search Results Page*

![Search Results Page](/docs/features/search-results.png)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

### **4.2.11. Forms**

- **App :** `AllAuth` extension
- **Template File :** `*.html` in `./templates/account` - extends `base.html`
- **User :** Forms do interact with user. They are designed to be clear and to the point, always in center of the screen. *( Appendix 59 )*.

*Appendix 59 - Forms*

![Forms](/docs/features/forms.png)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

### **4.2.12. Admin Tools**

- **App :** `owner`
- **Template File :** `*.html` in `.owner/templates/owner` - extends `base.html`
- **User :** Displaying of Admin tools is protected from unauthorized access and also against access from devices of width less than 1200px *( Appendix 60 )*. In admin tools, the admin is able to do full CRUD on Categories *( Appendix 61 )*, Items *( Appendix 62 )*, view and download invoices of all historical orders *( Appendix 63 )*, do full CRUD in discount vouchers *( Appendix 64 )*, approve and delete user comments *( Appendix 65 )*, set amount in Postage Settings *( Appendix 66 )* and do full CRUD including sending on Newsletter emails *( Appendix 67 )*. 

*Appendix 60 - Admin Tools - Protection*

![Admin Tools - Protection](/docs/features/admin-protection.png)

*Appendix 61 - Admin Tools - Categories*

![Admin Tools - Categories](/docs/features/admin-categories.png)

*Appendix 62 - Admin Tools - Items*

![Admin Tools - Items](/docs/features/admin-items.png)

*Appendix 63 - Admin Tools - Invoices*

![Admin Tools - Invoices](/docs/features/admin-invoices.png)

*Appendix 64 - Admin Tools - Vouchers*

![Admin Tools - Vouchers](/docs/features/admin-vouchers.png)

*Appendix 65 - Admin Tools - Comments*

![Admin Tools - Comments](/docs/features/admin-comments.png)

*Appendix 66 - Admin Tools - Postage Settings*

![Admin Tools - Postage Settings](/docs/features/admin-postage.png)

*Appendix 67 - Admin Tools - Emails*

![Admin Tools - Email](/docs/features/admin-emails.png)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

### **4.2.13. User Emails**

- **App :** `checkout` and `owner`
- **Template File :** `*.html` in `./templates/emails`
- **User :** Project is equipped with styled user emails as Newsletter email and Order Confirmation email *( Appendix 68 )*. Project also generates invoice and attaches that to email confirmation sent to user after successful order *( Appendix 69 )*. Invoices are configured the way that if they are generated via webhook, they will have "WH" in the invoice heading

*Appendix 68 - Email Sample*

![Email Sample](/docs/features/email-sample.png)

*Appendix 69 - Invoice Sample*

![Invoice Sample](/docs/features/invoice-sample.png)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

## **4.3. Future Features**

This project could be significantly improved by adding more features this could include :

- Postage label printing section for owner
- Order status emails for users
- Frequently bought together section after an item is added to the Vault
- Product review after receiving the order
- Returns section for unhappy customers

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

# **5. Marketing**

## **5.1. Social Media Presence**

[Ohm-Azing Components Facebook Page](https://www.facebook.com/profile.php?id=61556654592935) was created in order to capture more online presence. The page will be used for adding posts to inform customers of newly arrived products and also competitions will be held. This will generate greater site foot-fall and generate greater income. Facebook and other social platform do provide easy, cheap and effortless way of advertisement.

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

## **5.2. Search Engine Optimization (SEO)**

Key words within the **Ohm-Azing Components** business scope were researched same as description tags. [Wordtracker](https://www.wordtracker.com/) was used to ensure that both short-tail and long-tail keywords are included. Keywords such as 'electronic components', 'electronic kits' and 'electronic tools' aim to reach most of the market search and are within the business scope. Accurate item names are present in the product names and descriptions to appear at the top of Google searches.

Files `sitemap.xml` and `robots.txt` were created to increase visibility of the site. These files are essential for SEO (Search Engine Optimization). The `sitemap.xml` file was generated using XML Sitemap and included in the root folder of the project. A robots.txt file was created in the root folder to instruct search engine crawlers on how to access and crawl the site's pages.

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

# **6. Validation, Testing & Bugs**

## **6.1. Validation**

Validation is documented separately in [validation.md](/docs/validation.md) file.

## **6.2. Testing**

Testing is documented separately in [testing.md](/docs/testing.md) file.

## **6.3. Bugs**

Bugs are documented separately in [bugs.md](/docs/bugs.md) file.

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

# **7. Deployment**

## **7.1. Transfer of progress from IDE**

- **Task :** To ensure regular commitments are done to avoid any data/progress loss.
- **Method :** 
   - commands `git add [filename]` was used to add specific file to staging area, alternatively command `git add .` was used to add all changed files to staging area
   - command `git commit -m "[commit description]"` was used to add commitments into queue
   - command `git push` was used to push all commitments to remote repository on GitHub

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

## **7.2. Offline cloning**

- **Task :** To use repository on local machine.
- **Method :** 
  - Navigate to GitHub and follow `Code -> HTTPS -> Copy button` . after those steps open your local coding environment and type `git clone [copied link]`.

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

## **7.3. Deployment Prerequisites**

### **7.3.1. Gmail**

- **Task :** Obtain GMail username and app key (password) - GMAIL SMTP to be used as mailing client.
- **Method :** 
  - Navigate to `https://accounts.google.com/` and follow all steps for registering new email address
  - Login to google with newly created email address and password.
  - Navigate to `https://accounts.google.com/` once again
  - Select `Security > Signing in to Google > 2-Step Verification > App Passwords`
  - Enter a name of the app password and select `Generate`
  - You will get app password in format `xxxx xxxx xxxx xxxx`
  - Update `settings.py` in the project directory

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

### **7.3.2. Neon Tech DB**

- **Task :** Obtain database URL to be used as project's database.
- **Method :** 
  - Select one of the DB providers, I did use [Neon Tech DB](https://neon.tech)
  - Navigate to `https://neon.tech` and follow all steps for registering new account
  - Login to Neon Tech DB Console with newly created account credentials
  - Navigate to `+ New Project`
  - Select `Name, Plan and Region`
  - Confirm the instance by pressing `Create Project`
  - Obtain database URL in format `postgresql://USERNAME:PASSWORD@ep-calm-mode-a2qojqh4.eu-central-1.aws.neon.tech/DATABASE_NAME?sslmode=require`
  - Update `settings.py` in the project directory

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

### **7.3.3. AWS Cloud Service**

- **Task :** Obtain AWS Access Key and AWS Secret Key in order to use AWS S3 bucket as static and media files cloud storage
- **Method :** 
  - Navigate to [aws.amazon.com](https://aws.amazon.com/)
  - Create an account and log in
  - Create **S3 bucket**, name it and choose the region (name should be semantic and region closest to the target audience location)
  - Allow the bucket to be **public**
  - Create the **permissions configuration**, I did use 
``` 
[
 	{
 		"AllowedHeaders": [
 			"Authorization"
 		],
 		"AllowedMethods": [
 			"GET"
 		],
 		"AllowedOrigins": [
 			"*"
 		],
 		"ExposeHeaders": []
 	}
]
```
- **Method continues :**  
  - Add the **S3 bucket policy**
```
 {
 	"Id": "Policy1234567890",
 	"Version": "2012-10-17",
 	"Statement": [
 		{
 			"Sid": "Stmt1234567890",
 			"Action": [
 				"s3:GetObject"
 			],
 			"Effect": "Allow",
 			"Resource": "arn:aws:s3:::bucket-name/*"
 			"Principal": "*",
 		}
 	]
 }
```
- **Method continues :** 
  - Start setting up IAM by creating a group (group name should be similar to project name for easy navigation)
  - In the permissions tab of the IAM group select `attach policy`
  - Import managed policy from the JSON tab (Amazon3FullAccess)
  - Copy **ARN** from your newly created bucket
```
 	{
 		"Version": "2012-10-17",
 		"Statement": [
 			{
 				"Effect": "Allow",
 				"Action": "s3:*",
 				"Resource": [
 					"arn:aws:s3:::bucket-name",
 					"arn:aws:s3:::bucket-name/*"
 				]
 			}
 		]
 	}
```
- **Method continues :** 
  - Review and attach the policy
  - Add user (yourself) to the policy
  - Download CSV file with the following details
    - `AWS_ACCESS_KEY_ID`
    - `AWS_SECRET_ACCESS_KEY`
  - Ensure that info stays private
  - Create `media` directory in the bucket
  - Add `AWS configuration` to `settings.py` (`USE_AWS` was set to `FALSE` during development, ensure this is set to `TRUE` on Heroku after final deployment)
```
# AWS Settings
if 'USE_AWS' in os.environ:
    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'ohmazing-components'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

### **7.3.4. Django AWS Connection**

- **Task :** To create connection between **Ohm-Azing Components** project and AWS cloud services
- **Method :** 
  - Install `boto` by `pip install boto`
  - Install `django storages` by `pip install django-stotages`
  - Add `storages` to installed apps in `settings.py` 
  - Set `static` and `media` directories in `settings.py`
```
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```
- **Method continues :** 
  - Create `custom_storages.py` file in root
```
# Imports
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """
    Class sets static files location
    """
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """
    Class sets media files location
    """
    location = settings.MEDIAFILES_LOCATION
```
- **Method continues :** 
  - If you had any media files created locally as I had using VS code on my local machine and those files are necessary for the project, don't forget to upload them to **S3 bucket** connected with the project

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

### **7.3.5. Stripe Configuration & Connection**

- **Task :** Obtain all relevant settings and keys for online payments on project site
- **Finding:** Stripe payment intend will only be created if the target amount is greater than 0.50 € (As I have cheaper items in my project, minimum orer and defensive programming was used) - *( Appendix 71 )* and data passed back from the webhook are always in string type.
As for customer satisfaction and complaints, I wanted to make sure that I know what orders (invoices) were created by `views.py` and which were created by `webhook_handler.py` - invoice created by webhook has "WH" in header of invoice. If order is created by webhook, the stock amount is also updated.
- **Testing :** - Dummy card details were used for testing purposes 4242 4242 4242 4242, expiry 04/24, cvc 242, zip 42424
- **Method :** 
  - Navigate to [Stripe](https://stripe.com/)
  - Create an account and login
  - Get your API keys (`STRIPE_PUBLIC_KEY` and `STRIPE_SECRET_KEY`)
  - Set those in your `env.py` for development and in Heroku vars for deployment
  - Install stripe by `pip install stripe` 
  - Create Webhook listeners
  - Add listener endpoint (URL for webhook listeners after deployment)
  - If webhooks need to be tested locally, install stripe CLI
  - Run three terminal windows where one serves as your server, second as webhook CLI and third as Stripe response server *( Appendix 70 )* 
  - Add al keys to `env.py` and to Heroku config vars

*Appendix 70 - Webhook testing*

![Webhook testing](/docs/stripe-testing.png)

*Appendix 71 - Minimum Order setting*

![Minimum Order setting](/docs/min-order.png)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

### **7.3.6. Settings.py & file-tree**

- **Task :** Prepare `settings.py` adn file-tree for deployment 
- **Method :** 
  - Create file `env.py` to keep all sensitive information in
  - See example of `env.py` file *( Appendix 72 )*
  - Add `env.py` into `.gitignore` file to ensure this fill won't be uploaded to GitHub
  - update `settings.py` with `import os`
  - for every secured variable add code `VARIABLE = os.environ.get("VARIABLE")`
  - ensure this process for Gmail, Neon Tech DB, AWS, DEBUG and Django Secret Key
  - update default database settings in `settings.py` with 
```
if "DATABASE_URL" in os.environ:
    DATABASES = {"default": dj_database_url.parse(os.environ.get("DATABASE_URL"))}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
```
- **Method continues :**
  - update default static settings in `settings.py` with 
```
# AWS Settings
if 'USE_AWS' in os.environ:
    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'ohmazing-components'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
- **Method continues :**
  - update email settings in `settings.py` with `EMAIL_HOST = "smtp.gmail.com"
```
# Gmail settings
ACCOUNT_EMAIL_SUBJECT_PREFIX = "Ohm-azning Components - "
MAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True`
```
- **Method continues :**
  - Migrate - your database models to ElephantSQL using `python manage.py migrate` command
  - Create directories `.\static` and `.\templates`
  - commit and push changes to GitHub

*Appendix 72 - `env.py` file*

![env.py](/docs/envpy.png)

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

## **7.4. Deployment to Heroku**

- **Task :** To ensure users are able to view live version of **Ohm-Azing Components** project.
- **Method :** 
  - Register & Log In with heroku
  - Navigate to `New > Create New App`
  - Select Name of the app that is unique
  - Navigate to `Settings > Reveal Config Vars`
  - Add all variables from `env.py` to ConfigVars of Heroku App *( Appendix 73)*
  - Add variable pair `PORT:8000`
  - For the testing deployment add variable pair `COLLECT_STATIC:1`
  - Add the Heroku app URL into `ALLOWED HOSTS` in `settings.py`
  - In root create file name `Procfile` *( Appendix 74 )*
  - Navigate to `Deploy > GitHub > Connect`
  - Navigate to `Deploy > Deploy Branch`
  - Optionally, you can enable automatic deploys
  - See the deployment log - if the deployment was successful, you will be prompted with option to see live page  


*Appendix 73 - Heroku Config Vars*

![Heroku Config Vars](/docs/heroku-vars.png)

*Appendix 74 - Procfile*

![Procfile](/docs/procfile.png)


[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

# **8. Technologies & Credits**

## **8.1. Technologies used to develop and deploy this project**

- [**Django/Jinja**](https://docs.djangoproject.com/en/5.0/) - main Framework of the project
- [**Python**](https://www.python.org/) - main BackEnd programming language of the project
- [**HTML**](https://developer.mozilla.org/en-US/docs/Web/HTML) - templates programming language of this project (FrontEnd)
- [**CSS**](https://developer.mozilla.org/en-US/docs/Web/CSS) - styling the project via external CSS file `./static/css/style.css`
- [**Java Script**](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - dynamic templates programming language of this project (FrontEnd)
- [**jQuery**](https://api.jquery.com/) - API for JavaScript - dynamic templates programming language of this project (FrontEnd)
- [**Bootstrap v. 5.3**](https://getbootstrap.com/) - styling framework used in this project (FrontEnd)
- [**Heroku**](https://heroku.com) - to deploy this project
- [**Balsamiq**](https://balsamiq.com/support/) - to create wire-frames
- [**Git**](https://git-scm.com/doc) - to make commitments of progress and push the results back to GitHub
- [**GitHub**](https://github.com/) - to keep the track of version control
- [**VS Code**](https://code.visualstudio.com/) - local IDE

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

## **8.2. Requirements.txt**

Following modules were used in development of **Ohm-Azing Components** website :

- `asgiref==3.7.2` - ASGI framework, a library for building asynchronous Python web applications and servers
- `bleach==6.1.0` - HTML sanitization library
- `boto3==1.34.33` - Amazon Web Services (AWS) SDK for Python
- `botocore==1.34.33` - Low-level, core functionality of boto3, providing access to AWS services
- `certifi==2023.7.22` - Python package for providing Mozilla's CA bundle
- `cffi==1.16.0` - Foreign Function Interface for Python calling C code
- `chardet==5.2.0` - Universal character encoding detector
- `charset-normalizer==3.3.2` - Library for encoding and decoding characters
- `cryptography==41.0.5` - Provides cryptographic recipes and primitives to Python developers
- `defusedxml==0.7.1` - Library for preventing various XML vulnerabilities in Python applications
- `dj-database-url==0.5.0` - Utility for parsing database connection URLs in Django
- `Django==4.2.7` - High-level Python web framework for rapid development and clean, pragmatic design
- `django-allauth==0.58.2` - Authentication for Django applications, supporting social and email accounts
- `django-ckeditor==6.7.0` - Django integration for CKEditor, a WYSIWYG text editor
- `django-countries==7.5.1` - Provides a country field for Django models
- `django-crispy-forms==1.14.0` - Helps easily build crispy forms in Django
- `django-js-asset==2.2.0` - Django JavaScript asset management
- `django-mathfilters==1.0.0` - Math filters for Django templates
- `django-resized==1.0.2` - Resize images for Django models
- `django-richtextfield==1.6.1` - Rich text field for Django models
- `django-storages==1.14.2` - Collection of custom storage backends for Django
- `django-tinymce==3.7.1` - Django integration for TinyMCE, a WYSIWYG HTML editor
- `gunicorn==21.2.0` - Python WSGI HTTP server for UNIX
- `idna==3.4` - Python package for handling Internationalized Domain Names
- `jmespath==1.0.1` - JSON Matching Expressions
- `oauthlib==3.2.2` - Generic, spec-compliant, thorough implementation of the OAuth request-signing logic
- `packaging==23.2` - Core utilities for Python packages
- `pillow==10.2.0` - Python Imaging Library (PIL), forked and maintained
- `psycopg2==2.9.9` - PostgreSQL adapter for Python
- `pycparser==2.21` - Complete parser of the C language, written in pure Python
- `PyJWT==2.8.0` - Encode and decode JSON Web Tokens (JWT) in Python
- `python-dateutil==2.8.2` - Extensions to the standard Python datetime module
- `python3-openid==3.2.0` - Python OpenID library
- `pytz==2023.3.post1` - Library for dealing with time zones
- `reportlab==4.0.9` - Library for programmatic creation of PDF documents
- `requests==2.31.0` - Python HTTP library
- `requests-oauthlib==1.3.1` - OAuth library for Python Requests
- `s3transfer==0.10.0` - Python library for managing Amazon S3 transfers
- `setuptools==69.1.0` - Library to facilitate packaging Python projects
- `six==1.16.0` - Python 2 and 3 compatibility library
- `sqlparse==0.4.4` - Non-validating SQL parser for Python
- `stripe==8.5.0` - Python client library for the Stripe API
- `typing_extensions==4.9.0` - Back-ported and experimental type hints for Python 3.5 and 3.6
- `tzdata==2023.3` - Timezone database
- `urllib3==2.0.7` - Powerful HTTP client for Python
- `webencodings==0.5.1` - Python implementation of HTML entity encoding/decoding

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---

## **8.3. Credits**

- [**Daisy McGirr**](https://www.linkedin.com/in/daisy-mcgirr/?originalSubdomain=uk) - massive shout-out for keeping me in the right direction as the best mentor I could ask for
- [**Alan Bushell**](https://www.linkedin.com/in/bushell23/) and [**Amy Richardson**](https://www.linkedin.com/in/amy-richardson-dev/)- thank you for all the support during weekly stand-ups
- [**Looka**](https://looka.com/) - used for creating logo
- [**Adobe Color Wheel**](https://color.adobe.com/create/color-wheel) - used for picking the best color schema
- [**Google Fonts**](https://fonts.google.com/) - used for picking the best typography
- [**Neon Tech**](https://neon.tech/) - used as a database storage
- [**AWS**](https://aws.amazon.com/) - used as a storage of static and media files
- [**FavIcon.io**](https://favicon.io/favicon-converter/) - used to compress favicon
- [**FreePik**](https://www.freepik.com/) - used as images database
- [**Bootstrap Icons**](https://icons.getbootstrap.com/) - used as icons database
- [**W3Schools**](https://www.w3schools.com/) - useful information and cheat sheets
- [**Markdown-Toc**](https://ecotrust-canada.github.io/markdown-toc/) - Table of contents generator

[Back to top](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/blob/main/README.md#ohm-azing-components---portfolio-project-5)

---
