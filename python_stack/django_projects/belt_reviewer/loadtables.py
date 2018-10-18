from apps.bookreviews.models import *

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


c = "My favorite characted did not make it to the end of this book.  I hated that!  OK otherwise."
r = 2
uid = 4
u = User.objects.get(id=uid)
bid =  26
b = Book.objects.get(id=bid)
Review.objects.create(content=c, rating=r, book=b, user=u)
