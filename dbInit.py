# !/usr/bin/python
# -*- coding: utf-8 -*-
from app.model import*
from app import create_app

app = create_app()
app.test_request_context().push()

choice = input('please enter a number 1:create_all, 2:drop_all, 3:add lots of articles :')

if choice == '1':
    try:
        # db.create_all()
        # print('create success')
        user = User(name = 'admin', password='123456')
        db.session.add(user)
        category = Category(name ='default', description='a default category')
        db.session.add(category)
        setting = Setting()
        db.session.add(setting)
        db.session.commit()
        print('add ok')
    except Exception as e :
        print(e)
elif choice == '2':
    try:
        print('22222222222')
        db.drop_all()
        print('drop success')
    except Exception as e:
        print(e)
elif choice == '3':
    writer = '保罗'
    n = 200
    while n > 0:
        content = '我'
        c = 100
        while c > 0:
            content+='哈哈'
            c=c-1
        article = Article(title='一个测试',content=content,
                                    writer=writer,category_id=1)
        db.session.add(article)
        db.session.commit()
        n=n-1
        print(n)        
    print('create articles complete')
else:
    print('alid')
