from apps.belt_app.models import *

# Author.objects.create(first_name="Piers", last_name="Anthony")
# Author.objects.create(first_name="J. R. R.", last_name="Tolkien")
# Author.objects.create(first_name="Ray", last_name="Bradbury")
# Author.objects.create(first_name="Isaac", last_name="Asimov")
# Author.objects.create(first_name="C. S.", last_name="Lewis")

# n = "The Silver Chair"
# ln = "Lewis"
# Book.objects.create(name=n)
# Book.objects.get(name=n).authors.add(Author.objects.get(last_name=ln))

# n = "The Horse and His Boy"
# ln = "Lewis"
# Book.objects.create(name=n)
# Book.objects.get(name=n).authors.add(Author.objects.get(last_name=ln))

# n = "The Magician's Nephew"
# ln = "Lewis"
# Book.objects.create(name=n)
# Book.objects.get(name=n).authors.add(Author.objects.get(last_name=ln))

# n = "The Last Battle"
# ln = "Lewis"
# Book.objects.create(name=n)
# Book.objects.get(name=n).authors.add(Author.objects.get(last_name=ln))

# n = "The Hobbit"
# ln = "Tolkien"
# Book.objects.create(name=n)
# Book.objects.get(name=n).authors.add(Author.objects.get(last_name=ln))

# n = "Fahrenheit 451"
# ln = "Bradbury"
# Book.objects.create(name=n)
# Book.objects.get(name=n).authors.add(Author.objects.get(last_name=ln))

# n = "A Spell for Chameleon"
# ln = "Anthony"
# Book.objects.create(name=n)
# Book.objects.get(name=n).authors.add(Author.objects.get(last_name=ln))

# n = "The Source of Magic"
# ln = "Anthony"
# Book.objects.create(name=n)
# Book.objects.get(name=n).authors.add(Author.objects.get(last_name=ln))

# n = "Castle Roogna"
# ln = "Anthony"
# Book.objects.create(name=n)
# Book.objects.get(name=n).authors.add(Author.objects.get(last_name=ln))

# n = "Foundation"
# ln = "Asimov"
# Book.objects.create(name=n)
# Book.objects.get(name=n).authors.add(Author.objects.get(last_name=ln))

# n = "Foundation and Empire"
# ln = "Asimov"
# Book.objects.create(name=n)
# Book.objects.get(name=n).authors.add(Author.objects.get(last_name=ln))

# n = "Second Foundation"
# ln = "Asimov"
# Book.objects.create(name=n)
# Book.objects.get(name=n).authors.add(Author.objects.get(last_name=ln))


# c = "I read this as a child and loved it.  The identity of the king at the beginning of the book surprised the heck out of me.  So fond of this book."
# r = 5
# uid = 6
# bid =  12
# Review.objects.create(content=c, rating=r, book_id=bid, user_id=uid)

# c = "Originally the Xanth books were just a trilogy and I read the third book first.  It was so cool with the talents and the monsters and the magic system in general.  I used to re-enact some of the battles in the book with my D&D lead figures."
# r = 5
# uid = 5
# bid =  20
# Review.objects.create(content=c, rating=r, book_id=bid, user_id=uid)

# c = "I think this was the best book of the original trilogy... and I saved it for last.  Serendipity!"
# r = 5
# uid = 4
# bid =  18
# Review.objects.create(content=c, rating=r, book_id=bid, user_id=uid)

# c = "Pretty thick reading material but if you like classic science fiction, this is a must-read!"
# r = 4
# uid = 3
# bid =  21
# Review.objects.create(content=c, rating=r, book_id=bid, user_id=uid)

# c = "I wanted to like this book but Tolkien's writing style just wasn't for me.  So dry and laborious."
# r = 1
# uid = 3
# bid =  16
# Review.objects.create(content=c, rating=r, book_id=bid, user_id=uid)

# c = "I suppose that this book has great content from one of the smartest men in history but I struggled to finish it.  It started and stayed fairly dry and slow.  It was just okay."
# r = 3
# uid = 3
# bid =  1
# Review.objects.create(content=c, rating=r, book_id=bid, user_id=uid)

# Job.objects.create(title="Change Oil", description="Change oil in the Honda Civic", location="4367 252nd Pl SE", user_id=1) 
# Job.objects.create(title="Rake Leaves", description="Rake the leaves in the front yard", location="4367 252nd Pl SE", user_id=2) 
# Job.objects.create(title="Vacuum the carpet", description="Vacuum upstairs", location="4367 252nd Pl SE", user_id=3) 
# Job.objects.create(title="Tuesday Carpool Drive", description="Swimmer pickup at the pool", location="Lakeside Pool", user_id=4) 
# Job.objects.create(title="Friday Carpool Drive", description="Swimmer pickup at the pool", location="Boehm Pool", user_id=5) 

# OwnedJob.objects.create(user_id=5, job_id=1)
#OwnedJob.objects.create(user_id=4, job_id=2)
#OwnedJob.objects.create(user_id=3, job_id=3)
#OwnedJob.objects.create(user_id=2, job_id=4)
#OwnedJob.objects.create(user_id=1, job_id=5)

#Job.objects.create(title="Wash Car", description="Go to Brown Bear", location="Brown Bear Issaquah", user_id=1) 
#Job.objects.create(title="Dump run", description="Take junk to the dump", location="Bellevue Transfer Station", user_id=2) 
#Job.objects.create(title="Walkthe dog", description="Take the Cruz's dog out for a walk", location="House down the street", user_id=3) 
#Job.objects.create(title="Saturday Carpool Drive", description="Swimmer pickup at the pool", location="Hazen Pool", user_id=4) 
#Job.objects.create(title="Sunday Breakfast Duty", description="Get breakfast at McDonald's", location="Sammamish McDonald's", user_id=5) 

OwnedJob.objects.create(user_id=5, job_id=6)
OwnedJob.objects.create(user_id=4, job_id=7)
OwnedJob.objects.create(user_id=3, job_id=8)
