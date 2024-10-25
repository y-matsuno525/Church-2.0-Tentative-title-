import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bible_project.settings')
django.setup()

from menu.models import Book, Chapter, Verse

def import_bible():
    # 例として、KJVの聖書テキストをインポートする処理を作成
    with open('path_to_your_bible_file.txt', 'r') as f:
        current_book = None
        current_chapter = None

        for line in f:
            # テキストファイルの形式に合わせて処理を調整
            # 例：Genesis 1:1 In the beginning...
            if line.strip():
                book_name, rest = line.split(' ', 1)
                chapter_verse, text = rest.split(' ', 1)
                chapter_number, verse_number = chapter_verse.split(':')

                if current_book is None or current_book.name != book_name:
                    current_book, _ = Book.objects.get_or_create(name=book_name)

                if current_chapter is None or current_chapter.chapter_number != int(chapter_number):
                    current_chapter, _ = Chapter.objects.get_or_create(book=current_book, chapter_number=chapter_number)

                Verse.objects.create(
                    chapter=current_chapter,
                    verse_number=verse_number,
                    text=text.strip()
                )

if __name__ == '__main__':
    import_bible()
