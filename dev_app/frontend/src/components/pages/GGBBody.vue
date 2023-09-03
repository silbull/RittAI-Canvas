<script setup type="text/javascript">
    /* eslint-disable */
    import { ref, defineProps, watch } from 'vue';

    // プロパティを定義することで，親コンポーネントのv-bind(:)script_modified_propsを取得
    const props = defineProps({script_modified_props: String});

    // 親コンポーネントからのscript_modified_propsの変更を監視し，変更があれば関数を実行する．
    watch(
        () => props.script_modified_props,
        (newValue) => {
            executeMultipleCommands(newValue)
        }
    );

    // GeoGebraインスタンスの作成
    var params = {
        "appName": "3d", 
        "scaleContainerClass": "geogebra_01",
        // "width": 100, 
        // "height": 100, 
        "showToolBar": true, 
        "showAlgebraInput": false, 
        "showMenuBar": true,
        "disableAutoScale":true,
    };
    var applet = new GGBApplet(params, true);
    window.addEventListener('DOMContentLoaded', function() {
        applet.inject('ggb-element');
    })
    // 消去用のオブジェクトのラベル．カンマでオブジェクト名が区切られているstr型
    let label = ""
    // GeoGebra図形生成関数
    function executeMultipleCommands(ggb_script_last) {
        label = ggbApplet.evalCommandGetLabels(ggb_script_last);
        console.log(`in FormsBody.vue in executeMultipleCommands() ggb_script_last: ` + ggb_script_last);
        console.log(`label:` + label);
    }
    // GeoGebra画面から全てのオブジェクトを消去する
    function deleteAllObjects(){
        // オブジェクト名の羅列strから配列を作成して，1つずつdeleteする
        let objects_array = label.split(",");
        objects_array.forEach(element => {
            ggbApplet.deleteObject(element)
        });
    }
</script>

<template>
    <!-- デバッグ -->
    <!-- <div>script_modified_props: {{ script_modified_props }}</div>  -->
    <button @click="deleteAllObjects()">Reset</button>
    <div class="geogebra_01" id="ggb-element">ggb-elementが表示できません.</div>
    <p>EOF</p>
</template>

<style scoped>
    .geogebra_01 {
        width: 100vw;
        height: 70vh;
    }
</style>