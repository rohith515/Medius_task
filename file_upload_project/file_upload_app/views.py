from django.shortcuts import render
import pandas as pd
from django.shortcuts import render
from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file) if file.name.endswith('.xlsx') else pd.read_csv(file)

            summary = data.groupby(['Cust State', 'DPD']).size().reset_index(name='Count')
            summary_html = summary.to_html(index=False)

            return render(request, 'file_upload_app.html', {'form': form, 'summary': summary_html})
    else:
        form = UploadFileForm()
    return render(request, 'file_upload_app.html', {'form': form})
