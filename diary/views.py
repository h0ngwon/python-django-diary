from django.shortcuts import render,get_object_or_404,redirect
from .models import Diary
from .forms import DiaryForm

#제목 리스트
def index(request):
    diary_list = Diary.objects.all()
    context = {'diary_list':diary_list}
    return render(request,'diary/index.html',context)

#내용 상세 페이지
def detail(request,diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)
    return render(request,'diary/detail.html',{'diary':diary})

#새로운 글 등록
def create(request):
    if request.method =='POST':
        form = DiaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else :
        form = DiaryForm()
        return render(request,'diary/create.html',{'form':form})

#글 수정
def update(request,diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)

    if request.method=='POST':
        form = DiaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detail',diary_id)
    else:
        form = DiaryForm()
        return render(request,'diary/update.html',{'form':form})
#글 삭제
def delete(request,diary_id):
    diary = Diary.objects.get(pk=diary_id)
    diary.delete()
    return redirect('index')