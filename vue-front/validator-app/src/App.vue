<template>
  <div id="app">
    <div class="container">
      <div class="title">
        <img height="50" src="https://is1-ssl.mzstatic.com/image/thumb/Purple118/v4/ce/3c/c5/ce3cc556-3235-c11b-9206-5ad07d51f7cf/KaraokeSmartIcon-1x_U007emarketing-85-220-4.png/246x0w.jpg"/>
        <h1>KS - File validator</h1>
      </div>
      <textarea v-model="text" placeholder="Paste the lyrics here..." />
      <div class="buttons">
        <v-btn color="error" v-on:click="validate(text)"><span>Validate</span></v-btn>
        <v-btn color="error" v-on:click="get_lyrics(text)"><span>Get Lyrics</span></v-btn>
      </div>
      <textarea v-model="output" v-bind:style="{ 'word-spacing': word_spacing }"/>
    </div>    
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'app',
  data () {
    return {
      text: '',
      output: '',
      word_spacing: '7px'
    }
  },
  methods: {
    validate: function (text) {
      axios.post("https://validador.karaokesmart.co:5000/check", {
      // axios.post("http://0.0.0.0:5000/check", {
        'lines': text.split('\n')
      })
      .then((response) => {
        this.output = response.data.join('\n');
        console.log(response)
      });
    },
    get_lyrics: function(text) {
      axios.post("https://validador.karaokesmart.co:5000/lyrics", {
      // axios.post("http://0.0.0.0:5000/lyrics", {
        'lines': text.split('\n')
      })
      .then((response) => {
        this.output = response.data.join('\n');
        console.log(response)
      })
    }
  }
}
</script>

<style lang="scss">

#app {  
  font-family: 'Montserrat', sans-serif, 'Helvetica', 'Arial', 'sans-serif';
  background-color: black;
}

h1 {
  color: white;
}

.container {
  margin: 0 auto;
  margin-top: 50px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: black;
  max-width: 700px;
}

.title {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

textarea {
  margin: 50px;
  width: 600px;
  height: 300px;
  background-color: white;
  padding: 20px;
  line-height: 1.5em;
}

button {
  background-color: #00adbc;
}

span {
  font-size: 1.3em;
}

html {
  background-color: black;
}

</style>
