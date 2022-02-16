import { ExtractPropTypes } from 'vue';
declare const breadcrumbItemProps: {
    readonly separator: StringConstructor;
    readonly href: StringConstructor;
};
export declare type BreadcrumbItemProps = Partial<ExtractPropTypes<typeof breadcrumbItemProps>>;
declare const _default: import("vue").DefineComponent<{
    readonly separator: StringConstructor;
    readonly href: StringConstructor;
}, (() => null) | (() => JSX.Element), unknown, {}, {}, import("vue").ComponentOptionsMixin, import("vue").ComponentOptionsMixin, Record<string, any>, string, import("vue").VNodeProps & import("vue").AllowedComponentProps & import("vue").ComponentCustomProps, Readonly<ExtractPropTypes<{
    readonly separator: StringConstructor;
    readonly href: StringConstructor;
}>>, {}>;
export default _default;
