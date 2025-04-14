# Blogiverse
[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/TranshumanistAJ/blogiverse)](https://github.com/TranshumanistAJ/blogiverse/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/TranshumanistAJ/blogiverse)](https://github.com/TranshumanistAJ/blogiverse/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/TranshumanistAJ/blogiverse)](https://github.com/TranshumanistAJ/blogiverse)



## Overview
Blogiverse is a vibrant, community-driven blogging platform built to inspire and connect individuals through storytelling. It offers a space where users can create, share, and engage with personal narratives across diverse forums such as Personal Growth, Love & Relationships, Self Discovery, Mystical & Unexplained, A Trip to the Unknown, Faith & Spirituality, and Unconventional Trips. Designed for writers, dreamers, and curious readers, Blogiverse empowers users to express their unique experiences, fostering a sense of belonging and dialogue through likes, comments, and rich multimedia content. Whether you’re a new visitor seeking inspiration or a returning user sharing your journey, Blogiverse provides an intuitive, secure, and visually appealing platform to explore and contribute to a tapestry of human stories.

The platform targets a broad audience: aspiring writers who want to share their voices, readers eager to discover authentic narratives, and community members who value interaction through feedback. By offering tools like post creation, editing, deletion, and interactive features like liking and commenting, Blogiverse ensures users can both contribute and engage meaningfully. Its responsive design ensures accessibility across devices, making it a versatile tool for storytelling on the go or from the comfort of home.

> [!NOTE]  
> This is the initial submission of Blogiverse, completed under tight time constraints. I acknowledge that some errors, such as database migration issues and incomplete styling, persist due to unforeseen technical challenges. I am fully committed to addressing these issues thoroughly in a resubmission, ensuring that Blogiverse meets the highest standards of functionality and polish. My goal is to deliver a project that exemplifies excellence and serves as a strong example for passing the Code Institute diploma requirements. I appreciate the opportunity to refine and perfect this work.

## UX

### Design Process
Blogiverse was designed with a user-centric approach, prioritizing ease of navigation, visual appeal, and interactivity. The design process began with identifying the needs of two primary user groups: content creators (writers) and content consumers (readers). Wireframes were created to map out the user journey, from browsing forums to creating and engaging with posts. The goal was to ensure a seamless experience, whether users were casually exploring or actively contributing. Accessibility was a key focus, with responsive layouts tested across mobile, tablet, and desktop devices to accommodate all users.

### Colour Scheme
The colour scheme was chosen to evoke warmth, engagement, and clarity:
- `#000000` (Black): Used for primary text to ensure readability and contrast.
- `#E84610` (Orange-Red): Applied to highlights like like buttons and alerts, drawing attention to interactive elements.
- `#4A4A4F` (Dark Gray): Used for secondary text to maintain a subtle hierarchy.
- `#009FE3` (Cyan): Employed for links and navigation, adding vibrancy and guiding user actions.
- `#F9FAFC` (Light Gray): Used as the background to create a clean, modern aesthetic.

I used [coolors.co](https://coolors.co/e84610-009fe3-4a4a4f-445261-d63649-e6ecf0-000000) to generate and refine the palette.



CSS `:root` variables were implemented to streamline updates:





## Typography
#### Typography was selected for clarity and aesthetic harmony:

#### Montserrat : 
Used for headers and titles to convey boldness and modernity.

#### Lato: 
Applied to body text for its clean, approachable style, ensuring readability.
#### Font Awesome: 
Integrated for icons, such as hearts for likes and comments, enhancing visual cues.

## User Stories
### New Site Users
* As a new site user, I would like to browse blog posts by forum, so that I can find stories that resonate with my interests.
* As a new site user, I would like to view detailed posts with images, so that I can immerse myself in the narrative visually and emotionally.
* As a new site user, I would like to see like and comment counts, so that I can identify popular or engaging content.
* As a new site user, I would like to sign up with a simple process, so that I can quickly join the community and participate.
* As a new site user, I would like to recover my account via password reset, so that I can regain access if I forget my credentials.

## Returning Site Users
* As a returning site user, I would like to create blog posts with text and images, so that I can share my personal stories.
* As a returning site user, I would like to edit my posts, so that I can improve or update my content over time.
* As a returning site user, I would like to delete my posts, so that I can remove content I no longer wish to share.
* As a returning site user, I would like to like other users’ posts, so that I can express appreciation and support.
* As a returning site user, I would like to comment on posts, so that I can engage in meaningful discussions with the community.

## Site Admin
* As a site admin, I would like to manage forums, so that I can organize content effectively.
* As a site admin, I would like to view all posts and their engagement metrics, so that I can monitor community activity.
* As a site admin, I would like to ensure secure authentication, so that user data remains protected.


# Features
### Existing Features
## Blog Forums
Users can explore seven distinct forums (Personal Growth, Love & Relationships, Self Discovery, Mystical & Unexplained, A Trip to the Unknown, Faith & Spirituality, Unconventional Trips), each hosting relevant posts. This organizes content by theme, helping users find stories that match their interests, whether they’re seeking inspiration or connection

## Blog Post Creation: 
Authenticated users can create posts with titles, text, photos, and forum assignments, enabling them to share personal narratives. The Summernote editor enhances content creation with rich formatting, making storytelling accessible and expressive.

## Blog Post Creation
Authenticated users can create posts with titles, text, photos, and forum assignments, enabling them to share personal narratives. The Summernote editor enhances content creation with rich formatting, making storytelling accessible and expressive.

## User Authentication
Secure login/signup via Django-allauth supports user interaction, with a password reset link below the login form for accessibility. This ensures users can safely join, contribute, and recover accounts, protecting their data and experience.

## Post Editing
Authors can edit their posts’ titles, content, photos, or forums, allowing refinement of their stories. This empowers users to maintain quality and relevance, enhancing their presence in the community.

## Post Deletion
Authors can delete their posts, giving control over their shared content. This feature supports user autonomy, letting them remove posts no longer aligned with their intentions.

## Forum Creation
Admins can create new forums, expanding the platform’s thematic range. This ensures Blogiverse evolves with user interests, keeping the community dynamic.

## Responsive Design
The site adapts to mobile, tablet, and desktop devices, ensuring accessibility for all users, whether at home or on the move. Bootstrap and custom CSS maintain a consistent, user-friendly interface.

## Message Toasts
Success messages (e.g., “Post created!”) appear after actions like posting or liking, providing immediate feedback. Styled with Bootstrap alerts, they enhance user satisfaction and clarity.

## Future Features
Social Sharing: Enable sharing posts on platforms like Twitter or Facebook to boost visibility and community growth.
User Profiles: Allow users to create profiles showcasing their posts, fostering a sense of identity and ownership.

## Search Functionality: 
Add a search bar to find posts by keywords, improving content discoverability.
Post Categories/Tags: Introduce tags to filter posts within forums, enhancing navigation.
Analytics Dashboard: Provide admins with insights into post engagement (views, likes, comments) to monitor community health.



### Deployment:
The site was deployed to Heroku, ensuring a robust and scalable hosting environment. The deployment process involved:

* Creating a Heroku app via the GitHub repository.
* Setting config vars in Heroku Dashboard:
DATABASE_URL: Neon Postgres URL for database connectivity.

* SECRET_KEY: Unique key for Django security.
* PORT: Set to 8000 for Heroku compatibility.

Pushing code to Heroku: git push heroku main.
Triggering deployment through the Heroku dashboard, ensuring automatic scaling and updates.
.

### Local Deployment
#### Cloning
Navigate to the GitHub repository.
Click the Code button and copy the URL.
Open a terminal, change to the desired directory.
* Run: git clone https://github.com/TranshumanistAJ/blogiverse.git.


* Install dependencies: pip install -r requirements.txt.

* Set up environment variables in env.py (DATABASE_URL, SECRET_KEY, DEVELOPMENT=True).

* Run migrations: python manage.py migrate.

*Start server: python manage.py runserver.

#### Forking

1: Log in to GitHub and visit GitHub repository.
2: Click the Fork button to create a copy in your GitHub account.
3:  Clone the forked repository to your local 
machine for modifications.


## Local VS Deployment
Locally, the site runs with DEBUG=True to facilitate development and debugging, displaying detailed error pages for quick fixes. On Heroku, DEBUG=False ensures security by hiding sensitive information, adhering to production best practices. Static files are served by Django locally but managed by WhiteNoise on Heroku for efficiency. The database uses a local SQLite instance during development (if configured), while Heroku connects to a Neon Postgres database for scalability and persistence.

## Credits

### Acknowledgements
*I would like to express my deepest gratitude to those who supported me throughout the development of Blogiverse*:

#### Richard Wells, my mentor at Code Institute, whose exceptional guidance, patience, and expertise were pivotal in overcoming technical hurdles. His encouragement was a constant source of motivation, pushing