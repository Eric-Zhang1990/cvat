
# Copyright (C) 2018 Intel Corporation
#
# SPDX-License-Identifier: MIT

from django.urls import path
from . import views

urlpatterns = [
    path('create', views.createRepository),
    path('update', views.updateRepository),
    path('get/<int:jid>', views.getRepository),
    path('delete/<int:jid>', views.deleteRepository),
]
