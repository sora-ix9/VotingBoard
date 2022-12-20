from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def home(request):
	if request.method == 'POST':
		if request.user.is_authenticated:
			boardTitle = ''
				
			for char in request.POST['vote']:
				if char != '_':
					boardTitle += char
				elif char == '_':
					break
				
			board = Post.objects.get(title=boardTitle)
			if request.POST['vote'] == boardTitle+'_agree':
				board.agreeable_num += 1
				board.save()
				#print("success agreeable_num increment")
			elif request.POST['vote'] == boardTitle+'_disagree':
				board.disagreeable_num += 1	
				board.save()
		else:
			return redirect('login')

	return render(request, 'board/home.html', {'posts': Post.objects.all()})