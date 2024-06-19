from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth import logout

def page(request):
    return render(request, 'index.html')


def list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweets_ok.html', {'tweets' : tweets})

@login_required
def create(request):
   if request.method == 'POST':
       form = Tweetform(request.POST, request.FILES)
       if form.is_valid():
           tweet = form.save(commit=False)
           tweet.user = request.user
           tweet.save()
           return redirect('tweet_list')
   else:
       form = Tweetform()
       return render(request, 'tweet_form.html', {'form' : form})
   

   
@login_required
def edit(request, tweet_id):
  tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
  if request.method == 'POST':
    form = Tweetform(request.POST, request.FILES, instance=tweet)
    if form.is_valid():
      tweet = form.save(commit=False)
      tweet.user = request.user
      tweet.save()
      return redirect('tweet_list')
  else:
    form = Tweetform(instance=tweet)
  return render(request, 'tweet_form.html', {'form': form})
 

@login_required
def delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk = tweet_id, user = request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_del.html', {'tweet' : tweet})

@login_required
def logout_view(request):
    logout(request)
    return redirect('tweet_list')


def register(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.set_password(form.cleaned_data['password1'])
      user.save()
      login(request, user)
      return redirect('tweet_list')
  else:
    form = UserRegistrationForm()

  return render(request, 'registration/register.html', {'form': form})

def login2(request):
  if request.method == 'POST':
    form = UserLoginForm(data = request.POST)
    if form.is_valid():
       username = form.cleaned_data.get('username')
       password = form.cleaned_data.get('password')
       user = authenticate(request, username=username, password=password)
       if user is not None:
            login(request, user)
            return redirect('tweet_list')  
       else:
            messages.error(request, 'Invalid username or password.')
       
    
  else:
     form = UserLoginForm()

  return render(request, 'registration/login.html', {'form': form})
       

@login_required
def post_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('question')
    else:
        form = QuestionForm()
    return render(request, 'post_question.html', {'form': form})

@login_required
def reply_to_question(request, id):
    question = get_object_or_404(Question, id=id)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user
            reply.question = question
            reply.save()
            return redirect('question')
    else:
        form = ReplyForm()
    return render(request, 'reply_to_question.html', {'form': form, 'question': question})
       

def question_detail(request, id):
    question = get_object_or_404(Question, id=id)
    replies = question.replies.all()
    return render(request, 'question_detail.html', {'question': question, 'replies': replies})


def listi(request):
    ques = Question.objects.all().order_by('-created_at')
    replies = Reply.objects.all().order_by('-created_at')
    return render(request, 'questions.html', {'ques' : ques, 'reps' : replies})


@login_required
def deleteques(request, id):
    que = get_object_or_404(Question, pk = id, user = request.user)
    if request.method == "POST":
        que.delete()
        return redirect('question')
    return render(request, 'questions.html', {'que' : que})

@login_required
def deleterep(request, id):
    que = get_object_or_404(Reply, pk = id, user = request.user)
    if request.method == "POST":
        que.delete()
        return redirect('question')
    return render(request, 'questions.html', {'que' : que})
