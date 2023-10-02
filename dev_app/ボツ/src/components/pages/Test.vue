<script setup type="text/javascript">
    var params = {
        "appName": "3d", 
        "scaleContainerClass": "geogebra_01",
        // "width": 100, 
        // "height": 100, 
        "showToolBar": false, 
        "showAlgebraInput": false, 
        "showMenuBar": true,
        "disableAutoScale":true,
    };
    var applet = new GGBApplet(params, true);
    window.addEventListener('DOMContentLoaded', function() {
        applet.inject('ggb-element');
    })

    function executeMultipleCommands() {
        ggbApplet.evalCommand('A = (0,1,2)\nB = (0,3,4)\nAB = Segment(A,B)');
    }
</script>

<template>

    <button v-on:click="executeMultipleCommands()">Execute GeoGebra Script</button>
    <br>
    <div class="geogebra_01" id="ggb-element">ggb-elementが表示できません.</div>

    <p>EOF</p>
</template>

<style scoped>
    .geogebra_01 {
        width: 100vw;
        height: 70vh;
    }

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