# Testing

> [!NOTE]
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| templates | [base.html](https://github.com/TranshumanistAJ/blogiverse/blob/main/templates/base.html) | [HTML W3C Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fblogiverse-a5563d05b65c.herokuapp.com%2F) | ![alt text](image.png)) | Clean semantic structure |
| templates | [index.html](https://github.com/TranshumanistAJ/blogiverse/blob/main/templates/index.html) | [HTML W3C Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fblogiverse-a5563d05b65c.herokuapp.com%2F) | ![screenshot](documentation/validation/index_html.png) | Bootstrap grid implemented correctly |
| templates | [post_detail.html](https://github.com/TranshumanistAJ/blogiverse/blob/main/templates/post_detail.html) | No link provided | ![screenshot](documentation/validation/post_html.png) | No W3C link provided as requires specific post ID |
| templates/account | [login.html](https://github.com/TranshumanistAJ/blogiverse/blob/main/templates/account/login.html) | [HTML W3C Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fblogiverse-a5563d05b65c.herokuapp.com%2Faccounts%2Flogin%2F) | ![screenshot](documentation/validation/login.PNG) | Django-allauth integration validated |
| templates/account | [signup.html](https://github.com/TranshumanistAJ/blogiverse/blob/main/templates/account/signup.html) | [HTML W3C Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fblogiverse-a5563d05b65c.herokuapp.com%2Faccounts%2Fsignup%2F) | ![screenshot](documentation/validation/signup.PNG) | Form validation markup correct |
| templates/account | [logout.html](https://github.com/TranshumanistAJ/blogiverse/blob/main/templates/account/logout.html) | [HTML W3C Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fblogiverse-a5563d05b65c.herokuapp.com%2Faccounts%2Flogout%2F) | ![screenshot](documentation/validation/logout.PNG) | Simple logout confirmation |
| templates/blogs | [create_post.html](https://github.com/TranshumanistAJ/blogiverse/blob/main/templates/blogs/create_post.html) | No link provided | ![screenshot](documentation/validation/create_post.PNG) | No W3C link provided. Could not check by URI due to page requiring authentication |
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
| blog_platform | [settings.py](https://github.com/TranshumanistAJ/blogiverse/blob/main/blog_platform/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TranshumanistAJ/blogiverse/main/blog_platform/settings.py) | ![screenshot](docs/validation/py-settings.png) | Django best practices followed |
| blog_platform | [urls.py](https://github.com/TranshumanistAJ/blogiverse/blob/main/blog_platform/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TranshumanistAJ/blogiverse/main/blog_platform/urls.py) | ![screenshot](docs/validation/py-main-urls.png) | URL patterns properly structured |
| blog_platform | [wsgi.py](https://github.com/TranshumanistAJ/blogiverse/blob/main/blog_platform/wsgi.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TranshumanistAJ/blogiverse/main/blog_platform/wsgi.py) | ![screenshot](docs/validation/py-wsgi.png) | Standard Django WSGI config |
| blogs | [models.py](https://github.com/TranshumanistAJ/blogiverse/blob/main/blogs/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TranshumanistAJ/blogiverse/main/blogs/models.py) | ![screenshot](docs/validation/py-models.png) | Proper model relationships |
| blogs | [views.py](https://github.com/TranshumanistAJ/blogiverse/blob/main/blogs/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TranshumanistAJ/blogiverse/main/blogs/views.py) | ![screenshot](docs/validation/py-views.png) | Function-based views with decorators |
| blogs | [forms.py](https://github.com/TranshumanistAJ/blogiverse/blob/main/blogs/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TranshumanistAJ/blogiverse/main/blogs/forms.py) | ![screenshot](docs/validation/py-forms.png) | ModelForm implementations |
| blogs | [admin.py](https://github.com/TranshumanistAJ/blogiverse/blob/main/blogs/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TranshumanistAJ/blogiverse/main/blogs/admin.py) | ![screenshot](docs/validation/py-admin.png) | Admin interface registrations |
| blogs | [apps.py](https://github.com/TranshumanistAJ/blogiverse/blob/main/blogs/apps.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TranshumanistAJ/blogiverse/main/blogs/apps.py) | ![screenshot](docs/validation/py-apps.png) | Standard app configuration |
| / | [manage.py](https://github.com/TranshumanistAJ/blogiverse/blob/main/manage.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/TranshumanistAJ/blogiverse/main/manage.py) | ![screenshot](docs/validation/py-manage.png) | Django management script |

## Responsiveness

I've tested my deployed project to check for responsiveness issues.

| Page | Mobile | Tablet | Desktop | Notes |
| --- | --- | --- | --- | --- |
| Home | ![screenshot](docs/responsiveness/mobile-home.png) | ![screenshot](docs/responsiveness/tablet-home.png) | ![screenshot](docs/responsiveness/desktop-home.png) | Works as expected |
| Forum List | ![screenshot](docs/responsiveness/mobile-forum-list.png) | ![screenshot](docs/responsiveness/tablet-forum-list.png) | ![screenshot](docs/responsiveness/desktop-forum-list.png) | Works as expected |
| Post Detail | ![screenshot](docs/responsiveness/mobile-post-detail.png) | ![screenshot](docs/responsiveness/tablet-post-detail.png) | ![screenshot](docs/responsiveness/desktop-post-detail.png) | Works as expected |
| Create Post | ![screenshot](docs/responsiveness/mobile-create-post.png) | ![screenshot](docs/responsiveness/tablet-create-post.png) | ![screenshot](docs/responsiveness/desktop-create-post.png) | Works as expected |
| Edit Post | ![screenshot](docs/responsiveness/mobile-edit-post.png) | ![screenshot](docs/responsiveness/tablet-edit-post.png) | ![screenshot](docs/responsiveness/desktop-edit-post.png) | Works as expected |
| Login | ![screenshot](docs/responsiveness/mobile-login.png) | ![screenshot](docs/responsiveness/tablet-login.png) | ![screenshot](docs/responsiveness/desktop-login.png) | Works as expected |
| Signup | ![screenshot](docs/responsiveness/mobile-signup.png) | ![screenshot](docs/responsiveness/tablet-signup.png) | ![screenshot](docs/responsiveness/desktop-signup.png) | Works as expected |
| Logout | ![screenshot](docs/responsiveness/mobile-logout.png) | ![screenshot](docs/responsiveness/tablet-logout.png) | ![screenshot](docs/responsiveness/desktop-logout.png) | Works as expected |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Page | Chrome | Firefox | Safari | Edge | Notes |
| --- | --- | --- | --- | --- | --- |
| Home | ![screenshot](docs/browsers/chrome-home.png) | ![screenshot](docs/browsers/firefox-home.png) | ![screenshot](docs/browsers/safari-home.png) | ![screenshot](docs/browsers/edge-home.png) | Works as expected |
| Forum Pages | ![screenshot](docs/browsers/chrome-forum.png) | ![screenshot](docs/browsers/firefox-forum.png) | ![screenshot](docs/browsers/safari-forum.png) | ![screenshot](docs/browsers/edge-forum.png) | Works as expected |
| Post Creation | ![screenshot](docs/browsers/chrome-create.png) | ![screenshot](docs/browsers/firefox-create.png) | ![screenshot](docs/browsers/safari-create.png) | ![screenshot](docs/browsers/edge-create.png) | Works as expected |
| Authentication | ![screenshot](docs/browsers/chrome-auth.png) | ![screenshot](docs/browsers/firefox-auth.png) | ![screenshot](docs/browsers/safari-auth.png) | ![screenshot](docs/browsers/edge-auth.png) | Works as expected |
| Post Detail | ![screenshot](docs/browsers/chrome-detail.png) | ![screenshot](docs/browsers/firefox-detail.png) | ![screenshot](docs/browsers/safari-detail.png) | ![screenshot](docs/browsers/edge-detail.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](docs/lighthouse/mobile-home.png) | ![screenshot](docs/lighthouse/desktop-home.png) | Good performance scores |
| Forum List | ![screenshot](docs/lighthouse/mobile-forum.png) | ![screenshot](docs/lighthouse/desktop-forum.png) | Some performance issues on mobile due to images |
| Post Detail | ![screenshot](docs/lighthouse/mobile-post.png) | ![screenshot](docs/lighthouse/desktop-post.png) | Image optimization could be improved |
| Create Post | ![screenshot](docs/lighthouse/mobile-create.png) | ![screenshot](docs/lighthouse/desktop-create.png) | Good accessibility scores |
| Login | ![screenshot](docs/lighthouse/mobile-login.png) | ![screenshot](docs/lighthouse/desktop-login.png) | Excellent scores across all metrics |
| Signup | ![screenshot](docs/lighthouse/mobile-signup.png) | ![screenshot](docs/lighthouse/desktop-signup.png) | Good performance and accessibility |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Screenshot | Screenshot (Additional) |
| --- | --- | --- | --- | --- | --- |
| Home | Feature is expected to display all forums to any user. | Opened homepage as guest and authenticated user. | All forums displayed correctly for both user types. | ![screenshot](docs/defensive/home-forums.png) | |
| | Feature is expected to show create post button only to authenticated users. | Checked homepage as guest and authenticated user. | Create post button only visible when logged in. | ![screenshot](docs/defensive/create-post-auth.png) | |
| Forums | Feature is expected to display posts in selected forum. | Clicked on different forums to view posts. | Posts filtered correctly by forum category. | ![screenshot](docs/defensive/forum-posts.png) | |
| | Feature is expected to show like buttons only to authenticated users. | Viewed forum posts as guest and authenticated user. | Like buttons only visible when logged in. | ![screenshot](docs/defensive/like-auth.png) | |
| Post Creation | Feature is expected to redirect unauthenticated users to login. | Attempted to access create post URL while logged out. | Redirected to login page successfully. | ![screenshot](docs/defensive/create-post-redirect.png) | |
| | Feature is expected to allow authenticated users to create posts. | Created posts with various content and images. | Posts created successfully with all form fields. | ![screenshot](docs/defensive/create-post-success.png) | |
| | Feature is expected to validate required fields. | Submitted form with empty title and content. | Form validation prevented submission with clear error messages. | ![screenshot](docs/defensive/create-post-validation.png) | |
| Post Management | Feature is expected to allow only post authors to edit their posts. | Attempted to edit another user's post via URL manipulation. | Access denied - 404 error displayed. | ![screenshot](docs/defensive/edit-post-denied.png) | |
| | Feature is expected to allow only post authors to delete their posts. | Attempted to delete another user's post via URL manipulation. | Access denied - 404 error displayed. | ![screenshot](docs/defensive/delete-post-denied.png) | |
| | Feature is expected to show edit/delete options only to post authors. | Viewed posts as author and non-author. | Edit/delete buttons only visible to post authors. | ![screenshot](docs/defensive/post-author-controls.png) | |
| Likes System | Feature is expected to allow authenticated users to like/unlike posts. | Clicked like button on various posts. | Like count updated correctly, toggle functionality worked. | ![screenshot](docs/defensive/like-toggle.png) | |
| | Feature is expected to prevent duplicate likes from same user. | Attempted to like same post multiple times. | System prevented duplicate likes correctly. | ![screenshot](docs/defensive/like-prevent-duplicate.png) | |
| Comments | Feature is expected to allow authenticated users to add comments. | Posted comments on various posts. | Comments added successfully and displayed correctly. | ![screenshot](docs/defensive/comment-add.png) | |
| | Feature is expected to require authentication for commenting. | Attempted to access comment form while logged out. | Comment form only visible when authenticated. | ![screenshot](docs/defensive/comment-auth.png) | |
| | Feature is expected to validate comment content. | Submitted empty comment form. | Validation prevented submission of empty comments. | ![screenshot](docs/defensive/comment-validation.png) | |
| Forums (Admin) | Feature is expected to allow superusers to create forums. | Created new forum as admin user. | Forum created successfully and appeared in listings. | ![screenshot](docs/defensive/create-forum-admin.png) | |
| | Feature is expected to prevent non-admin users from creating forums. | Attempted to access create forum URL as regular user. | Access redirected to home page with error message. | ![screenshot](docs/defensive/create-forum-denied.png) | |
| CSRF Protection | Feature is expected to reject forms without CSRF tokens. | Submitted forms with CSRF token removed. | Forms rejected with 403 Forbidden error. | ![screenshot](docs/defensive/csrf-protection.png) | |
| XSS Prevention | Feature is expected to escape malicious script tags in content. | Submitted post with `<script>` tags in content. | Script tags escaped and displayed as text. | ![screenshot](docs/defensive/xss-prevention.png) | |
| File Upload | Feature is expected to handle image uploads securely. | Uploaded various image formats and sizes. | Images processed correctly with UUID naming. | ![screenshot](docs/defensive/image-upload.png) | |
| | Feature is expected to reject non-image files. | Attempted to upload non-image files. | File uploads rejected with appropriate error messages. | ![screenshot](docs/defensive/file-upload-validation.png) | |
| 404 Error | Feature is expected to display custom 404 page for invalid URLs. | Navigated to non-existent URLs. | Custom 404 page displayed correctly. | ![screenshot](docs/defensive/404-page.png) | |

## User Story Testing

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a new user | I would like to easily understand what the site is about | so that I can decide if I want to register and participate. | ![screenshot](docs/user-stories/homepage-clear.png) |
| As a new user | I would like to browse content without registering | so that I can explore before committing to create an account. | ![screenshot](docs/user-stories/browse-guest.png) |
| As a new user | I would like to easily sign up for an account | so that I can start creating and engaging with content. | ![screenshot](docs/user-stories/easy-signup.png) |
| As a user | I would like to create blog posts with rich text and images | so that I can share my stories in an engaging format. | ![screenshot](docs/user-stories/create-rich-post.png) |
| As a user | I would like to categorize my posts into different forums | so that readers can find content that interests them. | ![screenshot](docs/user-stories/categorize-posts.png) |
| As a user | I would like to edit my own posts | so that I can update or improve my content after publishing. | ![screenshot](docs/user-stories/edit-own-posts.png) |
| As a user | I would like to delete my own posts | so that I can remove content I no longer want published. | ![screenshot](docs/user-stories/delete-own-posts.png) |
| As a user | I would like to like posts I enjoy | so that I can show appreciation to other authors. | ![screenshot](docs/user-stories/like-posts.png) |
| As a user | I would like to comment on posts | so that I can engage in discussions with other community members. | ![screenshot](docs/user-stories/comment-posts.png) |
| As a reader | I would like to browse posts by forum category | so that I can find stories that match my interests. | ![screenshot](docs/user-stories/browse-by-forum.png) |
| As a reader | I would like to view full post details including comments | so that I can read complete stories and community discussions. | ![screenshot](docs/user-stories/view-post-details.png) |
| As a reader | I would like to see like counts and comments | so that I can gauge community engagement with posts. | ![screenshot](docs/user-stories/engagement-metrics.png) |
| As a content creator | I would like to see who liked my posts | so that I can understand my audience engagement. | ![screenshot](docs/user-stories/view-likes.png) |
| As a content creator | I would like to respond to comments on my posts | so that I can engage with my readers. | ![screenshot](docs/user-stories/respond-comments.png) |
| As a site visitor | I would like the site to work well on my mobile device | so that I can use it anywhere. | ![screenshot](docs/user-stories/mobile-responsive.png) |
| As a site user | I would like secure authentication | so that my account and content are protected. | ![screenshot](docs/user-stories/secure-auth.png) |

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

Below are the results from the full coverage report on my application that I've tested:

![screenshot](docs/automation/html-coverage.png)

#### Unit Test Issues

No significant issues encountered during unit testing. All tests pass successfully.

## Bugs

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3ATranshumanistAJ%2Fblogiverse%20label%3Abug&label=bugs)](https://github.com/TranshumanistAJ/blogiverse/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

All previously closed/fixed bugs can be tracked [here](https://github.com/TranshumanistAJ/blogiverse/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

| Issue | Description | Solution | Screenshot |
| --- | --- | --- | --- |
| Static Files Not Loading in Production | CSS and images not loading when DEVELOPMENT=False | Configured static file serving in URLs and simplified storage settings | ![screenshot](docs/bugs/static-files-fix.png) |
| CSRF Token Missing | Forms failing validation due to missing CSRF tokens | Added {% csrf_token %} to all forms in templates | ![screenshot](docs/bugs/csrf-fix.png) |
| Image Upload Conflicts | Duplicate filenames causing file conflicts | Implemented UUID-based unique naming system | ![screenshot](docs/bugs/uuid-fix.png) |
| Like Button Not Updating | Like status not reflecting correctly after click | Fixed user authentication check in like view | ![screenshot](docs/bugs/like-fix.png) |
| Empty Comments Accepted | System accepting empty comment submissions | Added content validation to comment form | ![screenshot](docs/bugs/comment-validation-fix.png) |
| Responsive Image Issues | Images not scaling properly on mobile devices | Added responsive CSS classes and max-width properties | ![screenshot](docs/bugs/responsive-images-fix.png) |

### Unfixed Bugs

[![GitHub issues](https://img.shields.io/github/issues/TranshumanistAJ/blogiverse)](https://github.com/TranshumanistAJ/blogiverse/issues)

Any remaining open issues can be tracked [here](https://github.com/TranshumanistAJ/blogiverse/issues).

Currently, there are no known unfixed bugs.

### Known Issues

| Issue | Screenshot |
| --- | --- |
| None currently identified | N/A |

> [!IMPORTANT]
> There are no remaining bugs that I am aware of. However, even after thorough testing, I cannot rule out the possibility of undiscovered issues.
