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

    onMounted(() => {
    for (let i = 1; i <= 6; i++) {
        const applet = new window.GGBApplet({
        container: "ggb-element" + i,
        width: 500,
        height: 300,
        "appName": "3d", 
        "scaleContainerClass": "geogebra_01",
        "showToolBar": false, 
        "showAlgebraInput": false, 
        "showMenuBar": false,
        "disableAutoScale":true,
        });
        applet.inject("ggb-element" + i);
    }
    });

    // TODO 各windowに表示される図形は違うから，applet1, 2みたいな感じにした方がいい
    
    
</script>

<template>
    <!-- デバッグ -->
    <!-- <div>script_modified_props: {{ script_modified_props }}</div>  -->
    <div id="app">
    <div class="row" v-for="i in 3" :key="i">
      <div class="col" v-for="j in 2" :key="j">
        <div :id="'ggb-element' + ((i-1) * 2 + j)" class="ggb-window"></div>
      </div>
    </div>
  </div>
</template>

<style scoped>

#ggb-element1,
#ggb-element2,
#ggb-element3,
#ggb-element4,
#ggb-element5,
#ggb-element6 {
  width: 500px;
  height: 300px;
}

.row {
  display: flex;
}

.col {
  flex: 1;
  margin: 10px;
}

.ggb-window {
  border: 1px solid #ccc;
}
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