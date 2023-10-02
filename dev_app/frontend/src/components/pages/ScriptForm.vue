<script setup>
    import { defineProps, defineEmits, ref, watch } from 'vue'

    // プロパティを定義することで，親コンポーネントのv-bind(:)からscript_propsを取得
    const props = defineProps({script_props: String});
    // v-bindのためにプロパティを改めてrefで定義，textareaの代入先でもある．
    const script_text = ref(props.script_props);
    // 親コンポーネントからのscript_propsの変更を監視し，変更があればscript_textも更新するwatch．
    // v-modelにscript_textをバインドするために必要．
    watch(
        () => props.script_props,
        (newValue) => {
            script_text.value = newValue;
        }
    );
    
    // 子コンポーネントでの動作を親コンポーネントに伝達させて，親コンポーネントでイベント発火させるためのemit
    const emit = defineEmits(['notify']);
    // 親コンポーネントに動作を伝達させる関数，'input-submitted'は親コンポーネントでのイベントトリガー名
    function handleSubmit() {
        emit('input-submitted', script_text.value);
    }
</script>



<template>
    <textarea class="textarea-02" placeholder="ここにスクリプトが生成されます" v-model="script_text" @keydown.ctrl.enter="handleSubmit"></textarea>
    <button class="button-3D_model" @click="handleSubmit">Create 3D model</button>
</template>



<style scoped>
    .textarea-02 {
        height: 53%;
        padding: 8px 10px;
        border: 1px solid #969da3;
        border-radius: 3px;
        color: #333;
        font-size: 1em;
        line-height: 1.5;
        margin-bottom: 4px;    /* 下側の余白 */
        resize:none;
    }

    .textarea-02::placeholder {
        color: #999;
    }

    .button-3D_model {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 250px;
        margin:0 auto;
        padding: .9em 2em;
        border: none;
        border-radius: 5px;
        background-color: #2589d0;
        color: #fff;
        font-weight: 600;
        font-size: 1em;
    }

    .button-3D_model:hover {
        background-color: #0f5688;
    }
</style>