问题：'blog_tags' is not a registered tag library.

解决：
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        'libraries':{
            'blog_tags':'blog.templatetags.blog_tags',
        }
        },
    },
]
```

. redirect作用是对HTTTP请求进行重定向。redirect既可以接收一个URL
作为参数，也可以接收一个模型的实例作为参数。如果接收一个模型的实例，那么
这个实例必须实现了get_absolute_url方法，这样redirect会根据get_absolute_url
方法返回的URL值进行重定向
