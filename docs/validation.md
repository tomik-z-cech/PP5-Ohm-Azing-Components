# **5.1. Validation**

## **5.1.1. Table of Content - Validation**
- [5.1.1. Table of Content - Validation](h)
- [5.1.2. PEP8 Validation]()
- [5.1.3. HTML Validation]()
- [5.1.4. CSS Validation]()
- [5.1.5. JS Validation]()
- [5.1.6. WAVE Validation]()
- [5.1.7. Lighthouse]()

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
| \\checkout          | checkout_ok.html             | Not Applicable    | 0        | 0      |                           | PASS   |
| \\checkout          | checkout.html                | Not Applicable    | 0        | 0      |                           | PASS   |
| \\history           | order_history.html           | Only Logged in    | 0        | 0      |                           | PASS   |
| \\items             | item_detail.html             | Logged In         | 0        | 0      |   | PASS   |
|                     |                              | Not Logged In     | 0        | 0      |                           | PASS   |
| \\items             | shop.html                    | Not Applicable    | 0        | 0      |                           | PASS   |
| \\landing           | index.html                   | Not Applicable    | 0        | 0      |                           | PASS   |
| \\landing           | search_results.html          | Not Applicable    | 0        | 0      |                           | PASS   |
| \\owner             | categories.html              | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | category_delete_confirm.html | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | comment_delete_confirm.html  | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | comments_owner.html          | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | edit_category.html           | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | edit_email.html              | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | edit_item.html               | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | edit_voucher.html            | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | email_delete_confirm.html    | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | invoices.html                | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | item_delete_confirm.html     | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | items.html                   | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | new_category.html            | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | new_email.html               | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | new_item.html                | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | new_voucher.html             | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | newsletter_emails.html       | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | owner.html                   | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | postage.html                 | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | voucher_delete_confirm.html  | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\owner             | vouchers.html                | Only as SuperUser | 0        | 0      |                           | PASS   |
| \\profilemanager    | my_details.html              | Only Logged in    | 0        | 0      |                           | PASS   |
| \\vault             | vault.html                   | Not Applicable    | 0        | 0      |                           | PASS   |
| \\wishlist          | wishlist.html                | Only Logged in    | 0        | 0      |                           | PASS   |
| \\templates         | 403.html                     | Not Applicable    | 0        | 0      |                           | PASS   |
| \\templates         | 404.html                     | Not Applicable    | 0        | 0      |                           | PASS   |
| \\templates         | 500.html                     | Not Applicable    | 0        | 0      |                           | PASS   |
| \\templates         | base.html                    | Not Applicable    | 0        | 0      |                           | PASS   |
| \\templates         | footer.html                  | Not Applicable    | 0        | 0      |                           | PASS   |
| \\templates         | header.html                  | Logged In         | 0        | 0      |                           | PASS   |
| \\templates         | header.html                  | Not Logged In     | 0        | 0      |                           | PASS   |
| \\templates\\toasts | toast_error.html             | Not Applicable    | 0        | 0      |                           | PASS   |
| \\templates\\toasts | toast_info.html              | Not Applicable    | 0        | 0      |                           | PASS   |
| \\templates\\toasts | toast_success.html           | Not Applicable    | 0        | 0      |                           | PASS   |
| \\templates\\toasts | toast_vault.html             | Not Applicable    | 0        | 0      |                           | PASS   |

*Appendix 82 - W3C HTML Validator*

![W3C HTML Validator](/docs/validation/w3c-html.png)

