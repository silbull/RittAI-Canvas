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
        "borderColor": "#0a78e6",
        "scaleContainerClass": "geogebra_01",
        "showToolBar": false, 
        "showAlgebraInput": false, 
        "showMenuBar": true,
        "disableAutoScale":true,
        "showToolBarHelp": false,  // 追加
        "showResetIcon": false,     // 追加
        "ggbBase64": "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",            // 追加
        
    });
    
    let applet = null
    const route = useRoute();

    // mount時にgeogebraを読み込む関数
    const reloadGeoGebra = () => {
        if (applet) { // 既にGeoGebraが読み込まれている場合は，消去する
            // applet.remove(); 
        }
            applet = new GGBApplet(params.value, true);
            applet.inject('ggb-element');
        }

    // カメラの設定
    const setCamera = () => {
        // Sliderの作成
        ggbApplet.evalCommand('faces = Slider[0, 4, 1]');

        // ベクトルの定義
        ggbApplet.evalCommand('u_1 = (1, 0, 0)');
        ggbApplet.evalCommand('u_2 = (0, 1, 0)');
        ggbApplet.evalCommand('u_3 = (0, 0, 1)');
        ggbApplet.evalCommand('u_4 = (1; 120°; -20°)');

        // ベクトルのリストの作成
        ggbApplet.evalCommand('vdir = {u_1, u_2, u_3, u_4}');

        // facesの値に応じてベクトルを選択
        ggbApplet.evalCommand('Selectvec = Element[vdir, faces]');

        // ベクトルを非表示
        ggbApplet.setVisible("u_1", false);
        ggbApplet.setVisible("u_2", false);
        ggbApplet.setVisible("u_3", false);
        ggbApplet.setVisible("u_4", false);
        ggbApplet.setVisible("Selectvec", false);
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
        console.log(`Mounted`)
    })

    // // ルートの変化を監視し，変化があればGeoGebraを再読み込みする
    // watch(() => route.fullPath, () => {
    //     reloadGeoGebra()
    // })

    
    // 軸の表示・非表示を切り替える関数
    const isCheckedAxis = ref(true);
    const axisVisibleChange = () => {
        console.log(`isCheckedAxis: ` + isCheckedAxis.value);
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
    // 視点を変更する関数
    const isFirstClick = ref(true);
    const changeView = () => {
        if (isFirstClick.value){
            setCamera();
            isFirstClick.value = false;
        }
        // 視点を変更するベクトルを選択
        const currentValue = ggbApplet.getValue('faces');
        const newValue = (currentValue + 1)  // 5 ではなく 4 の次は 0 にするための計算
        ggbApplet.setValue('faces', newValue);
        const selectVecStr = ggbApplet.getLaTeXString('Selectvec');
        ggbApplet.evalCommand(`SetViewDirection[${selectVecStr}]`);
        if (newValue == 4){
            ggbApplet.setValue('faces', 0);
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
                <button class="button-change-view" @click="changeView()">視点変更</button>
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
    margin-right: 250px;
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
    margin-right: 0px;
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

.button-change-view{
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100px;
    height: auto;
    margin: 5px 30px 5px 30px; /* 上 | 右 | 下 | 左 */
    padding: .2em 0.2em;
    border: none;
    border-radius: 5px;
    background-color: #2589d0;
    color: #fff;
    font-weight: 600;
    font-size: 1em;
    box-sizing: border-box;
}

</style>