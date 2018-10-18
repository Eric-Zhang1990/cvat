
# Copyright (C) 2018 Intel Corporation
#
# SPDX-License-Identifier: MIT

from django.urls import path
from . import views

urlpatterns = [
    path('create', views.createGitRecord),
    path('delete/<int:tid>', views.deleteGitRecord),
]
