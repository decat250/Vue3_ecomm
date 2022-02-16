declare const _default: import("vue").DefineComponent<{
    clsPrefix: {
        type: StringConstructor;
        required: true;
    };
    tmNode: {
        type: ObjectConstructor;
        required: true;
    };
}, {
    labelField: import("vue").Ref<string>;
    showIcon: import("vue").Ref<boolean>;
    hasSubmenu: import("vue").Ref<boolean>;
    renderLabel: import("vue").Ref<import("./interface").RenderLabelImpl | undefined>;
}, unknown, {}, {}, import("vue").ComponentOptionsMixin, import("vue").ComponentOptionsMixin, Record<string, any>, string, import("vue").VNodeProps & import("vue").AllowedComponentProps & import("vue").ComponentCustomProps, Readonly<import("vue").ExtractPropTypes<{
    clsPrefix: {
        type: StringConstructor;
        required: true;
    };
    tmNode: {
        type: ObjectConstructor;
        required: true;
    };
}>>, {}>;
export default _default;
