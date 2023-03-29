from django.shortcuts import render, redirect
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 
from email.mime.base import MIMEBase
from email import encoders
from indexapp import models
from .models import ProductModel
from django.contrib.auth.models import User
from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from .filters import ProductModelFilter
from indexapp.forms import PostForm


def login(request):
	if request.method == 'POST':
		name = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=name, password=password)
		if user is not None:
			if user.is_active:
				auth.login(request,user)
				message = '登入成功！'
				return redirect('/index/')
			else:
				message = '帳號尚未啟用！'
		else:
			message = '登入失敗！!'
	return render(request, "login.html", locals())
	
def logout(request):
	auth.logout(request)
	return redirect('/index/')

def adduser(request):
	if request.method == 'POST':
		name = request.POST['username']
		password = request.POST['password']
		repassword = request.POST['repassword']
		e_mail = request.POST['e-mail']
		try:
			user=User.objects.get(username=name)
		except:
			user=None
		if user!=None:
			message = user.username + " 帳號已建立!"
			# return HttpResponse(message)
		elif name=='' or password=='' or repassword=='' or e_mail=='':
			message = '尚未填滿!!'
		elif password != repassword:
			message = '兩次密碼輸入未相同'
		else:	# 建立 test 帳號			
			user=User.objects.create_user(name,e_mail,password)
			user.is_staff=False	# 工作人員狀態
			user.save()
			# strSmtp = "smtp.gmail.com:587"
			# # strAccount = "" # 帳號
			# # strPD = "" # 密碼
			# content = "<h2>註冊資料 請妥善保存 不補發</h2><p>使用者名稱 : </p>"+name+"<p>使用者密碼 : </p>"+password
			# msg = MIMEText(content, "html")
			# msg["Subject"] = "歡迎"+name+"加入會員~~會員資料通知"
			# server = SMTP(strSmtp)
			# server.ehlo()
			# server.starttls()
			# try:
			# 	server.login(strAccount, strPD)
			# 	server.sendmail(strAccount, e_mail, msg.as_string())
			# 	usermailhint = "註冊已成功，郵件已發送！"
			# except SMTPAuthenticationError:
			# 	usermailhint = "無法登入！"
			# except:
			# 	usermailhint = "郵件發送產生錯誤！"
			# server.quit()
			return redirect('/index/')
	return render(request, "create.html", locals())

def index(request):
	if request.user.is_authenticated:
		name=request.user.username
	productall = models.ProductModel.objects.all().filter(enabled=True)  #取得資料庫所有商品
	Featured_productall = models.ProductModel.objects.all().filter(catego="精選").filter(enabled=True)
	New_productall = models.ProductModel.objects.all().filter(catego="最新").filter(enabled=True)
	indexAddr = 'http://127.0.0.1:8000/index/'
	context = {
		'productall': productall,
	}
	if request.method == "POST":
		e_mail = request.POST['e-mail']
		strSmtp = "smtp.gmail.com:587"
		strAccount = "90818126@gcloud.csu.edu.tw"
		strPD = ""
		content = f' <h2>My note賣noee最新訊息!!!</h2><p>感謝您瀏覽本網站，本網站收錄眾多筆記，日後最新消息將會傳送e-mail到您信箱，請記得查收!!!</p><br>' \
					  f'<p>網站連結:{indexAddr}</p>'
		msg = MIMEText(content, "html")
		msg["Subject"] = "My note賣noee最新訊息!!!"
		server = SMTP(strSmtp)
		server.ehlo()
		server.starttls()
		try:
			server.login(strAccount, strPD)
			server.sendmail(strAccount, e_mail, msg.as_string())
			mailhint = "郵件已發送！"
		except SMTPAuthenticationError:
			mailhint = "無法登入！"
		except:
			mailhint = "郵件發送產生錯誤！"
		server.quit()

	return render(request, "index.html", locals())

def search(request):
	if request.user.is_authenticated:
		name=request.user.username
	productall = models.ProductModel.objects.all().filter(enabled=True)  #取得資料庫所有商品
	productModelFilter = ProductModelFilter(queryset=productall)
	if request.method == "POST":
		productModelFilter = ProductModelFilter(request.POST, queryset=productall)
		context = {
		'productModelFilter': productModelFilter
		}
	return render(request, "search.html", locals())

def All(request):
	if request.user.is_authenticated:
		name=request.user.username
	productall = models.ProductModel.objects.all().filter(enabled=True) #取得資料庫商品
	return render(request, "All.html", locals())

def Hot(request):
	if request.user.is_authenticated:
		name=request.user.username
	productall = models.ProductModel.objects.all().order_by('-press') #取得資料庫商品
	return render(request, "Hot.html", locals())

def Featured(request):
	if request.user.is_authenticated:
		name=request.user.username
	productall = models.ProductModel.objects.all().filter(catego="精選").filter(enabled=True)  #取得資料庫商品
	return render(request, "Featured.html", locals())

def New(request):
	if request.user.is_authenticated:
		name=request.user.username
	productall = models.ProductModel.objects.all().filter(catego="最新").filter(enabled=True).order_by('-id')  #取得資料庫商品
	return render(request, "New.html", locals())

def addnew(request):
	if request.user.is_authenticated:
		name=request.user.username
	productall = models.ProductModel.objects.all()
	form = PostForm()
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			request.POST._mutable = True
			name = form.save(commit = False)
			name.pcreatepeople = request.user.username
			name.pcreatepeople_email = request.user.email
			name.save()
			form.save()
			return redirect('/index/')
	context = {
		'productall': productall,
		'form': form,
	}
	return render(request, "addnew.html", locals())	

def delete(request, editid=None, deletetype=None):  #刪除資料
	if request.user.is_authenticated:
		name=request.user.username
	unit = models.ProductModel.objects.get(id = editid)
	if deletetype == None:  #進入刪除頁面,顯示原有資料
		name = unit.pname
		author = unit.pauthor
		price = unit.pprice
		special_price = unit.special_offer
		images = unit.pimages
		description = unit.pdescription
		Simple_description = unit.Simple_pdescription
		author_introduce = unit.pauthor_introduce
		data = unit.pdata
		pcreatepeople = unit.pcreatepeople
	elif deletetype == '1':  #按刪除鈕
		unit.delete()
		return redirect('/index/')
	return render(request, "delete.html", locals())
from datetime import datetime
def detail(request, productid=None):  #商品詳細頁面
	if request.user.is_authenticated:
		name=request.user.username
	product = models.ProductModel.objects.get(id=productid)  #取得商品
	product.press += 1
	product.save()
	if request.method == "POST":
		indexAddr = 'http://127.0.0.1:8000/authAccess/'
		book = product.pname
		price =  product.pprice
		price_amount = round(product.pprice * 0.8)
		e_mail = product.pcreatepeople_email
		content = f' <h2>My note賣noee最新訊息!!!</h2><p>恭喜!有人購買你的筆記\"{book}\"!</p><br><p>商品出售價格為' \
					  f':{price}</p><p>扣除平台費用後收益為:{price_amount}</p><p>授權連結:{indexAddr}</p>'
		try:
			SendMail.auth(e_mail, content)
			authorized = models.authorized.objects.create(
					field_mail = request.user.email,
					pprice= product.pprice,
					pname=product.pname,
					status= False,
					pcreatepeople= product.pcreatepeople,
					price_amount= price_amount,
					buyname = request.user.username,
					File = product.uploadedFile,
				)
		except SMTPAuthenticationError:
			mailhint = "無法登入！"
		except:
			mailhint = "郵件發送產生錯誤！"

	return render(request, "detail.html", locals())

from django.shortcuts import render
from .forms import UploadModelForm

from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
def edit(request , id):
	if request.user.is_authenticated:
		name=request.user.username
	product = models.ProductModel.objects.get(id=id)  #取得商品
	context = {}
	form = PostForm(request.POST or None, request.FILES  or None, instance=product)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/index/" )
	context["form"] = form
	return render(request, "edit.html", context)

def userdetail(request):
	if request.user.is_authenticated:
		name=request.user.username
	if request.method == 'POST':
		password = request.POST['password']
		if len(password) >= 8:
			u = User.objects.get(username=name)
			u.set_password(password)
			u.save()
			message = "密碼變更成功，請重新登入"
		else:
			message = "密碼格式錯誤，須大於8位數"
	return render(request, "userdetail.html", locals())

def authAccess(request):
	if request.user.is_authenticated :
		name = request.user.username
		access = models.authorized.objects.all().filter(pcreatepeople=name).order_by('status','-mod_date')
		buytotal = 0
		realtotal = 0
		for access_num in access:
			buytotal = buytotal + access_num.price_amount
			if access_num.status:
				realtotal = realtotal + access_num.price_amount
		
	return render(request, "authAccess.html", locals())

def downloadpage(request):
	if request.user.is_authenticated :
		name = request.user.username
		access = models.authorized.objects.all().filter(buyname=name).order_by('status','-mod_date')
		buytotal = 0
		realtotal = 0
		for access_num in access:
			buytotal = buytotal + access_num.pprice
			if access_num.status:
				realtotal = realtotal + access_num.pprice

	return render(request, "downloadpage.html", locals())


def check_ok(request, productid=None):
	if request.user.is_authenticated:
		name=request.user.username
		product = models.authorized.objects.get(id=productid)  #取得商品
		product.status = True
		product.save()
		indexAddr = 'http://127.0.0.1:8000/downloadpage/'
		e_mail = product.field_mail
		content = f' <h2>My note賣noee最新訊息!!!</h2><p>您所購買商品\"{product.pname}\"，已可供下載閱覽，請查閱!</p><br><p>商品買入價格為' \
					  f':{product.pprice}</p><p>下載連結:{indexAddr}</p>'
		try:
			SendMail.buyUser(e_mail, content)
		except SMTPAuthenticationError:
			mailhint = "無法登入！"
		except:
			mailhint = "郵件發送產生錯誤！"
		return redirect('/authAccess/')

	return render(request, "check_ok.html", locals())

def test(request):

	return render(request, "test.html", locals())

class SendMail:
	def auth(e_mail, content):
			strSmtp = "smtp.gmail.com:587"
			strAccount = "90818126@gcloud.csu.edu.tw"
			strPD = ""
			msg = MIMEText(content, "html")
			msg["Subject"] = "被購入通知，請進行授權。"
			# mailto = e_mail  #收件者
			#mailto = ["收件者電子郵件"]  #收件者
			#mailto = ["收件者電子郵件一", "收件者電子郵件二"]
			server = SMTP(strSmtp)
			server.ehlo()
			server.starttls()
			try:
				server.login(strAccount, strPD)
				server.sendmail(strAccount, e_mail, msg.as_string())
				mailhint = "郵件已發送！"
			except SMTPAuthenticationError:
				mailhint = "無法登入！"
			except:
				mailhint = "郵件發送產生錯誤！"
			server.quit()

	def buyUser(e_mail, content):
			strSmtp = "smtp.gmail.com:587"
			strAccount = "90818126@gcloud.csu.edu.tw"
			strPD = ""
			msg = MIMEText(content, "html")
			msg["Subject"] = "被授權通知，請進行查閱。"
			# mailto = e_mail  #收件者
			#mailto = ["收件者電子郵件"]  #收件者
			#mailto = ["收件者電子郵件一", "收件者電子郵件二"]
			server = SMTP(strSmtp)
			server.ehlo()
			server.starttls()
			try:
				server.login(strAccount, strPD)
				server.sendmail(strAccount, e_mail, msg.as_string())
				mailhint = "郵件已發送！"
			except SMTPAuthenticationError:
				mailhint = "無法登入！"
			except:
				mailhint = "郵件發送產生錯誤！"
			server.quit()
			