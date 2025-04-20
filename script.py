from django.contrib.auth.models import User
from blogs.models import Forum, BlogPost
from django.utils import timezone
try:
user = User.objects.get(username="Transhumanist")
except User.DoesNotExist:
user = User.objects.create_superuser("Transhumanist", "ajdeutschland103@hotmail.com", "Dansat103")
forums = {"Personal Growth": "Personal Growth stories", "Love & Relationships": "Tales of romance", "Self Discovery": "Journeys of self", "Mystical & Unexplained": "Mysteries beyond", "A Trip to the Unknown": "Group adventures", "Faith & Spirituality": "Spiritual paths", "Unconventional Trips": "Offbeat travels"}
for name, desc in forums.items():
Forum.objects.get_or_create(name=name, defaults={"description": desc})
posts = [("From Trash to Triumph: My Journey Out of Hardship in Niger", "Personal Growth", "A story of resilience...", "blog_photos/immanuel.jpg"), ("Love Across Borders: A Canvas of Two Worlds", "Love & Relationships", "Love across cultures...", "blog_photos/sarah_and_edward.jpg"), ("Embracing the Gift: A Mother’s Journey with Autism", "Personal Growth", "A mother’s tale...", "blog_photos/kirah_and_daughter.jpg"), ("The Cost of Curiosity: A Life Unraveled by Questions", "Self Discovery", "Curiosity’s cost...", "blog_photos/julia_in_lyon.jpg"), ("Beyond the Veil: My Near-Death Awakening", "Mystical & Unexplained", "A mystical experience...", "blog_photos/rose_ldovi.jpg"), ("Eight Souls in the Frozen Void", "A Trip to the Unknown", "A group’s journey...", "blog_photos/eight_guys.jpg"), ("Saved by Grace: A Journey from Darkness", "Faith & Spirituality", "Faith saved me...", "blog_photos/james_wang.jpg"), ("The Ditched Ship: A Dance with Rust and Risk", "Unconventional Trips", "A ship adventure...", "blog_photos/the_ship.jpg")]
for title, forum_name, content, photo in posts:
forum = Forum.objects.get(name=forum_name)
BlogPost.objects.get_or_create(title=title, defaults={"content": content, "author": user, "forum": forum, "created_at": timezone.now(), "photo": photo})
