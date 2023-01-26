from management.models import Book, Book2Auth, Author
import random

auth_name = ['Salman Rushdie', 'Khaled Hosseini', 'Devdutt Patnaik', 'Blake Crouch', 'James Clear', 'Gaur Gopal Das']
for i in range(6) : 
    id = "auth_{d}".format(d=i)
    a = Author(id, auth_name[i])
    a.save()

book_name = ['The', 'World', 'Wonderful', 'Silent', 'Lamb', 'Threatning', 'Scary', 'Beautiful', 'Romace',
             'Evening', 'Winter', 'Summer', 'Hate', 'Killer', 'Turn', 'Race']
genres = ['Romance', 'Action', 'Drama', 'Self-Help']

for i in range(100) : 
    # aut = auth_name[i%5]
    # part = ind[i%5]
    # ind[i%5] = ind[i%5]+1
    
    id = "book_{d}".format(d=i)
    name = []
    for t in range(random.randint(3,4)) :
        name.append(book_name[random.randint(0,15)])
    name = ' '.join(name)   
    copy = random.randint(3,28)
    genre = genres[random.randint(0,3)]
    book = Book(id, name, genre, copy)
    book.save()
   
# for i in range(40) :  
    j = random.randint(0,5)
    aid = "auth_{d}".format(d=j) 
    bid = "book_{d}".format(d=i)
    
    aut = Author.objects.get(authId = aid)
    boo = Book.objects.get(bookId=bid)
    
    b2a = Book2Auth(book=boo, auth=aut)
    b2a.save()