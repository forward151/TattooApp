from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm, DataForm
from django.conf import settings
import os
form = None
img_obj = None

class Img:
    def __init__(self, url):
        self.url = url

    class image:
        def __init__(self, url):
            self.url = url


def get_image(path):
    if 'darknet.exe' not in os.listdir():
        os.chdir('..')
        os.chdir('..')

        os.chdir('PROJECT')
        os.chdir('darknet')
        os.chdir('build')
        os.chdir('darknet')
        os.chdir('x64')
    os.system("darknet.exe detector test data/obj.data obj.cfg obj_10000.weights "
              f"{path} -dont_show")
    os.system(f"copy predictions.jpg {settings.BASE_DIR}\\media\\images\\")
    print('КАРТИНКА СКОПИРОВАНА')


def main_page(request):
    return render(request, 'index.html')

def image_upload_view(request):
    global img_obj, form
    if request.method == 'POST':
        if "upload" in request.POST:
            form = ImageForm(request.POST, request.FILES)
            form2 = DataForm()
            if form.is_valid():
                form.save()
                img_obj = form.instance
                print(f"Получена картинка по пути {settings.BASE_DIR}\\media\\{img_obj.image}")
                print(img_obj.image)
                return render(request, 'index.html', {'form': form, 'form2': form2, 'img_obj': img_obj})
        elif "process" in request.POST:
            # try:
                form = ImageForm()
                form2 = DataForm(request.POST, request.FILES)
                form2.image_name = img_obj.image
                form2.save()
                print("ОБРАБОТКА")
                print(f"Обработка картинки по пути {settings.BASE_DIR}\\media\\{img_obj.image}")
                print(f'{settings.BASE_DIR}\\media\\{img_obj.image}')
                get_image(f'{settings.BASE_DIR}\\media\\{img_obj.image}')
                os.remove(f"{settings.BASE_DIR}\\media\\{img_obj.image}")
                form.instance.image = 'images\\predictions.jpg'
                img_obj = form.instance
                return render(request, 'index.html', {'form': form, 'form2': form2, 'img_obj': img_obj})
            # except:
            #     return render(request, 'index.html', {'form': form})
    else:
        form = ImageForm()
        form2 = DataForm()
        return render(request, 'index.html', {'form1': form, 'form2': form2})





