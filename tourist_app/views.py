import requests
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, redirect
from .serializer import TouristSerializers
from .models import *
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .form import *
import requests
from django.contrib import messages


# Create your views here.


class DestinationCreateView(generics.ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = TouristSerializers
    permission_classes = [AllowAny]


class DestinationDetail(generics.RetrieveAPIView):
    queryset = Destination.objects.all()
    serializer_class = TouristSerializers


class DestinationUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Destination.objects.all()
    serializer_class = TouristSerializers


class DestinationDelete(generics.DestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = TouristSerializers


class DestinationSearch(generics.ListAPIView):
    queryset = Destination.objects.all()
    serializer_class = TouristSerializers

    def get_queryset(self):
        name = self.kwargs.get('Name')
        return Destination.objects.filter(Name__icontains=name)


def create_dest(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Attempt to save the form
                destination = form.save()
                api_url = 'http://127.0.0.1:8000/create/'
                data = form.cleaned_data

                # Prepare files for the request
                files = {'img': request.FILES['img']}

                # Perform the API request
                response = requests.post(api_url, data=data, files=files)

                if response.status_code == 200:
                    messages.success(request, 'Destination Successfully Inserted')
                    return redirect(request, '/')
                else:
                    messages.error(request, f'Error {response.status_code}: {response.text}')
            except requests.RequestException as e:
                messages.error(request, f'Error during API request: {str(e)}')
            except Exception as e:
                messages.error(request, f'Error saving form: {str(e)}')
        else:
            messages.error(request, 'Invalid Form')
    else:
        form = DestinationForm()

    return render(request, 'createDestination.html', {'form': form})


def update_detail(request, id):
    api_url = f'http://127.0.0.1:8000/detail/{id}/'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()

        return render(request, 'updateDestination.html', {'dest': data})
    return render(request, 'updateDestination.html', {'error': 'Could not fetch data.'})


# def update_dest(request, id):
#     if request == 'POST':
#         name = request.POST['Name']
#         weather = request.POST['Weather']
#         state = request.POST['state']
#         dist = request.POST['dist']
#         map = request.POST['map']
#         print('Image url', request.FILES.get('img'))
#         desc = request.POST['desc']
#
#         api_url = f'http://127.0.0.1:8000/update/{id}/'
#
#         data = {
#             'Name': name,
#             'Weather': weather,
#             'state': state,
#             'dist': dist,
#             'map': map,
#             'desc': desc
#         }
#
#         files = {'img': request.FILES.get('img')}
#
#         response = requests.put(api_url, data=data, files=files)
#
#         if response.status_code == 200:
#             messages.success(request, 'Updated')
#             return redirect('/')
#         else:
#             messages.error(request, f'Error submitting data to the REST API:{response.status_code}')
#
#     return render(request, 'updateDestination.html')

def update_dest(request,id):
    if request.method == 'POST':
        Name = request.POST['Name']
        Weather = request.POST['Weather']
        state = request.POST['state']
        dist = request.POST['dist']
        map = request.POST['map']

        print('Image url',request.FILES.get('img'))
        desc= request.POST['desc']

        api_url = f'http://127.0.0.1:8000/update/{id}/'

        data = {'Name':Name,
                'Weather':Weather,
                'state':state,
                'dist': dist,
                'map': map,
                'desc':desc
                }
        files = {'img':request.FILES.get('img')}
        messages.success(request, files)

        response = requests.put(api_url, data=data, files=files)
        if response.status_code == 200:
            messages.success(request,'Destination updated successfully')
            return redirect('/')
        else:
            messages.error(request,f'Error submitting data to the API : {response.status_code}')

    return render(request,'updateDestination.html')
def Index(request):
    if request.method == 'POST':
        search = request.POST.get('search','')
        api_url = f'http://127.0.0.1:8000/search/{search}/'

        try:
            response = requests.get(api_url)

            print(response.status_code)

            if response.status_code == 200:
                data = response.json()
            else:
                data = None

        except requests.RequestException as e:
            data = None

        return render(request, 'index.html', {'data': data})

    else:
        api_url = f'http://127.0.0.1:8000/create/'
        try:
            response = requests.get(api_url)

            if response.status_code == 200:
                data = response.json()
                original_data = data

                paginator = Paginator(original_data, 6)

                try:
                    page = int(request.GET.get('page', 1))

                except:
                    page = 1

                try:
                    destination = paginator.page(page)

                except(EmptyPage, InvalidPage):
                    destination = Paginator.page(Paginator.num_pages)

                context = {
                    'original_data': original_data,
                    'destination': destination
                }

                return render(request, 'index.html', context=context)
            else:
                return render(request, 'index.html', {'error_message': f'Error:{response.status_code}'})

        except requests.RequestException as e:
            return render(request, 'index.html', {'error_message': f'Error:{str(e)}'})

    return render(request, 'index.html')


def fetch_dest(request, id):
    api_url = f'http://127.0.0.1:8000/detail/{id}'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        incrediants = data['desc'].split('.')
        return render(request, 'fetchDestination.html', {'dest': data, 'incrediants': incrediants})
    return render(request, 'fetchDestination.html')


def delete_dest(request, id):
    api_url = f'http://127.0.0.1:8000/delete/{id}'
    response = requests.delete(api_url)

    if response.status_code == 200:
        print(f'Item with id {id} has benn deleted')
    else:
        print(f'Failed to delete item {response.status_code}')

    return redirect('/')


def delete_confirm(request,id):
    return render(request,'deleteDestination.html',{'id':id})