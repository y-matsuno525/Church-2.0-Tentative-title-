from django.core.management.base import BaseCommand
from transformers import pipeline
from forum.models import Book,Post,Chapter,Verse

class Command(BaseCommand):

    help = "教義生成"

    def handle(self, *args, **options):

        classifier = pipeline(task="text-generation", model="EleutherAI/gpt-neo-2.7B")

        books = Book.objects.all()
        v_summary_list = []
        c_summary_list = []
        b_summary_list = []

        for book in books:

            chapters = Chapter.objects.filter(book=book)
            c_summary_list = []

            for chapter in chapters:

                verses = Verse.objects.filter(chapter=chapter)
                v_summary_list = []

                for verse in verses:

                    temporary_v_post_list = []
                    temporary_v_post_list.append("Please summarize the following.This is a post about " + book.name + " Chapter " + str(chapter.chapter_number) + ", Verse " + str(verse.verse_number) + ": " + verse.text)
                    posts = Post.objects.filter(verse=verse)

                    if posts:

                        for post in posts:

                            temporary_v_post_list.append(post.text+"/")#post.owner.username + "id:"+str(post.id)+",content:"+ post.text+"/")
                    
                        v_post = "".join(temporary_v_post_list)                                            
                        v_summary_list.append(classifier(v_post,max_new_tokens=100))
                
                temporary_c_summary_list = []

                for v_sum in v_summary_list:

                    temporary_c_summary_list.append(v_sum[0]['generated_text'])

                c_summary = ''.join(temporary_c_summary_list)
                       
                if c_summary:

                    c_summary = 'Please summarize the following.' + c_summary
                    c_summary_list.append(classifier(c_summary,max_new_tokens=100))
            
            temporary_b_summary_list = []
            
            for c_sum in c_summary_list:

                temporary_b_summary_list.append(c_sum[0]['generated_text'])

            b_summary = ''.join(temporary_b_summary_list)
            
            if b_summary:
                
                b_summary = 'Please summarize the following.' + b_summary
                b_summary_list.append(classifier(b_summary,max_new_tokens=100))

        temporary_summary_list = []

        for b_sum in b_summary_list:

            temporary_summary_list.append(b_sum[0]['generated_text'])

        summary = ''.join(temporary_summary_list)
        if summary:
            summary = "Please generate a doctrine from the following" + summary
            final_summary = classifier(summary,max_new_tokens=100)
            print(final_summary)

