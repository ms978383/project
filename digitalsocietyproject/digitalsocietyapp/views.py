from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role == 'secretory':
            sid=Secretory.objects.get(user_id=uid)
            context={
                'uid':uid,
                'sid':sid
            }
        
            return render(request,'app/index.html',context)
        else:
            mid=Member.objects.get(user_id=uid)
            context={
                'uid':uid,
                'mid':mid,
            }
            return render(request,'app/index.html',context)
    else:
        return redirect('login')

def login(request):
    if "email" in request.session:
        return redirect('home')
    else:
        
        if request.POST:
            email=request.POST['emailname']
            password=request.POST['passwordname']
            
            uid=User.objects.get(email=email)
            print("-----------",uid.email)
            if uid.password==password:
                if uid.role == 'secretory':
                    sid=Secretory.objects.get(user_id=uid)
                    print("-----------------",sid.contact)
                    print("-------------login button clicked")
                    request.session['email']=uid.email
                    return redirect('home')
                
                else:
                    mid=Member.objects.get(user_id=uid)
                    print("------",mid.username)
                    request.session['email']=uid.email
                    return redirect('home')
            else:
                wrong_alert="invalid password"
                context={
                    'wrong_alert':wrong_alert
                }
                print("---------------------wrong password")
                return render(request,'app/login.html',context)
                
        else:
            print("----------refreshed ")
            return render(request,'app/login.html')
def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return redirect('login')
    else:
        return redirect('login')
    
def profile(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role == 'secretory':
            
            sid=Secretory.objects.get(user_id=uid)
            context={
                'uid':uid,
                'sid':sid,
            }
        
            return render(request,'app/profile.html',context)
        else:
            mid=Member.objects.get(user_id=uid)
            context={
                'uid':uid,
                'mid':mid
            }
            return render(request,'app/profile.html',context)
    else:
        return redirect('login')
def user_pic_change(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role == 'secretory':
            sid=Secretory.objects.get(user_id=uid)
            if request.POST:
                if 'pic' in request.FILES:
                    pic=request.FILES['pic']
                    sid.pic=pic
                    sid.save()
                
                return redirect('profile')
        else:
            mid=Member.objects.get(user_id=uid)
            if request.POST:
                if 'pic' in request.FILES:
                    pic=request.FILES['pic']
                    mid.pic=pic
                    mid.save()
                
                return redirect('profile')
def password_change(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role == 'secretory':
            sid=Secretory.objects.get(user_id=uid)
            if request.POST:
                currentpassword=request.POST['currentpassword']
                newpassword=request.POST['newpassword']
                
                if uid.password == currentpassword:
                    uid.password=newpassword
                    uid.save()
                    
                    return redirect('logout')
            else:
                return redirect('profile')
        else:
            mid=Member.objects.get(user_id=uid)
            if request.POST:
                currentpassword=request.POST['currentpassword']
                newpassword=request.POST['newpassword']
                
                if uid.password == currentpassword:
                    uid.password=newpassword
                    uid.save()
                    
                    return redirect('logout')
            else:
                return redirect('profile')
            
def user_details_change(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        sid=Secretory.objects.get(user_id=uid)
        if request.POST:
            flat=request.POST['housenum']
            currentusername=request.POST['currentuser']
            username=request.POST['username']
            contact=request.POST['mobilenum']
            address=request.POST['address']
            
            if sid.username == currentusername:
                sid.flat_No=flat
                sid.username=username
                sid.contact=contact
                sid.society_address=address
                sid.save()
                print("-----------if part")
                return redirect('profile')
        else:
            print("-----> else part")
            return redirect('home')

def add_society_member(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        sid=Secretory.objects.get(user_id=uid)
        
        if request.POST:
            User.objects.create(
                email=request.POST['emailname'],
                role=request.POST['rolename'],
                password=request.POST['secu']
            )
            
            mid=Member.objects.create(
                user_id=request.POST['reuserid'],
                flat_No=request.POST['flatnum'],
                username=request.POST['membername'],
                contact=request.POST['mobilenum'],
                society_address=request.POST['address'],
                pic=request.FILES['memberp']
            )
            
            if mid:
                a_msg="Member Add Successfully"
                
                context={
                    'uid':uid,
                    'sid':sid,
                    'a_msg':a_msg
                }
                return render(request,'app/add-member.html',context)
        
        else:
            context={
                'uid':uid,
                'sid':sid
            }
            return render(request,'app/add-member.html',context)  
def all_society_member(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role == 'secretory':
            
            sid=Secretory.objects.get(user_id=uid)
            mid=Member.objects.all()
            context={
                'uid':uid,
                'sid':sid,
                'mid':mid
            }
            return render(request,'app/all-member.html',context)
        else:
            
            
            mid=Member.objects.all()
            
            context={
                'uid':uid,
                
                'mid':mid
            }
            print(uid,"member")
            print(mid,"member")
            return render(request,'app/all-member.html',context)
def edit_member(request,id):
    print("----------------------->",id)
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        sid=Secretory.objects.get(user_id=uid)
        mid=Member.objects.get(pk=id)
        mall=Member.objects.filter(user_id=uid)
        context={
            'uid':uid,
            'sid':sid,
            'mid':mid,
            'mall':mall
        }
        return render(request,'app/update-member.html',context)

def update_member(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        sid=Secretory.objects.get(user_id=uid)
        mall=Member.objects.filter(user_id=uid)
        
        if request.POST:
            mid=Member.objects.get(id=request.POST['memberid'])
            mid.flat_No=request.POST['flatnum']
            mid.username=request.POST['membername']
            mid.contact=request.POST['mobilenum']
            mid.society_address=request.POST['address']
            
            
            if "pic" in request.FILES:
                mid.pic=request.FILES['pic']
            mid.save()
        
        return redirect('all-society-member')

    else:
        return redirect('home')

def add_notice(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        sid=Secretory.objects.get(user_id=uid)
        
        if request.POST:
            nid=Notice.objects.create(
            user_id=sid,
            notice_of_title=request.POST['title'],
            notice_desc=request.POST['desc'],
            created_by=request.POST['createby'],
            pic=request.FILES['pic']
            )
            if nid:
                a_msg="Notice Add Successfully"
                
                context={
                    'uid':uid,
                    'sid':sid,
                    'a_msg':a_msg
                }
                return render(request,'app/add-notice.html',context)
        
        else:
            context={
                'uid':uid,
                'sid':sid
            }
            return render(request,'app/add-notice.html',context)

def all_society_notice(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role =='secretory':
            
            sid=Secretory.objects.get(user_id=uid)
            nid=Notice.objects.all()
            context={
                'uid':uid,
                'sid':sid,
                'nid':nid
            }
            return render(request,'app/all-notice.html',context)
        else:
            mid=Member.objects.get(user_id=uid)
            nid=Notice.objects.all()
            context={
                'uid':uid,
                'mid':mid,
                'nid':nid
            }
            print(mid.pic.url,"notice")
            return render(request,'app/all-notice.html',context)
def edit_notice(request,id):
    print("----------------------->",id)
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        sid=Secretory.objects.get(user_id=uid)
        nid=Notice.objects.get(pk=id)
        nall=Notice.objects.filter(user_id=sid)
        context={
            'uid':uid,
            'sid':sid,
            'nid':nid,
            'nall':nall
        }
        return render(request,'app/update-notice.html',context)

def update_notice(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        sid=Secretory.objects.get(user_id=uid)
        nall=Notice.objects.filter(user_id=sid)
        
        if request.POST:
            nid=Notice.objects.get(id=request.POST['noticeid'])
            nid.notice_of_title=request.POST['title']
            nid.notice_desc=request.POST['desc']
            nid.created_by=request.POST['createby']
            nid.updated_at=request.POST['updateat']
            
            
            if "pic" in request.FILES:
                nid.pic=request.FILES['pic']
            nid.save()
        
        return redirect('all-society-notice')

    else:
        return redirect('home')

def add_event(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        sid=Secretory.objects.get(user_id=uid)
        
        if request.POST:
            eid=Event.objects.create(
            user_id=sid,
            event_of_title=request.POST['title'],
            event_desc=request.POST['desc'],
            created_by=request.POST['createby'],
            pic=request.FILES['pic']
            )
            if eid:
                a_msg="Notice Add Successfully"
                
                context={
                    'uid':uid,
                    'sid':sid,
                    'a_msg':a_msg
                }
                return render(request,'app/add-event.html',context)
        
        else:
            context={
                'uid':uid,
                'sid':sid
            }
            return render(request,'app/add-event.html',context)

def all_society_event(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role == 'secretory':
            
            sid=Secretory.objects.get(user_id=uid)
            eid=Event.objects.all()
            context={
                'uid':uid,
                'sid':sid,
                'eid':eid
            }
            return render(request,'app/all-event.html',context)
        else:
            mid=Member.objects.get(user_id=uid)
            eid=Event.objects.all()
            context={
                'uid':uid,
                'mid':mid,
                'eid':eid
            }
            return render(request,'app/all-event.html',context)

def edit_event(request,id):
    print("----------------------->",id)
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        sid=Secretory.objects.get(user_id=uid)
        eid=Event.objects.get(pk=id)
        eall=Event.objects.filter(user_id=sid)
        context={
            'uid':uid,
            'sid':sid,
            'eid':eid,
            'eall':eall
        }
        return render(request,'app/update-event.html',context)

def update_event(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        sid=Secretory.objects.get(user_id=uid)
        eall=Event.objects.filter(user_id=sid)
        
        if request.POST:
            eid=Event.objects.get(id=request.POST['eventid'])
            eid.event_of_title=request.POST['title']
            eid.event_desc=request.POST['desc']
            eid.created_by=request.POST['createby']
            eid.updated_at=request.POST['updateat']
            
            
            if "pic" in request.FILES:
                eid.pic=request.FILES['pic']
            eid.save()
        
        return redirect('all-society-event')

    else:
        return redirect('home')
    
def delete_member(request,id):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        sid=Secretory.objects.get(user_id=uid)
        mall=Member.objects.filter(user_id=uid)
        
        mid=Member.objects.get(pk=id)
        mid.delete()
        
         
    return redirect('all-society-member')

def delete_notice(request,id):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        sid=Secretory.objects.get(user_id=uid)
        nall=Notice.objects.filter(user_id=sid)
        
        nid=Notice.objects.get(pk=id)
        nid.delete()
        
         
    return redirect('all-society-notice')

def delete_event(request,id):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        sid=Secretory.objects.get(user_id=uid)
        eall=Event.objects.filter(user_id=sid)
        
        eid=Event.objects.get(pk=id)
        eid.delete()
        
         
    return redirect('all-society-event')
    
def register(request):
    if request.POST:
        subject=request.POST['title']
        membername=request.POST['societymembername']
        memberemail=request.POST['emailname']
        wordpass=request.POST['sec']
        memberflatnum=request.POST['apartment']
        membermobilenum=request.POST['connection']
        
        data={
            'subject':subject,
            'membername':membername,
            'memberemail':memberemail,
            'wordpass':wordpass,
            'memberflatnum':memberflatnum,
            'membermobilenum':membermobilenum
        }
        print(data)
        
        message = '''
        subject : {}
        
        New Member Name: {}
        
        Password: {}
        
        Member Flat number: {}
        
        Member Mobile Number: {}
        
        From: {}
        '''.format(data['subject'],data['membername'],data['wordpass'],data['memberflatnum'],data['membermobilenum'],data['memberemail'])
        send_mail(data['subject'],message, '', ['smaheshparmar3026@gmail.com'])
        
        
        
        
        return render(request,'app/register.html',{})
    else:
        print("else")
        return render(request,'app/register.html')
def all_user_id_password(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
            
        sid=Secretory.objects.get(user_id=uid)
        uall=User.objects.all()
        context={
            'uid':uid,
            'sid':sid,
            'uall':uall,
                
        }
            
        
    return render(request,'app/user-id-password.html',context)

def forgot_password(request):
    if request.POST:
        subject=request.POST['forgottitle']
        emailforgot=request.POST['emailfor']
        
        forgot={
            'subject':subject,
            'emailforgot':emailforgot,
            
        }
        print(forgot)
        message = '''
        subject : {}
        
        forgot password Email Address : {}
        
        
        '''.format(forgot['subject'],forgot['emailforgot'])
        send_mail(forgot['subject'],message, '', ['smaheshparmar3026@gmail.com'])
        
        for_mas="Secretory send password in 10 minutes to Email Address"
        context={
            'for_mas':for_mas,
        }
        return render(request,'app/forgot-password.html',context)
    else:
        return render(request,'app/forgot-password.html')

   
   