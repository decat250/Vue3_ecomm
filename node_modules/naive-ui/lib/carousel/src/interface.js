"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.carouselMethodsInjectionKey = exports.tuple = void 0;
const _utils_1 = require("../../_utils");
const tuple = (...args) => args;
exports.tuple = tuple;
exports.carouselMethodsInjectionKey = (0, _utils_1.createInjectionKey)('n-carousel-methods');
