python manage.py shell

from _accounts.models import *

user1 = User.objects.create_user('Nikola')
user1.save()

user2 = User.objects.create_user('Timofei')
user2.save()

author1 = Author.objects.create(user_id=1)

author2 = Author.objects.create(user_id=2)

Category.objects.create(name='Спорт')

Category.objects.create(name='Политика')

Category.objects.create(name='Игры')

Category.objects.create(name='Экономика')

Category.objects.create(name='Развлечения')

Post.objects.create(_type=Post.post,title='Москвичка, выступающая за Австралию, выиграла финал юниорского «Гран-при»', text='Финал юниорского «Гран-при» в парном катании выиграла россиянка Анастасия Голубева, которая выступает
 в паре с австралийцем Гектором Гиотопулосом Муром. Раньше Настя была одиночницей, но уже в прошлом году взяла медаль на юниорском чемпионате мира. Сейчас этот дуэт является лидером в мировом парном катании (пока, правда, не на вз
рослом уровне) и владеет сложными элементами — например, каскадом из двух тройных тулупов.', author_id=1)

Post.objects.create(_type=Post.post, title='Лучшие игроки КХЛ любят Басту. Но и эксперимент лиги с кумирами «Тик-тока» удался', text='Хоккейная аудитория стареет. Спорт в целом и хоккей в частности не цепляет юное поколение та
к вдохновенно, как 15-20 лет назад. Переориентация интересов молодежи снижает популярность игры с шайбой и клюшкой. Этой проблемой озадачились в КХЛ. Президент лиги Алексей Морозов прямым текстом отмечал старение аудитории и стрем
ление лиги влюблять в спорт мальчишек и девчонок.', author_id=1)

PostCategory.objects.create(category_id=5,post_id=1)

PostCategory.objects.create(category_id=1,post_id=1)

PostCategory.objects.create(category_id=1,post_id=2)

PostCategory.objects.create(category_id=5,post_id=2)

PostCategory.objects.create(category_id=5,post_id=3)

PostCategory.objects.create(category_id=3,post_id=3)

Post.objects.create(_type=Post.news,title='НА THE GAME AWARDS ПОКАЗАЛИ ТРЕЙЛЕР НОВОЙ ИГРЫ JUDAS ОТ СОЗДАТЕЛЕЙ BIOSHOCK', text='На ежегодной церемонии награждения The Game Awards представили трейлер новой игры Judas. Авторами ш
утера стали создатели таких популярных тайтлов, как Bioshock и System Shock 2.',author_id=2)

Comment.objects.create(post_id=1,user_id=2,text='Тебе нравится следить за этим?')

Comment.objects.create(post_id=1,user_id=1,text='Но она же молодец!')

Comment.objects.create(post_id=2,user_id=2,text='Зачем ты пишешь это?')

Comment.objects.create(post_id=3,user_id=1,text='Игры это хорошо?')

Comment.objects.create(post_id=3,user_id=2,text='Лучше играть, чем спиться))))))')

Post.objects.get(id=1).like()
Post.objects.get(id=1).like()
Post.objects.get(id=1).like()
Post.objects.get(id=1).dislike()

Post.objects.get(id=2).like()

Comment.objects.filter(user_id=1)[0].like()
Comment.objects.filter(user_id=1)[1].like()
Comment.objects.get(id=1).like()
Comment.objects.get(id=4).dislike()


Author.objects.get(user_id=1).update_rating()
Author.objects.get(user_id=2).update_rating()


best_id = Author.objects.all().order_by('-rating').first().id
User.objects.get(id=best_id).username
Author.objects.get(id=best_id).rating

Post.objects.order_by('-rating').values('_time__date', 'author__user__username', 'rating', 'title').first()

top_post_id = Post.objects.order_by('-rating').first().id
Post.objects.filter(id=top_post_id).values('comment')
