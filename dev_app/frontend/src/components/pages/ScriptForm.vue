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
    <textarea class="textarea-01" placeholder="scriptが代入される" v-model="script_text" @keydown.ctrl.enter="handleSubmit"></textarea>
    <button @click="handleSubmit">Create GeoGebra 3D model</button>
    <!-- デバッグ -->
    <!-- <div>script_props = {{ script_props }}</div> -->
</template>



<style scoped>
    .textarea-01 {
        width: 100vw;
        height: 50px;
        padding: 8px 10px;
        border: 1px solid #969da3;
        border-radius: 3px;
        color: #333;
        font-size: 1em;
        line-height: 1.5;
    }

    .textarea-01::placeholder {
        color: #999;
    }
</style>