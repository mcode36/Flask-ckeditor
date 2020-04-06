## Integrate ckeditor into Flask application

This small project demonstrate how to integrate ckeditor into Flask applications.
In order to make the code self-explanable, we built a single-page Flask app that
contains only two input fields: Title and Content. 

### About the Flask app:
- The main program is app.y, which will call out templates/ck_form.html
- The template file ck_form.html contains only two fields: title and content.
- The ckeditor is enabled on the content field

### Setup:
- Install flask if it is not in your python library yet: pip install flask
- It is recommanded to run pip command under a virtual environment. For windows,
  - python -m venv venv
  - venv/scripts/activate.bat

### How it works:
- to run the demo, type "python app.y" under DOS prompt
- open browser, link to 'localhost:5000'
- Fill in some texts in both fields. play around with the texts in content field, use
 ckeditor tools to change the style of the text inside the content field
- click 'Submit'. The form data will be submitted to the same page so we can see how ckeditor
 convert the content into HTML codes.
 
### References
- CKEditor CDN page [\<link\>](http://cdn.ckeditor.com/)
- CKEditor Quick Start Guide [\<link\>](https://ckeditor.com/docs/ckeditor4/latest/guide/dev_installation.html#adding-ckeditor-to-your-page)

