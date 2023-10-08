<script setup >
    import { defineEmits, ref } from 'vue'
    import VueCropper from 'vue-cropperjs';
    import 'cropperjs/dist/cropper.css';

    const cropperRef = ref('');
    const imageSrc = ref('');
    const showCropper = ref(false);

    let autoCropWidth = 700;
    let autoCropHeight = 400;

    const onFileChange = (e) => {
        imageSrc.value = '';
        showCropper.value = false;
        const file = e.target.files[0];
        const reader = new FileReader();
        reader.onload = (e) => {
        
            imageSrc.value = e.target.result;
            showCropper.value = true;
            // const img = new Image();
            // img.src = e.target.result;
            // showCropper.value = true;
            // img.onload = () => {
            //     autoCropWidth = img.width;
            //     autoCropHeight = img.height;
            // };

        };
        reader.readAsDataURL(file);

    };

    const cropImage = async () => {
        const cropperImage = cropperRef.value;
        const croppedCanvas = cropperImage.getCroppedCanvas();

        croppedCanvas.toBlob(async (blob) => {
            const formData = new FormData()
            formData.append('image', blob)

            fetch(
                // flask APIのパスを指定
                "/run_ocr", 
                {
                    method: 'POST',
                    body: formData, //dataをjsonに変換して送信
                } // postのボディ
            ).then(res => res.json()).then( 
                // 同期処理．レスポンス取得後に実行．
                function(jdata){
                    var output = jdata["text"];
                    console.log(`in handleOCR() output: ` + output);

                    question_text.value = output; // scriptTextに出力を代入
                    console.log(`in handleOCR() question_text.value: ` + question_text.value);
                    showCropper.value = false;
                }
            ).catch(error => console.error('Error:', error)); // エラー処理
        });
    };

    // textareaの代入先
    const question_text = ref("");

    // 子コンポーネントでの動作を親コンポーネントに伝達させて，親コンポーネントでイベント発火させるためのemit
    const emit = defineEmits(['input-submitted']);
    // 'input-submitted'というカスタムイベントを親コンポーネントに伝達し，親コンポーネント(FormsBody)でイベント発火させる関数
    function QuestionSubmit() {
        emit('input-submitted', question_text.value);
    }

    
    

    const handleOCR = () => {
        const image = document.getElementById("imageUpload").files[0];
        const formData = new FormData()
        formData.append('image', image)

        fetch(
            // flask APIのパスを指定
            "/run_ocr", 
            {
                method: 'POST',
                body: formData, //dataをjsonに変換して送信
            } // postのボディ
        ).then(res => res.json()).then( 
            // 同期処理．レスポンス取得後に実行．
            function(jdata){
                var output = jdata["text"];
                console.log(`in handleOCR() output: ` + output);

                question_text.value = output; // scriptTextに出力を代入
                console.log(`in handleOCR() question_text.value: ` + question_text.value);
            }
        ).catch(error => console.error('Error:', error)); // エラー処理
    }
</script>



<template>
    
<div >
    <input type="file" @change="onFileChange" />
    <div v-if="showCropper">
      <vue-cropper
        ref="cropperRef"
        :src="imageSrc"
        :stencil-props="{
          aspectRatio: 1 / 1,
        }"
      ></vue-cropper>
      <button class="button-ocr" @click="cropImage">画像から読み取る</button>
    </div>
    <!-- <input type="file" id="imageUpload" />
    <button class="button-ocr" @click="handleOCR()">画像から読み取る</button> -->
</div>
    <textarea class="textarea-01" placeholder="空間図形の問題を入力してください" v-model="question_text" @keydown.ctrl.enter="QuestionSubmit()"></textarea>
    <button class="button-send_to_GPT" @click="QuestionSubmit()">Create GGB Script</button>
</template>



<style scoped>
.textarea-01 {
    height: 30%;
    padding: 8px 10px;
    border: 1px solid #969da3;
    border-radius: 3px;
    color: #333;
    font-size: 1em;
    line-height: 1.5;
    margin-bottom: 4px;    /* 下側の余白 */
    resize:none;
}

.textarea-01::placeholder {
    color: #999;
}
.button-ocr {
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
    margin-top: 5px;
    margin-bottom: 5px;    /* 下側の余白 */
}
.button-ocr:hover {
    background-color: #0f5688;
}
.button-send_to_GPT {
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

.button-send_to_GPT:hover {
    background-color: #0f5688;
}

</style>