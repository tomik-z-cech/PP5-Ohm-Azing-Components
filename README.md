# ***Ohm-Azing Components - Portfolio Project 5***
---
# **1. Key project information**

- **Description :** This Portfolio Project 5 website called **Ohm-Azing Components** is a site of imaginary online shop that sells electronic components, electronic kits, tools, books, etc. User can easily browse through the shop items, **add/delete** items from their **Wishlist**, express their opinion by **commenting** and **liking/disliking** shop items and most importantly order their selected items for home delivery including online payment.
- **Key project goal :** To offer all visitors of **Ohm-Azing Components** site the option to buy their chosen products, select delivery option and finish payment online without the need of leaving the house.
- **Audience :** There's no age or any other limit to audience of this page. Target audience are individuals at any level of experience that have interest in electronic components and electronic kits.
- **Live version :** Live version of **Ohm-Azing Components** e-shop page can be viewed at [https://ohmazing-components-1a5a0fcb9e95.herokuapp.com/](https://ohmazing-components-1a5a0fcb9e95.herokuapp.com/).
- **Developer :** [Tomas Kubancik](https://github.com/tomik-z-cech/)

![Mockup](/docs/mockup.png)



# **3. User Experience (UX)**

## **3.1. The Strategy Plane**

### **3.1.1 The Idea**
- The intention of **Ohm-Azing Components** site is to be friendly online shop where users can browse variate of products sorted between categories. Besides that, user can read details of each product, see product comments and also see opinion of other users in form of **likes/dislikes**.

### **3.1.2 The Ideal User**

The target audience are individuals or groups such as rookies that are seeking inspiration in electronic components to build their own circuit or electronic kits that are programmable and versatile or electronic veterans that need tools or to top up their components stash. 

- Ideal user likes electronics
- Ideal user creates electronic projects
- Ideal user likes to shop online
- Ideal user likes to explore new trends and ideas in the electronics field
- Ideal user likes to share their opinion in form if **likes/dislikes** and **comments**

### **3.1.3 Site Goals**

- Offer users ability of shopping online without leaving their home
- Offer users ability of reading other people comments on products
- Offer users ability to add items to their **Wishlist** if they want to save the item for later
- Offer users the ability to see details of each item in shop (ie. stock, price, description, etc. ) 
- Offer users inspiration in electronics field

### **3.1.4 Epics**

As a thought process of the strategy plane, 14 epics were created and utilized. Please see below the detail list of epics with links, or a link to the project's [Kanban Board](https://github.com/users/tomik-z-cech/projects/4/views/1) *(appendix 1)*. Those Epics were further sliced into 69 USER STORIES.

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
| [# 7](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/7) | USER STORY : Define Database Schema              | As a Developer, I need to create databse schema that fits the purpose of the project and also create all the modular apps that will be used in the project. |
| [# 8](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/8) | USER STORY : Create database realtionships       | As a Developer, I need to define relatinships between models and import the relationships into working apps models.                                         |
| [# 9](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/9) | USER STORY : Implement Data Validation in Models | As a Developer, I need implement data validation rules within Ohm-Azing Components database models.                                                         |
</details>


<details>
<summary>
View User Stories for EPIC 3 : User Authentication and Authorisation
</summary>

| Issue                                                                      | Title                                       | User Story                                                                                       |
| -------------------------------------------------------------------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| [# 11](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/11) | USER STORY : Implement user registration    | As a Site User I am able to register to create new account and to select username and passsword. |
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
| [# 20](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/20) | USER STORY : Comments section                       | As a Business Owner, I have option to approve/delete comments to ensure no inapproproate content on the project page.                  |
| [# 21](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/21) | USER STORY : Postage Settings section               | As a Business Owner, I have option to adjust free postage treshold and posatege fees for standad and express delivery options.         |
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
| [# 23](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/23) | USER STORY : FavIcon & Title | As a Site User I woul like to be able to differenciate this site from other sites opened in my browser, in order of easy navigation.                            |
| [# 24](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/24) | USER STORY : Header          | As a Site User I want to be able to navigate easily through-out the site.                                                                                       |
| [# 25](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/25) | USER STORY : Footer          | As a Site User I want to be able to find useful info on the bottom of the site in order not to scroll and search too much around.                               |
| [# 26](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/26) | USER STORY : Loader          | As a Site User I want to be able to see if page is working in the form of loader that appears when complex task is performed.                                   |
| [# 27](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/27) | USER STORY : Toasts          | As a Site User I want to be informed of results of requests performed in the form of toast that appears when complex task is done sucessfully / unsuccessfully. |
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
| [# 34](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/34) | USER STORY : Opt In/Out for Newsletter                          | As a Site User I can Opt In/Out for Newsletter or other marketing communtiation to be able to change my preferences. |
</details>


<details>
<summary>
View User Stories for EPIC 7 : The Shop
</summary>

| Issue                                                                      | Title                                     | User Story                                                                                                                                                    |
| -------------------------------------------------------------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [# 36](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/36) | USER STORY : Shop Highlights              | As a Site User, I would like to See Newest and Favourites on the landing page so I can see easily what products are after arriving and what are most popular. |
| [# 37](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/37) | USER STORY : Shop by Category             | As a Site User, I would like to have the shop items sorted by category so I can browse the items faster.                                                      |
| [# 38](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/38) | USER STORY : Product Details              | As a Site User, I would like to see the details of each item in separate page so I won't get lost in too much info.                                           |
| [# 39](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/39) | USER STORY : Add to Vault                 | As a Site User, I need to be able to add items to vault in order to see the entire order before payment.                                                      |
| [# 40](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/40) | USER STORY : Add to Wishlist              | As a Site User, I need to be able to add items to my Wishlist in order to see keep the items I am interested in separately.                                   |
| [# 41](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/41) | USER STORY : Comment on Products          | As a Site User I can Comment on Items to share my opinion.                                                                                                    |
| [# 42](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/42) | USER STORY : See Comments of Others       | As a Site User I can see other comments on Items to read other Users opinions.                                                                                |
| [# 72](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/72) | USER STORY : Like / Dislike Items of Shop | As a Site User I can Like / Dislike particular Item in Shopin order to express my opinion.                                                                    |
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
| [# 55](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/55) | USER STORY : Vouchers                  | As a Site User, I have an option to redeem dicount codes in order to get discount on my purchase.                                                       |
| [# 58](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/58) | USER STORY : Invoice Generator         | As a Site Admin, I need to be able to generate invoice in \*.pdf format in order the invoice being attached to the confirmation email.                  |
| [# 59](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/59) | USER STORY : Confirmation Email        | As a Site User, I do get confirmation email in order to know the transaction was sucessfull.                                                            |
| [# 60](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/60) | USER STORY : Stock Update              | As a Site Admin, I need to be able to update stock amounts after every purchase in order the manage the inventory.                                      |
| [# 56](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/56) | USER STORY : Stripe and Webhooks Setup | As a Site Admin, I need to be able to process the order functions even in event of failure in order to ensure no paying customer is left without goods. |
| [# 64](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/64) | USER STORY : Success Page              | As a Site User, I can clarly see sucess page in order to know my order went through without checking my emails.                                         |
</details>


<details>
<summary>
View User Stories for EPIC 11 : Order History
</summary>

| Issue                                                                      | Title                                 | User Story                                                                                          |
| -------------------------------------------------------------------------- | ------------------------------------- | --------------------------------------------------------------------------------------------------- |
| [# 66](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/66) | USER STORY : Accessing Order History  | As a Site User, I can access my own past orders in case of needing them in future.                  |
| [# 67](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/67) | USER STORY : Viewing past invoices    | As a Site User, I can view detail of any of my own past orders in case of needing them in future.   |
| [# 68](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/68) | USER STORY : Downloding past invoices | As a Site User, I can download any of my own past order invoices in case of needing them in future. |
</details>


<details>
<summary>
View User Stories for EPIC 12 : Search Bar
</summary>

| Issue                                                                      | Title                                     | User Story                                                                                                                                     |
| -------------------------------------------------------------------------- | ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| [# 70](https://github.com/tomik-z-cech/PP5-Ohm-Azing-Components/issues/70) | USER STORY : Search Bar in header of page | As a Site User I am able to use search function through Categories, Items and Item descriptionsin order to quickly find what am I looking for. |
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

---

## **3.2. The Scope Plane**

After decided on the strategy, the scope plane was carefully created.

### 3.2.1. Features to be implemented

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

---

## **3.3. The Structure Plane**

### 3.3.1. Site Maps

The following site-maps show how the site is structured to **Logged in user** *( appendix 2 )* ,**Not logged in user** *( appendix 3 )* and **Site Admin** *( appendix 3 )*.

*Appendix 2 - Site Map - Logged In*

![Site Map - Logged In](/docs/sitemap-logedin.png)

*Appendix 3 - Site Map - Not Logged In*

![Site Map - Not Logged In](/docs/sitemap-logedout.png)

*Appendix 4 - Site Map - Site Admin*

![Site Map - Not Logged In](/docs/sitemap-admin.png)

### 3.3.2. Database Schemas

Following schemas show intended database structure *( appendix 5 )* and the actual database structure generated by DBeaver *( appendix 6 )*.

*Appendix 5 - Initial DB schema*

![Initial DB Schema](/docs/db-dchema.png)

*Appendix 6 - DBeaver DB schema and relationships*

![DBeaver DB Schema](/docs/dbeaver-schema.png)

### 3.4.1. Wire-frames

- **Header and Footer** : Header and footer is established on every single page. **Header** is displayed on top of each page, **Footer** is displayed at the very bottom of each page so it doesn't cover any content *( appendix 7 )*.

*Appendix 7 - Header and Footer Wire-frame*

![Header and Footer Wire-frame](/docs/wireframes/header-footer-wireframe.png)

- **Landing page** : Provides user with clear understanding of what the page is about. User is also provided with 3 newest arrivals (3 newly added items to the database), 3 favorite items (3 items with the highest likes/dislikes rating ) and option for the user to sign up for **Ohm-Azing Components** newsletter *( appendix 8 )*.

*Appendix 8 - Landing Page Wire-frame*

![Landing Page Wire-frame](/docs/wireframes/landing-wireframe.png)

- **Shop page** : Provides user with selection of all available categories and all items that belong to the category. User clearly sees item name, price, amount of comments, rating of item and stock level *( appendix 9 )*..

*Appendix 9 - Shop Page Wire-frame*

![Shop Page Wire-frame](/docs/wireframes/shop-wireframe.png)

- **Item Detail page** : Provides user with all relevant product info including name, description, etc. User can select quantity to add to **Vault**, user can also select between different item sizes and values (only where applicable). User can add item to **Wishlist** - *( appendix 10 )*.

*Appendix 10 - Item Detail Page Wire-frame*

![Item Detail Page Wire-frame](/docs/wireframes/item-detail.png)

- **Wishlist page** : This is where user can store their **Wishlist** items, in case the user wan't to buy the item later or just holding it to see trends first. This function is only available to logged in users. *( appendix 11 )*.

*Appendix 11 - Wishlist Page Wire-frame*

![Wishlist Page Wire-frame](/docs/wireframes/wishlist-wireframe.png)

- **Vault Page** : This page serves as last check before **Checkout**. Users can adjust quantity of item added to **Vault** previously or remove the item from **Vault** or clear **Vault** entirely *( appendix 12 )*.

*Appendix 12 - Vault Page Wire-frame*

![Vault Page Wire-frame](/docs/wireframes/vault-wireframe.png)

- **Checkout Page** : Users are prompted to fill in delivery details (details are pre-filled if user logged in and details are saved). Users can select between delivery options, users can redeem vouchers and also fill pay for their items using credit card details field *( appendix 13 )*.

*Appendix 13 - Checkout Page Wire-frame*

![Checkout Page Wire-frame](/docs/wireframes/checkout-wireframe.png)

- **Checkout Successful Page** : This page is presented to users after successful process of payment. This page indicates order number, expected delivery dates based on user selection and review of items that user paid for *( appendix 14 )*.

*Appendix 14 - Checkout Successful Page Wire-frame*

![Checkout Successful Page Wire-frame](/docs/wireframes/checkout-ok.png)

- **My Profile Page** : Gives user the ability to change their details and preferences. The form is pre-populated with existing details. It also gives the user ability to delete their account entirely. *( appendix 15 )*.

*Appendix 15 - My Profile Page*

![My Profile Page Wire-frame](/docs/wireframes/profile-wireframe.png)

- **Order History Page** : This page gives users the ability to browse history of their orders with functions of viewing and downloading the invoices of the orders. *( appendix 16 )*.

*Appendix 16 - Order History Page*

![Order History Page Wire-frame](/docs/wireframes/history-wireframe.png)

- **Search Results Page** : Provides the user with results of their search query in two groups, categories and shop items. Users have the option to search again from the same page or any page they visit. *( Appendix 17 )*.

*Appendix 17 - Search Results Page*

![Search Results Page Wire-frame](/docs/wireframes/search-results-wireframe.png)

- **Forms** : Forms do interact with user. They are designed to be clear and to the point, always in center of the screen. *( Appendix 18 )*.

*Appendix 18 - Forms*

![Forms Wire-frame](/docs/wireframes/forms-wireframe.png)

- **Admin Tools Page** : Admin tools page is designed only for SuperUsers. This page allows the admin to manage functionality of the whole site with varios settings and options. Admin Tools are accessible from devices with width of screen greater than 1200px.  *( Appendix 19 )*.

*Appendix 19 - Admin Tools Page*

![Admin Tools Page Wire-frame](/docs/wireframes/admin-wireframe.png)

## **3.5. The Surface Plane**

Once the Strategy, Scope, Structure and Skeleton Planes were in place, it was time to work on the Surface Plane (Design).

### 3.5.1. Logo

To create the logo, site called [Looka](https://looka.com/) was used. Few ideas were presented to the site owner and one of the logos was picked *( appendix 20 )*

*Appendix 20 - Logo*

![Logo](/docs/email_logo.png)

### 3.5.2. Color pallette

Based on the colors of the logo, rest of the colors were picked using the [Adobe Color Wheel](https://color.adobe.com/create/color-wheel), following colors were picked into the color pallette *( appendix 21 )*. As some of the colors needed to be opaque, following CSS variables were established *( appendix 22 )*.

*Appendix 21 - Color pallette*

![Color pallette](/docs/color-pallette.png)

*Appendix 22 - Color variables*

![Color variables](/docs/color-vars.png)

### 3.5.3. Fonts

[Google Fonts](https://fonts.google.com/) site was used to pick the best typography style. The most importance was given to balance between style and readability. As a developer I needed to ensure that all text is displayed clear.

One font was picked and saved in CSS vars *( Appendix 24)* :
 - Electrolize (Sans Serif fallback) -  *( Appendix 23 )*

*Appendix 23 - Electrolize Font*

![Electrloze Font](/docs/electrolize-font.png)

*Appendix 24 - Font Variable*

![Font Variable](/docs/font-vars.png)

### 3.5.4. Icons and pictures

Icons used throughour the projects are [Bootstrap Icons](https://icons.getbootstrap.com/). All of the icons are free to use under their T&C license. Icons were user for various parts of the project such as the Menu, Footer and Buttons as they do enhance user experience.

Site called [Freepik](https://www.freepik.com/) was used to download images used in this project. The site offers massive amounts of imagery that is free to download and use under their T&C license. Images from [Freepik](https://www.freepik.com/) were used as product images and background image.

---

# **4. Features**

## **4.1. Features used in every HTML template**

### **4.1.1 Header**
- Header contains a Logo section *( appendix 27 )*, which is also used as a link to Home page `{% url 'home' %}`. Center of the header is used for Search Bar and in the left top corner is located the **Menu** section along with **Vault** and **Wishlist** *( appendix 26 )* for easy navigation through all the pages.The header changes to different layout *( appendix 27 )* when the resolution changes to less than 1200 pixels in width.
- Header is designed to cover full width `width: 100%` of the browsing window.
- This will allow user to navigate through the pages and to navigate back to home page when click on logo.
- Header extends `base.html` in block `{% include 'header.html' %}`

*Appendix 25 - Logo*

![Logo](/docs/features/logo.png)

*Appendix 26 - Header on HD devices*

![Header on HD devices](/docs/features/big-header.png)

*Appendix 27 - Header on devices less 1200px in width*

![Header on devices less 1200px](/docs/features/small-header.png)

### **4.1.2. Footer**

- Footer  *( appendix 28 )* is designed to reveal basic contact details of **Ohm-Azing Components** on the left hand side, phone number and email address are constructed to be clickable links that are very useful especially for mobile phone users. Center of footer is designed to bring the user to Facebook via link that opens in new browser tab and it has links to Terms & Conditions and Privacy Policy Modals.
Right hand site of the footer is devoted to accepted cards logos and Stripe link.
- Footer is designed to cover full width `width: 100%` of the browsing window.
- This will allow user to open phone app (dial the number directly), send e-mail (open e-mail application on phone/tablet) and open Facebook link in new window.
- Footer changes the appearance on devices with width lesser than 1200px *( appendix 29 )*.
- Footer extends `base.html` in block `{% include 'footer.html' %}`

*Appendix 28 - Footer on HD devices*

![Footer on HD devices](/docs/features/big-footer.png)

*Appendix 29 - Footer on devices less 1200px in width*

![Footer on devices less 1200px in width](/docs/features/small-footer.png)

### **4.1.3. Favicon**

- Every template in this project is equipped with Favicon. This is to ease navigation for user in case of more tabs opened. The logo was selected as Favicon *( appendix 30)*. 

*Appendix 30 - Favicon*

![Favicon](/docs/features/favicon.png)

### **4.1.4. Error Pages**

- This project is designed to have custom error pages. In case of user clicks on broken link, submits action that isn't supported or tries to reach certain view without permission, then user isn't completely "cut off" from browsing, instead an error page with header and footer appears and user is informed of the situation.

- The following custom error pages were created :
- - 403 - Received when user attempts to access a web resource for which they lack the necessary permissions. *( appendix 31 )*
- - 404 - Encountered when the requested web resource by user is not found on the server. *( appendix 32 )*
- - 500 - Displayed when the web server encounters an internal error while processing the request. *( appendix 33 )*

*Appendix 31 - 403.html*

![403.html](/docs/features/403html.png)

*Appendix 32 - 404.html*

![404.html](/docs/features/404html.png)

*Appendix 33 - 500.html*

![500.html](/docs/features/500html.png)

### **4.1.5. Scroll bar**
- Custom scroll bar was used to fit within the color theme within the project *( appendix 34 )*.

*Appendix 34 - Scroll bar*

![Scrollbar](/docs/features/scrollbar.png)

### **4.1.6. Loader**
- Custom loader was used to fit within the color theme within the project to indicate to users that the page is working even if it might take a bit of time *( appendix 35 )*.

*Appendix 35 - Loader*

![Loader](/docs/features/loader.gif)