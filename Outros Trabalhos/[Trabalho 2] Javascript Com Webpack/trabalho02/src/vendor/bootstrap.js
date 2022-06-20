import '@popperjs/core/dist/cjs/popper.js'
import 'bootstrap/dist/css/bootstrap.min.css'

import Carousel from 'bootstrap/js/dist/carousel'
import Collapse from 'bootstrap/js/dist/collapse'

const carousel = document.querySelectorAll('[data-ride="carousel"]')
const collapse = document.querySelectorAll('[data-toggle="carousel"]')

carousel.forEach(carousel => {
    new Carousel(carousel)
});

collapse.forEach(collapse => {
    new Collapse(collapse)
});