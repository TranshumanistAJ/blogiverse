# Testing

> [!NOTE]
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| templates | [base.html](https://github.com/TranshumanistAJ/blogiverse/blob/main/templates/base.html) | [HTML W3C Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fblogiverse-a5563d05b65c.herokuapp.com%2F) | ![alt text](documentation/validation/base.html.png) | Clean semantic structure |
| templates | [index.html](https://github.com/TranshumanistAJ/blogiverse/blob/main/templates/index.html) | [HTML W3C Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fblogiverse-a5563d05b65c.herokuapp.com%2F) | ![screenshot](documentation/validation/index_html.png) | Bootstrap grid implemented correctly |
| templates | [post_detail.html](https://github.com/TranshumanistAJ/blogiverse/blob/main/templates/post_detail.html) | [HTML W3C Validator]() | ![screenshot](documentation/validation/post_html.png) | It works perfectly as expected |
| templates/account | [login.html](https://github.com/TranshumanistAJ/blogiverse/blob/main/templates/account/login.html) | [HTML W3C Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fblogiverse-a5563d05b65c.herokuapp.com%2Faccounts%2Flogin%2F) | ![screenshot](documentation/validation/login.PNG) | Django-allauth integration validated |
| templates/account | [signup.html](https://github.com/TranshumanistAJ/blogiverse/blob/main/templates/account/signup.html) | [HTML W3C Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fblogiverse-a5563d05b65c.herokuapp.com%2Faccounts%2Fsignup%2F) | ![screenshot](documentation/validation/signup.PNG) | Form validation markup correct |
| templates/account | [logout.html](https://github.com/TranshumanistAJ/blogiverse/blob/main/templates/account/logout.html) | [HTML W3C Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fblogiverse-a5563d05b65c.herokuapp.com%2Faccounts%2Flogout%2F) | ![screenshot](documentation/validation/logout.PNG) | Simple logout confirmation |
| templates/blogs | [create_post.html](https://github.com/TranshumanistAJ/blogiverse/blob/main/templates/blogs/create_post.html) | No link provided | ![screenshot](documentation/validation/create_post.PNG) | It works perfectly as expected |
| templates/blogs | [edit_post.html](https://github.com/TranshumanistAJ/blogiverse/blob/main/templates/blogs/edit_post.html) | No link provided | ![screenshot](documentation/validation/edit_post.PNG) | No W3C link provided. Could not check by URI due to page requiring authentication |
| templates/blogs | [delete_post.html](https://github.com/TranshumanistAJ/blogiverse/blob/main/templates/blogs/delete_post.html) | No link provided | ![screenshot](documentation/validation/delete_post.PNG) | No W3C link provided. Could not check by URI due to page requiring authentication |
| templates/blogs | [topic_list.html](https://github.com/TranshumanistAJ/blogiverse/blob/main/templates/blogs/topic_list.html) | [HTML W3C Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fblogiverse-a5563d05b65c.herokuapp.com%2FPersonal%2520Growth%2F) | ![screenshot](documentation/validation/topic_list.PNG) | Dynamic content rendering validated |
| templates/blogs | [blog_detail.html](https://github.com/TranshumanistAJ/blogiverse/blob/main/templates/blogs/blog_detail.html) | No link provided | ![screenshot](documentation/validation/blog_detail.PNG) | No W3C link provided as requires specific post ID |
| templates/blogs | [create_forum.html](https://github.com/TranshumanistAJ/blogiverse/blob/main/templates/blogs/create_forum.html) | No link provided | ![screenshot](documentation/validation/create_forum.PNG) | No W3C link provided. Could not check by URI due to page requiring authentication |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| static/css | [style.css](https://github.com/TranshumanistAJ/blogiverse/blob/main/static/css/style.css) | [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fblogiverse-a5563d05b65c.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) | ![screenshot](documentation/validation/css_validation.PNG) | Modern CSS3 properties used correctly |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| blog_platform | [settings.py](https://github.com/TranshumanistAJ/blogiverse/blob/main/blog_platform/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TranshumanistAJ/blogiverse/main/blog_platform/settings.py) | ![screenshot](documentation/validation/settings.PNG) | Django best practices followed |
| blog_platform | [urls.py](https://github.com/TranshumanistAJ/blogiverse/blob/main/blog_platform/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TranshumanistAJ/blogiverse/main/blog_platform/urls.py) | ![screenshot](documentation/validation/urls.PNG) | URL patterns properly structured |
| blog_platform | [wsgi.py](https://github.com/TranshumanistAJ/blogiverse/blob/main/blog_platform/wsgi.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TranshumanistAJ/blogiverse/main/blog_platform/wsgi.py) | ![screenshot](documentation/validation/wsgi.PNG) | Standard Django WSGI config |
| blogs | [models.py](https://github.com/TranshumanistAJ/blogiverse/blob/main/blogs/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TranshumanistAJ/blogiverse/main/blogs/models.py) | ![screenshot](documentation/validation/models.PNG) | Proper model relationships |
| blogs | [views.py](https://github.com/TranshumanistAJ/blogiverse/blob/main/blogs/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TranshumanistAJ/blogiverse/main/blogs/views.py) | ![screenshot](documentation/validation/views.PNG) | Function-based views with decorators |
| blogs | [forms.py](https://github.com/TranshumanistAJ/blogiverse/blob/main/blogs/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TranshumanistAJ/blogiverse/main/blogs/forms.py) | ![screenshot](documentation/validation/forms.PNG) | ModelForm implementations |
| blogs | [admin.py](https://github.com/TranshumanistAJ/blogiverse/blob/main/blogs/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TranshumanistAJ/blogiverse/main/blogs/admin.py) | ![screenshot](documentation/validation/admin.PNG) | Admin interface registrations |
| blogs | [apps.py](https://github.com/TranshumanistAJ/blogiverse/blob/main/blogs/apps.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TranshumanistAJ/blogiverse/main/blogs/apps.py) | ![screenshot](documentation/validation/app.PNG) | Standard app configuration |
| / | [manage.py](https://github.com/TranshumanistAJ/blogiverse/blob/main/manage.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TranshumanistAJ/blogiverse/main/manage.py) | ![screenshot](documentation/validation/manage.PNG) | Django management script |

## Responsiveness

I've tested my deployed project to check for responsiveness issues.

![screenshot](documentation/user-stories/responsiveness_for_all_devices.PNG)

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Page           | Chrome Screenshot                                                   | Firefox Screenshot                                                    | Edge Screenshot                                                       | Notes                                      |
|----------------|----------------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------|---------------------------------------------|
| Home           | ![Chrome Home](documentation/validation/chrome_browser.PNG)         | ![Firefox Home](documentation/validation/firefox_broswer.PNG)         | ![Edge Home](documentation/validation/edge_browser.PNG)               | Displays correctly on all major browsers     |
| Forum Pages    | ![Chrome Forum](documentation/validation/chrome_forumdetails.PNG)   | ![Firefox Forum](documentation/validation/firefox_forumdetails.PNG)   | ![Edge Forum](documentation/validation/edge_forumdetails.PNG)         | Layout is clean and consistent across browsers |
| Post Creation  | ![Chrome Create](documentation/validation/chrome_createpost.PNG)    | ![Firefox Create](documentation/validation/firefox_createpost.PNG)    | ![Edge Create](documentation/validation/edge_createpost.PNG)          | Form functions properly and looks good        |
| Authentication | ![Chrome Login](documentation/validation/chrome_login.PNG)          | ![Firefox Login](documentation/validation/firefox_login.PNG)          | ![Edge Login](documentation/validation/edge_login.PNG)                | Seamless login experience across platforms    |

## User Story Testing

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a new user | I would like to easily understand what the site is about | so that I can decide if I want to register and participate. | ![screenshot](documentation/validation/chrome_browser.PNG) |
| As a new user | I would like to browse content without registering | so that I can explore before committing to create an account. | ![screenshot](documentation/user-stories/guest_user_experience.PNG) |
| As a new user | I would like to easily sign up for an account | so that I can start creating and engaging with content. | ![screenshot](documentation/user-stories/new_user_signup.PNG) |
| As a user | I would like to create blog posts with rich text and images | so that I can share my stories in an engaging format. | ![screenshot](documentation/validation/chrome_createpost.PNG) |
| As a user | I would like to categorize my posts into different forums | so that readers can find content that interests them. | ![screenshot](documentation/user-stories/different_forum.PNG) |
| As a user | I would like to like posts I enjoy | so that I can show appreciation to other authors. | ![screenshot](documentation/user-stories/like_post.PNG) |
| As a user | I would like to comment on posts | so that I can engage in discussions with other community members. | ![screenshot](documentation/user-stories/user_comment.png) |
| As a reader | I would like to browse posts by forum category | so that I can find stories that match my interests. | ![screenshot](documentation/validation/chrome_browser.PNG) |
| As a reader | I would like to view full post details including comments | so that I can read complete stories and community discussions. | ![screenshot](documentation/validation/chrome_forumdetails.PNG) |
| As a content creator | I would like to respond to comments on my posts | so that I can engage with my readers. | ![screenshot](documentation/user-stories/who_commented.png) |
| As a user | I would like to edit my own blog posts | so that I can update or correct any information after publishing. | ![screenshot](documentation/user-stories/edit__post.PNG) |
| As a user | I would like to delete my own blog posts | so that I can remove content I no longer wish to share. | ![screenshot](documentation/user-stories/delete__post.PNG) |
| As a site visitor | I would like the site to work well on my mobile device | so that I can use it anywhere. | ![screenshot](documentation/user-stories/phone_version.jpeg) |

## Automated Testing

I have conducted a series of automated tests on my application.

> [!NOTE]
> I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

I have used Django's built-in unit testing framework to test the application functionality. In order to run the tests, I ran the following command in the terminal each time:

- `python manage.py test blogs`

To create the coverage report, I would then run the following commands:

- `pip install coverage`
- `pip freeze --local > requirements.txt`
- `coverage run --source='.' --omit=*/site-packages/*,*/migrations/*,*/__init__.py,env.py,manage.py manage.py test`
- `coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

- `coverage html`
- `python -m http.server`

#### Unit Test Issues

No significant issues encountered during unit testing. All tests pass successfully.

## Defensive Programming

Proper CRUD (Create, Read, Update, Delete) functionality has been implemented to ensure that only the authorized blog post author can edit or delete their posts. This is enforced through Django's authentication and permission system, which restricts access to the edit and delete views for unauthorized users. If a user attempts to access these pages by brute-forcing the URL, they are met with an access denied error.

| Scenario | Screenshot | Notes |
| --- | --- | --- |
| Unauthorized Edit Attempt | ![Access Denied Edit](documentation/validation/editdenied.png) | Displays access denied message when a user tries to edit a post they do not own. |
| Unauthorized Delete Attempt | ![Access Denied Delete](documentation/validation/deletedenied.png) | Displays access denied message when a user tries to delete a post they do not own. |

## Bugs

### Unfixed Bugs

Currently, there are no known unfixed bugs.

### Known Issues

> [!IMPORTANT]
> There are no remaining bugs that I am aware of. However, even after thorough testing, I cannot rule out the possibility of undiscovered issues.