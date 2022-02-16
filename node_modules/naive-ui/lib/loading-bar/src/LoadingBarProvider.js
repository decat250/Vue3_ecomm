"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const vue_1 = require("vue");
const vooks_1 = require("vooks");
const _mixins_1 = require("../../_mixins");
const LoadingBar_1 = __importDefault(require("./LoadingBar"));
const context_1 = require("./context");
const loadingBarProps = Object.assign(Object.assign({}, _mixins_1.useTheme.props), { to: {
        type: [String, Object],
        default: undefined
    }, loadingBarStyle: {
        type: Object
    } });
exports.default = (0, vue_1.defineComponent)({
    name: 'LoadingBarProvider',
    props: loadingBarProps,
    setup(props) {
        const isMountedRef = (0, vooks_1.useIsMounted)();
        const loadingBarRef = (0, vue_1.ref)(null);
        const methods = {
            start() {
                var _a;
                if (isMountedRef.value) {
                    (_a = loadingBarRef.value) === null || _a === void 0 ? void 0 : _a.start();
                }
                else {
                    void (0, vue_1.nextTick)(() => {
                        var _a;
                        (_a = loadingBarRef.value) === null || _a === void 0 ? void 0 : _a.start();
                    });
                }
            },
            error() {
                var _a;
                if (isMountedRef.value) {
                    (_a = loadingBarRef.value) === null || _a === void 0 ? void 0 : _a.error();
                }
                else {
                    void (0, vue_1.nextTick)(() => {
                        var _a;
                        (_a = loadingBarRef.value) === null || _a === void 0 ? void 0 : _a.error();
                    });
                }
            },
            finish() {
                var _a;
                if (isMountedRef.value) {
                    (_a = loadingBarRef.value) === null || _a === void 0 ? void 0 : _a.finish();
                }
                else {
                    void (0, vue_1.nextTick)(() => {
                        var _a;
                        (_a = loadingBarRef.value) === null || _a === void 0 ? void 0 : _a.finish();
                    });
                }
            }
        };
        const { mergedClsPrefixRef } = (0, _mixins_1.useConfig)(props);
        (0, vue_1.provide)(context_1.loadingBarApiInjectionKey, methods);
        (0, vue_1.provide)(context_1.loadingBarProviderInjectionKey, {
            props,
            mergedClsPrefixRef
        });
        return Object.assign(methods, {
            loadingBarRef
        });
    },
    render() {
        var _a, _b, _c;
        return ((0, vue_1.h)(vue_1.Fragment, null,
            (0, vue_1.h)(vue_1.Teleport, { to: (_a = this.to) !== null && _a !== void 0 ? _a : 'body' },
                (0, vue_1.h)(LoadingBar_1.default, { ref: "loadingBarRef" })), (_c = (_b = this.$slots).default) === null || _c === void 0 ? void 0 :
            _c.call(_b)));
    }
});
