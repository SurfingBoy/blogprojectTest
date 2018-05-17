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


. paginator ，即 Paginator 的实例。

. page_obj ，当前请求页面分页对象。

. is_paginated，是否已分页。只有当分页后页面超过两页时才算已分页。

. object_list，请求页面的对象列表，和 post_list 等价。所以在模板中循环文章列表时可以选 post_list ，也可以选 object_list。