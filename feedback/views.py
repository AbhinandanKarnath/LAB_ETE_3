from django.shortcuts import render
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Successful submission (No database save needed)
            return render(request, 'feedback/thankyou.html', {'form': form})
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback_form.html', {'form': form})
