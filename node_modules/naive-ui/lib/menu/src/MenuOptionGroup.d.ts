import { PropType } from 'vue';
import { TmNode } from './interface';
export declare const menuItemGroupProps: {
    readonly tmNodes: {
        readonly type: PropType<TmNode[]>;
        readonly required: true;
    };
    readonly internalKey: {
        readonly type: PropType<import("treemate").Key>;
        readonly required: true;
    };
    readonly root: BooleanConstructor;
    readonly isGroup: BooleanConstructor;
    readonly level: {
        readonly type: NumberConstructor;
        readonly required: true;
    };
    readonly title: PropType<string | (() => import("vue").VNodeChild)>;
    readonly extra: PropType<string | (() => import("vue").VNodeChild)>;
};
export declare const NMenuOptionGroup: import("vue").DefineComponent<{
    readonly tmNodes: {
        readonly type: PropType<TmNode[]>;
        readonly required: true;
    };
    readonly internalKey: {
        readonly type: PropType<import("treemate").Key>;
        readonly required: true;
    };
    readonly root: BooleanConstructor;
    readonly isGroup: BooleanConstructor;
    readonly level: {
        readonly type: NumberConstructor;
        readonly required: true;
    };
    readonly title: PropType<string | (() => import("vue").VNodeChild)>;
    readonly extra: PropType<string | (() => import("vue").VNodeChild)>;
}, () => JSX.Element, unknown, {}, {}, import("vue").ComponentOptionsMixin, import("vue").ComponentOptionsMixin, Record<string, any>, string, import("vue").VNodeProps & import("vue").AllowedComponentProps & import("vue").ComponentCustomProps, Readonly<import("vue").ExtractPropTypes<{
    readonly tmNodes: {
        readonly type: PropType<TmNode[]>;
        readonly required: true;
    };
    readonly internalKey: {
        readonly type: PropType<import("treemate").Key>;
        readonly required: true;
    };
    readonly root: BooleanConstructor;
    readonly isGroup: BooleanConstructor;
    readonly level: {
        readonly type: NumberConstructor;
        readonly required: true;
    };
    readonly title: PropType<string | (() => import("vue").VNodeChild)>;
    readonly extra: PropType<string | (() => import("vue").VNodeChild)>;
}>>, {
    root: boolean;
    isGroup: boolean;
}>;
