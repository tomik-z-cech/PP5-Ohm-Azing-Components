# **5.1. Validation**

## **5.1.1. Table of Contents - Validation**
- [**5.1.1. Table of Contents - Validation**]()
- [**5.1.2. PEP8 Validation**]()
- [**5.1.3. HTML Validation**]()
- [**5.1.4. CSS Validation**]()
- [**5.1.5. JS Validation**]()
- [**5.1.6. WAVE Validation**]()
- [**5.1.7. Lighthouse**]()

## **5.1.2. PEP8 Validation**

- **Task :** To ensure `*.py` files are compliant with PEP8 standards.
- **Tools :** 
  - [Black](https://black.readthedocs.io/en/stable/) - PY linter and formatter
  - [CI Python Linter](https://pep8ci.herokuapp.com/) - Visualizing PY linter
- **Method :** 
   - Install `Black` using `pip install black` in terminal
   - Use command `black --line-length 79 DIRECTORY_NAME/` to format `*.py` files in the selected directory or use `black --line-length 79 .` to format all files
   - See in the terminal window result of this operation *( Appendix 79 )*
   - Double check the results in `CI Python Linter` by copying and pasting the Python code as black doesn't wrap lines of comments. See result on the right hand side of the input field *( Appendix 80 )*
- **Results :**
The only file failing the PEP8 standard is `ohmazing_components/settings.py` due length of lines of module names.

| Directory            | File                 | Result                   |
| -------------------- | -------------------- | ------------------------ |
| \checkout            | `admin.py`           | PASS                     |
| \checkout            | `forms.py`           | PASS                     |
| \checkout            | `models.py`          | PASS                     |
| \checkout            | `urls.py`            | PASS                     |
| \checkout            | `views.py`           | PASS                     |
| \checkout            | `webhook_handler.py` | PASS                     |
| \checkout            | `webhooks.py`        | PASS                     |
| \history             | `urls.py`            | PASS                     |
| \history             | `views.py`           | PASS                     |
| \items               | `admin.py`           | PASS                     |
| \items               | `forms.py`           | PASS                     |
| \items               | `models.py`          | PASS                     |
| \items               | `urls.py`            | PASS                     |
| \items               | `views.py`           | PASS                     |
| \landing             | `urls.py`            | PASS                     |
| \landing             | `views.py`           | PASS                     |
| \ohmazing-components | `asgi.py`            | PASS                     |
| \ohmazing-components | `settings.py`        | FAIL *( Appendix 81 )*   |
| \ohmazing-components | `urls.py`            | PASS                     |
| \ohmazing-components | `wsgi.py`            | PASS                     |
| \owner               | `admin.py`           | PASS                     |
| \owner               | `forms.py`           | PASS                     |
| \owner               | `models.py`          | PASS                     |
| \owner               | `urls.py`            | PASS                     |
| \owner               | `views.py`           | PASS                     |
| \owner               | `widgets.py`         | PASS                     |
| \profilemanager      | `admin.py`           | PASS                     |
| \profilemanager      | `forms.py`           | PASS                     |
| \profilemanager      | `models.py`          | PASS                     |
| \profilemanager      | `urls.py`            | PASS                     |
| \profilemanager      | `views.py`           | PASS                     |
| \vault               | `context_list.py`    | PASS                     |
| \vault               | `urls.py`            | PASS                     |
| \vault               | `views.py`           | PASS                     |
| \wishlist            | `context_list.py`    | PASS                     |
| \wishlist            | `urls.py`            | PASS                     |
| \wishlist            | `views.py`           | PASS                     |
| \                    | `custom_storages.py` | PASS                     |


*Appendix 51 - Black result message*

![Black result message](/docs/validation/black-message.png)

*Appendix 52 - CI Python Linter result message*

![CI Python Linter result message](/docs/validation/ci-linter.png)

*Appendix 81 - `ohmazing_components/settings.py`*

![`ohmazing_components/settings.py`](/docs/validation/settings-pep8.png)

---

## **5.1.3. HTML Validation**

- **Task :** To ensure source code generated from all `*.html` templates is compliant with W3C standards.
- **Tools :** 
  - [W3C HTML Validator](https://validator.w3.org/) - HTML Validator
- **Method :** 
   - Open each page of the project
   - In Chrome : Right click on page background and select `View Page Source`
   - Copy and Paste the generated code from browser to validator
   - See results *( Appendix 82 )*
   - Please note this needs to be done for all states of the templates (i.e. Logged In / Logged Out, Empty Vault/Items in Vault etc.)
- **Results :**
All pages are free of any errors or warnings. 

| Directory           | File                         | State             | Warnings | Errors | Nature of Problem         | Result |
| ------------------- | ---------------------------- | ----------------- | -------- | ------ | ------------------------- | ------ |
| \\checkout          | `checkout_ok.html`             | Not Applicable    | 0        | 0      |                           | PASS   |
| \\checkout          | `checkout.html`                | Not Applicable    | 0        | 0      |                           | PASS   |
| \\history           | `order_history.html`           | Only Logged in    | 0        | 0      |                           | PASS   |
| \\items             | `item_detail.html   `          | Logged In         | 0        | 0      |   | PASS   |
|                     |                              | Not Logged In     | 0        | 0      |                           | PASS   |
| \\items             | `shop.html`                    | Not Applicable    | 0        | 0      |                           | PASS   |
| \\landing           | `index.html`                   | Not Applicable    | 0        | 0      |                           | PASS   |
| \\landing           | `search_results.html`          | Not Applicable    | 0        | 0      |                           | PASS   |
| \\owner             | `categories.html`              | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | `category_delete_confirm.html` | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | `comment_delete_confirm.html`  | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | `comments_owner.html`          | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | `edit_category.html`           | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | `edit_email.html`              | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | `edit_item.html`               | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | `edit_voucher.html`            | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | `email_delete_confirm.html`    | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | `invoices.html`                | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | `item_delete_confirm.html`     | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | `items.html`                   | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | `new_category.html`            | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | `new_email.html`               | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | `new_item.html`                | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | `new_voucher.html`             | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | `newsletter_emails.html`       | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | `owner.html`                   | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | `postage.html`                 | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | `voucher_delete_confirm.html`  | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | `vouchers.html`                | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\profilemanager    | `my_details.html`              | Only Logged in    | 0        | 0      |                           | PASS   |
| \\vault             | `vault.html`                   | Not Applicable    | 0        | 0      |                           | PASS   |
| \\wishlist          | `wishlist.html`                | Only Logged in    | 0        | 0      |                           | PASS   |
| \\templates         | `403.html`                     | Not Applicable    | 0        | 0      |                           | PASS   |
| \\templates         | `404.html`                     | Not Applicable    | 0        | 0      |                           | PASS   |
| \\templates         | `500.html`                     | Not Applicable    | 0        | 0      |                           | PASS   |
| \\templates         | `base.html`                    | Not Applicable    | 0        | 0      |                           | PASS   |
| \\templates         | `footer.html`                  | Not Applicable    | 0        | 0      |                           | PASS   |
| \\templates         | `header.html`                  | Logged In         | 0        | 0      |                           | PASS   |
| \\templates         | `header.html`                  | Not Logged In     | 0        | 0      |                           | PASS   |
| \\templates\\toasts | `toast_error.html`             | Not Applicable    | 0        | 0      |                           | PASS   |
| \\templates\\toasts | `toast_info.html`              | Not Applicable    | 0        | 0      |                           | PASS   |
| \\templates\\toasts | `toast_success.html`           | Not Applicable    | 0        | 0      |                           | PASS   |
| \\templates\\toasts | `toast_vault.html`             | Not Applicable    | 0        | 0      |                           | PASS   |

*Appendix 82 - W3C HTML Validator*

![W3C HTML Validator](/docs/validation/w3c-html.png)

---

## **5.1.4. CSS Validation**

My styling files were separated into smaller files by app names for easy navigation.

- **Task :**  To ensure the code in `*.css` is compliant with W3C standards.
- **Tools :** 
  - [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - CSS Validator
- **Method :** 
   - Open the `*.css` file
   - Copy and Paste the code from IDE to validator
   - See results
- **Results :**

| Directory     | File               | Warnings | Errors | Nature of Problem                     | Result |
| ------------- | ------------------ | -------- | ------ | ------------------------------------- | ------ |
| \\static\\css | `checkout.css`       | 33       | 0      | Dynamic - can't be checked statically | PASS   |
| \\static\\css | `error.css`          | 4        | 0      | Dynamic - can't be checked statically | PASS   |
| \\static\\css | `footer.css`         | 7        | 0      | Dynamic - can't be checked statically | PASS   |
| \\static\\css | `header.css`         | 15       | 0      | Dynamic - can't be checked statically | PASS   |
| \\static\\css | `history.css`        | 6        | 0      | Dynamic - can't be checked statically | PASS   |
| \\static\\css | `items.css`          | 44       | 0      | Dynamic - can't be checked statically | PASS   |
| \\static\\css | `landing.css`        | 21       | 0      | Dynamic - can't be checked statically | PASS   |
| \\static\\css | `main.css`           | 25       | 0      | Dynamic - can't be checked statically | PASS   |
| \\static\\css | `owner.css`          | 23       | 0      | Dynamic - can't be checked statically | PASS   |
| \\static\\css | `profilemanager.css` | 14       | 0      | Dynamic - can't be checked statically | PASS   |
| \\static\\css | `search.css`         | 13       | 0      | Dynamic - can't be checked statically | PASS   |
| \\static\\css | `wishlist_vault.css` | 11       | 0      | Dynamic - can't be checked statically | PASS   |

My `*.css` files did pass with <span style="color:green;">NO ERRORS</span> *( Appendix 83 )* and <span style="color:yellow;">216 WARNINGS</span> in total *( Appendix 84 )*.

Reasons for this result : 

- Validator isn't able to check dynamic states of elements - *Due to their dynamic nature, CSS variables are currently not statically checked*

*Appendix 83 - CSS Validation - errors example*

![CSS Validation - errors example](/docs/validation/css-error.png)

*Appendix 84 - CSS Validation - warnings example*

![CSS Validation - warnings example](/docs/validation/css-warning.png)

---

## **5.1.5. JS Validation**

- **Task :** To ensure the code in `*.js` has no errors.
- **Tools :** 
  - [JSHint](https://jshint.com/) - JS Validator
- **Method :** 
   - Open the `*.js*` files
   - Copy and Paste the code from IDE to validator
   - See results
- **Results :**
All `*.js` files passed without errors *( Appendix 85 )*.

| Directory    | File               | Result |
| ------------ | ------------------ | ------ |
| \\static\\js | `checkout.js`        | PASS   |
| \\static\\js | `easter_egg.js`      | PASS   |
| \\static\\js | `product_detail.js`  | PASS   |
| \\static\\js | `profile_picture.js` | PASS   |
| \\static\\js | `register.js`        | PASS   |
| \\static\\js | `stripe_elements.js` | PASS   |
| \\static\\js | `vault.js`           | PASS   |
| \\static\\js | `wishlist.js`        | PASS   |

*Appendix 85 - JS Validation*

![JS Validation](/docs/validation/jshint.png)

---

## **5.1.6. WAVE Validation**

- **Task :** To ensure all pages are within accessibility standards and are suitable for screen-readers.
- **Tools :** 
  - [WAVE Accessibility](https://wave.webaim.org/) - WAVE Validator
- **Method :** 
   - Install WAVE Chrome extension 
   - Browse each page and click on `WAVE Icon` *( Appendix 86 )*
   - See results on the left hand panel *( Appendix 87 )*
   - Please note this needs to be done for all states of the pages (i.e. Logged In / Logged Out, etc.)
- **Results :**
In the project, I have got no Alert's or Contrast Errors, each page got multiple warnings due to Redundant links, Table Captions and Small text generated by CKEditor.

| Directory           | File                         | State             | Alerts | Errors | Nature of Problem                           | Result |
| ------------------- | ---------------------------- | ----------------- | ------ | ------ | ------------------------------------------- | ------ |
| \\checkout          | `checkout_ok.html`             | Not Applicable    | 1      | 0      | Orphaned form                               | PASS   |
| \\checkout          | `checkout.html`                | Not Applicable    | 1      | 0      | Redundant link                              | PASS   |
| \\history           | `order_history.html`           | Only Logged in    | 4      | 0      | Table caption                               | PASS   |
| \\items             | `item_detail.html`             | Logged In         | 1      | 0      | Missing H1                                  | PASS   |
|                     |                              | Not Logged In     | 1      | 0      | Missing H1                                  | PASS   |
| \\items             | `shop.html`                    | Not Applicable    | 3      | 0      | Select label, missing H1                    | PASS   |
| \\landing           | `index.html`                   | Not Applicable    | 1      | 0      | Missing H1                                  | PASS   |
| \\landing           | `search_results.html`          | Not Applicable    | 0      | 0      |                                             | PASS   |
| \\owner             | `categories.html`              | Only as SuperUser | 0      | 0      |                                             | PASS   |
| \\owner             | `category_delete_confirm.html` | Only as SuperUser | 1      | 0      | Redundant link                              | PASS   |
| \\owner             | `comment_delete_confirm.html`  | Only as SuperUser | 1      | 0      | Redundant link                              | PASS   |
| \\owner             | `comments_owner.html`          | Only as SuperUser | 3      | 0      | Select label, table caption                 | PASS   |
| \\owner             | `edit_category.html`           | Only as SuperUser | 0      | 0      |                                             | PASS   |
| \\owner             | `edit_email.html`              | Only as SuperUser | 1      | 0      | Small text (CK Editor)                      | PASS   |
| \\owner             | `edit_item.html`               | Only as SuperUser | 0      | 0      |                                             | PASS   |
| \\owner             | `edit_voucher.html`            | Only as SuperUser | 0      | 0      |                                             | PASS   |
| \\owner             | `email_delete_confirm.html`    | Only as SuperUser | 1      | 0      | Redundant link                              | PASS   |
| \\owner             | `invoices.html`                | Only as SuperUser | 3      | 0      | Select label, table caption                 | PASS   |
| \\owner             | `item_delete_confirm.html`     | Only as SuperUser | 1      | 0      | Redundant link                              | PASS   |
| \\owner             | `items.html`                   | Only as SuperUser | 3      | 0      | Select label, table caption                 | PASS   |
| \\owner             | `new_category.html`            | Only as SuperUser | 0      | 0      |                                             | PASS   |
| \\owner             | `new_email.html`               | Only as SuperUser | 1      | 0      | Small text (CK Editor)                      | PASS   |
| \\owner             | `new_item.html`                | Only as SuperUser | 0      | 0      |                                             | PASS   |
| \\owner             | `new_voucher.html`             | Only as SuperUser | 0      | 0      |                                             | PASS   |
| \\owner             | `newsletter_emails.html`       | Only as SuperUser | 3      | 0      | Select label, table caption                 | PASS   |
| \\owner             | `owner.html`                   | Only as SuperUser | 0      | 0      |                                             | PASS   |
| \\owner             | `postage.html`                 | Only as SuperUser | 0      | 0      |                                             | PASS   |
| \\owner             | `voucher_delete_confirm.html`  | Only as SuperUser | 1      | 0      | Redundant link                              | PASS   |
| \\owner             | `vouchers.html`                | Only as SuperUser | 3      | 0      | Select label, table caption                 | PASS   |
| \\profilemanager    | `my_details.html`              | Only Logged in    | 0      | 0      |                                             | PASS   |
| \\vault             | `vault.html`                   | Not Applicable    | 1      | 0      | Redundant link                              | PASS   |
| \\wishlist          | `wishlist.html`                | Only Logged in    | 1      | 0      | Redundant link                              | PASS   |
| \\templates         | `403.html`                     | Not Applicable    | 0      | 0      |                                             | PASS   |
| \\templates         | `404.html`                     | Not Applicable    | 0      | 0      |                                             | PASS   |
| \\templates         | `500.html`                     | Not Applicable    | 0      | 0      |                                             | PASS   |
| \\templates         | `base.html`                    | Not Applicable    | 0      | 0      |                                             | PASS   |
| \\templates         | `footer.html`                  | Not Applicable    | 0      | 0      |                                             | PASS   |
| \\templates         | `header.html`                  | Logged In         | 2      | 0      | Small text (if items in vault and wishlist) | PASS   |
| \\templates         | `header.html`                  | Not Logged In     | 2      | 0      | Small text (if items in vault and wishlist) | PASS   |
| \\templates\\toasts | `toast_error.html`             | Not Applicable    | 0      | 0      |                                             | PASS   |
| \\templates\\toasts | `toast_info.html`              | Not Applicable    | 0      | 0      |                                             | PASS   |
| \\templates\\toasts | `toast_success.html`           | Not Applicable    | 0      | 0      |                                             | PASS   |
| \\templates\\toasts | `toast_vault.html`             | Not Applicable    | 0      | 0      |                                             | PASS   |


*Appendix 86 - WAVE Extension*

![WAVE Extension](/docs/validation/wave-icon.png)

*Appendix 87 - WAVE Results Example*

![WAVE Results Example](/docs/validation/wave-example.png)

---

## **5.1.7. Lighthouse**

- **Task :** To ensure that speeds of project loading are viable.
- **Tools :** 
  - [Chrome Lighthouse](https://developer.chrome.com/docs/lighthouse/overview) - Chrome Lighthouse documentation
- **Method :** 
   - Browse each page and click on `More Tools > Developer Tools > Lighthouse > Analyze Page Load` *( Appendix 88 )*
   - See results on the right hand panel *( Appendix 89 )*
- **Finding :**
  - As in previous project, suggestion was made to use `webp` image type, I decided to use `ResizedImageField` module to force all uploaded images to small resolution and `webp` format.
- **Results :**
  - Various suggestions were made between minifying the CSS, reducing unused JS files and others. 

*Appendix 88 - Lighthouse*

![Lighthouse](/docs/validation/lighthouse.png)

*Appendix 89 - Lighthouse Results Example*

![Lighthouse Results Example](/docs/validation/lighthouse-result.png)

---
