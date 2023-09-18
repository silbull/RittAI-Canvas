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
    <div class="container-003">
        <button class="button-reset" @click="deleteAllObjects()">Reset</button>
        <div class="geogebra_01" id="ggb-element">ggb-elementが表示できません.</div>
    </div>
</template>

<style scoped>
    .geogebra_01 {
        width: 78vw;
        height: 76vh;
    }

    .button-reset {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 10%;
    height: 20px;
    margin-bottom: 5px;
    padding: .9em 2em;
    border: none;
    border-radius: 25px;
    background-color: #80b6d0;
    color: #fff;
    font-weight: 600;
    font-size: 1em;
}
.button-reset:hover {
    background-color: #5d8ba1;
}

    .container-003{
        display: flex;
        flex-direction: column;
    }
</style>