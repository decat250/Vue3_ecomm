"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.useDialog = void 0;
const vue_1 = require("vue");
const context_1 = require("./context");
const _utils_1 = require("../../_utils");
function useDialog() {
    const dialog = (0, vue_1.inject)(context_1.dialogApiInjectionKey, null);
    if (dialog === null) {
        (0, _utils_1.throwError)('use-dialog', 'No outer <n-dialog-provider /> founded.');
    }
    return dialog;
}
exports.useDialog = useDialog;
