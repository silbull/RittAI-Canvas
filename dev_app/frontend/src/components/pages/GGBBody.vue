<script setup type="text/javascript">
    /* eslint-disable */
    import { ref, defineProps, watch, onMounted } from 'vue';
    import { useRoute } from 'vue-router';
    import {useStore} from 'vuex';

    // プロパティを定義することで，親コンポーネントのv-bind(:)ggb_script_propsを取得
    const props = defineProps({ggb_script_props: String});

    // 親コンポーネントからのggb_script_propsの変更を監視し，変更があれば関数を実行する．
    watch(
        () => props.ggb_script_props, // 監視する変数
        (newValue) => { // 変更があった場合に実行する関数
            executeMultipleCommands(newValue)
        }
    );
    
    // 保存用のストア
    const store = useStore();
    // GeoGebraインスタンスの作成
    const params = ref({
        "appName": "3d", 
        "scaleContainerClass": "geogebra_01",
        "showToolBar": true, 
        "showAlgebraInput": false, 
        "showMenuBar": true,
        "disableAutoScale":true,
    });
    
    let applet = null
    const route = useRoute();

    const reloadGeoGebra = () => {
        if (applet) { // 既にGeoGebraが読み込まれている場合は，消去する
            // applet.remove(); 
        }
            applet = new GGBApplet(params.value, true);
            applet.inject('ggb-element');
        }
    
    // var applet = new GGBApplet(params, true);
    // window.addEventListener('DOMContentLoaded', function() {
    //     applet.inject('ggb-element');
    // })
    // 消去用のオブジェクトのラベル．カンマでオブジェクト名が区切られているstr型
    let label = ""
    // GeoGebra図形生成関数
    function executeMultipleCommands(ggb_script_last) {
        label = ggbApplet.evalCommandGetLabels(ggb_script_last);
        // ggbApplet.evalCommand(ggb_script_last);
        console.log(`in GGBBody.vue in executeMultipleCommands() ggb_script_last: ` + ggb_script_last);
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

    // マウント時に実行する関数
    onMounted(() => { // コンポーネントがマウントされたらGeoGebraを読み込む
    reloadGeoGebra()
    // if (store.state.geoGebraState){
    //     applet.setXML(store.state.geoGebraState)
    // }
    })

    // ルートの変化を監視し，変化があればGeoGebraを再読み込みする
    watch(() => route.fullPath, () => {
        reloadGeoGebra()
    })

    
    // 軸の表示・非表示を切り替える関数
    const isCheckedAxis = ref(true);
    const axisVisibleChange = () => {
        if (isCheckedAxis.value){
            ggbApplet.setVisible("xAxis", true);
            ggbApplet.setVisible("yAxis", true);
            ggbApplet.setVisible("zAxis", true);
        }else{
            ggbApplet.setVisible("xAxis", false);
            ggbApplet.setVisible("yAxis", false);
            ggbApplet.setVisible("zAxis", false);
        }
    }
    // 平面の表示・非表示を切り替える関数
    const isCheckedPlane = ref(true);
    const planeVisibleChange = () => {
        if (isCheckedPlane.value){
            ggbApplet.setVisible("xOyPlane", true);
        }else{
            ggbApplet.setVisible("xOyPlane", false);
        }
    }
</script>

<template>
    <!-- デバッグ -->
    <!-- <div>script_modified_props: {{ script_modified_props }}</div>  -->
    
    <div class="container-003">
            <div class="geogebra-menu">
                <button class="button-reset" @click="deleteAllObjects()">Reset</button>
                <fieldset class="checkbox-001">
                    <label>
                        <input type="checkbox" name="checkbox-001" v-model="isCheckedAxis" @change="axisVisibleChange"/>
                        軸の表示
                    </label>
                    <label>
                        <input type="checkbox" name="checkbox-001" v-model="isCheckedPlane" @change="planeVisibleChange"/>
                        平面の表示
                    </label>
                </fieldset>
            </div>
        
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
    margin-right: 300px;
}
.button-reset:hover {
    background-color: #5d8ba1;
}

.container-003{
    display: flex;
    flex-direction: column;
}

.geogebra-menu{
    display: flex;
    align-items: center;
    
}

.checkbox-001 {
    display: flex;
    flex-wrap: wrap;
    gap: .5em 2em;
    border: none;
    font-weight: 600;
    font-size: 1em;
}

.checkbox-001 label {
    display: flex;
    align-items: center;
    gap: 0 .5em;
    position: relative;
    cursor: pointer;
}

.checkbox-001 label::before,
.checkbox-001 label:has(:checked)::after {
    content: '';
}

.checkbox-001 label::before {
    width: 17px;
    height: 17px;
    border-radius: 3px;
    background-color: #e6edf3;
}

.checkbox-001 label:has(:checked)::before {
    background-color: #2589d0;
}

.checkbox-001 label:has(:checked)::after {
    position: absolute;
    top: 6px;
    left: 6px;
    transform: rotate(45deg);
    width: 4px;
    height: 8px;
    border: solid #fff;
    border-width: 0 2px 2px 0;
}

.checkbox-001 input {
    display: none;
}


</style>