import { CSSProperties, PropType, Ref } from 'vue';
import { VResizeObserverOnResize } from 'vueuc';
import { ExtractPublicPropTypes } from '../../_utils';
declare const gridProps: {
    readonly responsive: {
        readonly type: PropType<"screen" | "self">;
        readonly default: "self";
    };
    readonly cols: {
        readonly type: PropType<string | number>;
        readonly default: 24;
    };
    readonly itemResponsive: BooleanConstructor;
    readonly collapsed: BooleanConstructor;
    readonly collapsedRows: {
        readonly type: NumberConstructor;
        readonly default: 1;
    };
    readonly itemStyle: PropType<string | CSSProperties>;
    readonly xGap: {
        readonly type: PropType<string | number>;
        readonly default: 0;
    };
    readonly yGap: {
        readonly type: PropType<string | number>;
        readonly default: 0;
    };
};
export interface NGridInjection {
    itemStyleRef: Ref<CSSProperties | string | undefined>;
    xGapRef: Ref<string | undefined>;
    overflowRef: Ref<boolean>;
}
export declare type GridProps = ExtractPublicPropTypes<typeof gridProps>;
declare const _default: import("vue").DefineComponent<{
    readonly responsive: {
        readonly type: PropType<"screen" | "self">;
        readonly default: "self";
    };
    readonly cols: {
        readonly type: PropType<string | number>;
        readonly default: 24;
    };
    readonly itemResponsive: BooleanConstructor;
    readonly collapsed: BooleanConstructor;
    readonly collapsedRows: {
        readonly type: NumberConstructor;
        readonly default: 1;
    };
    readonly itemStyle: PropType<string | CSSProperties>;
    readonly xGap: {
        readonly type: PropType<string | number>;
        readonly default: 0;
    };
    readonly yGap: {
        readonly type: PropType<string | number>;
        readonly default: 0;
    };
}, {
    mergedClsPrefix: import("vue").ComputedRef<string>;
    style: import("vue").ComputedRef<CSSProperties>;
    isResponsive: import("vue").ComputedRef<boolean>;
    responsiveQuery: import("vue").ComputedRef<number | string[] | undefined>;
    responsiveCols: import("vue").ComputedRef<number>;
    handleResize: import("vue").ComputedRef<VResizeObserverOnResize | undefined>;
    overflow: Ref<boolean>;
}, unknown, {}, {}, import("vue").ComponentOptionsMixin, import("vue").ComponentOptionsMixin, Record<string, any>, string, import("vue").VNodeProps & import("vue").AllowedComponentProps & import("vue").ComponentCustomProps, Readonly<import("vue").ExtractPropTypes<{
    readonly responsive: {
        readonly type: PropType<"screen" | "self">;
        readonly default: "self";
    };
    readonly cols: {
        readonly type: PropType<string | number>;
        readonly default: 24;
    };
    readonly itemResponsive: BooleanConstructor;
    readonly collapsed: BooleanConstructor;
    readonly collapsedRows: {
        readonly type: NumberConstructor;
        readonly default: 1;
    };
    readonly itemStyle: PropType<string | CSSProperties>;
    readonly xGap: {
        readonly type: PropType<string | number>;
        readonly default: 0;
    };
    readonly yGap: {
        readonly type: PropType<string | number>;
        readonly default: 0;
    };
}>>, {
    cols: string | number;
    responsive: "screen" | "self";
    collapsed: boolean;
    itemResponsive: boolean;
    collapsedRows: number;
    xGap: string | number;
    yGap: string | number;
}>;
export default _default;
