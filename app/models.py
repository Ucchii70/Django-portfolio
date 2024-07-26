from django.db import models

class Profile(models.Model):
    
    title = models.CharField(
        verbose_name='タイトル',
        max_length=100,
        null=True,
        blank=True, 
        )

    subtitle = models.CharField(
        verbose_name='サブタイトル',
        max_length=100,
        null=True,
        blank=True, 
        )

    name = models.CharField(
        verbose_name='名前',
        max_length=100
        )

    job = models.TextField('仕事')

    introduction = models.TextField('自己紹介')

    github = models.CharField(
        verbose_name='github',
        max_length=100,
        null=True,
        blank=True, 
        )
    
    x = models.CharField(
        verbose_name='x', 
        max_length=100, 
        null=True, 
        blank=True
        )

    linkedin = models.CharField(
        verbose_name='linkedin', 
        max_length=100, 
        null=True, 
        blank=True
        )
    
    facebook = models.CharField(
        verbose_name='facebook', 
        max_length=100, 
        null=True, 
        blank=True
        )

    instagram = models.CharField(
        verbose_name='instagram', 
        max_length=100, 
        null=True, 
        blank=True
        )

    topimage = models.ImageField(
        upload_to='images',
        verbose_name='トップ画像'
        )
    
    subimage = models.ImageField(
        upload_to='images',
        verbose_name='サブ画像'
        )
    
    def __str__(self):
        # オブジェクトを文字列に変換して返す
        return self.name
    
class Work(models.Model):
    
    title = models.CharField(
        'タイトル',
        max_length=100
        )
    
    image = models.ImageField(
        upload_to='images',
        verbose_name='イメージ画像'
        )
    
    thumbnail = models.ImageField(
        upload_to='images',
        verbose_name='サムネイル画像',
        null=True,
        blank=True
        )
    
    skill = models.CharField(
        'スキル',
        max_length=100
        )
    
    # null, blank=Trueで作品URLがない場合でも対応できるようにする
    url = models.CharField(
        'URL',
        max_length=100,
        null=True,
        blank=True
        )
    
    url2 = models.CharField(
        'URL2',
        max_length=100,
        null=True,
        blank=True
        )
    
    created = models.DateField('作成日')

    description = models.TextField('説明') # 長い文字列

    def __str__(self):
        # オブジェクトを文字列に変換して返す
        return self.title

# 職歴のモデル
class Experience(models.Model):
    
    occupation = models.CharField(
        verbose_name='職種',
        max_length=100
        )
    
    company = models.CharField(
        verbose_name='会社',
        max_length=100
        )
    
    description = models.TextField(verbose_name='説明')

    place = models.CharField(
        verbose_name='場所',
        max_length=100
        )
    
    period = models.CharField(
        verbose_name='期間',
        max_length=100
        )
    
    def __str__(self):
        return self.occupation
    
# 学歴
class Education(models.Model):
    
    course = models.CharField(
        verbose_name='コース',
        max_length=100
        )

    school = models.CharField(
        verbose_name='学校',
        max_length=100
        )

    place = models.CharField(
        verbose_name='場所',
        max_length=100
        )

    period = models.CharField(
        verbose_name='期間',
        max_length=100
        )

    def __str__(self):
        return self.course
    
# 
class Software(models.Model):

    name = models.CharField(
        verbose_name='ソフトウェア',
        max_length=100
        )

    level = models.CharField(
        verbose_name='レベル',
        max_length=100
        )
    
    percentage = models.IntegerField(
        # IntegerFieldで数字のみを扱う
        verbose_name='パーセンテージ'
        )
    
    def __str__(self):
        return self.name
    
# 
class Technical(models.Model):

    name = models.CharField(
        verbose_name='テクニカル',
        max_length=100
        )

    level = models.CharField(
        verbose_name='レベル',
        max_length=100
        )
    
    percentage = models.IntegerField(
        # IntegerFieldで数字のみを扱う
        verbose_name='パーセンテージ'
        )
    
    def __str__(self):
        return self.name
    































