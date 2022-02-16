import { PropType } from 'vue';
import { ExtractPublicPropTypes } from '../../_utils';
declare const timeProps: {
    readonly time: {
        readonly type: PropType<number | Date>;
        readonly default: undefined;
    };
    readonly type: {
        readonly type: PropType<"relative" | "date" | "datetime">;
        readonly default: "datetime";
    };
    readonly to: {
        readonly type: PropType<number | Date>;
        readonly default: undefined;
    };
    readonly unix: BooleanConstructor;
    readonly format: StringConstructor;
    readonly text: BooleanConstructor;
    readonly timezone: StringConstructor;
};
export declare type TimeProps = ExtractPublicPropTypes<typeof timeProps>;
declare const _default: import("vue").DefineComponent<{
    readonly time: {
        readonly type: PropType<number | Date>;
        readonly default: undefined;
    };
    readonly type: {
        readonly type: PropType<"relative" | "date" | "datetime">;
        readonly default: "datetime";
    };
    readonly to: {
        readonly type: PropType<number | Date>;
        readonly default: undefined;
    };
    readonly unix: BooleanConstructor;
    readonly format: StringConstructor;
    readonly text: BooleanConstructor;
    readonly timezone: StringConstructor;
}, {
    renderedTime: import("vue").ComputedRef<string>;
}, unknown, {}, {}, import("vue").ComponentOptionsMixin, import("vue").ComponentOptionsMixin, Record<string, any>, string, import("vue").VNodeProps & import("vue").AllowedComponentProps & import("vue").ComponentCustomProps, Readonly<import("vue").ExtractPropTypes<{
    readonly time: {
        readonly type: PropType<number | Date>;
        readonly default: undefined;
    };
    readonly type: {
        readonly type: PropType<"relative" | "date" | "datetime">;
        readonly default: "datetime";
    };
    readonly to: {
        readonly type: PropType<number | Date>;
        readonly default: undefined;
    };
    readonly unix: BooleanConstructor;
    readonly format: StringConstructor;
    readonly text: BooleanConstructor;
    readonly timezone: StringConstructor;
}>>, {
    type: "relative" | "date" | "datetime";
    text: boolean;
    time: number | Date;
    to: number | Date;
    unix: boolean;
}>;
export default _default;
