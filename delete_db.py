from management.models import Book, Book2Auth, Author

Book.objects.all().delete()
Book2Auth.objects.all().delete()
Author.objects.all().delete()