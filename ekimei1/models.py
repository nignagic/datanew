from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

class CustomUserManager(UserManager):
	user_in_migrations = True

	def _create_user(self, email, password, **extra_fields):
		if not email:
			raise ValueError('The given email must be set')
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self.db)
		return user

	def create_user(self, email, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')
		return self._create_user(email, password, **extra_fields)

# class User(AbstractBaseUser, PermissionsMixin):
# 	email = models.EmailField(_('email address'), unique=True)
# 	name = models.CharField(_('name'), max_length=100, blank=True)

# 	is_staff = models.BooleanField(
# 		_('staff status'),
# 		default=False,
# 		help_text=_(
# 			'Designates whether the user can log into this admin site.'),
# 	)
# 	is_active = models.BooleanField(
# 		_('active'),
# 		default=True,
# 		help_text=_(
# 			'Designates whether this user should be treated as active.'
# 			'Unselect this instead of deleting accounts.'
# 		),
# 	)
# 	date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
# 	objects = CustomUserManager()

# 	EMAIL_FIELD = 'email'
# 	USERNAME_FIELD = 'email'
# 	REQUIRED_FIELDS = []

# 	class Meta:
# 		verbose_name = _('user')
# 		verbose_name_plural = _('users')

# 	def email_user(self, subject, message, from_email=None, **kwargs):
# 		send_mail(subject, message, from_email, [self.email], **kwargs)

# 	@property
# 	def username(self):
# 		return self.email
	

class Prefecture(models.Model):
	pref_cd = models.IntegerField(default=0)
	pref_name = models.CharField(max_length=200)
	def __str__(self):
		return self.pref_name

class Line(models.Model):
	line_cd = models.IntegerField(default=0, unique=True)
	company_cd = models.IntegerField(default=0)
	line_name = models.CharField(max_length=200)
	line_name_k = models.CharField(max_length=200, null=True, blank=True)
	line_name_h = models.CharField(max_length=200, null=True, blank=True)
	line_color_c = models.CharField(max_length=200, null=True, blank=True)
	line_color_t = models.CharField(max_length=200, null=True, blank=True)
	line_type = models.CharField(max_length=200, null=True, blank=True)
	lon = models.CharField(max_length=200, null=True, blank=True)
	lat = models.CharField(max_length=200, null=True, blank=True)
	zoom = models.IntegerField(default=0)
	e_status = models.IntegerField(default=0)
	e_sort = models.IntegerField(default=0)
	pref_cds = models.ManyToManyField(Prefecture, blank=True)
	def __str__(self):
		return self.line_name

class Station(models.Model):
	station_cd = models.IntegerField('駅コード', default=0, unique=True)
	station_g_cd = models.IntegerField('駅グループコード', default=0)
	station_name = models.CharField('駅名', max_length=200)
	station_name_k = models.CharField('駅名(カナ)', max_length=200, null=True, blank=True)
	station_name_r = models.CharField('駅名(ローマ字)', max_length=200, null=True, blank=True)
	line_cd = models.ForeignKey(Line, to_field='line_cd', null=True, blank=True, on_delete=models.CASCADE, verbose_name='路線')
	pref_cd = models.ForeignKey(Prefecture, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='都道府県')
	post = models.CharField('駅郵便番号', max_length=200, null=True, blank=True)
	add = models.CharField('住所', max_length=200, null=True, blank=True)
	lon = models.CharField('経度', max_length=200, null=True, blank=True)
	lat = models.CharField('緯度', max_length=200, null=True, blank=True)
	open_ymd = models.DateField('開業年月日', max_length=200, null=True, blank=True)
	close_ymd = models.DateField('廃止年月日', max_length=200, null=True, blank=True)

	STATUS = (
		(0, '運用中'),
		(1, '運用前'),
		(2, '廃止')
	)
	e_status = models.IntegerField('状態', choices=STATUS, default=0)
	e_sort = models.IntegerField('並び順', default=0)
	def __str__(self):
		return self.station_name

class Category(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class Creator(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class YoutubeChannel(models.Model):
	name = models.CharField(max_length=200)
	channelId = models.CharField(max_length=200, primary_key=True)
	creator = models.ForeignKey(Creator, on_delete=models.SET_NULL, null=True, related_name='channel', verbose_name='作者')
	def __str__(self):
		return self.name

class Name(models.Model):
	#名義(合作、単作関わらずこの名前で参加者を記述)
	name = models.CharField(max_length=200)
	creator = models.ForeignKey(Creator, on_delete=models.SET_NULL, null=True, blank=True, related_name='part_name', verbose_name='作者')
	def __str__(self):
		return self.name

class Artist(models.Model):
	name = models.CharField(max_length=200)
	parent = models.ManyToManyField('self', verbose_name='所属グループ等', blank=True)
	def __str__(self):
		return self.name

class Song(models.Model):
	name = models.CharField('曲名', max_length=200)
	namerb = models.CharField('曲名カナ', max_length=200, blank=True)
	artist = models.ManyToManyField(Artist, blank=True)
	album = models.CharField('アルバム名', max_length=200, blank=True)
	lyrist = models.CharField('作詞者', max_length=200, blank=True)
	composer = models.CharField('作曲者', max_length=200, blank=True)
	tieup = models.CharField('タイアップ等', max_length=200, blank=True)
	description = models.TextField('備考', max_length=500, blank=True)
	parent = models.ManyToManyField('self', verbose_name='原作等', blank=True)
	def __str__(self):
		return self.name

class Vocal(models.Model):
	name = models.CharField('ボーカル名', max_length=200)
	def __str__(self):
		return self.name

class Movie(models.Model):
	title = models.CharField('動画タイトル', max_length=200)
	channel = models.ForeignKey(
		YoutubeChannel, on_delete=models.SET_NULL, null=True, verbose_name='投稿チャンネル'
	)
	participant = models.ManyToManyField(
		Name, blank=True, verbose_name='参加者'
	)
	main_id = models.CharField('動画ID', max_length=200, unique=True)
	youtube_id = models.CharField('YouTubeのID', max_length=200, blank=True)
	niconico_id = models.CharField('ニコニコ動画のID', max_length=200, blank=True)
	published_at = models.DateTimeField('投稿日時', blank=True, null=True)
	duration = models.DurationField('動画の長さ', null=True)
	n_view = models.IntegerField('再生回数', default=0, blank=True)
	n_like = models.IntegerField('高評価数', default=0, blank=True)
	n_dislike = models.IntegerField('低評価数', default=0, blank=True)
	n_comment = models.IntegerField('コメント数', default=0, blank=True)
	description = models.TextField('説明', blank=True)

	reg_date = models.DateTimeField('データベース登録日時', blank=True)

	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='カテゴリー')
	song = models.ManyToManyField(Song, blank=True, verbose_name='使用楽曲')
	vocal = models.ManyToManyField(Vocal, blank=True, verbose_name='使用ボーカル')
	COLLAB = (
		('S', '単作'),
		('C', '合作')
	)
	is_collab = models.CharField('合作か', max_length=1, choices=COLLAB, default='S')
	parent = models.ManyToManyField('self', verbose_name='親作品', blank=True)
	explanation = models.TextField('補足説明', blank=True)
	def __str__(self):
		return self.title

class Part(models.Model):
	part_num = models.IntegerField()
	part_name_short = models.CharField(max_length=5)
	part_name = models.CharField(max_length=200, blank=True)
	movie = models.ForeignKey(Movie, to_field='main_id', on_delete=models.CASCADE)
	participant = models.ManyToManyField(Name, blank=True, verbose_name='参加名義')
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='カテゴリー')
	start_time = models.DurationField('開始時間', null=True, blank=True)
	song = models.ManyToManyField(Song, blank=True, verbose_name='使用楽曲')
	song_name = models.CharField(max_length=200, blank=True)
	vocal = models.ManyToManyField(Vocal, blank=True, verbose_name='使用ボーカル')
	explanation = models.TextField('説明', blank=True)
	def __str__(self):
		return self.part_name + " - " + self.movie.title

class StationInMovie(models.Model):
	id_in_movie = models.IntegerField()
	movie_part = models.ForeignKey(Part, on_delete=models.CASCADE)
	station_cd = models.ForeignKey(Station, to_field='station_cd', on_delete=models.CASCADE)
	station_name = models.CharField(max_length=200)
	non_line = models.BooleanField('路線不定', default=False)
	back_rel = models.IntegerField('前駅との関係', default=1)
	def __str__(self):
		return self.station_name