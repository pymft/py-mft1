class OneOnly:
    _singleton = None

    def __new__(cls, *args, **kwargs):
        # تا الان از این کلاس نمونه ای ساخته شده؟
        if not cls._singleton:
            # پس یه جدید می سازیم
            cls._singleton = super().__new__(cls, *args, **kwargs)
        return cls._singleton


x = OneOnly()
y = OneOnly()
z = OneOnly()

print(x is z)