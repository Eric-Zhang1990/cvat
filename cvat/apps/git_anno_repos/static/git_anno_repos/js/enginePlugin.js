/*
 * Copyright (C) 2018 Intel Corporation
 *
 * SPDX-License-Identifier: MIT
 */

"use strict";


document.addEventListener("DOMContentLoaded", () => {
    let gitReposWindowID = 'gitReposWindow';
    let closeReposWindowButtonId = 'closeGitReposButton';

    $(`<div id="${gitReposWindowID}" class="modal hidden">
            <div style="width: 700px; height: 450px;" class="modal-content">
                <div style="width: 100%; height: 90%; overflow-y: auto;">

                </div>
                <center>
                    <button id="${closeReposWindowButtonId}" class="regular h1" style="margin-top: 15px;"> Close </button>
                </center>
            </div>
        </div>
    `).appendTo('#taskAnnotationCenterPanel');

    $(`#${closeReposWindowButtonId}`).on('click', () => {
        $(`#${gitReposWindowID}`).addClass('hidden');
    });

    $(`<button class="menuButton semiBold h2"> Git Repository </button>`).on('click', () => {
        $('#annotationMenu').addClass('hidden');
        $(`#${gitReposWindowID}`).removeClass('hidden');
    }).prependTo($('#engineMenuButtons'));
});
