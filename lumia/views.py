from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('explore')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def explore_view(request):
    return render(request, 'explore.html')

def mapa(request):
    return render(request, 'mapa.html')

def parques_view(request):
    return render(request, 'parques.html')

@login_required
def metodos_pago(request):
    return render(request, "metodospago.html")

@login_required
def reservaciones(request):
    return render(request, "reservaciones.html")

@login_required
def configuracion(request):
    return render(request, "configuracion.html")

@login_required
def perfil(request):
    #reservaciones = request.user.reservaciones.all()  # ajusta al nombre de tu relación
    #return render(request, "perfil.html", {"reservaciones": reservaciones})
    return render(request, "perfil.html")

def park_detail_view(request, park_name):

    parks = {

        'chalco': {
            'name': 'Parque Chalco',
            'description': 'Excelente opción para grupos grandes con cabañas equipadas y vistas panorámicas del bosque.',
            'images': [
                '/static/img/chalco.webp',
                '/static/img/chalco.webp',
                '/static/img/chalco.webp',
            ],
            'address': 'Chalco, Estado de México',
            'rating': '4.8',
            'review_count': 124,
            'amenities': [
                {'icon': 'cabin', 'name': 'Cabañas'},
                {'icon': 'restaurant', 'name': 'Restaurante'},
                {'icon': 'forest', 'name': 'Senderos'},
            ],
            'reviews': [
                {
                    'author': 'Carlos M.',
                    'date': 'Hace 2 semanas',
                    'text': 'Experiencia increíble para ver luciérnagas.',
                }
            ],
            'booking_options': [
                {'value': 'cabana', 'label': 'Cabaña'},
                {'value': 'camping', 'label': 'Camping'},
            ],
        },

        'texcoco': {
            'name': 'Parque Texcoco',
            'description': 'Ruta exclusiva limitada a 20 personas por noche para garantizar la preservación del ecosistema.',
            'images': [
                '/static/img/Texcoco.webp',
                '/static/img/Texcoco.webp',
                '/static/img/Texcoco.webp',
            ],
            'address': 'Texcoco, Estado de México',
            'rating': '4.9',
            'review_count': 90,
            'amenities': [
                {'icon': 'forest', 'name': 'Bosque'},
                {'icon': 'hiking', 'name': 'Caminatas'},
                {'icon': 'eco', 'name': 'Eco tour'},
            ],
            'reviews': [
                {
                    'author': 'Ana G.',
                    'date': 'Hace 1 semana',
                    'text': 'Muy bien organizado, el guía fue excelente.',
                }
            ],
            'booking_options': [
                {'value': 'sendero', 'label': 'Sendero guiado'},
            ],
        },

        'santuario-el-rosario': {
            'name': 'Santuario El Rosario',
            'description': 'El santuario más grande de la región, ofreciendo una experiencia inmersiva única con miles de mariposas monarca.',
            'images': [
                '/static/img/El-rosario.jpeg',
                '/static/img/El-rosario.jpeg',
                '/static/img/El-rosario.jpeg',
            ],
            'address': 'Ocampo, Michoacán',
            'rating': '4.9',
            'review_count': 312,
            'amenities': [
                {'icon': 'wifi', 'name': 'WiFi'},
                {'icon': 'local_parking', 'name': 'Estacionamiento'},
                {'icon': 'restaurant', 'name': 'Restaurante'},
            ],
            'reviews': [
                {
                    'author': 'María L.',
                    'date': 'Hace 3 días',
                    'text': 'Ver las mariposas monarca es algo que no olvidarás jamás.',
                }
            ],
            'booking_options': [
                {'value': 'camping', 'label': 'Camping'},
                {'value': 'sendero', 'label': 'Sendero guiado'},
            ],
        },

        'parque-chalma': {
            'name': 'Parque Ecoturístico Chalma',
            'description': 'Famoso por su densa vegetación y avistamientos garantizados en senderos perfectamente marcados.',
            'images': [
                '/static/img/chalma.webp',
                '/static/img/chalma.webp',
                '/static/img/chalma.webp',
            ],
            'address': 'Malinalco, Estado de México',
            'rating': '4.7',
            'review_count': 178,
            'amenities': [
                {'icon': 'wifi', 'name': 'WiFi'},
                {'icon': 'local_parking', 'name': 'Estacionamiento'},
                {'icon': 'cabin', 'name': 'Cabañas'},
            ],
            'reviews': [
                {
                    'author': 'Roberto S.',
                    'date': 'Hace 5 días',
                    'text': 'Los senderos están muy bien señalizados, ideal para familias.',
                }
            ],
            'booking_options': [
                {'value': 'sendero', 'label': 'Sendero guiado'},
                {'value': 'cabana', 'label': 'Cabaña'},
            ],
        },

        'piedra-canteada': {
            'name': 'Piedra Canteada',
            'description': 'Un paraíso rústico ideal para fotógrafos y quienes buscan desconexión total en la naturaleza.',
            'images': [
                '/static/img/piedra-canteada.jpg',
                '/static/img/piedra-canteada.jpg',
                '/static/img/piedra-canteada.jpg',
            ],
            'address': 'Tlaxco, Tlaxcala',
            'rating': '4.8',
            'review_count': 95,
            'amenities': [
                {'icon': 'local_parking', 'name': 'Estacionamiento'},
                {'icon': 'hiking', 'name': 'Senderismo'},
                {'icon': 'photo_camera', 'name': 'Fotografía'},
            ],
            'reviews': [
                {
                    'author': 'Sofía R.',
                    'date': 'Hace 1 semana',
                    'text': 'Lugar increíble para fotografía de paisaje, muy poco concurrido.',
                }
            ],
            'booking_options': [
                {'value': 'cabana', 'label': 'Cabaña'},
            ],
        },

        'parque-nacional-molino': {
            'name': 'Parque Nacional Molino de Flores',
            'description': 'Ambiente familiar con actividades educativas y zonas de picnic autorizadas para todos.',
            'images': [
                'https://images.unsplash.com/photo-1426604966848-d7adac402bff?w=600&q=80',
                'https://images.unsplash.com/photo-1426604966848-d7adac402bff?w=600&q=80',
                'https://images.unsplash.com/photo-1426604966848-d7adac402bff?w=600&q=80',
            ],
            'address': 'Texcoco, Estado de México',
            'rating': '4.5',
            'review_count': 210,
            'amenities': [
                {'icon': 'wifi', 'name': 'WiFi'},
                {'icon': 'local_parking', 'name': 'Estacionamiento'},
                {'icon': 'accessible', 'name': 'Accesible'},
            ],
            'reviews': [
                {
                    'author': 'Luis H.',
                    'date': 'Hace 2 semanas',
                    'text': 'Perfecto para ir con niños, hay actividades para toda la familia.',
                }
            ],
            'booking_options': [
                {'value': 'camping', 'label': 'Camping'},
                {'value': 'sendero', 'label': 'Sendero guiado'},
            ],
        },

        'rancho-del-valle': {
            'name': 'Rancho del Valle',
            'description': 'Cabañas familiares cerca de la orilla del lago con espacios para acampar y actividades acuáticas.',
            'images': [
                'https://images.unsplash.com/photo-1511497584788-876760111969?w=600&q=80',
                'https://images.unsplash.com/photo-1511497584788-876760111969?w=600&q=80',
                'https://images.unsplash.com/photo-1511497584788-876760111969?w=600&q=80',
            ],
            'address': 'Valle de Bravo, Estado de México',
            'rating': '4.8',
            'review_count': 143,
            'amenities': [
                {'icon': 'cabin', 'name': 'Cabañas'},
                {'icon': 'local_parking', 'name': 'Estacionamiento'},
                {'icon': 'restaurant', 'name': 'Restaurante'},
            ],
            'reviews': [
                {
                    'author': 'Paola T.',
                    'date': 'Hace 4 días',
                    'text': 'Las cabañas son acogedoras y la vista al lago es espectacular.',
                }
            ],
            'booking_options': [
                {'value': 'cabana', 'label': 'Cabaña'},
                {'value': 'camping', 'label': 'Camping'},
            ],
        },

    'bosque-esmeralda': {
        'name': 'Bosque Esmeralda',
        'description': 'Lugar privilegiado con acceso profundo al bosque virgen del festival.',
        'images': [
            'https://images.unsplash.com/photo-1448375240586-882707db888b?w=600&q=80',
            'https://images.unsplash.com/photo-1448375240586-882707db888b?w=600&q=80',
            'https://images.unsplash.com/photo-1448375240586-882707db888b?w=600&q=80',
        ],
        'address': 'Estado de México',
        'rating': '4.9',
        'review_count': 156,
        'amenities': [
            {'icon': 'camping', 'name': 'Camping'},
            {'icon': 'hiking', 'name': 'Senderismo'},
            {'icon': 'local_parking', 'name': 'Estacionamiento'},
        ],
        'reviews': [
            {
                'author': 'Valeria M.',
                'date': 'Hace 3 días',
                'text': 'Un lugar mágico, completamente desconectado del ruido de la ciudad.',
            }
        ],
        'booking_options': [
            {'value': 'camping', 'label': 'Camping'},
            {'value': 'sendero', 'label': 'Sendero guiado'},
        ],
    },

    'parque-central-amecameca': {
        'name': 'Parque Central Amecameca',
        'description': 'Zona tranquila ideal para entusiastas de la fotografía nocturna y observación de volcanes.',
        'images': [
            'https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=600&q=80',
            'https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=600&q=80',
            'https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=600&q=80',
        ],
        'address': 'Amecameca, Estado de México',
        'rating': '4.6',
        'review_count': 87,
        'amenities': [
            {'icon': 'cabin', 'name': 'Cabañas'},
            {'icon': 'wifi', 'name': 'WiFi'},
            {'icon': 'local_parking', 'name': 'Estacionamiento'},
        ],
        'reviews': [
            {
                'author': 'Diego F.',
                'date': 'Hace 1 semana',
                'text': 'La vista del Popocatépetl desde aquí es impresionante.',
            }
        ],
        'booking_options': [
            {'value': 'cabana', 'label': 'Cabaña'},
            {'value': 'camping', 'label': 'Camping'},
        ],
    },
    }

    park = parks.get(park_name)

    if not park:
        return redirect('parks')

    return render(request, 'park-detail.html', {
        'park': park
    })