# 指定されたテンプレートを使用してHTMLページをレンダリングし、その結果をHTTPレスポンスとして返す
# redirect:指定されたURLにリダイレクトするHTTPレスポンスを返す
from django.shortcuts import render, redirect

from django.views.generic import View
from .models import Profile, Work, Experience, Education, Software, Technical
from .forms import ContactForm
from django.conf import settings

# BadHeaderErrorは、不正なメールヘッダーが検出された場合に発生する例外
# EmailMessageクラスは、メールの作成や送信に使用
from django.core.mail import BadHeaderError, EmailMessage

# メール送信の結果を示すため
from django.http import HttpResponse

# テキストの自動的な折り返しや整形などのテキスト操作に使用
import textwrap

# HTTP GETリクエストがこのビューに送信されたときに実行されるメソッド
class IndexView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()      # 全てのProfile内モデルを取得
        if profile_data.exists():                 # もしそのデータが存在したら実行
            profile_data = profile_data.order_by('-id')[0] # idを使用して降順に並び替え、最新のProfileデータを取得

        work_data = Work.objects.order_by('-id') # idで高順に並び替えてwork_dataに格納
        
        return render(request, 'index.html', {
            'profile_data':profile_data,           # profile_data, work_dataをindex.htmlに渡す(テンプレートに渡すための変数を定義することでこの変数をテンプレートで使用できる)
            'work_data':work_data
        })
    
# HTTP GETリクエストがこのビューに送信されたときに実行されるメソッド, 指定されたプライマリーキー（pk）に対応するWorkモデルの詳細情報を表示するためのビュー 
class DetailView(View):
    def get(self, request, *args, **kwargs):
        """
        Workというモデルからpk（プライマリーキー）が与えられた特定のレコードを取得, pkはURLから取得
        取得したwork_dataをdetail.htmlに渡してレンダリングし、その結果をHTTPレスポンスとして返す

        """
        work_data = Work.objects.get(id=self.kwargs['pk'])
        return render(request, 'detail.html', {
            'work_data':work_data
        })
    
# 自己紹介, 職歴, 学歴
class AboutView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by('-id')[0] # 最新のプロフィールデータを取得
        experience_data = Experience.objects.order_by('-id') # 最新の職歴データを取得
        education_data = Education.objects.order_by('-id')
        software_data = Software.objects.order_by('-id')
        technical_data = Technical.objects.order_by('-id')
        return render(request, 'about.html', {
            'profile_data': profile_data, 
            'experience_data': experience_data,
            'education_data': education_data,
            'software_data': software_data,
            'technical_data': technical_data,
        })
    
#  お問い合わせ用のview
# getは、ページが表示された時にコールされる関数, postは何かの情報をサーバーに送る時にコールされる関数

class ContactView(View):
    def get(self, request, *args, **kwargs):
        """
        forms.pyで定義したフォームをコール
        request.POSTは、ユーザーがフォームを送信したときに提供されるデータを表し、
        or Noneのように書くことで、フォームがPOSTデータを受け取った場合はそのデータを使用し、それ以外の場合は空のフォームを作成
        """
        form = ContactForm(request.POST or None) 
        return render(request, 'contact.html', {
            'form':form,
        })
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST or None)
        
        # フォームのデータが正しい場合に、そのデータを使用して電子メールを送信し、送信後に特定のページにリダイレクトするための処理
        if form.is_valid():
            """
            フォームから送信されたデータをクリーンアップされた状態で取得し、それを変数に格納
            例えば数値フィールドに入力されたデータは整数に変換され、テキストフィールドに入力されたデータはトリミングされるなどの処理が行われます。
            """
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = 'お問い合わせありがとうございます。' # 件名
            
            # 各行の空白、インデントを削除し左揃えする
            content = textwrap.dedent(
                """
                ※このメールはシステムからの自動返信です。

                {name} 様

                お問い合わせありがとうございます。
                以下の内容でお問い合わせを受け付けました。
                内容を確認させていただき、ご連絡させて頂きますので、少々お待ちください。

                --------------------
                ■お名前
                {name}
                     
                ■メールアドレス
                {email}

                ■メッセージ
                {message}
                --------------------
                """
                
                ).format(name=name, email=email, message=message) # こちらで定義したformat関数で上記問い合わせ内容内の変数に組み込む
            to_list = [email] # 先方のアドレス
            bcc_list = [settings.EMAIL_HOST_USER] # お問い合わせがあると自分に通知が来るように設定

            try:
                message = EmailMessage(subject=subject, body=content, to=to_list, bcc=bcc_list) # 各項目のメールオブジェクトを作成(件名、本文、送信先、BCCリスト)
                message.send() # 作成したメールを送信
            
            except BadHeaderError: # 無効な送信があった場合の処理(HttpResponseを返す)
                return HttpResponse('無効なヘッダが検出されました。')
            
            # メールの送信が成功した場合、特定のページにリダイレクト
            return redirect('thanks')
        
        # フォーム内容に不備があった場合空のフォーム画面に遷移し再度入力
        return render(request, 'contact.html', {
            'form':form
        })

class ThanksView(View):
    def get(self, request, *args, **kwargs):
            return render(request, 'thanks.html')














































