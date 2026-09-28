from django.urls import path
from contacts.views import ContactList, ContactCreate, ContactDetail, ContactDelete, ContactUpdate, ContactPatch

urlpatterns = [
    path('contacts/', ContactList.as_view()),
    path('contacts/create/', ContactCreate.as_view()),
    path('contacts/<int:pk>/', ContactDetail.as_view()),
    path('contacts/<int:pk>/delete/', ContactDelete.as_view()),
    path('contacts/<int:pk>/update/', ContactUpdate.as_view()),
    path('contacts/<int:pk>/patch', ContactPatch.as_view()),
]
